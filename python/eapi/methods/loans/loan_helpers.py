#!/usr/bin/python3
import time
import json
import python.common.datagenerators.generatefakedata as fake
import python.eapi.methods.contacts.contact_helpers as cohelp
from python.eapi.methods.users.user import User
from python.eapi.methods.loanprograms.loanprogram import LoanProgram
from python.eapi.methods.loanpurposes.loanpurpose import LoanPurpose
from python.eapi.methods.loanstatuses.loanstatus import LoanStatus
from python.eapi.methods.loantypes.loantype import LoanType


def grab_post_json():
    """
    Grabs json for post endpoint.

    :return: json, the data.
    """

    the_time = int(time.time())
    the_name = "loan.test.x.{}".format(the_time)
    user = User().choose_random()
    borrower = json.loads(cohelp.grab_post_json(user, "borrower"))
    # Loans endpoint does not like it when its Loan Participants have "options".
    borrower.pop("options")
    coborrower = json.loads(cohelp.grab_post_json(user, "coborrower"))
    coborrower.pop("options")
    lprog = LoanProgram().choose_random()
    lpurp = LoanPurpose().choose_random()
    lstat = LoanStatus().choose_random()
    ltype = LoanType().choose_random()

    return json.dumps(
        {
            "external_id": fake.grab_external_id(the_name),
            "loan_number": the_time,
            "loan_rate": fake.grab_decimal(),
            "loan_term": 360,
            "loan_application_number": the_time,
            "buydown_points": fake.grab_percent(),
            "monthly_pi_payment": fake.grab_money(),
            "monthly_pi_with_mi_payment": fake.grab_money(),
            "investor": fake.grab_company(),
            "debt_to_income": fake.grab_percent(),
            "closing_disclosure_out_date": fake.grab_fake_date(),
            "closing_disclosure_signed_date": fake.grab_fake_date(),
            "source": fake.grab_source(),
            "purchase_price": fake.grab_money(),
            "appraised_value": fake.grab_money(),
            "is_first_time_buyer": fake.grab_bool(),
            "property_type": fake.grab_word(),
            "address": fake.grab_address_one(),
            "address_2": fake.grab_address_two(),
            "city": fake.grab_city(),
            "state": fake.grab_state_abbr(),
            "zip_code": fake.grab_zip(),
            "county": fake.grab_word(),
            "loan_name": the_name,
            "pre_approval_issued": fake.grab_bool(),
            "loan_amount": fake.grab_money(),
            "loan_to_value_combined": fake.grab_percent(),
            "loan_to_value": fake.grab_percent(),
            "occupancy_type": fake.grab_phrase(),
            "estimated_value": fake.grab_money(),
            "lock_status": fake.grab_phrase(),
            "escrow_waived": fake.grab_bool(),
            "referral_source": fake.grab_source(),
            "annual_review_date": fake.grab_fake_date(),
            "application_date": fake.grab_fake_date(),
            "appraisal_expected_date": fake.grab_fake_date(),
            "appraisal_ordered_date": fake.grab_fake_date(),
            "appraisal_received_date": fake.grab_fake_date(),
            "approval_date": fake.grab_fake_date(),
            "closing_date": fake.grab_fake_date(),
            "created_date": fake.grab_fake_date(),
            "credit_report_date": fake.grab_fake_date(),
            "ctc_date": fake.grab_fake_date(),
            "documents_signed_date": fake.grab_fake_date(),
            "epo_date": fake.grab_fake_date(),
            "last_modified_date": fake.grab_fake_date(),
            "first_payment_date": fake.grab_fake_date(),
            "funded_date": fake.grab_fake_date(),
            "loan_arm_expiration_date": fake.grab_fake_date(),
            "lock_date": fake.grab_fake_date(),
            "lock_expiration_date": fake.grab_fake_date(),
            "pre_approval_expiration_date": fake.grab_fake_date(),
            "pre_approval_issued_date": fake.grab_fake_date(),
            "processing_start_date": fake.grab_fake_date(),
            "underwriting_approval_date": fake.grab_fake_date(),
            "underwriting_submission_date": fake.grab_fake_date(),
            "resubmittal_date": fake.grab_fake_date(),
            "audits_date": fake.grab_fake_date(),
            "docs_out_date": fake.grab_fake_date(),
            "funds_requested_date": fake.grab_fake_date(),
            "funding_date": fake.grab_fake_date(),
            "post_closed_date": fake.grab_fake_date(),
            "purchased_date": fake.grab_fake_date(),
            "completion_date": fake.grab_fake_date(),
            "lien_position": fake.grab_phrase(),
            "amort_type": fake.grab_phrase(),
            "amort_type_arm_desc": fake.grab_phrase(),
            "owner": {
                "id": user["id"]
            },
            "loan_program": {
                "id": lprog["id"]
            },
            "loan_purpose": {
                "id": lpurp["id"]
            },
            "loan_status": {
                "id": lstat["id"]
            },
            "loan_type": {
                "id": ltype["id"]
            },
            "credit_score": {
                "credit_score": fake.grab_small_int(),
                "scoring_agency": fake.grab_company(),
                "score_date": fake.grab_fake_date(),
            },
            "borrower": borrower,
            "coborrower": coborrower,
            "buyers_agent": coborrower,
            "sellers_agent": coborrower,
            "settlement_agent": coborrower,
            "options": {
                "suppress_emails": fake.grab_bool()
            }
        }
    )


def grab_patch_json(json_origin):
    """
    Grabs json for patch endpoint.

    :param json_origin: json, the original.
    :return: json, the data.
    """

    new_user = User().choose_random()
    new_borrower = json.loads(cohelp.grab_post_json(new_user, "borrower"))
    new_borrower.pop("options")
    new_coborrower = json.loads(cohelp.grab_post_json(new_user, "coborrower"))
    new_coborrower.pop("options")
    new_lprog = LoanProgram().choose_random()
    new_lpurp = LoanPurpose().choose_random()
    new_lstat = LoanStatus().choose_random()
    new_ltype = LoanType().choose_random()

    return json.dumps(
        {
            "loan_name": "EDIT.{}".format(json_origin["loan_name"]),
            "owner": {
                "id": new_user["id"]
            },
            "loan_program": {
                "id": new_lprog["id"]
            },
            "loan_purpose": {
                "id": new_lpurp["id"]
            },
            "loan_status": {
                "id": new_lstat["id"]
            },
            "loan_type": {
                "id": new_ltype["id"]
            },
            "borrower": new_borrower,
            "coborrower": new_coborrower,
            "buyers_agent": new_coborrower,
            "sellers_agent": new_coborrower,
            "settlement_agent": new_coborrower
        }
    )