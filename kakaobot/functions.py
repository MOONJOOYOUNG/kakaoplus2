import json
import requests
import datetime
import random
from bs4 import BeautifulSoup
from . import parser

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

def alone():
    idx = random.randint(0, 6)
    a = ['오늘도 혼자이신가요...???? 친한 친구를 꼬셔 외롭지 않게 밥을 먹어요!','혼밥하면 학식이죠!!!',
         '사교성을 기르도록 노력합시다.....ㅜㅜ','대세는 혼밥이죠!! 평소 가고싶었던 식당으로 ~~', '혼자 먹는 밥이 무슨 의미가 있을까요?? 굶도록 합시다.'
         ,'지금 밥먹을 때냐... 다이어트나 하자.....','혼밥이 창피하다면 포장 음식을 추천해드려요!(맘스터치,도스마스,서브웨이,컵밥)'
         ]
    return a[idx]

#선언부
utcnow = datetime.datetime.utcnow()
time_gap = datetime.timedelta(hours=9)
kor_time = utcnow + time_gap

t = ['월', '화', '수', '목', '금', '토', '일']
r = kor_time.weekday()

html = requests.get('https://www.wsu.ac.kr/page/meal_list.jsp#self').text
soup = BeautifulSoup(html, 'html.parser')
a = soup.findAll("td", limit=61)

