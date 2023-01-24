# NHN_Edu

0.수집대상1 사전크롤링 후 과제시작.

1.장고 환경설정 후 크롬드라이버이용하여 크롤링 시작.

```python
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
```
2.파싱하여 값을 가공한 후에 데이터들을 리스트에 넣어 저장.

3.각 url마다 함수를 만들어 값 추출 후 아래사진처럼 링크연결.

<img width="1232" alt="스크린샷 2023-01-24 오후 6 33 16" src="https://user-images.githubusercontent.com/108647861/214257140-8bab118f-635b-4dec-b9b9-49f75d1aef52.png">

4.링크 클릭시 크롤링 추출값 출력
<img width="1232" alt="스크린샷 2023-01-24 오후 6 35 00" src="https://user-images.githubusercontent.com/108647861/214257386-d8b53030-44fc-4220-b7c1-cc63b83fe976.png">









회고

크롤링은 처음이라 시행착오가 많았다.

시간형태를 맞추는 것이 까다로웠다.(실패함)

이미 크롤링한 값을 원하는 형태로 바꿔주는 로직을 더 고민해봐야할것같다.

터미널에서는 제대로 나오던 값들이 runserver를 하니 오류가 생기는 부분이 많았다.

입출력이 자유형식이라 정말 데이터만 가공해서 가져오면 되는 과제여서 더욱 아쉬움이 남는다.

과제예시처럼 json을 활용하여 다시 공부해봐야겠다.
