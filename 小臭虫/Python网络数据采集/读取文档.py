'''
#读取txt文件
from urllib.request import urlopen
textPage = urlopen(
     'http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt')
print(str(textPage.read()[:100],'utf-8')) #以utf-8编码显示文件信息
'''

'''
#读取csv文件
from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen('http://pythonscraping.com/files/MontyPythonAlbums.csv'
               ).read().decode('ascii','ignore')
dataFile = StringIO(data)
dictReader = csv.DictReader(dataFile)

print(dictReader.fieldnames)
for row in dictReader:
     print(row)
'''

'''
#读取pdf文件
from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager,process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

def readPDF(pdfFile):
     rsrcmgr = PDFResourceManager()
     retstr = StringIO()
     laparams = LAParams()
     device = TextConverter(rsrcmgr,retstr,laparams = laparams)

     process_pdf(rsrcmgr,device,pdfFile)
     device.close()

     content = retstr.getvalue()
     retstr.close()
     return content

pdfFile = urlopen('http://pythonscraping.com/pages/warandpeace/chapter1.pdf') #读取网络pdf文件
#pdfFile = open("../../**.pdf",'rd')  #读取本地pdf文件
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()
'''

'''
#读取docx文档
from zipfile import ZipFile
from io import BytesIO
from urllib.request import urlopen

wordFile = urlopen('http://pythonscraping.com/pages/AwordDocument.docx').read()
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')
print(xml_content.decode('utf-8'))
'''










