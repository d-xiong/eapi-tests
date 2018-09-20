#!/usr/bin/python3
import unittest
from python.common.baseunittest import BaseUnitTest
from python.eapi.methods.contactnotes.contactnote import ContactNote


class TestContactNotes(BaseUnitTest):
    """Runs Contact Note test scenarios."""

    @BaseUnitTest.log_try_except
    def test_01_get_multi(self):
        """
        1. Get multiple.
        """

        the_cnote = ContactNote()
        the_cnote.get_multi()

    @BaseUnitTest.log_try_except
    def test_02_get_one(self):
        """
        1. Choose random, existing.
        2. Get only that one.
        """

        the_cnote = ContactNote()
        random_cnote = the_cnote.choose_random()
        the_cnote.get_one(random_cnote)

    @BaseUnitTest.log_try_except
    def test_03_post_one(self):
        """
        1. Create a new.
        2. Get the newly created.
        """

        the_cnote = ContactNote()
        json_cnote = the_cnote.post_one()
        the_cnote.get_one(json_cnote)

    @BaseUnitTest.log_try_except
    def test_04_patch_one(self):
        """
        1. Create new.
        2. Get the newly created.
        3. Update the created.
        4. Get the updates.
        """

        the_cnote = ContactNote()
        json_cnote = the_cnote.post_one()
        json_cnote = the_cnote.get_one(json_cnote)
        the_cnote.patch_one(json_cnote)
        the_cnote.get_one(json_cnote)

    @BaseUnitTest.log_try_except
    def test_05_delete_one(self):
        """
        1. Create new.
        2. Get the newly created.
        3. Delete the new.
        4. Get the freshly deleted, and expect a 404 response.
        """

        the_cnote = ContactNote()
        json_cnote = the_cnote.post_one()
        the_cnote.get_one(json_cnote)
        the_cnote.delete_one(json_cnote)
        the_cnote.get_one(json_cnote, expected_code=404)


if __name__ == '__main__':
    unittest.main()
