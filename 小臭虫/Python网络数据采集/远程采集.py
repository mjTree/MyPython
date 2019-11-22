'''
#PySocks
import socks
import socket
from urllib.request import urlopen

socks.set_default_proxy(socks.SOCKS5,'localhost',9150)
socket.socket = socks.socksocket
print(urlopen('http://icanhazip.com').read())
'''




from selenium import webdriver
dervice_args = ['--proxy=localhost:9150','--proxy-type=socks5',]
driver = webdriver.PhantomJS(executable_path='<path to PhantomJS>',service_args=service_args)

driver.get('http://icanhazip.com')
print(driver.page_source)
driver.close()
driver.quit()
