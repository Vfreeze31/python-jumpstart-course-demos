import datetime

def print_header():
    print('------------------------')
    print('     BIRTHDAY APP')
    print('------------------------')
    print()


def get_birthday_from_user():
    print('Tell us when you were born: ')
    year = int(input('What year were you born [YYYY]? '))
    month = int(input('What month were you born [MM]? '))
    day = int(input('What day were you born [DD]? '))
    print()

    birthday = datetime.datetime(year,month,day)
    return birthday


def compute_days_between_bday_and_now(birthday):
    now = datetime.datetime.now()
    bday = datetime.datetime(now.year,birthday.month,birthday.day)
    dt = now - bday
    days = int(dt.total_seconds() / 60 / 60 / 24)
    return days


def print_birthday_information(days):
    if days < 0:
        print('Your birthday is in {} days.'.format(-days))
    elif days > 0:
        print('You had your birthday {} days ago.'.format(days))
    else:
        print('Happy BIRTHDAY!!!')


def main():
    print_header()
    bday = get_birthday_from_user()
    number_of_days = compute_days_between_bday_and_now(bday)
    print_birthday_information(number_of_days)


main()