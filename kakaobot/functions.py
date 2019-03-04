import json
import requests
import datetime
import random
import time
from bs4 import BeautifulSoup
from . import parser
from selenium import webdriver

# 선언부
t = ['월', '화', '수', '목', '금', '토', '일']
driver = webdriver.PhantomJS()
driver2 = webdriver.PhantomJS()

# 요일 구하기.
def today():
    utcnow = datetime.datetime.utcnow()
    time_gap = datetime.timedelta(hours=9)
    kor_time = utcnow + time_gap
    r = kor_time.weekday()

    return r

# 다음 버스 파서
def bus_parser(string):
    parser = string.replace('			', '')
    parser = parser.replace('	', '')
    parser = parser.replace('	', '')
    parser = parser.replace(' 	', '')
    parser = parser.replace(' 	', '')
    parser = parser.replace('\n', ' ')
    return parser

#공릉동 미세먼지 체크
def check_dust():
    driver2.get('https://m.search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EA%B3%B5%EB%A6%89%EB%8F%99+%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80')
    html = driver2.page_source
    soup = BeautifulSoup(html, 'html.parser')
    dust = soup.select('.air_today span')
    value = int(dust[3].getText())
    message = "미세먼지 수치 : "+ dust[0].getText()
    if value < 31:
        message += ("\n공릉동 미세먼지는 좋음 입니다.")
    elif value < 81:
        message += ("\n공릉동 미세먼지는 보통 입니다")
    elif value < 151:
        message += ("\n공릉동 미세먼지는 나쁨 입니다")
    else:
        message +=("\n공릉동 미세먼지는 매우나쁨 입니다")
    return message


# 버스정류장
def bus_Gongneung():
    driver.get('https://m.map.naver.com/bus/station.nhn?stationID=124079')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    bus = soup.select('.end_list_info span')

    messages = ''
    messages = '◎공릉역 2번출구◎\n' + '☞노원 03번 버스☜\n' + bus[1].get_text() + \
               '\n☞노원 13번 버스☜\n' + bus[5].get_text()
    return messages

# 붕어방
def bus_bnag():
    driver.get('https://m.map.naver.com/bus/station.nhn?stationID=81706&busID=566')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    bus = soup.select('.end_list_info span')

    messages = ''
    messages = '◎과기대 붕어방◎\n' + '☞노원 13번 버스☜\n' + bus[1].get_text()
    return messages

def seok_1():
    driver.get('https://m.map.daum.net/actions/busStationInfo?busStopId=BS30329')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    bus = soup.select('.list_content_wrap span.info_situation')

    messages = '◎석계역 1번출구◎\n' + '☞지선 1136번 버스☜\n' +(bus_parser(bus[5].getText())) + \
                   '\n☞지선 1141번 버스☜\n' + (bus_parser(bus[6].getText())) + '\n☞노원 03번 버스☜\n' + (bus_parser(bus[17].getText())) + \
                   '\n☞노원 04번 버스☜\n' + (bus_parser(bus[18].getText())) + '\n☞노원 13번 버스☜\n' + (bus_parser(bus[19].getText()))        
    return messages  

def seok_2():
    driver.get('https://m.map.daum.net/actions/busStationInfo?busStopId=BS30743')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    bus = soup.select('.list_content_wrap span.info_situation')

    messages = '◎석계역 4번출구◎\n' + '☞지선 1136번 버스☜\n' +(bus_parser(bus[5].getText())) + \
                   '\n☞지선 1141번 버스☜\n' + (bus_parser(bus[7].getText())) + '\n☞노원 03번 버스☜\n' + (bus_parser(bus[22].getText())) + \
                   '\n☞노원 04번 버스☜\n' + (bus_parser(bus[23].getText())) + '\n☞노원 13번 버스☜\n' + (bus_parser(bus[24].getText()))
    return messages

#과기대 정문
def front_door():
    html = requests.get('https://m.map.daum.net/actions/busStationInfo?busStopId=11110561014').text
    soup = BeautifulSoup(html, 'html.parser')
    bus = soup.select('.list_content_wrap span.info_situation')

    messages = '◎과기대 정문◎\n' + '☞지선 1141번 버스☜\n' +(bus_parser(bus[0].getText())) + \
               '\n☞지선 1224번 버스☜\n' + (bus_parser(bus[1].getText())) + '\n☞지선 1227번 버스☜\n' + (bus_parser(bus[2].getText())) + \
               '\n☞노원 03번 버스☜\n' + (bus_parser(bus[3].getText()))
    return (messages)

