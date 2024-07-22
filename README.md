# amarillo-metrics

Amarillo plugin that provides Prometheus metrics

The metrics can be accessed with the `/` endpoint. HTTP basic authentication is used to protect it, the username and password can be configured through the `METRICS_USER` and `METRICS_PASSWORD` environment variables which you can optionally place in a file titled `secrets` in the Amarillo root directory.

## Installation

```
pip install amarillo-metrics
```

This package will install inside the amarillo/plugins folder in your python environment. Next time you launch Amarillo, it should be discovered automatically and you should see some messages like this:

```
INFO - Discovered plugins: ['amarillo.plugins.metrics', ...]
...
INFO - Running setup function for amarillo.plugins.metrics
```

## Provided metrics

In addition to the default metrics provided by the `prometheus_fastapi_instrumentator` library, `amarillo-metrics` provides the following data:

| Metric name     | Description               |
|-----------------------------|--------------------------------------------------------|
| amarillo_trips_created      | Shows how many trips have been created                 |
| amarillo_trips_updated      | Shows many existing trips have been updated            |
| amarillo_trips_deleted      | Shows how many trips have been deleted                 |
| amarillo_gtfs_downloads     | Shows the number of times the GTFS data was downloaded |
| amarillo_gtfs_file_size     | Total file size of GTFS data                           |
| amarillo_trips_number_total | The total number of trips stored by Amarillo           |
| amarillo_errors             | Number of errors in the error.log file                 |

## Example output

