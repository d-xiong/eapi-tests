#!/usr/bin/python3
import unittest
from python.common.baseunittest import BaseUnitTest
from python.eapi.methods.contacts.contact import Contact


class TestContacts(BaseUnitTest):
    """Runs Contact test scenarios."""

    @BaseUnitTest.log_try_except
    def test_01_get_multi(self):
        """
        1. Get multiple.
        """

        the_contact = Contact()
        the_contact.get_multi()

    @BaseUnitTest.log_try_except
    def test_02_get_one(self):
        """
        1. Choose random, existing.
        2. Get only that one.
        """

        the_contact = Contact()
        random_contact = the_contact.choose_random()
        the_contact.get_one(random_contact)

    @BaseUnitTest.log_try_except
    def test_03_post_one(self):
        """
        1. Create new.
        2. Get the newly created.
        """

        the_contact = Contact()
        json_contact = the_contact.post_one()
        the_contact.get_one(json_contact)

    @BaseUnitTest.log_try_except
    def test_04_patch_one(self):
        """
        1. Create new.
        2. Get the newly created.
        3. Update the created.
        4. Get the updates.
        """

        the_contact = Contact()
        json_contact = the_contact.post_one()
        json_contact = the_contact.get_one(json_contact)
        the_contact.patch_one(json_contact)
        the_contact.get_one(json_contact)

    @BaseUnitTest.log_try_except
    def test_05_delete_one(self):
        """
        1. Create new.
        2. Get the newly created.
        3. Delete the new.
        4. Get the freshly deleted, and expect a 404 response.
        """

        the_contact = Contact()
        json_contact = the_contact.post_one()
        the_contact.get_one(json_contact)
        the_contact.delete_one(json_contact)
        the_contact.get_one(json_contact, expected_code=404)


if __name__ == '__main__':
    unittest.main()