#과기대 정문 GS 방면
def front_door_gs():
    html = requests.get('https://m.map.daum.net/actions/busStationInfo?busStopId=11110561007').text
    soup = BeautifulSoup(html, 'html.parser')
    bus = soup.select('.list_content_wrap span.info_situation')

    messages = '◎과기대 정문 GS편의점◎\n' + '☞지선 1141번 버스☜\n' + (bus_parser(bus[0].getText())) + \
               '\n☞지선 1224번 버스☜\n' + (bus_parser(bus[1].getText())) + '\n☞지선 1227번 버스☜\n' + (
               bus_parser(bus[2].getText())) + \
               '\n☞노원 03번 버스☜\n' + (bus_parser(bus[3].getText()))
    return (messages)

#과기대 정문 13번
def front_door_13():
    html = requests.get("https://m.map.daum.net/actions/busStationInfo?busStopId=BS155717").text
    soup = BeautifulSoup(html, 'html.parser')
    bus = soup.select('.list_content_wrap span.info_situation')
    
    messages = '◎과기대 정문 13번◎\n' + (bus_parser(bus[0].getText())) 
    return (messages)

# 열람실
#def Library_seat():
#    if (driver2.current_url == 'http://portal.seoultech.ac.kr/portal/default/SEOULTECH/LOGIN'):
#        driver2.find_element_by_id('userId').send_keys("id")
#        driver2.find_element_by_id('password').send_keys("pw")
#        driver2.find_element_by_id('lok').click()
#        time.sleep(1)
#    try:
#        driver2.get('http://portal.seoultech.ac.kr/portal')
#        html = driver2.page_source
#        soup = BeautifulSoup(html, 'html.parser')
#        seat = soup.select('.gauge span')
#        messages = "◎도서관 열람실 사용 현황◎\n" \
#                   "◎ 1층 일반열람실1 ◎\n잔여 좌석 " + seat[0].text + \
#                   "\n◎ 1층 노트북열람실1 ◎\n잔여 좌석 " + seat[1].text + \
#                   "\n◎ 2층 일반열람실2 ◎\n잔여 좌석 " + seat[2].text + \
#                   "\n◎ 2층 노트북열람실 ◎\n잔여 좌석 " + seat[3].text + \
#                   "\n◎ 2층 일반열람실3 ◎\n잔여 좌석 " + seat[4].text + \
#                   "\n◎ 2층 별관스터디실 ◎\n잔여 좌석 " + seat[5].text
#        return (messages)
#    except:
#        return ('서버 성능 에러입니다. 다른 기능을 누른 후 버튼을 다시 눌러주세요.')

kb_idx = 0
sung_idx = 0
surim_idx = 0
food_two_idx = 0

kb_list = []
surim_list = []
sung_list = []
food_two_list = []

# kb 학사
def Kb_Dormitory():
    global  kb_idx
    global kb_list
    r = today()
    messages = ''

    if (kb_idx == 0):
        kb_list = []
        driver.get('http://domi.seoultech.ac.kr/support/food/?foodtype=kb')
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        kb = soup.findAll("td", limit=8)
        for i in kb:
            kb_list.append(i.get_text())
        kb_idx = 1

    if t[r] == '월':
        messages += (t[r] + '요일 KB 학사 학식 메뉴' + kb_list[1])
        return parser.dom_parser(messages)

    elif t[r] == '화':
        messages += (t[r] + '요일 KB 학사 학식 메뉴' + kb_list[2])
        return parser.dom_parser(messages)

    elif t[r] == '수':
        messages += (t[r] + '요일 KB 학사 학식 메뉴' + kb_list[3])
        return parser.dom_parser(messages)

    elif t[r] == '목':
        messages += (t[r] + '요일 KB 학사 학식 메뉴' + kb_list[4])
        return parser.dom_parser(messages)

    elif t[r] == '금':
        messages += (t[r] + '요일 KB 학사 학식 메뉴' + kb_list[5])
        return parser.dom_parser(messages)

    elif t[r] == '토':
        messages += (t[r] + '요일 KB 학사 학식 메뉴' + kb_list[6])
        messages += ('\n일요일 KB 학사 학식 메뉴' + kb_list[7])
        return parser.dom_parser(messages)

    elif t[r] == '일':
        messages += ('\n일요일 KB 학사 학식 메뉴' + kb_list[7])
        messages += '식단표가 다음주 식단표로 업데이트 되었습니다. 저번주 식단표를 확인해 주세요.'
        kb_idx == 0
        return parser.dom_parser(messages)


