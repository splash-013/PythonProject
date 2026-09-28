import pytest
from playwright.sync_api import Page

# CREATE A CLASS FOR LOGIN PAGE
class LoginPage:
     def __init__(self,page:Page): # CREATE A CONSTRUCTOR WHICH HAS ALL THE PAGE ELEMENTS
         self.page=page # page IS A NORMAL PAGE, NEED TO MAKE IT A CLASS PAGE BUT ADDING self.
         # INSIDE CLASS ALL VARIABLES SHOULD BE CLASS VARIABLE
         self.login_link=self.page.locator('#login2') # USER DEFINED CLASS VARIABLE
         self.username=self.page.locator('#loginusername')
         self.password=self.page.locator('#loginpassword')
         self.login_button=self.page.locator("button[onclick='logIn()']")

     # ACTION METHODS
     # FOR INDIVIDUAL ELEMENTS
     def click_login(self):
         self.login_link.click() # CLICK ACTION ON LOGIN LINK

     def enter_username(self,username):
         self.username.fill("") # CLEAR ANY AUTO SUGGESTION
         self.username.fill(username) # INPUT ACTION FOR USERNAME

     def enter_password(self,password):
         self.password.fill("")  # CLEAR ANY AUTO SUGGESTION
         self.password.fill(password) # INPUT ACTION FOR PASSWORD

     def click_login_button(self):
         self.login_button.click() # CLICK ACTION ON LOGIN BUTTON

     # COMBINE ALL THE LOGIN ACTION
     def perform_login(self,username,password):
         self.login_link.click()  # CLICK ACTION ON LOGIN LINK
         self.username.fill("")  # CLEAR ANY AUTO SUGGESTION
         self.username.fill(username)  # INPUT ACTION FOR USERNAME
         self.password.fill("")  # CLEAR ANY AUTO SUGGESTION
         self.password.fill(password)  # INPUT ACTION FOR PASSWORD
         self.login_button.click()  # CLICK ACTION ON LOGIN BUTTON

         # User_001
         # User@123

