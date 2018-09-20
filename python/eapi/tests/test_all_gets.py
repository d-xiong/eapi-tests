#!/usr/bin/python3
import unittest
from python.common.baseunittest import BaseUnitTest
from python.eapi.methods.users.user import User
from python.eapi.methods.roles.role import Role
from python.eapi.methods.teams.team import Team
from python.eapi.methods.contacts.contact import Contact
from python.eapi.methods.contactgroups.contactgroup import ContactGroup
from python.eapi.methods.contactnotes.contactnote import ContactNote
from python.eapi.methods.loans.loan import Loan
from python.eapi.methods.loantypes.loantype import LoanType
from python.eapi.methods.loanstatuses.loanstatus import LoanStatus
from python.eapi.methods.loanprograms.loanprogram import LoanProgram
from python.eapi.methods.loanpurposes.loanpurpose import LoanPurpose


class RunAllGets(BaseUnitTest):
    """Performs tests on all GET endpoints."""

    @BaseUnitTest.log_try_except
    def test_01_get_users(self):
        """
        1. Get multiple.
        """
        the_user = User()
        the_user.get_multi()

    @BaseUnitTest.log_try_except
    def test_02_get_one_user(self):
        """
        1. Choose a random, existing.
        2. Get only that one.
        """
        the_user = User()
        random_user = the_user.choose_random()
        the_user.get_one(random_user)

    @BaseUnitTest.log_try_except
    def test_03_get_roles(self):
        """
        1. Get multiple.
        """
        the_role = Role()
        the_role.get_multi()

    @BaseUnitTest.log_try_except
    def test_04_get_one_role(self):
        """
        1. Choose a random, existing.
        2. Get only that one.
        """
        the_role = Role()
        random_role = the_role.choose_random()
        the_role.get_one(random_role)

    @BaseUnitTest.log_try_except
    def test_05_get_teams(self):
        """
        1. Get multiple.
        """
        the_team = Team()
        the_team.get_multi()

    @BaseUnitTest.log_try_except
    def test_06_get_one_team(self):
        """
        1. Choose a random, existing.
        2. Get only that one.
        """
        the_team = Team()
        random_team = the_team.choose_random()
        the_team.get_one(random_team)

    @BaseUnitTest.log_try_except
    def test_07_get_contacts(self):
        """
        1. Get multiple.
        """
        the_contact = Contact()
        the_contact.get_multi()

    @BaseUnitTest.log_try_except
    def test_08_get_one_contact(self):
        """
        1. Choose a random, existing.
        2. Get only that one.
        """
        the_contact = Contact()
        random_contact = the_contact.choose_random()
        the_contact.get_one(random_contact)

    @BaseUnitTest.log_try_except
    def test_09_get_contact_groups(self):
        """
        1. Get multiple.
        """
        the_cgroup = ContactGroup()
        the_cgroup.get_multi()

    @BaseUnitTest.log_try_except
    def test_10_get_one_contact_group(self):
        """
        1. Choose a random, existing.
        2. Get only that one.
        """
        the_cgroup = ContactGroup()
        random_cgroup = the_cgroup.choose_random()
        the_cgroup.get_one(random_cgroup)

    @BaseUnitTest.log_try_except
    def test_11_get_contact_notes(self):
        """
        1. Get multiple.
        """
        the_cnote = ContactNote()
        the_cnote.get_multi()

    @BaseUnitTest.log_try_except
    def test_12_get_one_contact_note(self):
        """
        1. Choose a random, existing.
        2. Get only that one.
        """
        the_cnote = ContactNote()
        random_cnote = the_cnote.choose_random()
        the_cnote.get_one(random_cnote)

    @BaseUnitTest.log_try_except
    def test_13_get_loans(self):
        """
        1. Get multiple.
        """
        the_loan = Loan()
        the_loan.get_multi()

    @BaseUnitTest.log_try_except
    def test_14_get_one_loan(self):
        """
        1. Choose a random, existing.
        2. Get only that one.
        """
        the_loan = Loan()
        random_loan = the_loan.choose_random()
        the_loan.get_one(random_loan)

    @BaseUnitTest.log_try_except
    def test_15_get_loan_types(self):
        """
        1. Get multiple..
        """
        the_loantype = LoanType()
        the_loantype.get_multi()

    @BaseUnitTest.log_try_except
    def test_16_get_one_loan_type(self):
        """
        1. Choose a random, existing.
        2. Get only that one.
        """
        the_ltype = LoanType()
        random_loantype = the_ltype.choose_random()
        the_ltype.get_one(random_loantype)

    @BaseUnitTest.log_try_except
    def test_17_get_loan_statuses(self):
        """
        1. Get multiple.
        """
        the_loanstat = LoanStatus()
        the_loanstat.get_multi()

    @BaseUnitTest.log_try_except
    def test_18_get_one_loan_status(self):
        """
        1. Choose a random, existing.
        2. Get only that one.
        """
        the_lstat = LoanStatus()
        random_loanstat = the_lstat.choose_random()
        the_lstat.get_one(random_loanstat)

    @BaseUnitTest.log_try_except
    def test_19_get_loan_programs(self):
        """
        1. Get multiple.
        """
        the_loanprog = LoanProgram()
        the_loanprog.get_multi()

    @BaseUnitTest.log_try_except
    def test_20_get_one_loan_program(self):
        """
        1. Choose a random, existing.
        2. Get only that one.
        """
        the_lprog = LoanProgram()
        random_loanprog = the_lprog.choose_random()
        the_lprog.get_one(random_loanprog)

    @BaseUnitTest.log_try_except
    def test_21_get_loan_purposes(self):
        """
        1. Get multiple.
        """
        the_loanpurp = LoanPurpose()
        the_loanpurp.get_multi()

    @BaseUnitTest.log_try_except
    def test_22_get_one_loan_purpose(self):
        """
        1. Choose a random, existing.
        2. Get only that one.
        """
        the_lpurp = LoanPurpose()
        random_loanpurp = the_lpurp.choose_random()
        the_lpurp.get_one(random_loanpurp)


if __name__ == '__main__':
    unittest.main()
