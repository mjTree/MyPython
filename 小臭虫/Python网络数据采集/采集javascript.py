'''
#实例1，不能确定加载完成时间
from selenium import webdriver
import time

driver = webdriver.PhantomJS()
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
#time.sleep(3)
print(driver.find_element_by_id('content').text)
driver.close()
driver.quit()
'''



'''
#处理重定向
from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException

def waitForLoad(driver):
     elem = driver.find_element_by_tag_name('html')
     count = 0
     while True:
          count += 1
          if count > 20:
               print('过10s后返回')
               return
          time.sleep(.5)
          try:
               elem == driver.find_element_by_tag_name("html")
          except StaleElementReferenceException:
               return

driver = webdriver.PhantomJS()
driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
waitForLoad(driver)
print(driver.page_source)
'''


'''
#实例2,隐式等待加载时间完成
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.PhantomJS()
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
try:
     element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'loadedButton')))
finally:
     print(driver.find_element_by_id('content').text)
     driver.close()
     driver.quit()
'''


'''#百度教程代码

#事例1
from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get("http://hotel.qunar.com/")
data = driver.title
print(data)
driver.close()
driver.quit()


#事例2
from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get('http://hotel.qunar.com/city/beijing_city/dt-20438/?in_track=hotel_recom_beijing_city02')
data = driver.find_element_by_id("jd_comments").text
print(data)
driver.close()
driver.quit()


#事例3
from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get('http://hotel.qunar.com/city/beijing_city/dt-20438/?in_track=hotel_recom_beijing_city02')
data = driver.page_source
print(data[:88])
driver.close()
driver.quit()
'''
