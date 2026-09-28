from commonComponent_CRUD import request_context, read_json, base_url

# POST request

def create_booking(request_context):
    data=read_json("testData/post_requestBody.json")
    response=request_context.post(f"{base_url}/booking", data=data)
    assert response.status==200
    assert response.ok

