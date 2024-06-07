from datetime import date, datetime, timezone, timedelta
import zoneinfo

def retry_input(message):
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            while True:
                try:
                    result = func(*args, **kwargs)
                    break
                except:
                    print(message)
            return result
        return wrapper
    return outer_wrapper


@retry_input("Invalid time zone identifier. Provide the correct name.")
def input_timezone():
    tz_identifier = input("Enter the time zone: ")
    return zoneinfo.ZoneInfo(tz_identifier)
    

@retry_input("Invalid date value.")
def input_date(prompt: str) -> datetime:
    """
    Prompts the user to input a date in 'YYYY-MM-DD' format.
    Returns an aware datetime object, setting the time value as 0 in UTC+0 timezone
    """
    date_input = input(prompt)

    # replace() is used to keep the time value 0.
    # If use astimezone(), the time value will be changed as per the timezone.
    return datetime.strptime(date_input, '%Y-%m-%d').replace(tzinfo=timezone.utc)


@retry_input("Input must be an integer type.")
def input_int(prompt: str) -> int:
    """
    Receive integer input as string and converts it to integer
    """
    return int(input(prompt))


@retry_input("Invalid input. Please provide the correct option.")
def input_choice(prompt: str, choice_list: list, choice_type):
    """
    Prompts the user to input a choice from a set of options.
    """
    choice = int(input(prompt)) if choice_type == int else input(prompt).strip().lower()

    if choice not in choice_list:
        raise ValueError
    
    return choice


def validate_date(date: datetime, date_name: str, basis: str, value: datetime):
    """
    Validates a date input to be on or before/after a certain date.
    """
    basis_options = {
        'before': date < value, 
        'on or before': date <= value, 
        'after': date > value, 
        'on or after': date >= value
    }

    if basis not in basis_options:
        raise ValueError(f"Available basis values: {list(basis_options.keys())}")

    assert basis_options[basis], f"{date_name} must be {basis} {value}"

    return True


def current_dt_obj(custom_tz='local', tz_obj=None):
    """
    Returns an aware current datetime object. 
    """
    now = datetime.now(tz=timezone.utc)
    if custom_tz == 'local':
        return now.astimezone()
    elif custom_tz == 'utc0':
        return now
    elif custom_tz == 'other' and tz_obj:
        return now.astimezone(tz=tz_obj)
    raise ValueError("Invalid custom_tz value.")