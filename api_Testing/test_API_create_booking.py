# ----------------------------
# Test : Create booking
# Method : POST
# Data : Hard coded data
# ----------------------------


from playwright.sync_api import Playwright

def test_createBooking(playwright:Playwright):

    base_url = "https://restful-booker.herokuapp.com"  # CREATE A BASE URL VARIABLE

    request_context = playwright.request.new_context() # CREATE A NEW REQUEST CONTEXT for CRUD OPERATIONS (like browser context)

    # CREATE A REQUEST BODY
    request_body = {
    "firstname" : "Naruto",
    "lastname" : "Uzumaki",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2020-01-01",
        "checkout" : "2021-01-01"
    },
    "additionalneeds" : "Breakfast"
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

    assert booking["firstname"]=="Naruto"
    assert booking["lastname"]=="Uzumaki"

    # NESTED VALIDATIONS
    assert booking["bookingdates"]["checkin"] == "2020-01-01"

