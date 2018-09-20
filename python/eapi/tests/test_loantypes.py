#!/usr/bin/python3
import unittest
from python.common.baseunittest import BaseUnitTest
from python.eapi.methods.loantypes.loantype import LoanType


class TestLoanTypes(BaseUnitTest):
    """Runs Loan Type test scenarios."""

    @BaseUnitTest.log_try_except
    def test_01_get_multi(self):
        """
        1. Get multiple.
        """

        the_ltype = LoanType()
        the_ltype.get_multi()

    @BaseUnitTest.log_try_except
    def test_02_get_one(self):
        """
        1. Choose random, existing.
        2. Get only that one.
        """

        the_ltype = LoanType()
        random_ltype = the_ltype.choose_random()
        the_ltype.get_one(random_ltype)

    @BaseUnitTest.log_try_except
    def test_03_post_one(self):
        """
        1. Create new.
        2. Get the newly created.
        """

        the_ltype = LoanType()
        json_ltype = the_ltype.post_one()
        the_ltype.get_one(json_ltype)


if __name__ == '__main__':
    unittest.main()
