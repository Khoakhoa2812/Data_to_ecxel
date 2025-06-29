from pydantic_settings import BaseSettings
from functools import lru_cache
from pydantic import Field, HttpUrl


class Settings(BaseSettings):
    # DATABASE_URL: str
    # SUPABASE_KEY: str
    # SUPABASE_BUCKET_NAME: str  # default bucket
    # LOG_LEVEL: str = "INFO"
    SECRET_KEY: str
    #
    # redis_url: str = Field(..., env="REDIS_URL")
    #
    # ollama_api_url: HttpUrl = Field(..., env="OLLAMA_API_URL")
    # ollama_model_name: str = Field(..., env="OLLAMA_MODEL_NAME")
    # ollama_request_timeout: int = Field(default=300, description="Default timeout for Ollama requests in seconds.", env="OLLAMA_REQUEST_TIMEOUT")
    # ollama_complex_task_timeout: int = Field(default=600, description="Timeout for complex Ollama tasks (e.g., CV analysis) in seconds.", env="OLLAMA_COMPLEX_TASK_TIMEOUT")
    #
    # rate_limit: str = Field(default="10/minute", env="RATE_LIMIT")
    #
    # celery_broker_url: str | None = None
    # celery_result_backend: str | None = None


    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

    def __init__(self, **values):
        super().__init__(**values)
    #     # Use the same Redis URL for Celery if not explicitly set
    #     if self.celery_broker_url is None:
    #         self.celery_broker_url = self.redis_url
    #     if self.celery_result_backend is None:
    #         self.celery_result_backend = self.redis_url


@lru_cache()
def get_settings() -> Settings:
    return Settings()