from datetime import date, datetime
from functools import wraps


def find_time_for_execute(func):
    @wraps(func)
    def cover(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        print(f'Function\'s \'{func.__name__}\' execution time was: {end - start} seconds.')
    return cover


@find_time_for_execute
def my_age_in_days(year: int, month: int, day: int):
    birthday = date(year, month, day)
    today = date.today()
    delta = today - birthday
    print(f'Today I have lived {delta.days} days.')
    
my_age_in_days(1991, 2, 22)