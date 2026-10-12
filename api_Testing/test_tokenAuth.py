from playwright.sync_api import *


# -------------
# BEARER TOKEN AUTH
# URL: https://api.github.com/user/repos
# USERNAME: user
# PASSWORD: pass
# NOTE: Check for spaces in headers={"Authorization": f"Bearer {token}"})
# -------------

def test_token_auth(playwright: Playwright):
    # Create your token from github
    token = " ADD TOKEN"
    request_context = playwright.request.new_context()
    response = request_context.get("https://api.github.com/user/repos",
                                   headers={"Authorization": f"Bearer {token}"})
    assert response.status == 200