# 성림 학사
def Sungrim_Dormitory():
    global sung_idx
    global sung_list
    r = today()
    messages = ''

    if(sung_idx==0):
        sung_list = []
        driver.get('http://domi.seoultech.ac.kr/support/food/?foodtype=sung')
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        sung = soup.findAll("td", limit=8)
        for i in sung:
            sung_list.append(i.get_text())
        sung_idx = 1

    if t[r] == '월':
        messages += (t[r] + '요일 성림 학사 학식 메뉴' + sung_list[1])
        return parser.dom_parser(messages)

    elif t[r] == '화':
        messages += (t[r] + '요일 성림 학사 학식 메뉴' + sung_list[2])
        return parser.dom_parser(messages)

    elif t[r] == '수':
        messages += (t[r] + '요일 성림 학사 학식 메뉴' + sung_list[3])
        return parser.dom_parser(messages)

    elif t[r] == '목':
        messages += (t[r] + '요일 성림 학사 학식 메뉴' + sung_list[4])
        return parser.dom_parser(messages)

    elif t[r] == '금':
        messages += (t[r] + '요일 성림 학사 학식 메뉴' + sung_list[5])
        return parser.dom_parser(messages)

    elif t[r] == '토':
        messages += (t[r] + '요일 성림 학사 학식 메뉴' + sung_list[6])
        messages += ('\n일요일 성림 학사 학식 메뉴' + sung_list[7])
        return parser.dom_parser(messages)

    elif t[r] == '일':
        messages += ('\n일요일 성림 학사 학식 메뉴' + sung_list[7])
        messages += '식단표가 다음주 식단표로 업데이트 되었습니다. 저번주 식단표를 확인해 주세요.'
        sung_idx = 0
        return parser.dom_parser(messages)


# 수림 학사
def Surim_Dormitory():
    global surim_idx
    global surim_list
    r = today()
    messages = ''
    if(surim_idx == 0):
        surim_list = []
        driver.get('http://domi.seoultech.ac.kr/support/food/?foodtype=surim')
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        surim = soup.findAll("td", limit=8)
        for i in surim:
            surim_list.append(i.get_text())
        surim_idx = 1

    if t[r] == '월':
        messages += (t[r] + '요일 수림 학사 학식 메뉴' + surim_list[1])
        return parser.dom_parser(messages)

    elif t[r] == '화':
        messages += (t[r] + '요일 수림 학사 학식 메뉴' + surim_list[2])
        return parser.dom_parser(messages)

    elif t[r] == '수':
        messages += (t[r] + '요일 수림 학사 학식 메뉴' + surim_list[3])
        return parser.dom_parser(messages)

    elif t[r] == '목':
        messages += (t[r] + '요일 수림 학사 학식 메뉴' + surim_list[4])
        return parser.dom_parser(messages)

    elif t[r] == '금':
        messages += (t[r] + '요일 수림 학사 학식 메뉴' + surim_list[5])
        return parser.dom_parser(messages)

    elif t[r] == '토':
        messages += (t[r] + '요일 수림 학사 학식 메뉴' + surim_list[6])
        messages += ('\n일요일 수림 학사 학식 메뉴' + surim_list[7])
        return parser.dom_parser(messages)

    elif t[r] == '일':
        messages += ('\n일요일 수림 학사 학식 메뉴' + surim_list[7])
        messages += '식단표가 다음주 식단표로 업데이트 되었습니다. 저번주 식단표를 확인해 주세요.'
        surim_idx = 0
        return parser.dom_parser(messages)
