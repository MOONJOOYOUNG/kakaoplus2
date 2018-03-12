import json
import requests
import datetime
import random
from bs4 import BeautifulSoup
from . import parser
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

# 제2 학식

# kb 학사
def Kb_Dormitory():
    messages = ''

    if t[r] == '월':
        messages += (t[r] + '요일 KB 학사 학식 메뉴' + kb[1].get_text())
        return parser.dom_parser(messages)

    elif t[r] == '화':
        messages += (t[r] + '요일 KB 학사 학식 메뉴' + kb[2].get_text())
        return parser.dom_parser(messages)

    elif t[r] == '수':
        messages += (t[r] + '요일 KB 학사 학식 메뉴' + kb[3].get_text())
        return parser.dom_parser(messages)

    elif t[r] == '목':
        messages += (t[r] + '요일 KB 학사 학식 메뉴' + kb[4].get_text())
        return parser.dom_parser(messages)

    elif t[r] == '금':
        messages += (t[r] + '요일 KB 학사 학식 메뉴' + kb[5].get_text())
        return parser.dom_parser(messages)

    elif t[r] == '토':
        messages += (t[r] + '요일 KB 학사 학식 메뉴' + kb[6].get_text())
        return parser.dom_parser(messages)

    elif t[r] == '일':
        messages += (t[r] + '요일 KB 학사 학식 메뉴' + kb[7].get_text())
        return parser.dom_parser(messages)

# 성림 학사
def Sungrim_Dormitory():
    messages = ''

    if t[r] == '월':
        messages += (t[r] + '요일 성림 학사 학식 메뉴' + sung[1].get_text())
        return parser.dom_parser(messages)

    elif t[r] == '화':
        messages += (t[r] + '요일 성림 학사 학식 메뉴' + sung[2].get_text())
        return parser.dom_parser(messages)

    elif t[r] == '수':
        messages += (t[r] + '요일 성림 학사 학식 메뉴' + sung[3].get_text())
        return parser.dom_parser(messages)

    elif t[r] == '목':
        messages += (t[r] + '요일 성림 학사 학식 메뉴' + sung[4].get_text())
        return parser.dom_parser(messages)

    elif t[r] == '금':
        messages += (t[r] + '요일 성림 학사 학식 메뉴' + sung[5].get_text())
        return parser.dom_parser(messages)

    elif t[r] == '토':
        messages += (t[r] + '요일 성림 학사 학식 메뉴' + sung[6].get_text())
        return parser.dom_parser(messages)

    elif t[r] == '일':
        messages += (t[r] + '요일 성림 학사 학식 메뉴' + sung[7].get_text())
        return parser.dom_parser(messages)

# 수림 학사
def Surim_Dormitory():
    messages = ''

    if t[r] == '월':
        messages += (t[r] + '요일 수림 학사 학식 메뉴' + surim[1].get_text())
        return parser.dom_parser(messages)

    elif t[r] == '화':
        messages += (t[r] + '요일 수림 학사 학식 메뉴' + surim[2].get_text())
        return parser.dom_parser(messages)

    elif t[r] == '수':
        messages += (t[r] + '요일 수림 학사 학식 메뉴' + surim[3].get_text())
        return parser.dom_parser(messages)

    elif t[r] == '목':
        messages += (t[r] + '요일 수림 학사 학식 메뉴' + surim[4].get_text())
        return parser.ser(messages)

    elif t[r] == '금':
        messages += (t[r] + '요일 수림 학사 학식 메뉴' + surim[5].get_text())
        return parser.dom_parser(messages)

    elif t[r] == '토':
        messages += (t[r] + '요일 수림 학사 학식 메뉴' + surim[6].get_text())
        return parser.dom_parser(messages)

    elif t[r] == '일':
        messages += (t[r] + '요일 서캠퍼스 학식 메뉴' + surim[7].get_text())
        return parser.dom_parser(messages)

