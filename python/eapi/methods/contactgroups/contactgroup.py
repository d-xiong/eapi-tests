#!/usr/bin/python3
import json
import random
from python.common.eapi.baserequest import BaseRequest
import python.eapi.variables.variables_eapi as vari
import python.eapi.methods.contactgroups.contactgroup_helpers as cghelp


class ContactGroup(BaseRequest):
    """Class for Contact Group endpoint methods."""

    def get_multi(self, number=1, size=100):
        """
        Get multiple.

        :param number: int, the page number.
        :param size: int, how many per page.
        :return: json, the response.
        """

        url = (
            vari.BASE_URL
            + "/v1/contact-groups?page[number]={}&page[size]={}".format(number,
                                                                        size)
        )
        response = self.get_endpoint(url)
        return json.loads(response.text)

    def get_one(self, cgroup, expected_code=200):
        """
        Get one.

        :param cgroup: json, an existing.
        :param expected_code: int, expected response code.
        :return: json, the response.
        """

        url = vari.BASE_URL + "/v1/contact-groups/{}".format(cgroup["id"])
        response = self.get_endpoint(url, expected_code)
        return json.loads(response.text)

    def post_one(self):
        """
        Post new.

        :return: json, the new.
        """

        url = vari.BASE_URL + "/v1/contact-groups"
        payload = cghelp.grab_post_json()
        response = self.post_endpoint(url, payload)
        return json.loads(response.text)

    def patch_one(self, origin_cgroup):
        """
        Patch existing.

        :param origin_cgroup: json, the original.
        """

        url = (
            vari.BASE_URL
            + "/v1/contact-groups/{}".format(origin_cgroup["id"])
        )
        payload = cghelp.grab_patch_json(origin_cgroup)
        self.patch_endpoint(url, payload)

    def delete_one(self, cgroup):
        """
        Delete existing.

        :param cgroup: json, an existing.
        """

        url = vari.BASE_URL + "/v1/contact-groups/{}".format(cgroup["id"])
        self.delete_endpoint(url)

    def choose_random(self, selected=None):
        """
        Choose at random, and return the "selected" field.

        :param selected: str, the field to return.
        :return: ???: Depends on "selected" variable.
        """

        this_json = self.get_multi()
        num = random.randint(0, len(this_json["items"]) - 1)

        # Loops until it finds a non-blank "group_name" field.
        #     Prevents the following error: "invalid value for team name".
        #     This error can occur in EAPI Contact endpoint tests.
        while not this_json["items"][num]["group_name"]:
            num = random.randint(0, len(this_json["items"]) - 1)

        if selected is None:
            return this_json["items"][num]
        return this_json["items"][num][selected]
