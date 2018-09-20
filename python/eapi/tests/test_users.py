#!/usr/bin/python3
import unittest
from python.common.baseunittest import BaseUnitTest
from python.eapi.methods.users.user import User


class TestUsers(BaseUnitTest):
    """Runs User test scenarios."""

    @BaseUnitTest.log_try_except
    def test_01_get_multi(self):
        """
        1. Get multiple.
        """

        the_user = User()
        the_user.get_multi()

    @BaseUnitTest.log_try_except
    def test_02_get_one(self):
        """
        1. Choose random, existing.
        2. Get only that one.
        """

        the_user = User()
        random_user = the_user.choose_random()
        the_user.get_one(random_user)

    @BaseUnitTest.log_try_except
    def test_03_post_one(self):
        """
        1. Choose random, required existing data.
        2. Create new.
        3. Get the newly created.
        """

        the_user = User()
        random_user = the_user.choose_random()
        json_user = the_user.post_one(random_user )
        the_user.get_one(json_user)

    @BaseUnitTest.log_try_except
    def test_04_patch_one(self):
        """
        1. Choose random, required existing data.
        2. Create new.
        3. Get the newly created.
        4. Choose another random, required existing data.
        5. Update the created.
        6. Get the updates.
        """

        the_user = User()
        random_user = the_user.choose_random()
        json_user = the_user.post_one(random_user )
        json_user = the_user.get_one(json_user)
        the_user.patch_one(json_user)
        the_user.get_one(json_user)


if __name__ == '__main__':
    unittest.main()
