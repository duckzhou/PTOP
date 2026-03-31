from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, Text
from sqlalchemy.sql import func
import enum
from app.core.database import Base

class TaskType(str, enum.Enum):
    REMOVE_BG = "remove_bg"
    IMG2IMG = "img2img"
    IMG2VIDEO = "img2video"
    PACKAGE_EXPORT = "package_export"

class TaskStatus(str, enum.Enum):
    PENDING = "pending"
    QUEUED = "queued"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

class GenerationTask(Base):
    __tablename__ = "generation_tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    asset_pack_id = Column(Integer, ForeignKey("asset_packs.id"), nullable=False)
    asset_item_id = Column(Integer, ForeignKey("asset_items.id"), nullable=True)
    
    task_type = Column(Enum(TaskType), nullable=False)
    status = Column(Enum(TaskStatus), default=TaskStatus.PENDING)
    priority = Column(Integer, default=5)
    
    # 输入输出
    input_data = Column(Text, default="{}")
    output_data = Column(Text, default="{}")
    error_message = Column(Text)
    
    # 进度
    progress = Column(Integer, default=0)
    progress_message = Column(String(200))
    
    # Celery 任务 ID
    celery_task_id = Column(String(100))
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
    asset_pack = relationship("AssetPack", back_populates="tasks")
