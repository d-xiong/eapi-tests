#!/usr/bin/python3
import pymysql
from sshtunnel import SSHTunnelForwarder
import python.eapi.variables.variables_eapi as vari
import python.variables_global as variglob


def perform_mysql_call(query):
    """
    Connect to mysql, and perform a query.

    :param query: str, the sql query
    :return: array (?), the sql results.
    """

    # Need to SSH Tunnel in, prior to connecting to database, if not on
    #   the server.
    if variglob.IS_LOCAL_ENVIRONMENT:

        with SSHTunnelForwarder(
            (vari.SSH_HOST, vari.SSH_PORT),
            ssh_pkey=vari.SSH_RSA_KEY_PATH,
            ssh_username=vari.SSH_USER,
            ssh_password=vari.SSH_PASSWORD,
            remote_bind_address=(vari.DB_HOST, 3306)
        ) as server:

            connection = pymysql.connect(
                host="127.0.0.1",
                user=vari.DB_USER,
                password=vari.DB_PASSWORD,
                db=vari.DB_NAME,
                port=server.local_bind_port
            )

            try:
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    db_results = cursor.fetchall()
            finally:
                connection.close()

            return db_results

    # Otherwise, if on server, no need to SSH in beforehand.
    else:
        connection = pymysql.connect(
            host=vari.DB_HOST,
            user=vari.DB_USER,
            password=vari.DB_PASSWORD,
            db=vari.DB_NAME,
            port=vari.DB_PORT
        )

        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                db_results = cursor.fetchall()
        finally:
            connection.close()

        return db_results
