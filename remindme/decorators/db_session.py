from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from functools import wraps

# Models
from remindme.models.base import Base
from remindme.models.reminders import Reminder  # noqa: F401

DB_URI = "sqlite:///remindme.db"
Engine = create_engine(DB_URI)
Session = sessionmaker(bind=Engine)
Base.metadata.create_all(Engine)


def db_session(func):
    """
    Decorator to create a database session.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        session = Session()
        try:
            result = func(*args, **kwargs)
            session.add(result)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    return wrapper
