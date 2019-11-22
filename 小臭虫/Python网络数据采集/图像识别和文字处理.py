'''
#PS的模糊功能
from PIL import Image,ImageFilter

kitten = Image.open('71U.jpg')
blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
blurryKitten.save('kitten_blurred.jpg')
blurryKitten.show()
'''


'''
#处理格式规范文字
from PIL import Image
import subprocess

def cleanFile(filePath,newFilePath):
     image = Image.open(filePath)

     #对图片进行阀值过滤再保存
     image = image.point(lambda x:0 if x<143 else 255)
     image.save(newFilePath)

     #调用系统tesseract命令对图片进行OCR识别
     subprocess.call(["tesseract",newFilePath,"output"])

     #打开文件读取结果
     outputFile = open("output.txt",'r')
     print(outputFile.read())
     outputFile.close()

cleanFile('alice_color1.png','alice_color2.png')
'''


'''
#从网站图片中抓取文字
import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver

#创建新的selenium driver
driver = webdriver.PhantomJS()
#如果PhantomJS出问题，用火狐浏览器试一试
driver = webdriver.Firefox()

driver.get('http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200')
time.sleep(2)

#单机图书预览按钮
driver.find_element_by_id('sitbLogoImg').click()
imageList = set()

#等待页面加载完成
time.sleep(5)
#当向右箭头可以点击时开始翻页
while 'pointer' in driver.find_element_by_id('sitbReaderRightPageTurner').get_attribute('style'):
     driver.find_element_by_id('sitbReaderRightPageTurner').click()
     time.sleep(2)
     #获取已加载页面
     pages = driver.find_elements_by_xpath("//div[@class='pageImage']/div/img")
     for page in pages:
          image = page.get_attribute('src')
          imageList.add(image)

driver.quit()

#用Tesseract处理收集的URL链接
for image in sorted(imageList):
     urlretrieve(image,'page.jpg')
     p = subprocess.Popen(['tesseract','page.jpg','page'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
     p.wait()
     f = open('page.txt','r')
     print(f.read())
'''



#读取验证码与训练Tesseract






