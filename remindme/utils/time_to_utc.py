from datetime import datetime, timezone
import calendar


def time_to_utc(time_string: str) -> str:
    """
    Convert a given time to UTC.
    """
    # TODO Hi zay :D
    #TODO: Hey Matt!
    split_time_string = time_string.split(" ")
    timeElements = {}
    thing_to_remind = ""
    for index, word in enumerate(split_time_string):
        if word.isnumeric() and split_time_string[index + 1].isalpha():
            timeElements[split_time_string[index + 1]] = int(word)
            thing_to_remind = " ".join(split_time_string[index + 2:])
            break

    #You can replace these with the current time. They were fixed for testing
    time_to_remind = {
        "year": datetime.today().year,
        "month": 12,
        "day": 31,
        "hour": 20,
        "minute": 31,
    }

    year =time_to_remind['year']
    month =time_to_remind['month']
    day =time_to_remind['day']
    hour = time_to_remind['hour']
    minute = time_to_remind['minute']

    MINUTES_IN_HOUR = 60
    MONTHS_IN_YEAR = 12
    HOURS_IN_DAY = 24

    minute += timeElements["minutes"]

    if(minute >= MINUTES_IN_HOUR):
        hour += minute // MINUTES_IN_HOUR
        minute = minute % MINUTES_IN_HOUR #Remaining minutes


    if(hour >= HOURS_IN_DAY):
        day+= hour // HOURS_IN_DAY
        # In the event the user puts some absurd number, using module will grab the remainder
        hour %= HOURS_IN_DAY

    while True:
        days_in_month =calendar.monthrange(year,month)[1]
        if(day > days_in_month):
            day -= days_in_month
            month += 1
            if(month > MONTHS_IN_YEAR):
                month = 1
                year += 1
        else:
            break

    t = datetime(year, month, day, hour, minute, datetime.now().second, datetime.now().microsecond,tzinfo=timezone.utc)
    return str(t)
