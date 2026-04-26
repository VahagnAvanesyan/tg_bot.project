from sqlalchemy import Column, BigInteger, String, DateTime
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"

    id          = Column(BigInteger, primary_key=True)  # Telegram user_id
    first_name  = Column(String(100))
    last_name   = Column(String(100), nullable=True)
    username    = Column(String(100), nullable=True)
    photo_url   = Column(String(500), nullable=True)
    created_at  = Column(DateTime, server_default=func.now())