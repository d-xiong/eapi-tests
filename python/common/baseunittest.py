#!/usr/bin/python3
import unittest
import functools
from python.common.baselogger import BaseLogger


class BaseUnitTest(unittest.TestCase):
    """Shared parent base class for all Tests. Mainly for logging."""

    # This needs to be out here, to ensure it is only called ONCE across all
    #   instances of the class.
    log = BaseLogger()

    @classmethod
    def setUpClass(cls):
        """Writes starting log message for each test suite."""

        cls.log.info("===============")
        cls.log.info("STARTING TESTS: {}".format(cls.__name__))
        cls.log.info("===============")

    def setUp(self):
        """Writes starting log message for each test."""

        self.log.start_test(self.id())

    def tearDown(self):
        """Writes ending log message for each test."""

        self.log.end_test()

    @classmethod
    def tearDownClass(cls):
        """Writes ending log message for each test suite."""

        cls.log.info("===== TESTS COMPLETED: {}".format(cls.__name__))

    @staticmethod
    def log_try_except(func):
        """
        A decorator that wraps the passed in function and logs exceptions,
        should one occur.

        :param func: the function, to be completed.
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as err:
                BaseUnitTest.log.exception(err)
                raise  # Re-raise the exception

        return wrapper
