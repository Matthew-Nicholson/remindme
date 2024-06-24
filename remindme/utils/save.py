from remindme.decorators.db_session import db_session
from remindme.models.reminders import Reminder


@db_session
def save(time: str, reminder: str):
    """
    Save the reminder to the database.
    """
    return Reminder(time=time, reminder=reminder)