#테크노 파크 파서
def park_parser(string):
    parser = string.replace('        ', '')
    parser = parser.replace('\n', '')
    return parser

#2학 방학.
def vacation_two():
    html = requests.get('https://bds.bablabs.com/restaurants/LTI0NTI4MDMx?campus_id=o8RPQZ7Zme').text
    soup = BeautifulSoup(html, 'html.parser')
    food_two = soup.select('.card-body span')
    
    r = today()
    messages = ''
    try:
        if t[r] == '월':
            messages += ('◎' + t[r] + '요일 제2학생 식당 메뉴\n'+ '◎점심◎\n' + park_parser(food_two[5].get_text()) + '\n'
                         + park_parser(food_two[7].get_text()) + '\n◎저녁◎\n' + park_parser(food_two[10].get_text()) 
             + '\n' + park_parser(food_two[12].get_text()))
            return (messages)

        elif t[r] == '화':
            messages += ('◎' + t[r] + '요일 제2학생 식당 메뉴\n' + '◎점심◎\n' + park_parser(food_two[5].get_text()) + '\n'
                         + park_parser(food_two[7].get_text()) + '\n◎저녁◎\n' + park_parser(food_two[10].get_text()) 
             + '\n' + park_parser(food_two[12].get_text()))
            return (messages)

        elif t[r] == '수':
            messages += ('◎' + t[r] + '요일 제2학생 식당 메뉴\n' + '◎점심◎\n' + park_parser(food_two[5].get_text()) + '\n'
                         + park_parser(food_two[7].get_text()) + '\n◎저녁◎\n' + park_parser(food_two[10].get_text()) 
             + '\n' + park_parser(food_two[12].get_text()))
            return (messages)

        elif t[r] == '목':
            messages += ('◎' + t[r] + '요일 제2학생 식당 메뉴\n' + '◎점심◎\n' + park_parser(food_two[5].get_text()) + '\n'
                         + park_parser(food_two[7].get_text()) + '\n◎저녁◎\n' + park_parser(food_two[10].get_text()) 
             + '\n' + park_parser(food_two[12].get_text()))
            return (messages)

        elif t[r] == '금':
            messages += ('◎' + t[r] + '요일 제2학생 식당 메뉴\n' + '◎점심◎\n' + park_parser(food_two[5].get_text()) + '\n'
                         + park_parser(food_two[7].get_text()) + '\n◎저녁◎\n' + park_parser(food_two[10].get_text()) 
             + '\n' + park_parser(food_two[12].get_text()))
            return (messages)

        elif t[r] == '토':
            messages += ('토요일 제공하지 않습니다.\n')
            return messages

        elif t[r] == '일':
            messages += ('일요일은 제공하지 않습니다.\n')
            return messages
    except:
        return ('홈페이지의 학식 메뉴가 업로드 되지 않았습니다.')

#테크노 파크 식단
def TechPark():
    html = requests.get('https://bds.bablabs.com/restaurants/LTI0NTI2NjU2?campus_id=o8RPQZ7Zme').text
    soup = BeautifulSoup(html, 'html.parser')
    park = soup.select('.card-body span')

    r = today()
    messages = ''
    try:
        if t[r] == '월':
            messages += ('◎' + t[r] + '요일 테크노파크 식당 메뉴◎\n' + '◎중식 A코너◎\n' + park_parser(park[3].get_text()) + '\n◎중식 B코너◎\n'
                         + park_parser(park[4].get_text()) + '\n◎저녁◎\n' + park_parser(park[7].get_text()))
            return (messages)

        elif t[r] == '화':
            messages += ('◎' + t[r] + '요일 테크노파크 식당 메뉴◎\n' + '◎중식 A코너◎\n' + park_parser(park[3].get_text()) + '\n◎중식 B코너◎\n'
                         + park_parser(park[4].get_text()) + '\n◎저녁◎\n' + park_parser(park[7].get_text()))
            return (messages)

        elif t[r] == '수':
            messages += ('◎' + t[r] + '요일 테크노파크 식당 메뉴◎\n' + '◎중식 A코너◎\n' + park_parser(park[3].get_text()) + '\n◎중식 B코너◎\n'
                         + park_parser(park[4].get_text()) + '\n◎저녁◎\n' + park_parser(park[7].get_text()))
            return (messages)

        elif t[r] == '목':
            messages += ('◎' + t[r] + '요일 테크노파크 식당 메뉴◎\n' + '◎중식 A코너◎\n' + park_parser(park[3].get_text()) + '\n◎중식 B코너◎\n'
                         + park_parser(park[4].get_text()) + '\n◎저녁◎\n' + park_parser(park[7].get_text()))
            return (messages)

        elif t[r] == '금':
            messages += ('◎' + t[r] + '요일 테크노파크 식당 메뉴◎\n' + '◎중식 A코너◎\n' + park_parser(park[3].get_text()) + '\n◎중식 B코너◎\n'
                         + park_parser(park[4].get_text()) + '\n◎저녁◎\n' + park_parser(park[7].get_text()))
            return (messages)

        elif t[r] == '토':
            messages += ('토요일 제공하지 않습니다.\n')
            return messages

        elif t[r] == '일':
            messages += ('일요일은 제공하지 않습니다.\n')
            return messages
    except:
        return ('홈페이지의 학식 메뉴가 업로드 되지 않았습니다.')

