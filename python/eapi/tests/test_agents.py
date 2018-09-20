#!/usr/bin/python3
import unittest
from python.common.baseunittest import BaseUnitTest
from python.eapi.methods.agents.agent import Agent


class TestAgent(BaseUnitTest):
    """Runs Agent test scenarios."""

    @BaseUnitTest.log_try_except
    def test_01_get_multi(self):
        """
        1. Get multiple.
        """

        the_agent = Agent()
        the_agent.get_multi()

    @BaseUnitTest.log_try_except
    def test_02_get_one(self):
        """
        1. Choose one random, existing.
        2. Get only that one.
        """

        the_agent = Agent()
        random_agent = the_agent.choose_random()
        the_agent.get_one(random_agent)

    @BaseUnitTest.log_try_except
    def test_03_post(self):
        """
        1. Create new.
        2. Get the newly created.
        """

        the_agent = Agent()
        json_agent = the_agent.post_one()
        the_agent.get_one(json_agent)

    @BaseUnitTest.log_try_except
    def test_04_patch(self):
        """
        1. Create new.
        2. Get the newly created.
        3. Update the created.
        4. Get the updates.
        """

        the_agent = Agent()
        json_agent = the_agent.post_one()
        json_agent = the_agent.get_one(json_agent)
        the_agent.patch_one(json_agent)
        the_agent.get_one(json_agent)


if __name__ == '__main__':
    unittest.main()
