#!/usr/bin/python3
import platform
import python.config as config


"""Intended to store global variables."""


# Detect testing environment.
server = platform.node()
# For testing locally.
IS_LOCAL_ENVIRONMENT = False
# For manual targeting of environments. Potential options are:
# [prod, staging, qa7, qa8, qa9, qa10, qa11, qa12, qa13, qa14, qa15, qa16]
MANUAL_TARGET_ENVIRONMENT = "staging"


def set_manual_database_config():
    """
    Picks the config, based on MANUAL_TARGET_ENVIRONMENT variable.

    :return: dict, the selected database config.
    """

    if MANUAL_TARGET_ENVIRONMENT in "prod":
        return config.DATABASE_PROD
    elif MANUAL_TARGET_ENVIRONMENT in "staging":
        return config.DATABASE_STAGING
    elif "qa" in MANUAL_TARGET_ENVIRONMENT:
        return config.DATABASE_QA
    else:
        # TODO - Add in DEV environment settings, instead of this error?
        raise ValueError("Unable to find database for the targeted "
                         "environment: {}".format(MANUAL_TARGET_ENVIRONMENT))


# Set Database values, if run on server.
if server in ("",
              ""):
    DATABASE_CONFIG = set_manual_database_config()
elif server in ("",
                "",
                "",
                "prod6.totalexpert.net",
                "",
                ""):
    DATABASE_CONFIG = config.DATABASE_PROD
elif server in ("",
                "",
                "",
                ""):
    DATABASE_CONFIG = config.DATABASE_STAGING
elif "qa" in server:
    DATABASE_CONFIG = config.DATABASE_QA
# Else, trigger local environment settings.
else:
    IS_LOCAL_ENVIRONMENT = True
    DATABASE_CONFIG = set_manual_database_config()


# This section is used to allow for manually override of the variables,
#   via bamboo.
OVERRIDE_DB_HOST = None
OVERRIDE_DB_DBNAME = None
OVERRIDE_DB_USER = None
OVERRIDE_DB_PASSWORD = None
OVERRIDE_DB_PORT = None
if OVERRIDE_DB_HOST:
    DATABASE_CONFIG["host"] = OVERRIDE_DB_HOST
if OVERRIDE_DB_DBNAME:
    DATABASE_CONFIG["dbname"] = OVERRIDE_DB_DBNAME
if OVERRIDE_DB_USER:
    DATABASE_CONFIG["user"] = OVERRIDE_DB_USER
if OVERRIDE_DB_PASSWORD:
    DATABASE_CONFIG["password"] = OVERRIDE_DB_PASSWORD
if OVERRIDE_DB_PORT:
    DATABASE_CONFIG["port"] = OVERRIDE_DB_PORT
