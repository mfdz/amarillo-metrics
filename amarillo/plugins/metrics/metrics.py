import json
import logging
import os
import random
from typing import Callable

from fastapi import APIRouter, HTTPException, Depends, Request
from datetime import datetime
from prometheus_client.exposition import generate_latest
from prometheus_client import Gauge, Counter
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_fastapi_instrumentator import metrics as pfi_metrics
from prometheus_fastapi_instrumentator.metrics import Info
from fastapi import Depends, HTTPException, FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.responses import PlainTextResponse

from amarillo.plugins.metrics.secrets import secrets

logger = logging.getLogger(__name__)

security = HTTPBasic()

gtfs_download_counter = Counter("amarillo_gtfs_downloads", "How many times GTFS data was downloaded")
grfs_download_counter = Counter("amarillo_grfs_downloads", "How many times GRFS data was downloaded")

def increment_gtfs_download_counter():
    gtfs_download_counter.inc()

def increment_grfs_download_counter():
    grfs_download_counter.inc()

trips_created_counter = Counter("amarillo_trips_created", "How many trips have been created")
trips_updated_counter = Counter("amarillo_trips_updated", "How many existing trips have been updated")
trips_deleted_counter = Counter("amarillo_trips_deleted", "How many trips have been deleted")


def amarillo_trips_number_total() -> Callable[[Info], None]:
    METRIC = Gauge("amarillo_trips_number_total", "Total number of trips.")

    def instrumentation(info: Info) -> None:
        trips_count = sum([len(files) for r, d, files in os.walk("./data/carpool")])
        METRIC.set(trips_count)

    return instrumentation


router = APIRouter(
    prefix="/metrics",
    tags=["amarillo_metrics"]
)

@router.get("/")
def metrics(credentials: HTTPBasicCredentials = Depends(security)):
    if (credentials.username != secrets.metrics_user 
        or credentials.password != secrets.metrics_password):

        raise HTTPException(
            status_code=401,
            detail="Unauthorized",
            headers={"WWW-Authenticate": "Basic"},
        )
    
    # total_requests_metric.labels(endpoint="/amarillo-metrics").inc()
    return PlainTextResponse(content=generate_latest())


#TODO: maybe replace with an @setup decorator? would make it more obvious this is invoked from outside
def setup(app: FastAPI):
    app.include_router(router)


    instrumentator = Instrumentator().instrument(app)
    instrumentator.add(pfi_metrics.default())
    instrumentator.add(amarillo_trips_number_total())


    instrumentator.instrument(app)