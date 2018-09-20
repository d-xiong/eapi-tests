#!/usr/bin/python3
import base64
import python.common.datagenerators.generatemysql as gensql


def grab_oauth_from_client(user_id=None, scopes=None):
    """
    Grabs the client_id and client_secret values for the target user in mysql,
    and generates a base64 oauth string from these.

    :param user_id: int, the target.
    :param scopes: str, the required scopes.
    :return: str, the encoded oauth.
    """

    query = (
        "SELECT client_id, client_secret "
        "FROM oauth_clients "
        "WHERE user_id = {} AND scope = \"{}\";".format(user_id, scopes)
    )
    first_result = gensql.perform_mysql_call(query)[0]
    id_and_secret = "{}:{}".format(first_result[0], first_result[1])
    encoded_oauth = base64.b64encode(id_and_secret.encode('utf-8'))
    return encoded_oauth.decode('ascii')
