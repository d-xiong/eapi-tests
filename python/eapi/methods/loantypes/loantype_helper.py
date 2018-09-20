#!/usr/bin/python3
import time
import json


def grab_post_json():
    """
    Grabs json for post endpoint.

    :return: json, the data.
    """

    return json.dumps(
        {
            "loan_type": "loantype.test.x.{}".format(int(time.time()))
        }
    )
