#!/usr/bin/python3
import unittest
from python.common.baseunittest import BaseUnitTest
from python.eapi.methods.loanpurposes.loanpurpose import LoanPurpose


class TestLoanPurposes(BaseUnitTest):
    """Runs Loan Purpose test scenarios."""

    @BaseUnitTest.log_try_except
    def test_01_get_multi(self):
        """
        1. Get multiple.
        """

        the_lpurp = LoanPurpose()
        the_lpurp.get_multi()

    @BaseUnitTest.log_try_except
    def test_02_get_one(self):
        """
        1. Choose random, existing.
        2. Get only that one.
        """

        the_lpurp = LoanPurpose()
        random_lpurp = the_lpurp.choose_random()
        the_lpurp.get_one(random_lpurp)

    @BaseUnitTest.log_try_except
    def test_03_post_one(self):
        """
        1. Create new.
        2. Get newly created.
        """

        the_lpurp = LoanPurpose()
        json_lpurp = the_lpurp.post_one()
        the_lpurp.get_one(json_lpurp)


if __name__ == '__main__':
    unittest.main()
