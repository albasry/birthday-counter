import datetime


# "people" function is to add and save data in the dictionary
def people(names, ages, name_day, names_dic):
    # Here I set the value as a list to output two pieces of information
    # at the same time for the same key
    names_dic[names] = [ages, name_day]
    return names_dic


add_names = dict()


def main_inputs():
    while True:
        input_name = input('Enter the name: ').strip().capitalize()

        # We put some conditions to force the user
        # to enter valid inputs for ( year, month, day) variables
        while True:
            try:
                year = int(input('Enter a year: ').strip())
                if 0 < year <= datetime.date.today().year:
                    break
                else:
                    print(f'Invalid date. For {input_name}.')
            except ValueError:
                print(f'Invalid date. For {input_name}.')
        while True:
            try:
                month = int(input('Enter a month: ').strip())
                if 0 < month <= 12:
                    break
                else:
                    print(f'Invalid date. For {input_name}.')
            except ValueError:
                # print('Invalid date. Please try again.')
                print(f'Invalid date. For {input_name}.')
        while True:
            try:
                day = int(input('Enter a day: ').strip())
                if 0 < day <= 31:
                    break
                else:
                    print(f'Invalid date. For {input_name}.')
            except ValueError:
                # print('Invalid date. Please try again.')
                print(f'Invalid date. For {input_name}.')

        year_month_day = datetime.date(year, month, day)
        # Age calculation = What date today - What date the user input
        # like( 2023 - 1920 )
        age = year_month_day.today().year - year_month_day.year
        name_of_day = year_month_day.strftime('%A')

        people_adding = people(input_name, age, name_of_day, add_names)
        for key, value in people_adding.items():
            # Hunt data from the index list[0], list[1], ...
            print('-', key, 'is', value[0], f'Years old, and she/he is born at', value[1])
        # ================================================================
        if len(people_adding) == 1:
            print('- There is no oldest or youngest person')
        else:
            # Use the built-in "min" and "max" functions to find the oldest and youngest persons,
            # These functions eliminate the need for loops and additional variables
            # to keep track of the maximum and minimum values.
            max_key = max(people_adding, key=people_adding.get)
            print('- The oldest one is', max_key)
            min_key = min(people_adding, key=people_adding.get)
            print('- The youngest one is', min_key)
        # ===============================================================
        print('- Total People: ', len(people_adding))
        # =========================================================
        # This option to give the user decision "continue or stop"
        decision = ''
        while decision not in ('y', 'n'):
            decision = input('Do you want to continue (y/n)?: ').lower()
        if decision == 'n':
            exit()


main_inputs()
