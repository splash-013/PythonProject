import base64

import pytest
from playwright.sync_api import Playwright


# -------------
# BASIC AUTH
# URL: https://httpbin.org/basic-auth/user/pass
# USERNAME: user
# PASSWORD: pass
# NOTE: Check for spaces in headers={"Authorization": f"Bearer {token}"})
# -------------
def test_basic_auth(playwright: Playwright):
    request_context = playwright.request.new_context()

    credentials = base64.b64encode(b"user:pass").decode("utf-8")

    response = request_context.get("https://httpbin.org/basic-auth/user/pass",
                                   headers={"Authorization": f"Basic {credentials}"})

    assert response.status == 200
