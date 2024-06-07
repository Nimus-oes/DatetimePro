from datetime import datetime, timedelta

def elapsed_days(date1: datetime, date2: datetime) -> int:
    """
    Calculates the remaining or elpased days bewteen two dates.
    Subtracts date1 from date2 and returns the difference in days.
    """
    # Convert both dates to naive objects with date() for simpler day calculation
    return (date2.date() - date1.date()).days


def matching_date(base_date: datetime, elapsed_days: int, direction: str) -> datetime:
    delta = timedelta(days=elapsed_days)
    matching_d = base_date + delta if direction == 'forward' else base_date - delta
    
    # Return the matching date in simpler naive format with date()
    return matching_d.date()


def age(birthdate: datetime, today: datetime) -> int:
    # Subtract birth year from current year and then subtract 1 more if the birthday has happened this year yet.
    # if ((birthdate.month, birthdate.day) > (today.month, today.day)) is true, it subtracts 1 or 0 if False.
    return today.year - birthdate.year - ((birthdate.month, birthdate.day) > (today.month, today.day))


def weekday(date: datetime) -> str:
    weekday = date.weekday()
    weekday_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    return weekday_list[weekday]