# 제 2학생 식단
def Food_two():
    driver.get('http://www.seoultech.ac.kr/life/student/food/')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    food_two = soup.findAll("td", limit=130)
    messages = ''

    if t[r] == '월':
        messages += (t[r] + '요일 제2학생 식당 메뉴\n' + '◎중식 든든 ' + food_two[13].get_text() + '◎\n'
                     + food_two[8].get_text() + ' ' + food_two[18].get_text() + ' ' + food_two[23].get_text() + ' ' + food_two[28].get_text() + ' ' +
                     food_two[33].get_text() + '\n')
        messages += ('◎중식 푸짐 4200원◎\n' + food_two[39].get_text() + ' ' + food_two[44].get_text() + ' ' + food_two[49].get_text() + ' ' + food_two[54].get_text() + ' ' +
                     food_two[59].get_text() + ' ' + food_two[65].get_text() + '\n')
        messages += ('◎석식 푸짐 3500◎\n' + food_two[98].get_text() + ' ' + food_two[103].get_text() + ' ' + food_two[108].get_text() + ' ' + food_two[113].get_text() + ' ' +
                     food_two[118].get_text() + ' ' + food_two[123].get_text() + '\n')
        messages += '◎간단 메뉴 + 공깃밥◎\n계란라면 2800원\n떡계란라면 치즈계란라면\n물만두계란라면 3200원\n'
        messages += '◎운영시간 - 중식 11:00~14:00 석식 17:00~19:00 (18:40분까지 주문가능)◎'

        return parser.food_parser(messages)

    elif t[r] == '화':
        messages += (t[r] + '요일 제2학생 식당 메뉴\n' + '◎든든 ' + food_two[14].get_text() + '◎\n'
                     + food_two[9].get_text() + ' ' + food_two[19].get_text() + ' ' + food_two[24].get_text() + ' ' + food_two[29].get_text() + ' ' +
                     food_two[34].get_text() + '\n')
        messages += ('◎푸짐 4200원◎\n' + food_two[40].get_text() + ' ' + food_two[45].get_text() + ' ' + food_two[50].get_text() + ' ' + food_two[55].get_text() + ' ' +
                     food_two[60].get_text() + ' ' + food_two[65].get_text() + '\n')
        messages += ('◎석식 푸짐 3500◎\n' + food_two[99].get_text() + ' ' + food_two[104].get_text() + ' ' + food_two[109].get_text() + ' ' + food_two[114].get_text() + ' ' +
                     food_two[119].get_text() + ' ' + food_two[124].get_text() + '\n')
        messages += '◎간단 메뉴 + 공깃밥◎\n계란라면 2800원\n떡계란라면 치즈계란라면\n물만두계란라면 3200원\n'
        messages += '◎운영시간 - 중식 11:00~14:00 석식 17:00~19:00 (18:40분까지 주문가능)◎'
        return parser.food_parser(messages)

    elif t[r] == '수':
        messages += (t[r] + '요일 제2학생 식당 메뉴\n' + '◎든든 ' + food_two[15].get_text() + '◎\n'
                     + food_two[10].get_text() + ' ' + food_two[20].get_text() + ' ' + food_two[25].get_text() + ' ' + food_two[30].get_text() + ' ' +
                     food_two[35].get_text() + '\n')
        messages += ('◎푸짐 4200원◎\n' + food_two[41].get_text() + ' ' + food_two[46].get_text() + ' ' + food_two[51].get_text() + ' ' + food_two[56].get_text() + ' ' +
                     food_two[61].get_text() + ' ' + food_two[66].get_text() + '\n')
        messages += ('◎석식 푸짐 3500◎\n' + food_two[100].get_text() + ' ' + food_two[105].get_text() + ' ' + food_two[110].get_text() + ' ' + food_two[115].get_text() + ' ' +
                     food_two[120].get_text() + ' ' + food_two[125].get_text() + '\n')
        messages += '◎간단 메뉴 + 공깃밥◎\n계란라면 2800원\n떡계란라면 치즈계란라면\n물만두계란라면 3200원\n'
        messages += '◎운영시간 - 중식 11:00~14:00 석식 17:00~19:00 (18:40분까지 주문가능)◎'

        return parser.food_parser(messages)

    elif t[r] == '목':
        messages += (t[r] + '요일 제2학생 식당 메뉴\n' + '◎든든 ' + food_two[16].get_text() + '◎\n'
                     + food_two[11].get_text() + ' ' + food_two[21].get_text() + ' ' + food_two[26].get_text() + ' ' + food_two[31].get_text() + ' ' +
                     food_two[36].get_text() + '\n')
        messages += ('◎푸짐 4200원◎\n' + food_two[42].get_text() + ' ' + food_two[47].get_text() + ' ' + food_two[52].get_text() + ' ' + food_two[57].get_text() + ' ' +
                     food_two[62].get_text() + ' ' + food_two[67].get_text() + '\n')
        messages += ('◎석식 푸짐 3500◎\n' + food_two[101].get_text() + ' ' + food_two[106].get_text() + ' ' + food_two[111].get_text() + ' ' + food_two[116].get_text() + ' ' +
                     food_two[121].get_text() + ' ' + food_two[126].get_text() + '\n')
        messages += '◎간단 메뉴 + 공깃밥◎\n계란라면 2800원\n떡계란라면 치즈계란라면\n물만두계란라면 3200원\n'
        messages += '◎운영시간 - 중식 11:00~14:00 석식 17:00~19:00 (18:40분까지 주문가능)◎'

        return parser.food_parser(messages)

    elif t[r] == '금':
        messages += (t[r] + '요일 제2학생 식당 메뉴\n' + '◎든든 ' + food_two[17].get_text() + '◎\n'
                     + food_two[12].get_text() + ' ' + food_two[22].get_text() + ' ' + food_two[27].get_text() + ' ' + food_two[32].get_text() + ' ' +
                     food_two[37].get_text() + '\n')
        messages += ('◎푸짐 4200원◎\n' + food_two[43].get_text() + ' ' + food_two[48].get_text() + ' ' + food_two[53].get_text() + ' ' + food_two[58].get_text() + ' ' +
                     food_two[63].get_text() + ' ' + food_two[68].get_text() + '\n')
        messages += ('◎석식 푸짐 3500◎\n' + food_two[102].get_text() + ' ' + food_two[107].get_text() + ' ' + food_two[112].get_text() + ' ' + food_two[117].get_text() + ' ' +
                     food_two[122].get_text() + ' ' + food_two[127].get_text() + '\n')
        messages += '◎간단 메뉴 + 공깃밥◎\n계란라면 2800원\n떡계란라면 치즈계란라면\n물만두계란라면 3200원\n'
        messages += '◎운영시간 - 중식 11:00~14:00 석식 17:00~19:00 (18:40분까지 주문가능)◎'

        return parser.food_parser(messages)

    elif t[r] == '토':
        messages += ('토요일 제공하지 않습니다.\n')
        return messages

    elif t[r] == '일':
        messages += ('토요일 제공하지 않습니다.\n')
        return messages

