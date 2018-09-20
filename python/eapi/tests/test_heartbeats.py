#!/usr/bin/python3
import unittest
from python.common.baseunittest import BaseUnitTest
from python.eapi.methods.heartbeats.heartbeat import Heartbeat


class TestHeartbeats(BaseUnitTest):
    """Runs Heartbeat test scenarios."""

    @BaseUnitTest.log_try_except
    def test_01_get_heartbeat(self):
        """
        1. Get the heartbeat.
        """

        the_heart = Heartbeat()
        the_heart.get_heartbeat()

    @BaseUnitTest.log_try_except
    def test_02_get_teapot(self):
        """
        1. Get the teapot.
        """

        the_heart = Heartbeat()
        the_heart.get_teapot()


if __name__ == '__main__':
    unittest.main()
