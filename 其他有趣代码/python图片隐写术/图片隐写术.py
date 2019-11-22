#coding:utf-8
# Python3 图片隐写术

from PIL import Image

"""
function:取得一个PIL图像并且更改所有值为偶数(使最低有效位为0)
"""
def makeImageEven(image):
    pixels = list(image.getdata())    # 得到一个[(r,g,b,t)]列表
    # 更改所有值为偶数(魔法般的移位)
    evenPixels = [(r>>1<<1,g>>1<<1,b>>1<<1,t>>1<<1) for [r,g,b,t] in pixels]
    evenImage = Image.new(image.mode, image.size)    # 创建一个相同大小的图片副本
    evenImage.putdata(evenPixels)    # 把上面的像素放入到图片副本
    return evenImage


"""
function:内置函数bin()的替代,返回固定长度的二进制字符串
"""
def constLenBin(int):
    # 去掉 bin()返回的二进制字符串中的'0b',并在左边补足'0'直到字符串长度为8
    binary = "0"*(8-(len(bin(int))-2))+bin(int).replace('0b','')
    return binary

"""
funtion:将字符串编码到图片中
"""
def encodeDataInImage(image, data):
    evenImage = makeImageEven(image)    # 获得最低有效位为0的图片副本
    binary = ''.join(map(constLenBin, bytearray(data, 'utf-8')))  # 将要隐藏字符串转成2进制
    # 如果不能编码全部数据则抛出异常
    if len(binary) > len(image.getdata()) * 4:
        raise Exception('在此图像中不能编码超过'+ len(evenImage.getdata())*4 +'位')
    # 将 binary 中的二进制字符串信息编码进像素里
    encodedPixels = [(r+int(binary[index*4+0]),g+int(binary[index*4+1]),\
                      b+int(binary[index*4+2]),t+int(binary[index*4+3])) \
                     if index*4<len(binary) else(r,g,b,t) for index,(r,g,b,t) \
                     in enumerate(list(evenImage.getdata()))]
    encodedImage = Image.new(evenImage.mode, evenImage.size)  # 创建新图片以存放编码后的像素
    encodedImage.putdata(encodedPixels)    # 添加编码后的数据
    return encodedImage

"""
function:从二进制字符串转为 UTF-8 字符串
"""
def binaryToString(binary):
    index = 0
    string = []
    rec = lambda x, i: x[2:8] + (rec(x[8:],i-1) if i>1 else '') if x else ''
    # rec = lambda x, i: x and (x[2:8] + (i > 1 and rec(x[8:], i-1) or '')) or ''
    fun = lambda x,i:x[i+1:8] + rec(x[8:],i-1)
    while index+1 < len(binary):
        chartype = binary[index:].index('0')
        length = chartype*8 if chartype else 8
        string.append(chr(int(fun(binary[index:index+length],chartype),2)))
        index += length
    return ''.join(string)

"""
function:解码隐藏数据
"""
def decodeImage(image):
    pixels = list(image.getdata())  # 获得像素列表
    # 提取图片中所有最低有效位中的数据
    binary = ''.join([str(int(r>>1<<1!=r))+str(int(g>>1<<1!=g))+str(int(b>>1<<1!=b))\
                      +str(int(t>>1<<1!=t)) for (r,g,b,t) in pixels])
    # 找到数据截止处的索引
    locationDoubleNull = binary.find('0000000000000000')
    endIndex = locationDoubleNull+(8-(locationDoubleNull % 8)) if locationDoubleNull%8 != 0 else locationDoubleNull
    data = binaryToString(binary[0:endIndex])
    return data


encodeDataInImage(Image.open("doraemon.png"), '我腿短呀').save('doraemon1.png')
print(decodeImage(Image.open("doraemon1.png")))





























