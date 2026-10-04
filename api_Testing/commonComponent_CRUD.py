# FILE USED IN test_API_booking_CRUD file

import json
import pytest
from playwright.sync_api import Playwright
from pytest_playwright.pytest_playwright import playwright

# BASE URL
base_url="https://restful-booker.herokuapp.com"

# UTILITY FUNCTION TO READ JSON
def read_json(file_path):
    file=open(file_path,"r")
    return json.load(file)

# FIXTURE TO CREATE REQUEST CONTEXT
@pytest.fixture(scope="session")
def request_context(playwright:Playwright):
    context=playwright.request.new_context()
    yield context
    context.dispose()




