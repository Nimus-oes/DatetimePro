import calc, inputdata

def cmd_dday():
    print("This feature calculates the remaining or elapsed days to a target date.")
    target_d = inputdata.input_date("Provide a target date (YY-MM-DD): ")
    current_d = inputdata.current_dt_obj('local')
    diff = calc.calc_elapsed_days(current_d, target_d)

    print(f"D+{-diff}" if diff < 0 else f"D-{diff}")


def cmd_elapsed():
    print("This feature calculates the elapsed days betwen two dates.")
    date1 = inputdata.input_date("Provide a date 1 (YY-MM-DD): ")
    date2 = inputdata.input_date("Provide a date 2 (YY-MM-DD): ")
    diff = calc.calc_elapsed_days(date1, date2)
    print(f"{abs(diff)} days")


def cmd_matchingd():
    print("This feature finds a date based on elapsed days from the base date.")
    elapsed_d = inputdata.input_int("Provide elapsed days in numbers only: ")
    base_d = inputdata.input_date("Provide a base date (YY-MM-DD): ")
    direction = inputdata.input_choice(
        prompt="Provide a direction to find a date (Forward/Backward): ",
        choice_list=["forward", "backward"],
        choice_type=str
    )
    match = calc.calc_matching_date(base_d, elapsed_d, direction)
    print(match)


def cmd_weekday():
    print("This feature finds a weekday of the provided date.")
    date = inputdata.input_date("Provide a date (YY-MM-DD): ")
    weekday = calc.calc_weekday(date)
    print(weekday)


def cmd_age():
    print("This feature calculates an age based on the birth date.")
    birthdate = inputdata.input_date("Provide a birth date (YY-MM-DD): ")
    current_d = inputdata.current_dt_obj(custom_tz='local')
    inputdata.validate_date(birthdate, "Birth date", "on or before", current_d)
    age = calc.calc_age(birthdate, current_d)
    print(f"{age} years old.")