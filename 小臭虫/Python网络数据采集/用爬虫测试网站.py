'''
#Python单元测试
import unittest

class TestAddition(unittest.TestCase):
     def setup(self):
          print("设置测试")
     def tearDown(self):
          print("拆除测试")
     def test_twoPlusTwo(self):
          total = 2+2
          self.assertEqual(4,total)
if __name__=='__main__':
     unittest.main()
'''



'''
#测试维基百科
from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest

class TestWiKipedia(unittest.TestCase):
     bsObj = None
     def setUpClass():
          global bsObj
          url = "http://en.wikipedia.org/wiki/Monty_Python"
          bsObj = BeautifulSoup(urlopen(url))

     def test_titleText(self):
          global bsObj
          pageTitle = bsObj.find('h1').get_text()
          self.assertEuqal('Monty Python',pageTitle)

     def test_contentExists(self):
          global bsObj
          content = bsObj.find('div',{'id':'mw-content-text'})
          self.assertIsNotNone(content)

if __name__=='__main__':
     unittest.main()
'''



'''
#Selenium单元测试
from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get("http://en.wikipedia.org/wiki/Money_Python")
assert "Money Python" in driver.title
driver.close()
driver.quit()
'''



#与网站进行交互
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.PhantomJS(executable_path='<Path to Phantom JS>')
driver.get("http://pythonscraping.com/pages/files/from.html")

firstnameField




#Python单元测试和Selenium单元测试




         
