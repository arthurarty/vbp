from utils.date import time_now_as_string


user_1 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'dob': '20/02/1990',
    'password': 'qwe',
    'repeatPassword': 'qwe',
    'email': 'john.doe@example.com',
    'phone_number': '256703201444',
    'phone_number2': '256703201444',
}

# password mismatch
user_2 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'dob': '20/02/1990',
    'password': 'qwe',
    'repeatPassword': 'qwertywer',
    'email': 'john.doe@example.com',
    'phone_number': '256703201444',
    'phone_number2': '256703201464',
}

# user older than 70
user_aged_80 = {
    'first_name': 'Luke',
    'last_name': 'Bin',
    'dob': '13/09/1933',
    'password': 'qwertywer',
    'repeatPassword': 'qwertywer',
    'email': 'luke.bin@example.com',
    'phone_number': '256703201456',
    'phone_number2': '256703201456',
}

# wrong date format
user_4 = {
    'first_name': 'Luke',
    'last_name': 'Bin',
    'dob': '13091933',
    'password': 'qwertywer',
    'repeatPassword': 'qwertywer',
    'email': 'luke.bin@example.com',
    'phone_number': '256703201456',
    'phone_number2': '256703201456',
}

# user below 18
user_5 = {
    'first_name': 'Bill',
    'last_name': 'Bin',
    'dob': time_now_as_string(),
    'password': 'qwertywer',
    'repeatPassword': 'qwertywer',
    'email': 'luk.bin@example.com',
    'phone_number': '256703201456',
    'phone_number2': '256703201456',
}
