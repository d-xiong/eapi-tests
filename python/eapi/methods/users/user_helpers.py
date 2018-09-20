#!/usr/bin/python3
import time
import json
import python.common.datagenerators.generatefakedata as fake
from python.eapi.methods.roles.role import Role
from python.eapi.methods.teams.team import Team


def grab_post_json(user):
    """
    Grabs json for post endpoint.

    :param: user: json, an existing.
    :return: json, the data.
    """

    the_name = "eapi.user.test.x.{}".format(int(time.time()))
    the_image_url = "https://i.imgur.com/uGOD7Wr.jpg"
    team = Team().choose_random()
    role = Role().choose_random()

    return json.dumps(
        {
            "external_id": fake.grab_external_id(the_name),
            "email": fake.grab_email(the_name),
            "new_email": "EDIT.{}".format(fake.grab_email(the_name)),
            "status": fake.grab_bool(),
            "type": fake.grab_user_type(),
            "role": {
                "role_name": role["role_name"]
            },
            "info": {
                "address": fake.grab_address_one(),
                "address_2": fake.grab_address_two(),
                "city": fake.grab_city(),
                "state": fake.grab_state_abbr(),
                "zip_code": fake.grab_zip(),
                "first_name": fake.grab_first_name(),
                "last_name": fake.grab_last_name(),
                "phone_cell": fake.grab_phone(),
                "phone_office": fake.grab_phone(),
                "phone_fax": fake.grab_phone(),
                "job_title": fake.grab_job(),
                "cost_center": fake.grab_building_number(),
                "website": fake.grab_url(),
                "testimonial_url": fake.grab_url(),
                "timezone_name": fake.grab_timezone(),
                "location_id": fake.grab_building_number(),
                "company": fake.grab_company()
            },
            "settings_marketing": {
                "application_url": fake.grab_url(),
                "disclaimer": fake.grab_phrase(),
                "license_title": fake.grab_job(),
                "social_facebook": fake.grab_url(),
                "social_twitter": fake.grab_url(),
                "social_google": fake.grab_url(),
                "social_linkedin": fake.grab_url(),
                "social_youtube": fake.grab_url(),
                "weekly_spend_threshold": fake.grab_percent(),
                "daily_spend_threshold": fake.grab_percent() - 1.00,
                "agent_bio": fake.grab_phrase(),
                "short_name": "short.{}".format(fake.grab_username()),
                "post_close_survey_url": fake.grab_url(),
                "wistia_id": fake.grab_large_int(),
                "user_quote": fake.grab_phrase(),
                "profile_img_url": the_image_url,
                "logo_img_url": the_image_url
            },
            "expenditure_approver": {
                "id": user["id"]
            },
            "licenses": [
                {
                    "license_name": fake.grab_state_abbr(),
                    "content": "license.{}".format(fake.grab_large_int())
                }
            ],
            "teams": fake.grab_one_from_validated_array(team, "id")
        }
    )


def grab_patch_json(origin_user):
    """
    Grabs json for patch endpoint.

    :param origin_user: json, the original.
    :return: json, the data.
    """

    the_name = "eapi.user.test.x.{}".format(int(time.time()))
    the_image_url = "https://i.imgur.com/6eOsW2Z.gif"
    team = Team().choose_random()
    role = Role().choose_random()

    return json.dumps(
        {
            "external_id": "EDIT.{}".format(origin_user["external_id"]),
            "email": origin_user["email"],
            "new_email": "EDIT.{}".format(origin_user["email"]),
            "type": fake.grab_user_type(),
            "role": {
                "role_name": role["role_name"]
            },
            "info": {
                "address": "EDIT.{}".format(origin_user["info"]["address"]),
                "first_name": "EDIT.{}".format(origin_user["info"]
                                                          ["first_name"])
            },
            "settings_marketing": {
                "disclaimer": "EDIT.{}".format(origin_user["settings_marketing"]
                                                          ["disclaimer"]),
                "profile_img_url": the_image_url
            },
            "licenses": [
                {
                    "license_name": fake.grab_state_abbr(),
                    "content": "EDIT.license.{}".format(the_name)
                }
            ],
            "remove_licenses": fake.grab_one_from_old_json(origin_user,
                                                           target="licenses"),
            "teams": fake.grab_one_from_validated_array(team, "id"),
            "remove_teams": fake.grab_one_from_old_json(origin_user,
                                                        target="teams")
        }
    )
