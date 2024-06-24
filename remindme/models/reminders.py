from sqlalchemy import Column, Integer, String

from remindme.models.base import Base


class Reminder(Base):
    __tablename__ = "reminders"

    id = Column(Integer, primary_key=True)
    time = Column(String)
    reminder = Column(String)
