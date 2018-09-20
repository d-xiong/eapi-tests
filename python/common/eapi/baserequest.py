#!/usr/bin/python3
import requests
import json
from python.common.baselogger import BaseLogger
import python.eapi.variables.variables_eapi as vari
import python.common.datagenerators.generateoauth as oauth


class BaseRequest(object):
    """
    Shared parent base class for Requests endpoint methods.
        - Create (POST)
        - Read (GET)
        - Update (PATCH)
        - Delete (DELETE)
    """

    # This needs to be out here, to ensure it is only called ONCE across all
    #   instances of the class.
    log = BaseLogger()
    log.info("===============")
    log.info("GRABBING OAUTH")
    log.info("===============")

    try:
        basic_auth = oauth.grab_oauth_from_client(user_id=vari.BASE_USER_ID,
                                                  scopes=vari.BASE_SCOPES)
    except Exception as err:
        log.exception(err)
        raise

    def __init__(self):
        """Sets logs, and grabs auth token."""

        self.creds = "Bearer {}".format(self.post_authenticate())
        self.log.debug("Token: {}".format(self.creds))

    def post_authenticate(self, expected_code=200):
        """
        Share posts to auth endpoint and grabs access token. I moved the auth
        into here, to prevent import errors... R.I.P.

        :param expected_code: int, the expected response code.
        :return: str, the auth access token.
        """

        url = vari.BASE_URL + "/v1/token"
        payload = "grant_type=client_credentials"
        headers = {
            'Authorization': "Basic {}".format(self.basic_auth),
            'Cache-Control': "no-cache",
            'Content-Type': "application/x-www-form-urlencoded"
        }
        response = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers
        )
        assert response.status_code == expected_code, (response.status_code,
                                                       response.text)
        json_response = json.loads(response.text)
        return json_response["access_token"]

    def get_endpoint(self, url, expected_code=200):
        """
        Shared GET endpoint.

        :param url: str, the targeted environment.
        :param expected_code: int, the expected response code.
        :return: obj, response object.
        """

        headers = {
            'Authorization': self.creds
        }
        response = requests.request(
            "GET",
            url,
            headers=headers,
        )
        try:
            assert response.status_code == expected_code, \
                (response.status_code, url, response.text)
            self.log.pass_msg("GET: {0} {1}".format(response.status_code, url))
        except AssertionError:
            self.log.fail_msg("GET: Received {0}, Expected {1}.".format(
                    response.status_code,
                    expected_code
            ))
            raise
        return response

    def post_endpoint(self, url, payload, expected_code=201):
        """
        Shared POST endpoint.

        :param url: str, the targeted environment.
        :param payload: json, the intended data.
        :param expected_code: int, the expected response code.
        :return: obj, response object.
        """

        headers = {
            'Authorization': self.creds,
            'Content-Type': "application/json"
        }
        self.log.debug("Sending POST Payload: " + str(payload))
        response = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers
        )
        try:
            assert response.status_code == expected_code, (response.status_code,
                                                           url,
                                                           payload,
                                                           response.text)
            self.log.pass_msg("POST: {0} {1}".format(response.status_code, url))
        except AssertionError:
            self.log.fail_msg(
                "POST: Received {0}, Expected {1}.".format(
                    response.status_code,
                    expected_code
                )
            )
            raise
        return response

    def patch_endpoint(self, url, payload, expected_code=200):
        """
        Shared PATCH endpoint.

        :param url: str, the targeted environment.
        :param payload: the intended data.
        :param expected_code: int, the expected response code.
        :return: obj, response object.
        """

        headers = {
            'Authorization': self.creds,
            'Content-Type': "application/json"
        }
        self.log.debug("Sending PATCH Payload: " + str(payload))
        response = requests.request(
            "PATCH",
            url,
            data=payload,
            headers=headers
        )
        try:
            assert response.status_code == expected_code, (response.status_code,
                                                           url,
                                                           payload,
                                                           response.text)
            self.log.pass_msg(
                "PATCH: {0} {1}".format(response.status_code, url)
            )
        except AssertionError:
            self.log.fail_msg(
                "PATCH: Received {0}, Expected {1}.".format(
                    response.status_code,
                    expected_code
                )
            )
            raise
        return response

    def delete_endpoint(self, url, expected_code=200):
        """
        Shared DELETE endpoint.

        :param url: str, the targeted environment.
        :param expected_code: int, the expected response code.
        :return: obj, response object.
        """

        headers = {
            'Authorization': self.creds
        }
        response = requests.request(
            "DELETE",
            url,
            headers=headers
        )
        try:
            assert response.status_code == expected_code, (response.status_code,
                                                           url,
                                                           response.text)
            self.log.pass_msg(
                "DELETE: {0} {1}".format(response.status_code, url)
            )
        except AssertionError:
            self.log.fail_msg("DELETE: Received {0}, Expected {1}.".format(
                response.status_code,
                expected_code
            ))
            raise
        return response
