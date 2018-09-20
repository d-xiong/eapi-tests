#!/usr/bin/python3
import json
from python.common.eapi.baserequest import BaseRequest
import python.eapi.variables.variables_eapi as vari


class Heartbeat(BaseRequest):
    """Class for Heartbeat endpoint methods."""

    def get_heartbeat(self):
        """
        Get the heartbeat.

        :return: json, of the response.
        """

        url = vari.BASE_URL + "/v1/heartbeat"
        response = self.get_endpoint(url)
        return json.loads(response.text)

    def get_teapot(self):
        """
        Get the teapot.

        :return: json, of the response.
        """

        url = vari.BASE_URL + "/v1/teapot"
        response = self.get_endpoint(url, expected_code=418)  # Unique code...
        return json.loads(response.text)
