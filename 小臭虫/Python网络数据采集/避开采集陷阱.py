'''
#修改请求头
import requests
from bs4 import BeautifulSoup

session = requests.Session()
headers = {"User-Agent":
           "Mozilla/5.0(Macintosh;Intel Mac OS X 10_9_5)AppleWebKit 537.36(KHTML,like Gecko)Chrome",
           "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
           }
url = "http://www.whatismybrowser.com/developers/what-http-headrs-is-my-browser-sending"

req = session.get(url,headers=headers)
bsObj = BeautifulSoup(req.text)
print(bsObj.find("table",{"class":"table-striped"}).get_text)
'''



'''
#处理cookie 事例1
from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get('http://pythonscraping.com')
driver.implicitly_wait(1)
print(driver.get_cookies())
driver.close()
driver.quit()
'''



'''
#处理cookie 事例2
from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get('http://pythonscraping.com')
driver.implicitly_wait(1)
print(driver.get_cookies())
driver.close()
driver.quit()

savedCookies = driver.get_cookies()

driver2 = webdriver.PhantomJS()
driver2.get('http://pythonscraping.com')
driver2.delete_all_cookies()
for cookie in savedCookies:
     driver2.add_cookie(cookie)

driver2.get('http://pythonscraping.com')
driver.implicitly_wait(1)
print(driver2.get_cookies())
driver.close()
driver.quit()
'''


'''
#避免蜜罐
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.PhantomJS()
driver.get('http://pythonscraping.com/pages/itsatrap.html')

links = driver.find_elements_by_tag_name('a')
for link in links:
     if not link.is_displayed():
          print('The link '+link.get_attribute('href')+' is a trap')

fields = driver.find_elements_by_tag_name('input')
for field in fields:
     if not field.is_displayed():
          print('Do not change value of:'+field.get_attribute('name'))
driver.close()
driver.quit()
'''
