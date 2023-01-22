import time ,json, pprint,re, os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import ElementNotInteractableException



options = webdriver.ChromeOptions() # 크롬 옵션 객체 생성
options.add_experimental_option("excludeSwitches",["enable-logging"]) # 불필요한 메세지 제거
options.add_argument("headless") #  브라우저띄우지않기


driver = webdriver.Chrome(service=Service(ChromeDriverManager(path="NHN_Edu").install()), options=options)

# driver.get("https://school.iamservice.net/organization/1674/group/2001892")

url = "https://school.iamservice.net/organization/19710/group/2091428"
driver.get(url)
html = driver.page_source
driver.implicitly_wait(5)

posts = driver.find_elements(By.CLASS_NAME,"bx_cont")
# print(len(posts))#20

post_list = []

for i in range(len(posts)-10):
    post = posts[i]

    #정보
    post_url = post.find_element(By.CLASS_NAME,"btn_detail")
    title = post.find_element(By.CLASS_NAME,"tit_cont").text
    published_datetime = post.find_element(By.CLASS_NAME,"bx_etc")
    body = post.find_element(By.CLASS_NAME,"desc")
    attachment_list = post.find_element(By.CLASS_NAME,"name").text

    print(post_url)
    print(title)
    print(published_datetime)
    print(body)
    print(attachment_list)


# import requests
# from bs4 import BeautifulSoup

# URL ="https://school.iamservice.net/organization/19710/group/2091428"
# res = requests.get(URL)
# res.raise_for_status()

# soup = BeautifulSoup(res.text, "lxml")

# posts = soup.find_all("section",attrs={"class":"inner_cont"})
# print(posts)
# url = posts[0].a["href"]
# title = posts[0].h4.get_text()
# published_datetim = posts[0].p.get_text()
# attachment_list = posts[0].span.get_text()

# print(url)
# print(title)
# print(published_datetim)
# print(attachment_list)

