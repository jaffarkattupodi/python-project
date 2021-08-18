from pageobjects.loginpage import login
from selenium import webdriver
from utilities import xlutilities
import pytest

class Test:
    baseurl='https://www.amazon.in/'
    path='C:\\Users\\Admin\\Documents\\Book1.xlsx'
    # username='8309027006'
    # password='jaff@r6581'
    # product='samsung mobiles'

    def testlogin(self,set):
        self.driver=set
        self.driver.get(self.baseurl)

        lp=login(self.driver)
        lp.setAllmenu()
        lp.clicksignuplink()
        rows=xlutilities.getrow(self.path,'Sheet1')
        for row in range(2,rows+1):
            user=xlutilities.readrow(self.path,'Sheet1',row,1)
            password=xlutilities.readrow(self.path,'Sheet1',row,2)
            product=xlutilities.readrow(self.path,'Sheet1',row,3)
            lp.setuseremail(user)
            lp.clickcontinue()
            lp.setuserpassword(password)
            lp.clicksigninbutton()
            if self.driver.title == 'Online Shoppingdasasda site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in':
                assert True
            else:
                self.driver.save_screenshot('C:\\Users\\Admin\\PycharmProjects\\pythonProject\\screenshots\\amazon.png')
    def testproduct(self,set):
        self.driver=set
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(5)
        lp = login(self.driver)
        lp.setAllmenu()
        lp.clicksignuplink()
        rows = xlutilities.getrow(self.path, 'Sheet1')
        for row in range(2, rows + 1):
            user = xlutilities.readrow(self.path, 'Sheet1', row, 1)
            password = xlutilities.readrow(self.path, 'Sheet1', row, 2)
            product = xlutilities.readrow(self.path, 'Sheet1', row, 3)
            lp.setuseremail(user)
            lp.clickcontinue()
            lp.setuserpassword(password)
            lp.clicksigninbutton()
            lp.setsearchbar(product)
            lp.clickproduct()
            if self.driver.title == 'Samsung Galaxy M31 (Ocean Blue, 6GB RAM, 128GB Storage) : Amazon.in: Electronics':
                self.driver.save_screenshot('C:\\Users\\Admin\\PycharmProjects\\pythonProject\\screenshots\\amazonproduct.png')
            else:
                assert False