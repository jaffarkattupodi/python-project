
from selenium.webdriver.common.by import By
class login:
    Allmenu_id='nav-hamburger-menu'
    signup_link_xpath="//a[text()='Sign In']"
    UserEmail_xpath="//input[@id='ap_email']"
    continue_button_id='continue'
    Userpassword_id='ap_password'
    signinbutton_id='signInSubmit'
    searchbar_id='twotabsearchtextbox'
    product_xpath="//img[@alt='Samsung Galaxy M31 (Ocean Blue, 6GB RAM, 128GB Storage)']"



    def __init__(self,driver):
        self.driver=driver

    def setAllmenu(self):
        self.driver.find_element(By.ID,self.Allmenu_id).click()
    def clicksignuplink(self):
        self.driver.find_element(By.XPATH,self.signup_link_xpath).click()
    def setuseremail(self,username):
        self.driver.find_element(By.XPATH,self.UserEmail_xpath).send_keys(username)
    def clickcontinue(self):
        self.driver.find_element(By.ID,self.continue_button_id).click()
    def setuserpassword(self,password):
        self.driver.find_element(By.ID,self.Userpassword_id).send_keys(password)
    def clicksigninbutton(self):
        self.driver.find_element(By.ID,self.signinbutton_id).click()
    def setsearchbar(self,product):
        self.driver.find_element(By.ID,self.searchbar_id).send_keys(product)
    def clickproduct(self):
        self.driver.find_element(By.XPATH,self.product_xpath)
