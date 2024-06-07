import calculators, data

def dday():
    print("This feature calculates the remaining or elapsed days to a target date.")
    target_d = data.input_date("Provide a target date (YY-MM-DD): ")
    current_d = data.current_dt_obj('local')
    diff = calculators.elapsed_days(current_d, target_d)

    print(f"D+{-diff}" if diff < 0 else f"D-{diff}")


def elapsed():
    print("This feature calculates the elapsed days betwen two dates.")
    date1 = data.input_date("Provide a date 1 (YY-MM-DD): ")
    date2 = data.input_date("Provide a date 2 (YY-MM-DD): ")
    diff = calculators.elapsed_days(date1, date2)
    print(f"{abs(diff)} days")


def matching_date():
    print("This feature finds a date based on elapsed days from the base date.")
    elapsed_d = data.input_int("Provide elapsed days in numbers only: ")
    base_d = data.input_date("Provide a base date (YY-MM-DD): ")
    direction = data.input_choice(
        prompt="Provide a direction to find a date (Forward/Backward): ",
        choice_list=["forward", "backward"],
        choice_type=str
    )
    match = calculators.matching_date(base_d, elapsed_d, direction)
    print(match)


def weekday():
    print("This feature finds a weekday of the provided date.")
    date = data.input_date("Provide a date (YY-MM-DD): ")
    weekday = calculators.weekday(date)
    print(weekday)


def age():
    print("This feature calculates an age based on the birth date.")
    birthdate = data.input_date("Provide a birth date (YY-MM-DD): ")
    current_d = data.current_dt_obj(custom_tz='local')
    data.validate_date(birthdate, "Birth date", "on or before", current_d)
    age = calculators.age(birthdate, current_d)
    print(f"{age} years old.")