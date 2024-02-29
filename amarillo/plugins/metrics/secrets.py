from pydantic import Field, ConfigDict
from pydantic_settings import BaseSettings
# Example: secrets = { "mfdz": "some secret" }
class Secrets(BaseSettings):
    model_config = ConfigDict(extra='allow')
    metrics_user: str = Field(env = 'METRICS_USER')
    metrics_password: str = Field(env = 'METRICS_PASSWORD')

secrets = Secrets(_env_file='secrets', _env_file_encoding='utf-8')

