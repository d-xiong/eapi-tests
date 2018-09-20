#!/usr/bin/python3
import json
import random
from python.common.eapi.baserequest import BaseRequest
import python.eapi.variables.variables_eapi as vari
import python.eapi.methods.contactnotes.contactnote_helpers as cnhelp


class ContactNote(BaseRequest):
    """Class for Contact Note endpoint methods."""

    def get_multi(self, number=1, size=100):
        """
        Get multiple.

        :param number: int, the page number.
        :param size: int, how many per page.
        :return: json, the response.
        """

        url = (
            vari.BASE_URL
            + "/v1/contact-notes?page[number]={}&page[size]={}".format(number,
                                                                       size)
        )
        response = self.get_endpoint(url)
        return json.loads(response.text)

    def get_one(self, cnote, expected_code=200):
        """
        Get one.

        :param cnote: json, an existing.
        :param expected_code: int, the expected response code.
        :return: json, the response.
        """

        url = vari.BASE_URL + "/v1/contact-notes/{}".format(cnote["id"])
        response = self.get_endpoint(url, expected_code)
        return json.loads(response.text)

    def post_one(self):
        """
        Post new.

        :return: json, the new.
        """

        url = vari.BASE_URL + "/v1/contact-notes"
        payload = cnhelp.grab_post_json()
        response = self.post_endpoint(url, payload)
        return json.loads(response.text)

    def patch_one(self, json_cnote):
        """
        Patch existing.

        :param json_cnote: json, the original.
        """

        url = vari.BASE_URL + "/v1/contact-notes/{}".format(json_cnote["id"])
        payload = cnhelp.grab_patch_json(json_cnote)
        self.patch_endpoint(url, payload)

    def delete_one(self, cnote):
        """
        Delete existing.

        :param cnote: json, an existing.
        """

        url = vari.BASE_URL + "/v1/contact-notes/{}".format(cnote["id"])
        self.delete_endpoint(url)

    def choose_random(self, selected=None):
        """
        Choose at random, and return the "selected" field.

        :param selected: str, the field to return.
        :return: ???: Depends on "selected" variable.
        """

        this_json = self.get_multi()
        num = random.randint(0, len(this_json["items"]) - 1)
        if selected is None:
            return this_json["items"][num]
        return this_json["items"][num][selected]
