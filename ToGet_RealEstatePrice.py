# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 12:19:13 2020

@author: nerguri
"""

import requests
import re

##지역코드 앞5자리, 계약월 6자리 입력** 
LAWD_CD = '11410'
DEAL_YMD = '201512'

##GET으로 파라미터 넘기기 : dictionary 이용
params = {'LAWD_CD': LAWD_CD, 'DEAL_YMD': DEAL_YMD}
url = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHRent?serviceKey=UlQuKXvKIghn1yCxeO7qEk7kwJMP%2FhPKmqGlO8VaAkGQK4mNsZXotpPGk%2BhXQBr5sQkumy903VclndttTDJhjA%3D%3D&"
response = requests.get(url, params=params)

##data변수에 지역코드와 계약월이 일치하는 데이터 입력
data = response.text

##XML 파일을 "<item>" 키워드 기준으로 자르기 ->  "<item>" 기준으로 리스트화
data_list = data.split('<item>')
