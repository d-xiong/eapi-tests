#!/usr/bin/python3
import unittest
from python.common.baseunittest import BaseUnitTest
from python.eapi.methods.teams.team import Team


class TestTeams(BaseUnitTest):
    """Runs Team test scenarios."""

    @BaseUnitTest.log_try_except
    def test_01_get(self):
        """
        1. Get multiple.
        """

        the_team = Team()
        the_team.get_multi()

    @BaseUnitTest.log_try_except
    def test_02_get_one(self):
        """
        1. Choose random, existing.
        2. Get only that one.
        """

        the_team = Team()
        random_team = the_team.choose_random()
        the_team.get_one(random_team)

    @BaseUnitTest.log_try_except
    def test_03_post(self):
        """
        1. Create new.
        2. Get the newly created.
        """

        the_team = Team()
        json_team = the_team.post_one()
        the_team.get_one(json_team)

    @BaseUnitTest.log_try_except
    def test_04_patch(self):
        """
        1. Create new.
        2. Get the newly created.
        3. Update the created.
        4. Get the updates.
        """

        the_team = Team()
        json_team = the_team.post_one()
        json_team = the_team.get_one(json_team)
        the_team.patch_one(json_team)
        the_team.get_one(json_team)

    @BaseUnitTest.log_try_except
    def test_05_delete(self):
        """
        1. Create new.
        2. Get the newly created.
        3. Delete the created.
        4. Get the freshly deleted, and expect a 404 response.
        """

        the_team = Team()
        json_team = the_team.post_one()
        the_team.get_one(json_team)
        the_team.delete_one(json_team)
        the_team.get_one(json_team, expected_code=404)


if __name__ == '__main__':
    unittest.main()
