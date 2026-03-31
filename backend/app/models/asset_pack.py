from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from app.core.database import Base

class AssetPackStatus(str, enum.Enum):
    DRAFT = "draft"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

class AssetPack(Base):
    __tablename__ = "asset_packs"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String(200), nullable=False)
    description = Column(Text)
    
    # 状态
    status = Column(Enum(AssetPackStatus), default=AssetPackStatus.DRAFT)
    progress = Column(Integer, default=0)
    
    # 导出
    export_url = Column(String(500))
    export_platforms = Column(Text, default="[]")
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
    user = relationship("User", back_populates="asset_packs")
    items = relationship("AssetItem", back_populates="asset_pack", cascade="all, delete")
    tasks = relationship("GenerationTask", back_populates="asset_pack")
