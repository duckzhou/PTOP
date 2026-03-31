from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from app.core.database import Base

class AssetItemType(str, enum.Enum):
    IMAGE = "image"
    VIDEO = "video"

class AssetItem(Base):
    __tablename__ = "asset_items"
    
    id = Column(Integer, primary_key=True, index=True)
    asset_pack_id = Column(Integer, ForeignKey("asset_packs.id"), nullable=False)
    type = Column(Enum(AssetItemType), nullable=False)
    
    # 源文件
    source_url = Column(String(500))
    
    # 处理结果
    result_url = Column(String(500))
    
    # 状态
    status = Column(String(20), default="pending")
    error_message = Column(Text)
    
    order_index = Column(Integer, default=0)
    created_at = Column(DateTime, server_default=func.now())
    
    asset_pack = relationship("AssetPack", back_populates="items")
