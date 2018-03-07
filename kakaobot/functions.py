import json
import requests
import datetime
import random
from bs4 import BeautifulSoup
from . import parser
import time, requests
from selenium import webdriver
def NearCampus():

    idx = random.randint(0, 35)
    a = ['원화루', '미가', '문희네', '예다랑', '도스마스', '213버거', '맘스터치', '할머니국밥', '엉터리생고기', '안동찜닭', '그린토마토', '지지고', '서브웨이',
         '알촌',
         '돈다리', '일미닭갈비', '낭만순두부', '해뜨는집', '솔뫼해장국', '오늘은닭', '통통우동&컵밥', '강청골 순대국밥', '솔바람 꽃내음', '마루',
         '민동', '엽기떡볶이', '빨봉분식', '우리들족발', '고향집', '고향의맛', '덤', '또또와 식당', '할머니 족발보쌈', '뒤집어진 뚝배기', '피자스쿨', '도깨비장터']
    return a[idx]

def FoodList():
    message = ''
    a = ['원화루', '미가', '문희네', '예다랑', '도스마스', '213버거', '맘스터치', '할머니국밥', '엉터리생고기', '안동찜닭', '그린토마토', '지지고', '서브웨이',
         '알촌',
         '돈다리', '일미닭갈비', '낭만순두부', '해뜨는집', '솔뫼해장국', '오늘은닭', '통통우동&컵밥', '강청골 순대국밥', '솔바람 꽃내음', '마루',
         '민동', '엽기떡볶이', '빨봉분식', '우리들족발', '고향집', '고향의맛', '덤', '또또와 식당', '할머니 족발보쌈', '뒤집어진 뚝배기', '피자스쿨', '도깨비장터']

    for idx, tag in enumerate(a, 1):
        message += (str(idx) + '.' + a[idx - 1] + " ")

    messages = message.replace("'", '')
    messages = message.replace(",", ' ')

    return messages

#선언부
utcnow = datetime.datetime.utcnow()
time_gap = datetime.timedelta(hours=9)
kor_time = utcnow + time_gap

t = ['월', '화', '수', '목', '금', '토', '일']
r = kor_time.weekday()
driver = webdriver.PhantomJS()

#kb 학사
driver.get('http://domi.seoultech.ac.kr/support/food/?foodtype=kb')
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
kb = soup.findAll("td", limit=8)

# 성림 학사
driver.get('http://domi.seoultech.ac.kr/support/food/?foodtype=sung')
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
sung = soup.findAll("td", limit=8)


# 수림 학사.
driver.get('http://domi.seoultech.ac.kr/support/food/?foodtype=surim')
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
surim = soup.findAll("td", limit=8)

