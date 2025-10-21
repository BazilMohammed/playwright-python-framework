from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self,page:Page):
        self.page = page
        self.login_link = page.locator('text="Login"')
        self.username_input = page.locator('#username')
        self.password_input = page.locator('#password')
        self.submit_button = page.locator('input[type="submit"]')
        self.logout_link = page.locator('a[href="/logout"]')
       
   
    
    def navigate(self,base_url:str):
        self.page.goto(base_url)

    def login(self,username,password):
        self.login_link.click()
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()