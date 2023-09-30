from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey
from .database import Base
from datetime import datetime

class Student(Base):
    __tablename__ = "student"
    id = Column(String, primary_key=True, index=True)
    name = Column(Text)
    email = Column(Text)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)