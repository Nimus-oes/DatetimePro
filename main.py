import inputdata, cmd_calc, sys

def should_continue():
    flag = inputdata.input_choice(
        prompt="Keep using? (Y/N): ",
        choice_list=["y", "n"],
        choice_type=str
    )

    if flag == 'n':
        print("Program ended")
        sys.exit()


def main():
    menu_func = [
        ("D-Day", cmd_calc.cmd_dday),
        ("Days Elapsed between Two Dates", cmd_calc.cmd_elapsed),
        ("Matching Date", cmd_calc.cmd_matchingd),
        ("Day of the Week", cmd_calc.cmd_weekday),
        ("Age", cmd_calc.cmd_age),
        ("[Exit]", sys.exit)
    ]

    menu_text = """"""
    menu_list = []

    for index, item in enumerate(menu_func):
        menu_list.append(index + 1)
        menu_text += f"{index + 1}. {item[0]}\n"


    menu_display = f"""
==========DatetimePro Menu==========
{menu_text}
"""

    while True:
        print(menu_display)
        menu_num = inputdata.input_choice(
            prompt="Enter a menu number: ",
            choice_list=menu_list,
            choice_type=int
        )

        menu_func[menu_num - 1][1]()

        should_continue()


if __name__ == "__main__":
    main()