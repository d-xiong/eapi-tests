#!/usr/bin/python3
import unittest
from python.common.baseunittest import BaseUnitTest
from python.eapi.methods.roles.role import Role


class TestRoles(BaseUnitTest):
    """Runs Role test scenarios."""

    @BaseUnitTest.log_try_except
    def test_01_get_multi(self):
        """
        1. Get multiple.
        """

        the_role = Role()
        the_role.get_multi()

    @BaseUnitTest.log_try_except
    def test_02_get_one(self):
        """
        1. Choose a random, existing.
        2. Get only that one.
        """

        the_role = Role()
        random_role = the_role.choose_random()
        the_role.get_one(random_role)


if __name__ == '__main__':
    unittest.main()
