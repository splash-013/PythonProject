# ----------------------------
# Test : Create booking
# Method : POST
# Data : Random data generation (Faker library)
# ----------------------------

import json
from _pydatetime import timedelta, datetime

from faker import Faker
from playwright.sync_api import Playwright

def test_createBooking(playwright:Playwright):

    base_url = "https://restful-booker.herokuapp.com"  # CREATE A BASE URL VARIABLE

    request_context = playwright.request.new_context() # CREATE A NEW REQUEST CONTEXT for CRUD OPERATIONS (like browser context)

    # CREATE RANDOM DATA USING FAKER
    faker=Faker()

    first_name=faker.first_name()
    last_name=faker.last_name()
    total_price=faker.random_int(min=100, max=5000)
    deposit_paid=faker.boolean()
    checkin_date=datetime.now().strftime("%Y-%m-%d")
    checkout_date=(datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d")
    additional_need=faker.word()

    request_body = {
        "firstname": first_name,
        "lastname": last_name,
        "totalprice": total_price,
        "depositpaid": deposit_paid,
        "bookingdates": {
            "checkin": checkin_date,
            "checkout": checkout_date
        },
        "additionalneeds": additional_need
    }

    # CREATE A RESPONSE USING ABOVE THREE
    response=request_context.post(f"{base_url}/booking", data=request_body)  # PASSING THE URL WITH THE ENDPOINT - /booking and DATA

    # ASSERTIONS
    assert response.ok
    assert response.status==200

    response_body = response.json() # GET RESPONSE BODY
    print("Response Body ==>",response_body)

    # VALIDATE FIELDS/ATTRIBUTES IN RESPONSE BODY
    assert "bookingid" in response_body
    assert "booking" in response_body

    # DATA VALIDATIONS IN RESPONSE BODY
    booking = response_body["booking"] # GET booking FROM RESPONSE BODY TO VALIDATE

    assert booking["firstname"]==first_name
    assert booking["lastname"]==last_name

    # NESTED VALIDATIONS
    assert booking["bookingdates"]["checkin"] == checkin_date

