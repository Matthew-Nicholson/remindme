from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Reminder(Base):
    __tablename__ = "reminders"

    id = Column(Integer, primary_key=True)
    TIMESTAMP = Column(DateTime(timezone=True), server_default=func.now())
    user = Column(String)
    time = Column(DateTime)
    message = Column(String)
    channel = Column(String)
    guild = Column(String)
    delivered = Column(Integer, default=0)
    deleted = Column(Integer, default=0)
