#!/usr/bin/python3
import unittest
from python.common.baseunittest import BaseUnitTest
from python.eapi.methods.loans.loan import Loan


class TestLoans(BaseUnitTest):
    """Runs Loan test scenarios."""

    @BaseUnitTest.log_try_except
    def test_01_get_multi(self):
        """
        1. Get multiple.
        """

        the_loan = Loan()
        the_loan.get_multi()

    @BaseUnitTest.log_try_except
    def test_02_get_one(self):
        """
        1. Choose a random existing team id.
        2. Get only that team.
        """

        the_loan = Loan()
        random_loan = the_loan.choose_random()
        the_loan.get_one(random_loan)

    @BaseUnitTest.log_try_except
    def test_03_post_one(self):
        """
        1. Create new.
        2. Get the newly created.
        """

        the_loan = Loan()
        json_loan = the_loan.post_one()
        the_loan.get_one(json_loan)

    @BaseUnitTest.log_try_except
    def test_04_patch_one(self):
        """
        1. Create new.
        2. Get the newly created.
        3. Update the created.
        4. Get the updates.
        """

        the_loan = Loan()
        json_loan = the_loan.post_one()
        json_loan = the_loan.get_one(json_loan)
        the_loan.patch_one(json_loan)
        the_loan.get_one(json_loan)

    @BaseUnitTest.log_try_except
    def test_05_delete_one(self):
        """
        1. Create new.
        2. Get the newly created.
        3. Delete the new.
        4. Get the freshly deleted, and expect a 404 response.
        """

        the_loan = Loan()
        json_loan = the_loan.post_one()
        the_loan.get_one(json_loan)
        the_loan.delete_one(json_loan)
        the_loan.get_one(json_loan, expected_code=404)


if __name__ == '__main__':
    unittest.main()
