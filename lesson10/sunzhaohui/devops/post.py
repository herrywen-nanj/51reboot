# _*_ encoding:utf-8 _*_
__author__ = 'sunzhaohui'
__date__ = '2019-07-21 15:28'

import requests
URL = 'http://127.0.0.1:8000/hello/hello/'
#requests.post(URL,data='year=2012&month=09')

payload = {'key1':'value1','key2':'value2'}

headers = {'content-type': 'application/json'}
res =requests.post(URL,data=payload,headers=headers)