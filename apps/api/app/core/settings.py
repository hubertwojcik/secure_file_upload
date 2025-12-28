from pydantic import BaseModel
import os
from pathlib import Path

class Settings(BaseModel):
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    QUARANTINE_DIR: str = Path(os.getenv("QUARANTINE_DIR"))
    CLEAN_DIR: str = Path(os.getenv("CLEAN_DIR"))
    MAX_UPLOAD_BYTES: int = int(os.getenv("MAX_UPLOAD_BYTES"))

settings = Settings()

Path(settings.QUARANTINE_DIR).mkdir(parents=True, exist_ok=True)
Path(settings.CLEAN_DIR).mkdir(parents=True, exist_ok=True)