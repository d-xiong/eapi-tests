#!/usr/bin/python3
from faker import Faker
import random
import time


fake = Faker()
max_length = 256


def fuzz_strings():
    # TODO - Add in random call for a fuzz method.
    pass


def fuzz_bools():
    # TODO - Add in random call for a fuzz method.
    pass


def fuzz_ints():
    # TODO - Add in random call for a fuzz method.
    pass


def fuzz_floats():
    # TODO - Add in random call for a fuzz method.
    pass


""" 
Fuzz methods below???
"""


def fuzzer_max_string():
    return fake.pystr(max_length, max_length)


def fuzzer_max_int():
    return int(fake.pyfloat(max_length, 0, True))


def fuzzer_negative_number():
    return fake.random_number(10, False) * -1


def fuzzer_bool():
    return random.choice(True, False, 0, 1)


def fuzzer_invalid_timezone():
    valid_timezones = [
        "America/New_York",
        "America/Chicago",
        "America/Denver",
        "America/Phoenix",
        "America/Los_Angeles",
        "America/Anchorage",
        "America/Adak",
        "Pacific/Honolulu"
    ]

    the_timezone = fake.timezone()

    while the_timezone in valid_timezones:
        the_timezone = fake.timezone()

    return the_timezone


def fuzzer_datetime_format():
    the_time = time.localtime(time.time())
    the_time_formatted = [
            time.strftime('%Y-%m-%d %H:%M:%S', the_time),
            time.strftime('%m-%d-%Y %H:%M:%S', the_time),
            time.strftime('%d-%m-%Y %H:%M:%S', the_time),
            time.strftime('%Y/%m/%d %H:%M:%S', the_time),
            time.strftime('%m/%d/%Y %H:%M:%S', the_time),
            time.strftime('%d/%m/%Y %H:%M:%S', the_time)
        ]
    return random.choice(the_time_formatted)
