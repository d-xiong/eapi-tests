#!/usr/bin/python3
import random
from faker import Faker


fake = Faker()


def grab_address_one():
    return fake.street_address()


def grab_address_two():
    return fake.secondary_address()


def grab_bool():
    return fake.boolean()


def grab_building_number():
    return fake.building_number()


def grab_city():
    return fake.city()


def grab_company():
    return fake.company()


def grab_credit_score():
    """
    Actual credit scores are not used due to HIPAA. Instead, we store
    generalizations of their credit score, as strings.

    :return: str, the selected.
    """

    credit_options = ['Excellent', 'Good', 'Fair', 'Poor', 'Very Poor']
    return random.choice(credit_options)


def grab_decimal():
    return fake.pyfloat(left_digits=2, right_digits=2, positive=True)


def grab_email(name):
    return "{}@example.com".format(name)


def grab_external_id(name):

    return "external.id.{}".format(name)


def grab_external_status(name, index="status"):
    return "external.{}.{}".format(index, name)


def grab_fake_date():
    return '{0:%Y-%m-%d %H:%M:%S}'.format(fake.date_this_century())


def grab_first_name():
    return fake.first_name()


def grab_full_name():
    return fake.name()


def grab_image_url():
    return fake.image_url()


def grab_job():
    return fake.job()


def grab_large_int():
    return fake.random_number(12, True)


def grab_last_name():
    return fake.last_name()


def grab_money():
    return fake.pyfloat(left_digits=6, right_digits=2, positive=True)


def grab_one_from_old_json(origin_json, target=None, index=0):
    """
    Receives a json of arrays. Grabs an array from the json.

    :param origin_json: json, the original.
    :param target: str, the target parameter.
    :param index: int, the target index.
    :return: array, the data.
    """

    if target is None:
        return []
    else:
        if target in origin_json:
            return [origin_json[target][index]]
        else:
            return []


def grab_one_from_validated_array(item, index="id"):
    """
    Validates the array, for empty. Returns index, or empty.

    :param item: array, the array object.
    :param index: str, the index.
    :return: array, the data.
    """

    if item is None:
        return []
    else:
        return [
            {
                index: item[index]
            }
        ]


def grab_percent():
    return fake.pyfloat(left_digits=3, right_digits=2, positive=True)


def grab_phone():
    return fake.phone_number()


def grab_phrase():
    return fake.bs()


def grab_prefix():
    return fake.prefix()


def grab_small_int():
    return fake.random_number(3, False)


def grab_source():
    return fake.bs()


def grab_state_abbr():
    """
    The site only support the 50 states and DC. This method is used in areas
    where validation for the "state" field is present.
    Faker supports US territories, so errors can occur if its state_abbr()
    is called.

    :return: str, the selected.
    """

    states = [
        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL",
        "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME",
        "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH",
        "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI",
        "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI",
        "WY"
    ]
    return random.choice(states)


def grab_suffix():
    return fake.suffix()


def grab_timezone():
    """
    The site only support these timezones.

    :return: str, the selected.
    """

    timezones = [
        "America/New_York",
        "America/Chicago",
        "America/Denver",
        "America/Phoenix",
        "America/Los_Angeles",
        "America/Anchorage",
        "America/Adak",
        "Pacific/Honolulu"
    ]
    return random.choice(timezones)


def grab_username():
    return fake.user_name()


def grab_user_type():
    """
    Grabs a user type, which is supported by the site. "Organization" is also
    supported, but is not applied here.

    :return: str, the selected.
    """

    return random.choice(["Lender", "Realtor", "Title"])


def grab_url():
    return fake.uri()


def grab_word():
    return fake.word()


def grab_zip():
    return fake.zipcode()
