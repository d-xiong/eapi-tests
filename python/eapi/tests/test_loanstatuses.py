#!/usr/bin/python3
import unittest
from python.common.baseunittest import BaseUnitTest
from python.eapi.methods.loanstatuses.loanstatus import LoanStatus


class TestLoanStatus(BaseUnitTest):
    """Runs Loan Status test scenarios."""

    @BaseUnitTest.log_try_except
    def test_01_get_multi(self):
        """
        1. Get multiple.
        """

        the_lstat = LoanStatus()
        the_lstat.get_multi()

    @BaseUnitTest.log_try_except
    def test_02_get_one(self):
        """
        1. Choose random, existing.
        2. Get only that one.
        """

        the_lstat = LoanStatus()
        random_lstat = the_lstat.choose_random()
        the_lstat.get_one(random_lstat)

    @BaseUnitTest.log_try_except
    def test_03_post_one(self):
        """
        1. Create new.
        2. Get the newly created.
        """

        the_lstat = LoanStatus()
        json_lstat = the_lstat.post_one()
        the_lstat.get_one(json_lstat)


if __name__ == '__main__':
    unittest.main()