# kb 학사
def Kb_Dormitory():
    messages = ''

    if t[r] == '월':
        messages += (t[r] + '요일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + kb[0].get_text())
        return parser.ser(messages)

    elif t[r] == '화':
        messages += (t[r] + '요일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + kb[1].get_text())
        return parser.ser(messages)

    elif t[r] == '수':
        messages += (t[r] + '요일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + kb[2].get_text())
        return parser.ser(messages)

    elif t[r] == '목':
        messages += (t[r] + '요일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + kb[3].get_text())
        return parser.ser(messages)

    elif t[r] == '금':
        messages += (t[r] + '요일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + kb[4].get_text())
        return parser.ser(messages)

    elif t[r] == '토':
        messages += (t[r] + '요일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + kb[5].get_text())
        return messages

    elif t[r] == '일':
        messages += (t[r] + '요일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + kb[6].get_text())
        return parser.ser(messages)

# 성림 학사
def Sungrim_Dormitory():
    messages = ''

    if t[r] == '월':
        messages += (t[r] + '요일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + sung[0].get_text())
        return parser.ser(messages)

    elif t[r] == '화':
        messages += (t[r] + '요일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + sung[1].get_text())
        return parser.ser(messages)

    elif t[r] == '수':
        messages += (t[r] + '요일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + sung[2].get_text())
        return parser.ser(messages)

    elif t[r] == '목':
        messages += (t[r] + '요일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + sung[3].get_text())
        return parser.ser(messages)

    elif t[r] == '금':
        messages += (t[r] + '요일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + sung[4].get_text())
        return parser.ser(messages)

    elif t[r] == '토':
        messages += (t[r] + '요일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + sung[5].get_text())
        return messages

    elif t[r] == '일':
        messages += (t[r] + '요일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + sung[6].get_text())
        return parser.ser(messages)

# 수림 학사
def Surim_Dormitory():
    messages = ''

    if t[r] == '월':
        messages += (t[r] + '요일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + surim[0].get_text())
        return parser.ser(messages)

    elif t[r] == '화':
        messages += (t[r] + '요일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + surim[1].get_text())
        return parser.ser(messages)

    elif t[r] == '수':
        messages += (t[r] + '요일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + surim[2].get_text())
        return parser.ser(messages)

    elif t[r] == '목':
        messages += (t[r] + '요일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + surim[3].get_text())
        return parser.ser(messages)

    elif t[r] == '금':
        messages += (t[r] + '요일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + surim[4].get_text())
        return parser.ser(messages)

    elif t[r] == '토':
        messages += (t[r] + '요일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + surim[5].get_text())
        return messages

    elif t[r] == '일':
        messages += (t[r] + '요일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + surim[6].get_text())
        return parser.ser(messages)

#kb 학사 전체
def TommorrowWestCampus():
    messages = ''

    messages += ('월요일 학식 메뉴\n' + kb[0].get_text())
    messages += ('화요일 학식 메뉴\n' + kb[1].get_text())
    messages += ('수요일 학식 메뉴\n' + kb[2].get_text())
    messages += ('목요일 학식 메뉴\n' + kb[3].get_text())
    messages += ('금요일 학식 메뉴\n' + kb[4].get_text())
    messages += ('토요일 학식 메뉴\n' + kb[5].get_text())
    messages += ('일요일 학식 메뉴\n' + kb[6].get_text())
    return parser.ser(messages)


# 성림 학사 전체
def TommorrowEastCampus():
    messages = ''

    messages += ('월요일 학식 메뉴\n' + sung[0].get_text())
    messages += ('화요일 학식 메뉴\n'+ sung[1].get_text())
    messages += ('수요일 학식 메뉴\n' + sung[2].get_text())
    messages += ('목요일 학식 메뉴\n' + sung[3].get_text())
    messages += ('금요일 학식 메뉴\n' + sung[4].get_text())
    messages += ('토요일 학식 메뉴\n' + sung[5].get_text())
    messages += ('일요일 학식 메뉴\n' + sung[6].get_text())
    return parser.dong(messages)


# 수림 학사 전체
def TommorrowDormitory():
    messages = ''

    messages += ('월요일 학식 메뉴\n' + surim[0].get_text())
    messages += ('화요일 학식 메뉴\n' + surim[1].get_text())
    messages += ('수요일 학식 메뉴\n' + surim[2].get_text())
    messages += ('목요일 학식 메뉴\n' + surim[3].get_text())
    messages += ('금요일 학식 메뉴\n' + surim[4].get_text())
    messages += ('토요일 학식 메뉴\n' + surim[5].get_text())
    messages += ('일요일 학식 메뉴\n' + surim[6].get_text())
    return parser.kik(messages)

# 네이버 실시간 검색.
def naver_rank():
    html = requests.get('http://naver.com').text
    soup = BeautifulSoup(html, 'html.parser')
    message = []
    tag_list = soup.select('.PM_CL_realtimeKeyword_rolling .ah_item .ah_k')

    for idx, tag in enumerate(tag_list, 1):
        message.append(str(idx) + '.' + tag.text)
    return message

# 멜론 음악 검색.
def melon_search(query):
    params = {
        'jscallback': '_',
        'query': query,
    }
    jsonp_string = requests.get('http://www.melon.com/search/keyword/index.json', params=params).text
    json_string = jsonp_string.replace('_(', '').replace(');', '')
    meta = json.loads(json_string)
    messages = []

    if 'SONGCONTENTS' in meta:
        for song in meta['SONGCONTENTS']:
            messages.append('''[{ALBUMNAME}] {SONGNAME} by {ARTISTNAME}
   - http://www.melon.com/song/detail.htm?songId={SONGID}'''.format(**song))

    if messages:
        message = '\n'.join(messages)
    else:
        message = '검색어 "{}"에 대한 노래 검색결과가 없습니다.'.format(query)
    return message
