import time , pprint
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

options = webdriver.ChromeOptions() # 크롬 옵션 객체 생성
options.add_experimental_option("excludeSwitches",["enable-logging"]) # 불필요한 메세지 제거
options.add_argument("headless") #  브라우저 띄우지않기

driver = webdriver.Chrome(service=Service(ChromeDriverManager(path="NHN_Edu").install()), options=options)

#성남시
seongnam = "https://blog.naver.com/PostList.nhn?blogId=sntjdska123&from=postList&categoryNo=51"
driver.get(seongnam)
html = driver.page_source
driver.implicitly_wait(5)

#현재 scrollHeight 가져오기
last_height = driver.execute_script("return document.body.scrollHeight")

while True :
    #scrollHeight까지 스크롤
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')

    #새로운 내용 로딩될때까지 기다림
    time.sleep(1)

    #새로운 내용 로딩 됐는지 확인
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height


posts = driver.find_elements(By.ID,"postListBody")


# print(len(posts))#160

post_list = []

for idx in range(len(posts[0:10])):
    post = posts[idx]

    #정보
    url = post.find_element(By.TAG_NAME,'a')
    title = post.find_element(By.CLASS_NAME,"title").text
    published_datetime = post.find_element(By.CLASS_NAME,"date").text
    body = None
    attachment_list = None

    post_list.append({
        "url":url,
        "title":title,
        "published_datetime":published_datetime,
        "body":body,
        "attachment_list":attachment_list,
        })

# pprint.pprint(post_list)
driver.quit()

soup = BeautifulSoup(html, "html.parser")

posts = soup.select("thumnaillist")

for idx in range(len(posts[0:10])):
    post = posts[idx]
    
    url = post.a['href']
    title = post.find('strong.title').get_text()
    published_datetime = post.select_one('span.date').get_text()
    body = None
    attachment_list = None
    post_list.append({
        "url":url,
        "title":title,
        "published_datetime":published_datetime,
        "body":body,
        "attachment_list":attachment_list,
        })
pprint.pprint(post_list)