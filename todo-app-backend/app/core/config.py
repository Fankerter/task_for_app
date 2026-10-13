import os
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[1] / ".env")


@dataclass(frozen=True)
class Settings:
    database_url: str
    cors_origins: list[str]


def get_settings() -> Settings:
    return Settings(
        database_url=os.getenv("DATABASE_URL"),
        cors_origins=os.getenv("CORS_ORIGINS").split(",")
    )


