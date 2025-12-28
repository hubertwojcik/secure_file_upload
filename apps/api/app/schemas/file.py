from pydantic import BaseModel
from datetime import datetime
from app.db.enums import FileStatus

class FileOut(BaseModel):
    id: str
    original_name: str
    content_type: str | None
    size_bytes: int
    sha256: str
    status: FileStatus
    verdict_reason: str | None
    created_at: datetime
    scanned_at: datetime | None

    class Config:
        from_attributes = True

class UploadResponse(BaseModel):
    id: str
    status: FileStatus