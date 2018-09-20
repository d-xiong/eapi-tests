#!/usr/bin/python3
import unittest
from python.common.baseunittest import BaseUnitTest
from python.eapi.methods.contactgroups.contactgroup import ContactGroup


class TestContactGroups(BaseUnitTest):
    """Runs Contact Group test scenarios."""

    @BaseUnitTest.log_try_except
    def test_01_get_multi(self):
        """
        1. Get multiple.
        """

        the_cgroup = ContactGroup()
        the_cgroup.get_multi()

    @BaseUnitTest.log_try_except
    def test_02_get_one(self):
        """
        1. Choose random, existing.
        2. Get only that one.
        """

        the_cgroup = ContactGroup()
        random_cgroup = the_cgroup.choose_random()
        the_cgroup.get_one(random_cgroup)

    @BaseUnitTest.log_try_except
    def test_03_post_one(self):
        """
        1. Create new.
        2. Get the newly created.
        """

        the_cgroup = ContactGroup()
        json_cgroup = the_cgroup.post_one()
        the_cgroup.get_one(json_cgroup)

    @BaseUnitTest.log_try_except
    def test_04_patch_one(self):
        """
        1. Create new.
        2. Get the newly created.
        3. Update the created.
        4. Get the updates.
        """

        the_cgroup = ContactGroup()
        json_cgroup = the_cgroup.post_one()
        json_cgroup = the_cgroup.get_one(json_cgroup)
        the_cgroup.patch_one(json_cgroup)
        the_cgroup.get_one(json_cgroup)

    @BaseUnitTest.log_try_except
    def test_05_delete_one(self):
        """
        1. Create new.
        2. Get the newly created.
        3. Delete the created.
        4. Get the freshly deleted, and expect a 404 response.
        """

        the_cgroup = ContactGroup()
        json_cgroup = the_cgroup.post_one()
        the_cgroup.get_one(json_cgroup)
        the_cgroup.delete_one(json_cgroup)
        the_cgroup.get_one(json_cgroup, expected_code=404)


if __name__ == '__main__':
    unittest.main()
