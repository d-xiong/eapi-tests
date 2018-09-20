#!/usr/bin/python3
import time
import json


def grab_post_json():
    """
    Grabs json for post endpoint.

    :return: json, the data.
    """

    # This import being in here currently prevents recursive imports.
    #   Need a better way to handle this.
    from python.eapi.methods.users.user import User
    user = User().choose_random()
    the_name = "team.test.x.{}".format(int(time.time()))

    return json.dumps(
        {
            "team_name": the_name,
            "managers": [
                {
                    "id": user["id"]
                }
            ]
        }
    )


def grab_patch_json(origin_team):
    """
    Grabs json for patch endpoint.

    :param origin_team: json, the original.
    :return: json, the data.
    """

    # This import being in here currently prevents recursive imports.
    #   Need a better way to handle this.
    from python.eapi.methods.users.user import User
    user = User().choose_random()

    return json.dumps(
        {
            "team_name": "EDIT." + origin_team["team_name"],
            "managers": [
                {
                    "id": user["id"]
                }
            ],
            "remove_managers": grab_old_managers(origin_team)
        }
    )


def grab_old_managers(origin_team):
    """
    Validates to ensure data was provided.

    :param origin_team: json, the original.
    :return: array, the data.
    """

    if "managers" in origin_team:
        return [origin_team["managers"][0]]
    else:
        return []
