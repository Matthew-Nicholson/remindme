from remindme.utils.time_to_utc import time_to_utc


def save(time: str, reminder: str):
    """
    Save the reminder to the database.
    """
    time = time_to_utc(time)