def WestCampus():
    messages = ''

    if t[r] == '토':
        messages = "학식 기능은 토요일에 제공되지 않습니다."
        return messages

    if t[r] == '월':
        messages += (t[r] + '요일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + a[0].get_text())
        messages += ('\n●미스터 셰프 메뉴●\n' + a[1].get_text())
        messages += ('\n●누들 및 중국 음식 메뉴●\n' + a[2].get_text())
        messages += ('\n●교직원 메뉴●\n' + a[3].get_text())
        return parser.ser(messages)

    elif t[r] == '화':
        messages += (t[r] + '요일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + a[4].get_text())
        messages += ('\n●미스터 셰프 메뉴●\n' + a[5].get_text())
        messages += ('\n●누들 및 중국 음식 메뉴●\n' + a[6].get_text())
        messages += ('\n●교직원 메뉴●\n' + a[7].get_text())
        return parser.ser(messages)

    elif t[r] == '수':
        messages += (t[r] + '요일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + a[8].get_text())
        messages += ('\n●미스터 셰프 메뉴●\n' + a[9].get_text())
        messages += ('\n●누들 및 중국 음식 메뉴●\n' + a[10].get_text())
        messages += ('\n●교직원 메뉴●\n' + a[11].get_text())
        return parser.ser(messages)

    elif t[r] == '목':
        messages += (t[r] + '요일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + a[12].get_text())
        messages += ('\n●미스터 셰프 메뉴●\n' + a[13].get_text())
        messages += ('\n●누들 및 중국 음식 메뉴●\n' + a[14].get_text())
        messages += ('\n●교직원 메뉴●\n' + a[15].get_text())
        return parser.ser(messages)

    elif t[r] == '금':
        messages += (t[r] + '요일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + a[16].get_text())
        messages += ('\n●미스터 셰프 메뉴●\n' + a[17].get_text())
        messages += ('\n●누들 및 중국 음식 메뉴●\n' + a[18].get_text())
        messages += ('\n●교직원 메뉴●\n' + a[19].get_text())
        return parser.ser(messages)

    elif t[r] == '일':
        messages += ('월요일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + a[0].get_text())
        messages += ('\n●미스터 셰프 메뉴●\n' + a[1].get_text())
        messages += ('\n●누들 및 중국 음식 메뉴●\n' + a[2].get_text())
        messages += ('\n●교직원 메뉴●\n' + a[3].get_text())
        return parser.ser(messages)

def EastCampus():
    messages = ''

    if t[r] == '토':
        messages = "학식 기능은 토요일에 제공되지 않습니다."
        return messages

    if t[r] == '월':
        messages += (t[r] + '요일 동캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + a[20].get_text())
        messages += ('\n●미스터 셰프 메뉴●\n' + a[21].get_text())
        messages += ('\n●누들 및 중국 음식 메뉴●\n' + a[22].get_text())
        messages += ('\n●교직원 메뉴●\n' + a[23].get_text())
        return parser.dong(messages)

    elif t[r] == '화':
        messages += (t[r] + '요일 동캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + a[24].get_text())
        messages += ('\n●미스터 셰프 메뉴●\n' + a[25].get_text())
        messages += ('\n●누들 및 중국 음식 메뉴●\n' + a[26].get_text())
        messages += ('\n●교직원 메뉴●\n' + a[27].get_text())
        return parser.dong(messages)

    elif t[r] == '수':
        messages += (t[r] + '요일 동캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + a[28].get_text())
        messages += ('\n●미스터 셰프 메뉴●\n' + a[29].get_text())
        messages += ('\n●누들 및 중국 음식 메뉴●\n' + a[30].get_text())
        messages += ('\n●교직원 메뉴●\n' + a[31].get_text())
        return parser.dong(messages)

    elif t[r] == '목':
        messages += (t[r] + '요일 동캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + a[32].get_text())
        messages += ('\n●미스터 셰프 메뉴●\n' + a[33].get_text())
        messages += ('\n●누들 및 중국 음식 메뉴●\n' + a[34].get_text())
        messages += ('\n●교직원 메뉴●\n' + a[35].get_text())
        return parser.dong(messages)

    elif t[r] == '금':
        messages += (t[r] + '요일 동캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + a[36].get_text())
        messages += ('\n●미스터 셰프 메뉴●\n' + a[37].get_text())
        messages += ('\n●누들 및 중국 음식 메뉴●\n' + a[38].get_text())
        messages += ('\n●교직원 메뉴●\n' + a[39].get_text())
        return parser.dong(messages)

    elif t[r] == '일':
        messages += ('월요일 동캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + a[20].get_text())
        messages += ('\n●미스터 셰프 메뉴●\n' + a[21].get_text())
        messages += ('\n●누들 및 중국 음식 메뉴●\n' + a[22].get_text())
        messages += ('\n●교직원 메뉴●\n' + a[23].get_text())
        return parser.dong(messages)

def Dormitory():
    messages = ''

    if t[r] == '월':
        messages += (t[r] + '요일 기숙사 학식 메뉴\n' + '●조식●\n' + a[40].get_text())
        messages += ('\n●중식●\n' + a[41].get_text())
        messages += ('\n●석식●\n' + a[42].get_text())
        return parser.kik(messages)

    elif t[r] == '화':
        messages += (t[r] + '요일 기숙사 학식 메뉴\n' + '●조식●\n' + a[43].get_text())
        messages += ('\n●중식●\n' + a[44].get_text())
        messages += ('\n●석식●\n' + a[45].get_text())
        return parser.kik(messages)

    elif t[r] == '수':
        messages += (t[r] + '요일 기숙사 학식 메뉴\n' + '●조식●\n' + a[46].get_text())
        messages += ('\n●중식●\n' + a[47].get_text())
        messages += ('\n●석식●\n' + a[48].get_text())
        return parser.kik(messages)

    elif t[r] == '목':
        messages += (t[r] + '요일 기숙사 학식 메뉴\n' + '●조식●\n' + a[49].get_text())
        messages += ('\n●중식●\n' + a[50].get_text())
        messages += ('\n●석식●\n' + a[51].get_text())
        return parser.kik(messages)

    elif t[r] == '금':
        messages += (t[r] + '요일 기숙사 학식 메뉴\n' + '●조식●\n' + a[52].get_text())
        messages += ('\n●중식●\n' + a[53].get_text())
        messages += ('\n●석식●\n' + a[54].get_text())
        return parser.kik(messages)

    elif t[r] == '토':
        messages += (t[r] + '요일 기숙사 학식 메뉴\n' + '●조식●\n' + a[55].get_text())
        messages += ('\n●중식●\n' + a[56].get_text())
        messages += ('\n●석식●\n' + a[57].get_text())
        return parser.kik(messages)

    elif t[r] == '일':
        messages += (t[r] + '요일 기숙사 학식 메뉴\n' + '●조식●\n' + a[58].get_text())
        messages += ('\n●중식●\n' + a[59].get_text())
        messages += ('\n●석식●\n' + a[60].get_text())
        return parser.kik(messages)

def TommorrowWestCampus():
    messages = ''

    if t[r] == '금':
        messages = "주말 학식 메뉴는 제공되지 않습니다."
        return messages
    elif t[r] == '토':
        messages = "주말 학식 메뉴는 제공되지 않습니다."
        return messages

    if t[r] == '일':
        messages += ('내일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + a[0].get_text())
        messages += ('\n●미스터 셰프 메뉴●\n' + a[1].get_text())
        messages += ('\n●누들 및 중국 음식 메뉴●\n' + a[2].get_text())
        messages += ('\n●교직원 메뉴●\n' + a[3].get_text())
        return parser.ser(messages)

    elif t[r] == '월':
        messages += ( '내일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + a[4].get_text())
        messages += ('\n●미스터 셰프 메뉴●\n' + a[5].get_text())
        messages += ('\n●누들 및 중국 음식 메뉴●\n' + a[6].get_text())
        messages += ('\n●교직원 메뉴●\n' + a[7].get_text())
        return parser.ser(messages)

    elif t[r] == '화':
        messages += ('내일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + a[8].get_text())
        messages += ('\n●미스터 셰프 메뉴●\n' + a[9].get_text())
        messages += ('\n●누들 및 중국 음식 메뉴●\n' + a[10].get_text())
        messages += ('\n●교직원 메뉴●\n' + a[11].get_text())
        return parser.ser(messages)

    elif t[r] == '수':
        messages += ('내일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + a[12].get_text())
        messages += ('\n●미스터 셰프 메뉴●\n' + a[13].get_text())
        messages += ('\n●누들 및 중국 음식 메뉴●\n' + a[14].get_text())
        messages += ('\n●교직원 메뉴●\n' + a[15].get_text())
        return parser.ser(messages)

    elif t[r] == '목':
        messages += ('내일 서캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + a[16].get_text())
        messages += ('\n●미스터 셰프 메뉴●\n' + a[17].get_text())
        messages += ('\n●누들 및 중국 음식 메뉴●\n' + a[18].get_text())
        messages += ('\n●교직원 메뉴●\n' + a[19].get_text())
        return parser.ser(messages)

def TommorrowEastCampus():
    messages = ''

    if t[r] == '금':
        messages = "주말 학식 메뉴는 제공되지 않습니다."
        return messages
    elif t[r] == '토':
        messages = "주말 학식 메뉴는 제공되지 않습니다."
        return messages
        

    if t[r] == '일':
        messages += ('내일 동캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + a[20].get_text())
        messages += ('\n●미스터 셰프 메뉴●\n' + a[21].get_text())
        messages += ('\n●누들 및 중국 음식 메뉴●\n' + a[22].get_text())
        messages += ('\n●교직원 메뉴●\n' + a[23].get_text())
        return parser.dong(messages)

    elif t[r] == '월':
        messages += ('내일 동캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + a[24].get_text())
        messages += ('\n●미스터 셰프 메뉴●\n' + a[25].get_text())
        messages += ('\n●누들 및 중국 음식 메뉴●\n' + a[26].get_text())
        messages += ('\n●교직원 메뉴●\n' + a[27].get_text())
        return parser.dong(messages)

    elif t[r] == '화':
        messages += ('내일 동캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + a[28].get_text())
        messages += ('\n●미스터 셰프 메뉴●\n' + a[29].get_text())
        messages += ('\n●누들 및 중국 음식 메뉴●\n' + a[30].get_text())
        messages += ('\n●교직원 메뉴●\n' + a[31].get_text())
        return parser.dong(messages)

    elif t[r] == '수':
        messages += ('내일 동캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + a[32].get_text())
        messages += ('\n●미스터 셰프 메뉴●\n' + a[33].get_text())
        messages += ('\n●누들 및 중국 음식 메뉴●\n' + a[34].get_text())
        messages += ('\n●교직원 메뉴●\n' + a[35].get_text())
        return parser.dong(messages)

    elif t[r] == '목':
        messages += ('내일 동캠퍼스 학식 메뉴\n' + '●Western Food 양식 메뉴●\n' + a[36].get_text())
        messages += ('\n●미스터 셰프 메뉴●\n' + a[37].get_text())
        messages += ('\n●누들 및 중국 음식 메뉴●\n' + a[38].get_text())
        messages += ('\n●교직원 메뉴●\n' + a[39].get_text())
        return parser.dong(messages)

def TommorrowDormitory():
    messages = ''

    if t[r] == '일':
        messages += ('내일  기숙사 학식 메뉴\n' + '●조식●\n' + a[40].get_text())
        messages += ('\n●중식●\n' + a[41].get_text())
        messages += ('\n●석식●\n' + a[42].get_text())
        return parser.kik(messages)

    elif t[r] == '월':
        messages += ('내일 기숙사 학식 메뉴\n' + '●조식●\n' + a[43].get_text())
        messages += ('\n●중식●\n' + a[44].get_text())
        messages += ('\n●석식●\n' + a[45].get_text())
        return parser.kik(messages)

    elif t[r] == '화':
        messages += ('내일 기숙사 학식 메뉴\n' + '●조식●\n' + a[46].get_text())
        messages += ('\n●중식●\n' + a[47].get_text())
        messages += ('\n●석식●\n' + a[48].get_text())
        return parser.kik(messages)

    elif t[r] == '수':
        messages += ('내일  기숙사 학식 메뉴\n' + '●조식●\n' + a[49].get_text())
        messages += ('\n●중식●\n' + a[50].get_text())
        messages += ('\n●석식●\n' + a[51].get_text())
        return parser.kik(messages)

    elif t[r] == '목':
        messages += ('내일 기숙사 학식 메뉴\n' + '●조식●\n' + a[52].get_text())
        messages += ('\n●중식●\n' + a[53].get_text())
        messages += ('\n●석식●\n' + a[54].get_text())
        return parser.kik(messages)
    
    elif t[r] == '금':
        messages += (t[r] + '요일 기숙사 학식 메뉴\n' + '●조식●\n' + a[55].get_text())
        messages += ('\n●중식●\n' + a[56].get_text())
        messages += ('\n●석식●\n' + a[57].get_text())
        return parser.kik(messages)

    elif t[r] == '토':
        messages += (t[r] + '요일 기숙사 학식 메뉴\n' + '●조식●\n' + a[58].get_text())
        messages += ('\n●중식●\n' + a[59].get_text())
        messages += ('\n●석식●\n' + a[60].get_text())
        return parser.kik(messages)

def naver_rank():
    html = requests.get('http://naver.com').text
    soup = BeautifulSoup(html, 'html.parser')
    message = []
    tag_list = soup.select('.PM_CL_realtimeKeyword_rolling .ah_item .ah_k')

    for idx, tag in enumerate(tag_list, 1):
        message.append(str(idx) + '.' + tag.text)
    return message


def melon_search(query):
    params = {
        'jscallback': '_',
        'query': query,
    }
    jsonp_string = requests.get('http://www.melon.com/search/keyword/index.json', params=params).text
    json_string = jsonp_string.replace('_(','').replace(');','')
    meta = json.loads(json_string)

    messages = []
    if 'SONGCONTENTS' in meta:
        for song in meta['SONGCONTENTS']:
            messages.append('''[{ALBUMNAME}] {SONGNAME} by {ARTISTNAME} - http://www.melon.com/song/detail.htm?songId={SONGID}'''.format(**song))

            if messages:
                message = '\n'.join(messages)
            else:
                message = '검색어 "{}"에 대한 노래 검색결과가 없습니다.'.format(query)

            return message
