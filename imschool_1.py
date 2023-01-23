import time , pprint
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
# from openpyxl import Workbook
# from selenium.common.exceptions import ElementNotInteractableException

# wb = Workbook(write_only=True)
# ws = wb.create_sheet('페이지 정보')
# ws.append(['url','제목','게시일자','게시물본문','첨부파일리스트'])

options = webdriver.ChromeOptions() # 크롬 옵션 객체 생성
options.add_experimental_option("excludeSwitches",["enable-logging"]) # 불필요한 메세지 제거
options.add_argument("headless") #  브라우저 띄우지않기


driver = webdriver.Chrome(service=Service(ChromeDriverManager(path="NHN_Edu").install()), options=options)

# driver.get("https://school.iamservice.net/organization/1674/group/2001892")

site = "https://school.iamservice.net/organization/1674/group/2001892"#수내초
driver.get(site)
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


posts = driver.find_elements(By.CLASS_NAME,"bx_cont")
# print(len(posts))#160

post_list = []

for idx in range(len(posts[0:10])):
    post = posts[idx]

    #정보
    url = post.find_element(By.CLASS_NAME,"btn_detail")
    title = post.find_element(By.CLASS_NAME,"tit_cont").text
    published_datetime = post.find_element(By.CLASS_NAME,"bx_etc").text
    body = post.find_elements(By.CLASS_NAME,"desc")
    attachment_list = post.find_elements(By.CLASS_NAME,"name")

    post_list.append({
        "url":url,
        "title":title,
        "published_datetime":published_datetime,
        "body":body,
        "attachment_list":attachment_list,
        })
    # ws.append([url,title,published_datetime,body[0],attachment_list])
# pprint.pprint(post_list)
driver.quit()

soup = BeautifulSoup(html, "html.parser")

posts = soup.select(".bx_cont")

for post in posts:
    title = post.select_one('h4.tit_cont').get_text()
    url = post.a['href']
    published_datetime = post.p['span']
    body = post.select('p.desc')
    attachment_list = post.select('span.name')
    post_list.append({
        "url":url,
        "title":title,
        "published_datetime":published_datetime,
        "body":body,
        "attachment_list":attachment_list,
        })
pprint.pprint(post_list)



