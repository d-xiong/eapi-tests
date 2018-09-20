#!/usr/bin/python3
import time
import json
import random
from faker import Faker
import python.common.datagenerators.generatemysql as gensql
from python.eapi.methods.contacts.contact import Contact


def grab_post_json():
    """
    Grabs json for post endpoint.

    :return: json, the data.
    """

    fake = Faker()
    the_name = "notes.test.x.{}".format(int(time.time()))
    contact = Contact().choose_random()

    return json.dumps(
        {
            "title": the_name,
            "note": fake.paragraph(
                nb_sentences=3,
                variable_nb_sentences=True,
                ext_word_list=None
            ),
            "type_id": 1,
            "contact": {
                "id": contact["id"]
            },
            "owner": {
                # The owner username has to be the same as the selected
                #   contact's, otherwise it returns a 422 error.
                "username": contact["owner"]["username"]
            }
        }
    )


def grab_patch_json(origin_cnote):
    """
    Grabs json for patch endpoint.

    :param origin_cnote: json, the original.
    :return: json, the data.
    """

    return json.dumps(
        {
            "title": "EDIT.{}".format(origin_cnote["title"]),
            "note": "EDIT.{}".format(origin_cnote["note"]),
            "type_id": 2,
            "contact": {
                "id": grab_contact_id_sql(origin_cnote["owner"]["id"])
            }
        }
    )


def grab_contact_id_sql(owner_id):
    """
    Grab a contact id, using pymysql and sshtunnel. This is required, as the
        contact and contact note must have the same owners. I was unable to
        figure out how to do this easily, via the endpoints.

    :param owner_id: int, the user id.
    :return: int, a random contact id, that has the same owner id.
    """

    query = (
        'SELECT id '
        'FROM leads '
        'WHERE owner_id = {} '
        'AND deleted_at IS NULL;'.format(owner_id)
    )
    all_results = gensql.perform_mysql_call(query)
    only_id_fields = [item[0] for item in all_results]
    return only_id_fields[random.randint(0, len(only_id_fields) - 1)]
