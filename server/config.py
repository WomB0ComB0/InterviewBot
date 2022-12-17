from dataclasses import dataclass
import os


@dataclass
class AppConfig:
    app_host: str
    app_port: int
    cohere_api_key: str
    db_address: str


def get_app_config() -> AppConfig:
    return AppConfig(
        app_host=os.getenv("APP_HOST"),
        app_port=os.getenv("APP_HOST"),
        cohere_api_key=os.getenv("COHERE_API_KEY"),
        db_address=os.getenv("DB_ADDRESS"),
    )
