#!/usr/bin/python3


"""
Intended to store user-sensitive variables.

This file functions as an example of the 'config.py' file. This file displays
what should be included, for this repo to be functional. This 'config.py' file
is not included when pushing/pulling from git.

Steps:
    1. Create a copy of this file.
    2. Rename the new copied file as 'config.py'.
    3. Fill in all required empty fields below, as necessary.
"""


database_user = ""  # Manually set this value.
database_password = ""  # Manually set this value.


DATABASE_PROD = {
    "host": "",
    "dbname": "",
    "user": database_user,
    "password": database_password,
    "port": 0
}
DATABASE_STAGING = {
    "host": "",
    "dbname": "",
    "user": database_user,
    "password": database_password,
    "port": 0
}
DATABASE_QA = {
    "host": "",
    "dbname": "",
    "user": database_user,
    "password": database_password,
    "port": 0
}


# These are used in local testing only, since an SSH into the server is required
#   before connecting to the databases.
SSH_CONFIG = {
    "host": "",
    "port": ,
    "user": "",  # Manually set this value.
    "password": "",  # Manually set this value.
    "rsa_key_path": ""  # Manually set this value.
}
