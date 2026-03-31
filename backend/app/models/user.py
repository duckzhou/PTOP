from sqlalchemy import Column, Integer, String, DateTime, Numeric, Boolean
from sqlalchemy.sql import func
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    name = Column(String(100))
    
    # 订阅与额度
    subscription_tier = Column(String(20), default="free")  # free/pro/enterprise
    credits_total = Column(Numeric(10, 2), default=0)
    credits_used = Column(Numeric(10, 2), default=0)
    credits_reset_at = Column(DateTime)
    
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
