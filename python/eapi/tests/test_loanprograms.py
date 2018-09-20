#!/usr/bin/python3
import unittest
from python.common.baseunittest import BaseUnitTest
from python.eapi.methods.loanprograms.loanprogram import LoanProgram


class TestLoanPrograms(BaseUnitTest):
    """Runs Loan Program test scenarios."""

    @BaseUnitTest.log_try_except
    def test_01_get_multi(self):
        """
        1. Get multiple.
        """

        the_lprog = LoanProgram()
        the_lprog.get_multi()

    @BaseUnitTest.log_try_except
    def test_02_get_one(self):
        """
        1. Choose random, existing.
        2. Get only that one.
        """

        the_lprog = LoanProgram()
        random_lprog = the_lprog.choose_random()
        the_lprog.get_one(random_lprog)

    @BaseUnitTest.log_try_except
    def test_03_post_one(self):
        """
        1. Create a new.
        2. Get the newly created.
        """

        the_lprog = LoanProgram()
        json_lprog = the_lprog.post_one()
        the_lprog.get_one(json_lprog)


if __name__ == '__main__':
    unittest.main()
