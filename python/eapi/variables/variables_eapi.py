#!/usr/bin/python3
import python.config as config
import python.variables_global as variglob


"""Intended to store only the EAPI variables."""


# Info for manual target of the database user's oauth.
BASE_USER_ID = 0
BASE_SCOPES = ("")


api_urls = {
    "prod": "",
    "staging": "",
    "qa7": "",
    "qa8": "",
    "qa9": "",
    "qa10": "",
    "qa11": "",
    "qa12": "",
    "qa13": "",
    "qa14": "",
    "qa15": "",
    "qa16": ""
}


BASE_URL = api_urls[variglob.MANUAL_TARGET_ENVIRONMENT]


DB_HOST = variglob.DATABASE_CONFIG["host"]
DB_NAME = variglob.DATABASE_CONFIG["dbname"]
DB_USER = variglob.DATABASE_CONFIG["user"]
DB_PASSWORD = variglob.DATABASE_CONFIG["password"]
DB_PORT = variglob.DATABASE_CONFIG["port"]


if variglob.IS_LOCAL_ENVIRONMENT:
    SSH_HOST = config.SSH_CONFIG["host"]
    SSH_PORT = config.SSH_CONFIG["port"]
    SSH_USER = config.SSH_CONFIG["user"]
    SSH_PASSWORD = config.SSH_CONFIG["password"]
    SSH_RSA_KEY_PATH = config.SSH_CONFIG["rsa_key_path"]
