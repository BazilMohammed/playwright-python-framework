import pytest
import yaml
import playwright
from playwright.sync_api import expect 
from playwright.sync_api import Page
from pathlib import Path # <-- 1. Add this import

# This function adds the --env command-line option to pytest
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa", help="environment to run tests against")

# This is the fixture that will be available to all our tests
@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

@pytest.fixture(scope="session")
def app_config(env):
    config_path = Path(__file__).parent / "config.yaml"
    with open(config_path) as f:
        config = yaml.safe_load(f)
    return config[env]

@pytest.fixture(scope="function")
def logged_in_page(playwright):
    login_url='https://practicetestautomation.com/practice-test-login/'
    username = "student"
    password = "Password123"

    request_context = playwright.request.new_context()
    response = request_context.post(login_url,
                               form={
                                   "username": username,
                                   "password": password
                               })
    expect(response).to_be_ok()
    #Page.goto(login_url)
    storage_state = request_context.storage_state()
    browser = playwright.chromium.launch()
    context = browser.new_context(storage_state=storage_state)
    page = context.new_page()
    page.goto('https://practicetestautomation.com/logged-in-successfully/')
    yield page
    context.close()
    browser.close()