# 제 2학생 식단
def Food_two():
    global food_two_idx
    global food_two_list
    r = today()
        
    if(food_two_idx == 0):
        food_two_list = []
        driver.get('http://www.seoultech.ac.kr/life/student/food/')
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        food_two = soup.select(".dts_design td", limit=132)
        for idx,i in enumerate(food_two):
            food_two_list.append(i.get_text())
        food_two_idx = 1

    messages = ''
    try:
        if t[r] == '월':
            messages += (t[r] + '요일 제2학생 식당 메뉴\n' + '◎중식 든든 ' + food_two_list[8] + '◎\n'
                         + food_two_list[13] + ' ' + food_two_list[18] + ' ' + food_two_list[23] + ' ' +
                         food_two_list[28]+ ' ' +
                         food_two_list[33] + '\n')
            messages += ('◎중식 푸짐 4200원◎\n' + food_two_list[39] + ' ' + food_two_list[44] + ' ' + food_two_list[
                49] + ' ' + food_two_list[54] + ' ' +
                         food_two_list[59] + ' ' + food_two_list[64] + ' ' + food_two_list[69] + '\n')
            messages += ('◎석식 푸짐 3500◎\n' + food_two_list[102] + ' ' + food_two_list[107] + ' ' + food_two_list[
                112] + ' ' +
                         food_two_list[117] + ' ' + food_two_list[122] + ' ' + food_two_list[127] +'\n')
            messages += '◎간단 메뉴 + 공깃밥◎\n계란라면 2800원\n떡계란라면 치즈계란라면\n물만두계란라면 3200원\n'
            messages += '◎운영시간 - 중식 11:00~14:00 석식 17:00~19:00 (18:40분까지 주문가능)◎'

            return parser.food_parser(messages)

        elif t[r] == '화':
            messages += (t[r] + '요일 제2학생 식당 메뉴\n' + '◎든든 ' + food_two_list[9] + '◎\n'
                         + food_two_list[14] + ' ' + food_two_list[19] + ' ' + food_two_list[24] + ' ' +
                         food_two_list[29] + ' ' +
                         food_two_list[34] + '\n')
            messages += ('◎푸짐 4200원◎\n' + food_two_list[40] + ' ' + food_two_list[45] + ' ' + food_two_list[50] + ' ' +
                         food_two_list[55] + ' ' + food_two_list[60] + ' ' + food_two_list[65] + ' ' + food_two_list[70] +'\n')
            messages += ('◎석식 푸짐 3500◎\n' + food_two_list[103] + ' ' + food_two_list[108] + ' ' + food_two_list[
                         113] + ' ' + food_two_list[118] + ' ' +
                         food_two_list[123] + ' ' + food_two_list[128] + '\n')
            messages += '◎간단 메뉴 + 공깃밥◎\n계란라면 2800원\n떡계란라면 치즈계란라면\n물만두계란라면 3200원\n'
            messages += '◎운영시간 - 중식 11:00~14:00 석식 17:00~19:00 (18:40분까지 주문가능)◎'
            return parser.food_parser(messages)

        elif t[r] == '수':
            messages += (t[r] + '요일 제2학생 식당 메뉴\n' + '◎든든 ' + food_two_list[10] + '◎\n'
                         + food_two_list[15] + ' ' + food_two_list[20] + ' ' + food_two_list[25] + ' ' +
                         food_two_list[30] + ' ' +
                         food_two_list[35] + '\n')
            messages += (
            '◎푸짐 4200원◎\n' + food_two_list[41] + ' ' + food_two_list[46] + ' ' + food_two_list[51] + ' ' +
            food_two_list[56] + ' ' +
            food_two_list[61] + ' ' + food_two_list[66] + ' ' + food_two_list[71] +'\n')
            messages += ('◎석식 푸짐 3500◎\n' + food_two_list[104] + ' ' + food_two_list[109] + ' ' + food_two_list[
                114] + ' ' + food_two_list[119] + ' ' +
                         food_two_list[124] + ' ' + food_two_list[129] + '\n')
            messages += '◎간단 메뉴 + 공깃밥◎\n계란라면 2800원\n떡계란라면 치즈계란라면\n물만두계란라면 3200원\n'
            messages += '◎운영시간 - 중식 11:00~14:00 석식 17:00~19:00 (18:40분까지 주문가능)◎'

            return parser.food_parser(messages)

        elif t[r] == '목':
            messages += (t[r] + '요일 제2학생 식당 메뉴◎\n' + '◎든든 ' + food_two_list[11] + '◎\n'
                         + food_two_list[16] + ' ' + food_two_list[21] + ' ' + food_two_list[26] + ' ' +
                         food_two_list[31] + ' ' +
                         food_two_list[36] + '\n')
            messages += (
            '◎푸짐 4200원◎\n' + food_two_list[42] + ' ' + food_two_list[47] + ' ' + food_two_list[52] + ' ' +
            food_two_list[57] + ' ' +
            food_two_list[62] + ' ' + food_two_list[67] + ' ' + food_two_list[72] +'\n')
            messages += ('◎석식 푸짐 3500◎\n' + food_two_list[105] + ' ' + food_two_list[110] + ' ' + food_two_list[
                115] + ' ' + food_two_list[120] + ' ' +
                         food_two_list[125] + ' ' + food_two_list[130] + '\n')
            messages += '◎간단 메뉴 + 공깃밥◎\n계란라면 2800원\n떡계란라면 치즈계란라면\n물만두계란라면 3200원\n'
            messages += '◎운영시간 - 중식 11:00~14:00 석식 17:00~19:00 (18:40분까지 주문가능)◎'

            return parser.food_parser(messages)

        elif t[r] == '금':
            messages += (t[r] + '요일 제2학생 식당 메뉴\n' + '◎든든 ' + food_two_list[12] + '◎\n'
                         + food_two_list[17] + ' ' + food_two_list[22] + ' ' + food_two_list[27] + ' ' +
                         food_two_list[32] + ' ' +
                         food_two_list[37] + '\n')
            messages += (
            '◎푸짐 4200원◎\n' + food_two_list[43] + ' ' + food_two_list[48] + ' ' + food_two_list[53] + ' ' +
            food_two_list[58] + ' ' +
            food_two_list[63] + ' ' + food_two_list[68] + ' ' + food_two_list[73] +'\n')
            messages += ('◎석식 푸짐 3500◎\n' + food_two_list[106] + ' ' + food_two_list[111] + ' ' + food_two_list[
                116] + ' ' + food_two_list[121] + ' ' +
                         food_two_list[126] + ' ' + food_two_list[131] + '\n')
            messages += '◎간단 메뉴 + 공깃밥◎\n계란라면 2800원\n떡계란라면 치즈계란라면\n물만두계란라면 3200원\n'
            messages += '◎운영시간 - 중식 11:00~14:00 석식 17:00~19:00 (18:40분까지 주문가능)◎'

            return parser.food_parser(messages)
        
        elif t[r] == '토':
            messages += ('토요일은 제공하지 않습니다.\n')
            return messages

        elif t[r] == '일':
            messages += ('일요일은 제공하지 않습니다.\n')
            food_two_idx = 0
            return messages
    except:
        return ('식당 메뉴가 업로드 되지 않았습니다.')    


