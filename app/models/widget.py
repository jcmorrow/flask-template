from app import db

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime


class Widget(db.Model):
    __tablename__ = 'widgets'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    quantity = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
