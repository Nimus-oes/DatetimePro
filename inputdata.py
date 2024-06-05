from datetime import date, datetime, timezone, timedelta
import zoneinfo


def timezone_obj(custom_tz=None):
    """
    Creates a timezone object
    """
    if custom_tz: 
        all_tz = zoneinfo.available_timezones()
        while True:
            tz_identifier = input("Enter the time zone: ")
            if tz_identifier in all_tz:
                return zoneinfo.ZoneInfo(tz_identifier)
            else:
                print("Invalid time zone identifier. Provide the correct name.")

    return timezone.utc
   

def input_date(prompt: str, tz_obj=None):
    """
    Prompts the user to input a date in 'YYYY-MM-DD' format.
    Returns an aware datetime object.
    """
    if not tz_obj:
        tz_obj = timezone_obj()

    while True:
        date_input = input(prompt)
        try:
            naive_date = datetime.strptime(date_input, '%Y-%m-%d')
        except ValueError:
            print("Invalid date value.")
            continue
        aware_date = naive_date.replace(tzinfo=tz_obj)
        return aware_date
    

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


def input_int(prompt: str) -> int:
    """
    Receive integer input as string and converts it to integer
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Input must be an integer type.")


def input_choice(prompt: str, choice_list: list, choice_type):
    """
    Prompts the user to input a choice from a set of options.
    """
    while True:
        choice = input_int(prompt) if choice_type == int else input(prompt).strip().lower()

        if choice in choice_list:
            return choice
        else:
            print(f"No menu found. Please choose from {choice_list}.")


def current_dt_obj(custom_tz='local', tz_obj=None):
    """
    Returns a current datetime object. 
    """
    now = datetime.now(tz=timezone.utc)
    if custom_tz == 'local':
        return now.astimezone()
    elif custom_tz == 'utc':
        return now
    elif custom_tz == 'other' and tz_obj:
        return now.astimezone(tz=tz_obj)
    raise ValueError("Invalid custom_tz value.")
