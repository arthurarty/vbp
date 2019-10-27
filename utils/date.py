import datetime


def convert_date_string(date_string):
    """
    convert date string to date time object that
    can be stored in db
    """
    try:
        date = datetime.datetime.strptime(date_string, '%d/%m/%Y')
        return date
    except ValueError:
        raise ValueError


def calculate_age(dob):
    """
    Calculate and return the age of a user
    """
    current_date = datetime.datetime.now()
    return current_date.year - dob.year


def time_now_as_string():
    """
    Creates a date string in the format dd/mm/yyyy
    using the current date
    """
    date = datetime.datetime.now()
    return date.strftime('%d/%m/%Y')
