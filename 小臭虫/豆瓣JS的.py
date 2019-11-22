#coding:utf-8

import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getLinks(url):
    driver = webdriver.PhantomJS()
    driver.get(url)
    #a = driver.find_element_by_id('wrapper').text;print(a)
    pageSource = driver.page_source
    html_parse = BeautifulSoup(pageSource)
    html = html_parse.findAll("div",{"class":"item-root"})
    driver.close()
    driver.quit()
    return html

url = 'http://deal.ggzy.gov.cn/ds/deal/dealList.jsp'
html = getLinks(url)

html = str(html)
aa = re.findall(r'https:\/\/book.douban.com\/subject\/.*?\/',html)[0]
