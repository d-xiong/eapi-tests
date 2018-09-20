#!/usr/bin/python3
import time
import json
import python.common.datagenerators.generatefakedata as fake
from python.eapi.methods.users.user import User
from python.eapi.methods.contactgroups.contactgroup import ContactGroup


def grab_post_json(user=None, name="lead"):
    """
    Grabs json for post endpoint.

    :return: json, the data.
    """

    the_name = "{}.test.x.{}".format(name, int(time.time()))
    if user is None:
        user = User().choose_random()
    cgroup = ContactGroup().choose_random()

    return json.dumps(
        {
            "title": fake.grab_prefix(),
            "first_name": fake.grab_first_name(),
            "last_name": fake.grab_last_name(),
            "suffix": fake.grab_suffix(),
            "nickname": fake.grab_username(),
            "email": fake.grab_email(the_name),
            "email_work": "work.{}".format(fake.grab_email(the_name)),
            "ok_to_email": fake.grab_bool(),
            "address": fake.grab_address_one(),
            "address_2": fake.grab_address_two(),
            "city": fake.grab_city(),
            "state": fake.grab_state_abbr(),
            "zip_code": fake.grab_zip(),
            "ok_to_mail": fake.grab_bool(),
            "phone_cell": fake.grab_phone(),
            "phone_office": fake.grab_phone(),
            "phone_home": fake.grab_phone(),
            "ok_to_call": fake.grab_bool(),
            "employer_name": fake.grab_company(),
            "employer_address": fake.grab_address_one(),
            "employer_address_2": fake.grab_address_two(),
            "employer_city": fake.grab_city(),
            "employer_state": fake.grab_state_abbr(),
            "employer_zip": fake.grab_zip(),
            "employer_license_number": fake.grab_large_int(),
            "license_number": fake.grab_large_int(),
            "source": fake.grab_source(),
            "last_modified_date": fake.grab_fake_date(),
            "creation_date": fake.grab_fake_date(),
            "last_contacted_date": fake.grab_fake_date(),
            "referred_to": fake.grab_full_name(),
            "referred_by": fake.grab_full_name(),
            "classification": fake.grab_large_int(),
            "list_date": fake.grab_fake_date(),
            "close_date": fake.grab_fake_date(),
            "external_id": fake.grab_external_id(the_name),
            "credit_score": fake.grab_credit_score(),
            "birthday": fake.grab_fake_date(),
            "credit_score_date": fake.grab_fake_date(),
            "credit_score_expiration_date": fake.grab_fake_date(),
            "linkedin_url": fake.grab_url(),
            "website_url": fake.grab_url(),
            "other_url": fake.grab_url(),
            "fax": fake.grab_phone(),
            "owner": {
                "id": user["id"]
            },
            "external_status": {
                "status_name": fake.grab_external_status(the_name)
            },
            "contact_groups": fake.grab_one_from_validated_array(cgroup,
                                                                 "group_name"),
            "external_ids": [
                {
                    "source": fake.grab_source(),
                    "external_id": fake.grab_external_status(the_name,
                                                             "relationships")
                }
            ],
            "preferences": {
                "is_silenced": fake.grab_bool()
            },
            "options": {
                "suppress_emails": fake.grab_bool()
            }
        }
    )


def grab_patch_json(origin_contact):
    """
    Grabs json for patch endpoint.

    :param origin_contact: json, the original.
    :return: json, the data.
    """

    the_name = "lead.test.x.{}".format(int(time.time()))
    cgroup = ContactGroup().choose_random()

    return json.dumps(
        {
            "first_name": "EDIT.{}".format(origin_contact["first_name"]),
            "email": "EDIT.{}".format(origin_contact["email"]),
            "external_id": "EDIT.{}".format(origin_contact["external_id"]),
            "external_status": {
                "status_name": "NEW.external.status.{}".format(the_name)
            },
            "contact_groups": fake.grab_one_from_validated_array(cgroup,
                                                                 "group_name"),
            "remove_contact_groups": fake.grab_one_from_old_json(
                origin_contact,
                target="contact_groups"
            ),
            "external_ids": [
                {
                    "source": "OurSystem",
                    "external_id":
                        "NEW.external.relationship.{}".format(the_name)
                }
            ],
            "preferences": {
                "is_silenced": fake.grab_bool()
            },
            "options": {
                "suppress_emails": fake.grab_bool()
            }
        }
    )
