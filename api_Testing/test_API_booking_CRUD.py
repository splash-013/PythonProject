from commonComponent_CRUD import request_context, read_json, base_url

#--------------
# POST request
#--------------
def test_create_booking(request_context):
    data=read_json("testData/post_requestBody.json")
    response=request_context.post(f"{base_url}/booking", data=data)
    assert response.status==200
    assert response.ok

    response_body=response.json()
    print("Response body===>",response_body)

    # MAKING booking_id GLOBAL TO MAKE IT AVAILABLE FOR ALL THE FUNCTIONS
    global booking_id, booking_firstName, booking_lastName
    booking_id=response_body["bookingid"]
    booking_firstName=response_body["booking"]["firstname"]
    booking_lastName=response_body["booking"]["lastname"]

#--------------
# GET request
#--------------
def test_get_booking_by_id(request_context):
    response=request_context.get(f"{base_url}/booking/{booking_id}")
    assert response.ok
    assert response.status==200


def test_get_booking_by_name(request_context):
    response=request_context.get(f"{base_url}/booking?firstname={booking_firstName}&lastname={booking_lastName}")
    assert response.ok
    assert response.status == 200

#--------------
# POST request - Create Token
#--------------
def test_create_token(request_context):
    data=read_json("testData/post_token_RequestBody.json")
    response=request_context.post(f"{base_url}/auth", data=data)
    response_body=response.json()
    global token
    token = response_body["token"]
    print("Token===>",token)
    assert response.status == 200

#--------------
# PATCH request - Token is required to update the data
#--------------
def test_partial_update_booking(request_context):
    data=read_json("testData/patch_requestBody.json")
    response=request_context.patch(f"{base_url}/booking/{booking_id}",
                                   data=data,
                                   headers={"Cookie":f"token={token}"})
    response_body=response.json()
    assert response.status == 200
    assert "firstname" in response_body
    print("Partial updated booking: ", response_body)

    for key in data.keys(): # keys() method to get the key from key value pair
        assert key in response_body
        assert response_body[key]==data[key]

#--------------
# PUT request - Token is required to update the data
#--------------
def test_full_update_booking(request_context):
    data=read_json("testData/put_requestBody.json")
    response=request_context.put(f"{base_url}/booking/{booking_id}",
                        data=data,
                        headers={"Cookie":f"token={token}"})

    response_body = response.json()

    assert response.status == 200
    assert "firstname" in response_body
    print("Updated booking: ", response_body)

    for key in data.keys():  # keys() method to get the key from key value pair
        assert key in response_body
        assert response_body[key] == data[key]

#--------------
# DELETE request
#--------------
def test_delete_booking(request_context):
    response=request_context.delete(f"{base_url}/booking/{booking_id}",
                                    headers={"Cookie":f"token={token}"})

    assert response.status==201









