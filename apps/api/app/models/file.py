from sqlalchemy import String, BigInteger, DateTime, Enum, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.db.enums import FileStatus

class FileRecord(Base):
    __tablename__ = "files"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    original_name: Mapped[str] = mapped_column(String(255), nullable=False)
    content_type: Mapped[str | None] = mapped_column(String(255), nullable=True)
    size_bytes: Mapped[int] = mapped_column(BigInteger, nullable=False)
    sha256: Mapped[str] = mapped_column(String(64), nullable=False)
    
    status: Mapped[FileStatus] = mapped_column(Enum(FileStatus), nullable=False, default = FileStatus.PENDING_SCAN)
    verdict_reason: Mapped[str | None] = mapped_column(Text, nullable=True)
    
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone = True), nullable=False, default=lambda: datetime.now(timezone.utc))
    scannet_at: Mapped[datetime | None] = mapped_column(DateTime(timezone = True), nullable=True)    
    
    