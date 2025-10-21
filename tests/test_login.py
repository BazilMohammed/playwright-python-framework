from playwright.sync_api import Page,expect
from page_objects.login_page import LoginPage
import json

with open('data/test-data.json') as f:
    user_data = json.load(f)

# def test_successful_login(page:Page,app_config):
#     base_url = app_config['base_url']
#     login_page = LoginPage(page)
#     login_page.navigate(base_url)
#     valid_user = user_data['valid_user']
#     login_page.login(valid_user['username'],valid_user['password'])
#     expect(login_page.logout_link).to_be_visible



def test_student_can_log_out(logged_in_page: Page):
    """
    This test receives a page that is already logged in.
    """
    success_message = logged_in_page.locator("h1.post-title")
    expect(success_message).to_have_text("Logged In Successfully")

    # 2. Test the logout functionality
    logout_button = logged_in_page.locator('a:has-text("Log out")')
    logout_button.click()
    
    # 3. Assert that logout was successful by checking the URL
    expect(logged_in_page).to_have_url("https://practicetestautomation.com/practice-test-login/")