def Food_two_tomorrow():
    global food_two_idx
    global food_two_list
    if(food_two_idx == 0):
        food_two_list = []
        driver.get('http://www.seoultech.ac.kr/life/student/food/')
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        food_two = soup.select(".dts_design td", limit=132)
        for i in food_two:
            food_two_list.append(i.get_text())

    messages = ''
    try:
        messages += ('월요일 제2학생 식당 메뉴\n' + '◎중식 든든 ' +  food_two_list[8] + '◎\n'
                         + food_two_list[13] + ' ' + food_two_list[18] + ' ' + food_two_list[23] + ' ' +
                         food_two_list[28]+ ' ' +
                         food_two_list[33] + '\n')
        messages += ('◎중식 푸짐 4200원◎\n' + food_two_list[39] + ' ' + food_two_list[44] + ' ' + food_two_list[
            49] + ' ' + food_two_list[54] + ' ' +
                     food_two_list[59] + ' ' + food_two_list[64] + ' ' + food_two_list[69] + '\n')
        messages += ('◎석식 푸짐 3500◎\n' + food_two_list[102] + ' ' + food_two_list[107] + ' ' + food_two_list[
            112] + ' ' +
                     food_two_list[117] + ' ' + food_two_list[122] + ' ' + food_two_list[127] +'\n')

        messages += ('\n화요일 제2학생 식당 메뉴\n' + '◎든든 ' + food_two_list[9] + '◎\n'
                         + food_two_list[14] + ' ' + food_two_list[19] + ' ' + food_two_list[24] + ' ' +
                         food_two_list[29] + ' ' +
                         food_two_list[34] + '\n')
        messages += ('◎푸짐 4200원◎\n' + food_two_list[40] + ' ' + food_two_list[45] + ' ' + food_two_list[50] + ' ' +
                     food_two_list[55] + ' ' + food_two_list[60] + ' ' + food_two_list[65] + ' ' + food_two_list[70] +'\n')
        messages += ('◎석식 푸짐 3500◎\n' + food_two_list[103] + ' ' + food_two_list[108] + ' ' + food_two_list[
                     113] + ' ' + food_two_list[118] + ' ' +
                     food_two_list[123] + ' ' + food_two_list[128] + '\n')
        messages += ('\n수요일 제2학생 식당 메뉴\n' + '◎든든 ' + food_two_list[10] + '◎\n'
                         + food_two_list[15] + ' ' + food_two_list[20] + ' ' + food_two_list[25] + ' ' +
                         food_two_list[30] + ' ' +
                         food_two_list[35] + '\n')
        messages += (
        '◎푸짐 4200원◎\n' + food_two_list[41] + ' ' + food_two_list[46] + ' ' + food_two_list[51] + ' ' +
        food_two_list[56] + ' ' +
        food_two_list[61] + ' ' + food_two_list[66] + ' ' + food_two_list[71] +'\n')
        messages += ('◎석식 푸짐 3500◎\n' + food_two_list[104] + ' ' + food_two_list[109] + ' ' + food_two_list[
            114] + ' ' + food_two_list[119] + ' ' +
                     food_two_list[124] + ' ' + food_two_list[129] + '\n')

        messages += ('\n목요일 제2학생 식당 메뉴◎\n' + '◎든든 ' + food_two_list[11] + '◎\n'
                         + food_two_list[16] + ' ' + food_two_list[21] + ' ' + food_two_list[26] + ' ' +
                         food_two_list[31] + ' ' +
                         food_two_list[36] + '\n')
        messages += (
        '◎푸짐 4200원◎\n' + food_two_list[42] + ' ' + food_two_list[47] + ' ' + food_two_list[52] + ' ' +
        food_two_list[57] + ' ' +
        food_two_list[62] + ' ' + food_two_list[67] + ' ' + food_two_list[72] +'\n')
        messages += ('◎석식 푸짐 3500◎\n' + food_two_list[105] + ' ' + food_two_list[110] + ' ' + food_two_list[
            115] + ' ' + food_two_list[120] + ' ' +
                     food_two_list[125] + ' ' + food_two_list[130] + '\n')

        messages += ('\n금요일 제2학생 식당 메뉴\n' + '◎든든 ' + food_two_list[12] + '◎\n'
                         + food_two_list[17] + ' ' + food_two_list[22] + ' ' + food_two_list[27] + ' ' +
                         food_two_list[32] + ' ' +
                         food_two_list[37] + '\n')
        messages += (
        '◎푸짐 4200원◎\n' + food_two_list[43] + ' ' + food_two_list[48] + ' ' + food_two_list[53] + ' ' +
        food_two_list[58] + ' ' +
        food_two_list[63] + ' ' + food_two_list[68] + ' ' + food_two_list[73] +'\n')
        messages += ('◎석식 푸짐 3500◎\n' + food_two_list[106] + ' ' + food_two_list[111] + ' ' + food_two_list[
            116] + ' ' + food_two_list[121] + ' ' +
                     food_two_list[126] + ' ' + food_two_list[131] + '\n')
        messages
        messages += '◎간단 메뉴 + 공깃밥◎\n계란라면 2800원\n떡계란라면 치즈계란라면\n물만두계란라면 3200원\n'
        messages += '◎운영시간 - 중식 11:00~14:00 석식 17:00~19:00 (18:40분까지 주문가능)◎'

        return parser.food_parser(messages)
    except:
        return ('식당 메뉴가 업로드 되지 않았습니다.')    

