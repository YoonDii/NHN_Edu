from django.shortcuts import render, get_list_or_404

# Create your views here.
from .models import Searchlist

import requests
from bs4 import BeautifulSoup

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "prepjt.settings")
import django
django.setup()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from datetime import datetime

options = webdriver.ChromeOptions() # 크롬 옵션 객체 생성
options.add_experimental_option("excludeSwitches",["enable-logging"]) # 불필요한 메세지 제거
options.add_argument("headless") #  브라우저 띄우지않기
options.add_experimental_option("detach", True) # 브라우저 꺼짐 방지

driver = webdriver.Chrome(service=Service(ChromeDriverManager(path="NHN_Edu").install()), options=options)
driver.implicitly_wait(5)

def index(request):
    pass
    return render(request, 'index.html')

#imscchool1 수내초
def imschool1(request):
    driver.get('https://school.iamservice.net/organization/1674/group/2001892')
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser') 
    posts = soup.select('.bx_cont')

    post_list = []
    for post in posts:
        url = post.find('a').attrs['href']
        title = post.select_one('h4.tit_cont').get_text()
        published_datetime = post.select('span')[-1].get_text()
        date_time = datetime.strptime(published_datetime,'%Y.%m.%d')
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

    for i in post_list:
        s = Searchlist(parse_type = "imschool_1", url = i['url'], title = i['title'], body = i['body'], published_datetime = i['published_datetime'], attachment_list = i['attachment_list'])
        s.save()

    data = get_list_or_404(Searchlist.objects.filter(parse_type = "imschool_1"))
    return render(request, 'post.html', {'post':data[:10]})


#imschool 용인초
def imschool2(request):
    driver.get('https://school.iamservice.net/organization/19710/group/2091428')
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser') 
    posts = soup.select('.bx_cont')

    post_list = []
    for post in posts:
        url = post.find('a').attrs['href']
        title = post.select_one('h4.tit_cont').get_text()
        published_datetime = post.select('span')[-1].get_text()
        date_time = datetime.strptime(published_datetime,'%Y.%m.%d')
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

    for i in post_list:
        s = Searchlist(parse_type = "imschool_2", url = i['url'], title = i['title'], body = i['body'], published_datetime = i['published_datetime'], attachment_list = i['attachment_list'])
        s.save()

    data = get_list_or_404(Searchlist.objects.filter(parse_type = "imschool_2"))
    return render(request, 'post.html', {'post':data[0:10]})


# blog1 성남시
def blog1(request):
    driver.get('https://blog.naver.com/PostList.nhn?blogId=sntjdska123&from=postList&categoryNo=51')
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser') 
    posts = soup.select('a.link.pcol2')
    
    post_list = []
    
    for post in posts:
        url = "https://blog.naver.com/" + post.attrs['href']
        title = post.find('strong').string
        published_datetime = post.select_one('sapn.date')
        body = str(post.find('img'))

        post_list.append({
            'url':url, 
            'title':title,  
            'body':body, 
            'published_datetime':published_datetime, 
            'attachment_list': "None"
            })

    for i in post:
        s = Searchlist(parse_type = "blog_1", url = i['url'], title = i['title'], body = i['body'], published_datetime = i['published_datetime'], attachment_list = i['attachment_list'])
        s.save()

    data = get_list_or_404(Searchlist.objects.filter(parse_type = "blog_1"))
    return render(request, 'post.html', {'post':data[0:10]})


# blog2 정부정책
def blog2(request):
    driver.get('https://blog.naver.com/PostList.nhn?blogId=hellopolicy&from=postList&categoryNo=168')
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser') 
    posts = soup.select('a.link.pcol2')
    
    post_list = []
    
    for post in posts:
        url = "https://blog.naver.com/" + post.attrs['href']
        title = post.find('strong').string
        published_datetime = post.select_one('sapn.date').text
        body = str(post.find('img'))

        post_list.append({
            'url':url, 
            'title':title,  
            'body':body, 
            'published_datetime':published_datetime, 
            'attachment_list': "None"
            })

    for i in post:
        s = Searchlist(parse_type = "blog_2", url = i['url'], title = i['title'], body = i['body'], published_datetime = i['published_datetime'], attachment_list = i['attachment_list'])
        s.save()

    data = get_list_or_404(Searchlist.objects.filter(parse_type = "blog_2"))
    return render(request, 'post.html', {'post':data[0:10]})


#news BBC
def news(request):
    driver.get('http://feeds.bbci.co.uk/news/rss.xml')
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser') 
    posts = soup.select('div.paditembox > div')
    
    post_list = []
    
    for post in posts:
        url = post.find('link').get_text()
        title = post.find('a').string
        body = str(post.find('div'))

        post_list.append({
            'url':url, 
            'title':title,  
            'body':body, 
            'attachment_list': "None"})

    for i in post:
        s = Searchlist(parse_type = "news", url = i['url'], title = i['title'], body = i['body'], attachment_list = i['attachment_list'])
        s.save()

    data = get_list_or_404(Searchlist.objects.filter(parse_type = "news"))
    return render(request, 'post.html', {'post':data[0:10]})


def post(request):
    return render(request, 'post.html')