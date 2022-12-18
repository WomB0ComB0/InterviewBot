from dataclasses import dataclass
from dotenv import load_dotenv
from enum import Enum
import os


class Environment(Enum):
    PROD = "prod"
    DEV = "dev"

    @staticmethod
    def value_of(item: str) -> "Environment":
        type_map = {"prod": Environment.PROD, "dev": Environment.DEV}

        enum_val = type_map.get(item.lower(), None)

        if enum_val is None:
            raise ValueError(f"{item} is not a valid enum value")

        return enum_val


@dataclass
class AppConfig:
    app_host: str
    app_port: int
    cohere_api_key: str
    db_address: str

    @staticmethod
    def new_config(environ: str) -> "AppConfig":
        env = Environment.value_of(environ)

        if env == Environment.DEV:
            load_dotenv()

        return AppConfig(
            app_host=os.getenv("HOST"),
            app_port=int(os.getenv("PORT")),
            cohere_api_key=os.getenv("COHERE_API_KEY"),
            db_address=os.getenv("DB_ADDRESS"),
        )