#kb 학사 전체
def KB_All():
    messages = ''

    messages += ('◎월요일 학식 메뉴◎' + kb[1].get_text())
    messages += ('◎화요일 학식 메뉴◎' + kb[2].get_text())
    messages += ('◎수요일 학식 메뉴◎' + kb[3].get_text())
    messages += ('◎목요일 학식 메뉴◎' + kb[4].get_text())
    messages += ('◎금요일 학식 메뉴◎' + kb[5].get_text())
    messages += ('◎토요일 학식 메뉴◎' + kb[6].get_text())
    messages += ('◎일요일 학식 메뉴◎' + kb[7].get_text())
    return parser.dom_parser(messages)

# 성림 학사 전체
def Sungrim_All():
    messages = ''

    messages += ('◎월요일 학식 메뉴◎' + sung[1].get_text())
    messages += ('◎화요일 학식 메뉴◎' + sung[2].get_text())
    messages += ('◎수요일 학식 메뉴◎' + sung[3].get_text())
    messages += ('◎목요일 학식 메뉴◎' + sung[4].get_text())
    messages += ('◎금요일 학식 메뉴◎' + sung[5].get_text())
    messages += ('◎토요일 학식 메뉴◎' + sung[6].get_text())
    messages += ('◎일요일 학식 메뉴◎' + sung[7].get_text())
    return parser.dom_parser(messages)

# 수림 학사 전체
def Surim_All():
    messages = ''

    messages += ('◎월요일 학식 메뉴◎' + surim[1].get_text())
    messages += ('◎화요일 학식 메뉴◎' + surim[2].get_text())
    messages += ('◎수요일 학식 메뉴◎' + surim[3].get_text())
    messages += ('◎목요일 학식 메뉴◎' + surim[4].get_text())
    messages += ('◎금요일 학식 메뉴◎' + surim[5].get_text())
    messages += ('◎토요일 학식 메뉴◎' + surim[6].get_text())
    messages += ('◎일요일 학식 메뉴◎' + surim[7].get_text())
    return parser.dom_parser(messages)

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
