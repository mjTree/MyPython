
#提交表单1
import requests

#params = {'firstname':'mjTree','lastname':'zzz'}
#r = requests.post('http://pythonscraping.com/pages/files/processing.php',data=params)
#print(r.text)

params = {'TPL_username':'薛志豪525','TPL_password':'woaiwojia1996'}
r = requests.post('https://member/login.jhtml?redirectURL=https%3A%2F%2F618.tmall.com%2F',data=params)
print(r.text)

'''
#提交表单2
import requests

params = {'email_addr':'ryan.e.mitchell@gmail.com'}
r = requests.post(
     'http://post.oreilly.com/client/o/oreilly/forms/quicksignup.cgi',data=params)
print(r.text)
'''


'''
#提交文件和图片
import requests

files = {'uploadFile':open('D:/我的电脑资源/图片/聊天表情/71U.jpg','rb')}
r = requests.post(
     'http://pythonscraping.com/pages/processing2.php',files=files)
     'http://pythonscraping.com/files/form2.html'
print(r.text)
'''


'''
#处理登陆和cookie实例1
import requests

params = {'username':'路','password':'password'}
r = requests.post(
     'http://pythonscraping.com/pages/cookies/welcome.php',params)
print("Cookie is set to:")
print(r.cookies.get_dict())
print('------------')
print('Going to profile page...')
r = requests.get(
     'http://pythonscraping.com/pages/cookies/profile.php',cookies=r.cookies)
print(r.text)
'''


'''
#处理登陆和cookie实例2
import requests

session = requests.Session()

params = {'username':'uesrname','password':'password'}
s = session.post('http://pythonscraping.com/pages/cookies/welcome.php',params)

print("Cookie is set to:")
print(s.cookies.get_dict())
print('------------')
print('Going to profile page...')
s = session.get('http://pythonscraping.com/pages/cookies/profile.php')
print(s.text)
'''


import requests

params = {'username':'1000000000','password':'123','yzm':'NDpp7'}
r = requests.post(
     'http://localhost:58627/Login/Index',params)
print("Cookie is set to:")
print(r.cookies.get_dict())
print('------------')
print('Going to profile page...')
r = requests.get(
     'http://localhost:58627/Login/Index',cookies=r.cookies)
print(r.text)