# kb 학사 전체
def KB_All():
    global kb_idx
    global kb_list
    if (kb_idx == 0):
        kb_list = []
        driver.get('http://domi.seoultech.ac.kr/support/food/?foodtype=kb')
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        kb = soup.findAll("td", limit=8)
        for i in kb:
            kb_list.append(i.get_text())
        
        
    messages = ''
    messages += ('◎월요일 학식 메뉴◎' + kb_list[1])
    messages += ('◎화요일 학식 메뉴◎' + kb_list[2])
    messages += ('◎수요일 학식 메뉴◎' + kb_list[3])
    messages += ('◎목요일 학식 메뉴◎' + kb_list[4])
    messages += ('◎금요일 학식 메뉴◎' + kb_list[5])
    messages += ('◎토요일 학식 메뉴◎' + kb_list[6])
    messages += ('◎일요일 학식 메뉴◎' + kb_list[7])
    return parser.dom_parser(messages)


# 성림 학사 전체
def Sungrim_All():
    global sung_list
    global sung_idx
    if(sung_idx==0):
        sung_list = []
        driver.get('http://domi.seoultech.ac.kr/support/food/?foodtype=sung')
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        sung = soup.findAll("td", limit=8)
        for i in sung:
            sung_list.append(i.get_text())
        
    messages = ''
    messages += ('◎월요일 학식 메뉴◎' + sung_list[1])
    messages += ('◎화요일 학식 메뉴◎' + sung_list[2])
    messages += ('◎수요일 학식 메뉴◎' + sung_list[3])
    messages += ('◎목요일 학식 메뉴◎' + sung_list[4])
    messages += ('◎금요일 학식 메뉴◎' + sung_list[5])
    messages += ('◎토요일 학식 메뉴◎' + sung_list[6])
    messages += ('◎일요일 학식 메뉴◎' + sung_list[7])
    return parser.dom_parser(messages)


# 수림 학사 전체
def Surim_All():
    global surim_list
    global surim_idx
    if(surim_idx == 0):
        driver.get('http://domi.seoultech.ac.kr/support/food/?foodtype=surim')
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        surim = soup.findAll("td", limit=8)
        for i in surim:
            surim_list.append(i.get_text())
        
    messages = ''

    messages += ('◎월요일 학식 메뉴◎' + surim_list[1])
    messages += ('◎화요일 학식 메뉴◎' + surim_list[2])
    messages += ('◎수요일 학식 메뉴◎' + surim_list[3])
    messages += ('◎목요일 학식 메뉴◎' + surim_list[4])
    messages += ('◎금요일 학식 메뉴◎' + surim_list[5])
    messages += ('◎토요일 학식 메뉴◎' + surim_list[6])
    messages += ('◎일요일 학식 메뉴◎' + surim_list[7])
    return parser.dom_parser(messages)

