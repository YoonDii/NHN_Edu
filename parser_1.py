import requests
from bs4 import BeautifulSoup

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "prepjt.settings")
import django
django.setup()

from blog.models import Searchlist
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pytz
from datetime import datetime

options = webdriver.ChromeOptions() # 크롬 옵션 객체 생성
options.add_experimental_option("excludeSwitches",["enable-logging"]) # 불필요한 메세지 제거
options.add_argument("headless") #  브라우저 띄우지않기
options.add_experimental_option("detach", True) # 브라우저 꺼짐 방지

driver = webdriver.Chrome(service=Service(ChromeDriverManager(path="NHN_Edu").install()), options=options)
driver.implicitly_wait(5)

def iamschool():
    driver.get("https://school.iamservice.net/organization/1674/group/2001892")
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser') 
    posts = soup.select('.bx_cont')

    post_list = []
    for post in posts:
        url = post.a['href']
        title = post.select_one('h4.tit_cont').get_text()
        published_datetime = post.select('span')[-1].get_text() #뒤에 날짜추출
        date_time = datetime.strptime(published_datetime,'%Y-%m-%D %z')
        body = post.select('p.desc')
        attachment_list = post.select('span.name')

        attlist = []
        for att in range(len(attachment_list)):
            atts = attachment_list[att]
            a = atts.get_text()
            attlist.append(a)

        post_list.append({
        "url":url,
        "title":title,
        "published_datetime":date_time,
        "body":body,
        "attachment_list":attlist,
        })
    
    return post_list


# if __name__=='__main__':
#     data_dict = imschool()

#     for i in data_dict:
#         s = Searchlist(url = i['url'], title = i['title'], body = i['body'], published_datetime = i['published_datetime'], attachment_list = i['attachment_list'])
#         s.save()
