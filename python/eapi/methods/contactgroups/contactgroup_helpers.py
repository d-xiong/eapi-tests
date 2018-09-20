#!/usr/bin/python3
import time
import json
from python.eapi.methods.users.user import User


def grab_post_json():
    """
    Grabs json for post endpoint.

    :return: json, the data.
    """

    user = User().choose_random()

    return json.dumps(
        {
            "group_name": "group.test.x.{}".format(int(time.time())),
            "owner": {
                "id": user["id"]
            }
        }
    )


def grab_patch_json(origin_cgroup):
    """
    Grabs json for patch endpoint.

    :param origin_cgroup: json, the original.
    :return: json, the data.
    """

    return json.dumps(
        {
            "group_name": "EDIT.{}".format(origin_cgroup["group_name"])
        }
    )
