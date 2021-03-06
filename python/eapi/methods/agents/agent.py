#!/usr/bin/python3
import json
import random
from python.common.eapi.baserequest import BaseRequest
import python.eapi.variables.variables_eapi as vari
import python.eapi.methods.agents.agent_helpers as ahelp


class Agent(BaseRequest):
    """Class for Agent endpoint methods."""

    def get_multi(self, number=1, size=100):
        """
        Get multiple.

        :param number: int, the page number.
        :param size: int, how many per page.
        :return: json, the response.
        """

        url = (
            vari.BASE_URL
            + "/v1/agent-users?page[number]={}&page[size]={}".format(number,
                                                                     size))
        response = self.get_endpoint(url)
        return json.loads(response.text)

    def get_one(self, agent, expected_code=200):
        """
        Get one.

        :param agent: json, an existing.
        :param expected_code: int, the expected response code.
        :return: json, the response.
        """

        url = vari.BASE_URL + "/v1/agent-users/{}".format(agent["id"])
        response = self.get_endpoint(url, expected_code)
        return json.loads(response.text)

    def post_one(self):
        """
        Post new.

        :return: json, the new.
        """

        url = vari.BASE_URL + "/v1/agent-users"
        payload = ahelp.grab_post_json()
        response = self.post_endpoint(url, payload)
        return json.loads(response.text)

    def patch_one(self, origin_agent):
        """
        Patch existing.

        :param origin_agent: json, the original.
        """

        url = vari.BASE_URL + "/v1/agent-users/{}".format(origin_agent["id"])
        payload = ahelp.grab_patch_json(origin_agent)
        self.patch_endpoint(url, payload)

    def choose_random(self, selected=None):
        """
        Choose at random, and return the "selected" field.

        :param selected: str, the field to return.
        :return: ???, Depends on "selected" variable.
        """

        this_json = self.get_multi()
        num = random.randint(0, len(this_json["items"]) - 1)
        if selected is None:
            return this_json["items"][num]
        return this_json["items"][num][selected]