```
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 13967.0
python_gc_objects_collected_total{generation="1"} 12387.0
python_gc_objects_collected_total{generation="2"} 3551.0
# HELP python_gc_objects_uncollectable_total Uncollectable objects found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 1166.0
python_gc_collections_total{generation="1"} 105.0
python_gc_collections_total{generation="2"} 8.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="9",patchlevel="2",version="3.9.2"} 1.0
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 1.438466048e+09
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 3.35314944e+08
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1.72068979128e+09
# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 3219.7999999999997
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 25.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 8192.0
# HELP amarillo_gtfs_downloads_total How many times GTFS data was downloaded
# TYPE amarillo_gtfs_downloads_total counter
amarillo_gtfs_downloads_total 0.0
# HELP amarillo_gtfs_downloads_created How many times GTFS data was downloaded
# TYPE amarillo_gtfs_downloads_created gauge
amarillo_gtfs_downloads_created 1.7206897945591528e+09
# HELP amarillo_grfs_downloads_total How many times GRFS data was downloaded
# TYPE amarillo_grfs_downloads_total counter
amarillo_grfs_downloads_total 0.0
# HELP amarillo_grfs_downloads_created How many times GRFS data was downloaded
# TYPE amarillo_grfs_downloads_created gauge
amarillo_grfs_downloads_created 1.720689794559193e+09
# HELP amarillo_trips_created_total How many trips have been created
# TYPE amarillo_trips_created_total counter
amarillo_trips_created_total 0.0
# HELP amarillo_trips_created_created How many trips have been created
# TYPE amarillo_trips_created_created gauge
amarillo_trips_created_created 1.7206897945592172e+09
# HELP amarillo_trips_updated_total How many existing trips have been updated
# TYPE amarillo_trips_updated_total counter
amarillo_trips_updated_total 0.0
# HELP amarillo_trips_updated_created How many existing trips have been updated
# TYPE amarillo_trips_updated_created gauge
amarillo_trips_updated_created 1.7206897945592382e+09
# HELP amarillo_trips_deleted_total How many trips have been deleted
# TYPE amarillo_trips_deleted_total counter
amarillo_trips_deleted_total 0.0
# HELP amarillo_trips_deleted_created How many trips have been deleted
# TYPE amarillo_trips_deleted_created gauge
amarillo_trips_deleted_created 1.7206897945592575e+09
# HELP http_requests_total Total number of requests by method, status and handler.
# TYPE http_requests_total counter
http_requests_total{handler="/metrics",method="GET",status="3xx"} 6.0
http_requests_total{handler="/metrics/",method="GET",status="4xx"} 4.0
# HELP http_requests_created Total number of requests by method, status and handler.
# TYPE http_requests_created gauge
http_requests_created{handler="/metrics",method="GET",status="3xx"} 1.721213705555679e+09
http_requests_created{handler="/metrics/",method="GET",status="4xx"} 1.7212137055845356e+09
# HELP http_request_size_bytes Content length of incoming requests by handler. Only value of header is respected. Otherwise ignored. No percentile calculated. 
# TYPE http_request_size_bytes summary
http_request_size_bytes_count{handler="/metrics"} 6.0
http_request_size_bytes_sum{handler="/metrics"} 3824.0
http_request_size_bytes_count{handler="/metrics/"} 4.0
http_request_size_bytes_sum{handler="/metrics/"} 1912.0
# HELP http_request_size_bytes_created Content length of incoming requests by handler. Only value of header is respected. Otherwise ignored. No percentile calculated. 
# TYPE http_request_size_bytes_created gauge
http_request_size_bytes_created{handler="/metrics"} 1.721213705555746e+09
http_request_size_bytes_created{handler="/metrics/"} 1.7212137055846236e+09
# HELP http_response_size_bytes Content length of outgoing responses by handler. Only value of header is respected. Otherwise ignored. No percentile calculated. 
# TYPE http_response_size_bytes summary
http_response_size_bytes_count{handler="/metrics"} 6.0
http_response_size_bytes_sum{handler="/metrics"} 0.0
http_response_size_bytes_count{handler="/metrics/"} 4.0
http_response_size_bytes_sum{handler="/metrics/"} 100.0
# HELP http_response_size_bytes_created Content length of outgoing responses by handler. Only value of header is respected. Otherwise ignored. No percentile calculated. 
# TYPE http_response_size_bytes_created gauge
http_response_size_bytes_created{handler="/metrics"} 1.7212137055558207e+09
http_response_size_bytes_created{handler="/metrics/"} 1.7212137055847287e+09
# HELP http_request_duration_highr_seconds Latency with many buckets but no API specific labels. Made for more accurate percentile calculations. 
# TYPE http_request_duration_highr_seconds histogram
http_request_duration_highr_seconds_bucket{le="0.01"} 8.0
http_request_duration_highr_seconds_bucket{le="0.025"} 10.0
http_request_duration_highr_seconds_bucket{le="0.05"} 10.0
http_request_duration_highr_seconds_bucket{le="0.075"} 10.0
http_request_duration_highr_seconds_bucket{le="0.1"} 10.0
http_request_duration_highr_seconds_bucket{le="0.25"} 10.0
http_request_duration_highr_seconds_bucket{le="0.5"} 10.0
http_request_duration_highr_seconds_bucket{le="0.75"} 10.0
http_request_duration_highr_seconds_bucket{le="1.0"} 10.0
http_request_duration_highr_seconds_bucket{le="1.5"} 10.0
http_request_duration_highr_seconds_bucket{le="2.0"} 10.0
http_request_duration_highr_seconds_bucket{le="2.5"} 10.0
http_request_duration_highr_seconds_bucket{le="3.0"} 10.0
http_request_duration_highr_seconds_bucket{le="3.5"} 10.0
http_request_duration_highr_seconds_bucket{le="4.0"} 10.0
http_request_duration_highr_seconds_bucket{le="4.5"} 10.0
http_request_duration_highr_seconds_bucket{le="5.0"} 10.0
http_request_duration_highr_seconds_bucket{le="7.5"} 10.0
http_request_duration_highr_seconds_bucket{le="10.0"} 10.0
http_request_duration_highr_seconds_bucket{le="30.0"} 10.0
http_request_duration_highr_seconds_bucket{le="60.0"} 10.0
http_request_duration_highr_seconds_bucket{le="+Inf"} 10.0
http_request_duration_highr_seconds_count 10.0
http_request_duration_highr_seconds_sum 0.07150086999172345
# HELP http_request_duration_highr_seconds_created Latency with many buckets but no API specific labels. Made for more accurate percentile calculations. 
# TYPE http_request_duration_highr_seconds_created gauge
http_request_duration_highr_seconds_created 1.720689794571802e+09
# HELP http_request_duration_seconds Latency with only few buckets by handler. Made to be only used if aggregation by handler is important. 
# TYPE http_request_duration_seconds histogram
http_request_duration_seconds_bucket{handler="/metrics",le="0.1",method="GET"} 6.0
http_request_duration_seconds_bucket{handler="/metrics",le="0.5",method="GET"} 6.0
http_request_duration_seconds_bucket{handler="/metrics",le="1.0",method="GET"} 6.0
http_request_duration_seconds_bucket{handler="/metrics",le="+Inf",method="GET"} 6.0
http_request_duration_seconds_count{handler="/metrics",method="GET"} 6.0
http_request_duration_seconds_sum{handler="/metrics",method="GET"} 0.02843798598041758
http_request_duration_seconds_bucket{handler="/metrics/",le="0.1",method="GET"} 4.0
http_request_duration_seconds_bucket{handler="/metrics/",le="0.5",method="GET"} 4.0
http_request_duration_seconds_bucket{handler="/metrics/",le="1.0",method="GET"} 4.0
http_request_duration_seconds_bucket{handler="/metrics/",le="+Inf",method="GET"} 4.0
http_request_duration_seconds_count{handler="/metrics/",method="GET"} 4.0
http_request_duration_seconds_sum{handler="/metrics/",method="GET"} 0.04306288401130587
# HELP http_request_duration_seconds_created Latency with only few buckets by handler. Made to be only used if aggregation by handler is important. 
# TYPE http_request_duration_seconds_created gauge
http_request_duration_seconds_created{handler="/metrics",method="GET"} 1.7212137055559032e+09
http_request_duration_seconds_created{handler="/metrics/",method="GET"} 1.7212137055848691e+09
# HELP amarillo_trips_number_total Total number of trips.
# TYPE amarillo_trips_number_total gauge
amarillo_trips_number_total 2.0
# HELP amarillo_gtfs_file_size_MB Total file size of GTFS data.
# TYPE amarillo_gtfs_file_size_MB gauge
amarillo_gtfs_file_size_MB 12.301814
# HELP amarillo_grfs_file_size_MB Total file size of GRFS data.
# TYPE amarillo_grfs_file_size_MB gauge
amarillo_grfs_file_size_MB 0.0
# HELP amarillo_errors Number of errors in the error.log file
# TYPE amarillo_errors gauge
amarillo_errors 36.0

```