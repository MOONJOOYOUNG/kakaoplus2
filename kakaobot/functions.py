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
#        driver2.find_element_by_id('userId').send_keys("18510068")
#        driver2.find_element_by_id('password').send_keys("answndud12#")
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

kb = ''
surim = ''
sung = ''
food_two = ''

kb_idx = 0
sung_idx = 0
surim_idx = 0
food_two_idx = 0

# kb 학사
def Kb_Dormitory():
    global  kb_idx, kb
    r = today()
    messages = ''

    if (kb_idx == 0):
        driver.get('http://domi.seoultech.ac.kr/support/food/?foodtype=kb')
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        kb = soup.findAll("td", limit=8)
        kb_idx = 1

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
        messages += ('\n일요일 KB 학사 학식 메뉴' + kb[7].get_text())
        return parser.dom_parser(messages)

    elif t[r] == '일':
        messages += '식단표가 다음주 식단표로 업데이트 되었습니다. 저번주 식단표를 확인해 주세요.'
        kb_idx == 0
        return parser.dom_parser(messages)


# 성림 학사
def Sungrim_Dormitory():
    global sung_idx,sung
    r = today()
    messages = ''

    if(sung_idx==0):
        driver.get('http://domi.seoultech.ac.kr/support/food/?foodtype=sung')
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        sung = soup.findAll("td", limit=8)
        sung_idx = 1

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
        messages += ('\n일요일 성림 학사 학식 메뉴' + sung[7].get_text())
        return parser.dom_parser(messages)

    elif t[r] == '일':
        messages += '식단표가 다음주 식단표로 업데이트 되었습니다. 저번주 식단표를 확인해 주세요.'
        sung_idx = 0
        return parser.dom_parser(messages)


# 수림 학사
def Surim_Dormitory():
    global surim_idx,surim
    r = today()
    messages = ''
    if(surim_idx == 0):
        driver.get('http://domi.seoultech.ac.kr/support/food/?foodtype=surim')
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        surim = soup.findAll("td", limit=8)
        surim_idx = 1

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
        return parser.dom_parser(messages)

    elif t[r] == '금':
        messages += (t[r] + '요일 수림 학사 학식 메뉴' + surim[5].get_text())
        return parser.dom_parser(messages)

    elif t[r] == '토':
        messages += (t[r] + '요일 수림 학사 학식 메뉴' + surim[6].get_text())
        messages += ('\n일요일 수림 학사 학식 메뉴' + surim[7].get_text())
        return parser.dom_parser(messages)

    elif t[r] == '일':
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
    park = soup.select('.card-body span')

    r = today()
    messages = ''
    try:
        if t[r] == '월':
            messages += ('◎' + t[r] + '요일 테크노파크 식당 메뉴◎\n'+ '◎점심◎\n' + park_parser(food_two[5].get_text()) + '\n'
                         + park_parser(food_two[7].get_text()) + '\n◎저녁◎\n' + park_parser(food_two[10].get_text()) 
             + '\n' + park_parser(food_two[12].get_text()))
            return (messages)

        elif t[r] == '화':
            messages += ('◎' + t[r] + '요일 테크노파크 식당 메뉴◎\n' + '◎점심◎\n' + park_parser(food_two[5].get_text()) + '\n'
                         + park_parser(food_two[7].get_text()) + '\n◎저녁◎\n' + park_parser(food_two[10].get_text()) 
             + '\n' + park_parser(food_two[12].get_text()))
            return (messages)

        elif t[r] == '수':
            messages += ('◎' + t[r] + '요일 테크노파크 식당 메뉴◎\n' + '◎점심◎\n' + park_parser(food_two[5].get_text()) + '\n'
                         + park_parser(food_two[7].get_text()) + '\n◎저녁◎\n' + park_parser(food_two[10].get_text()) 
             + '\n' + park_parser(food_two[12].get_text()))
            return (messages)

        elif t[r] == '목':
            messages += ('◎' + t[r] + '요일 테크노파크 식당 메뉴◎\n' + '◎점심◎\n' + park_parser(food_two[5].get_text()) + '\n'
                         + park_parser(food_two[7].get_text()) + '\n◎저녁◎\n' + park_parser(food_two[10].get_text()) 
             + '\n' + park_parser(food_two[12].get_text()))
            return (messages)

        elif t[r] == '금':
            messages += ('◎' + t[r] + '요일 테크노파크 식당 메뉴◎\n' + '◎점심◎\n' + park_parser(food_two[5].get_text()) + '\n'
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
    global  food_two, food_two_idx
    r = today()
        
    if(food_two_idx == 0):
        driver.get('http://www.seoultech.ac.kr/life/student/food/')
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        food_two = soup.select(".dts_design td", limit=130)
        food_two_idx = 1

    messages = ''
    try:
        if t[r] == '월':
            messages += (t[r] + '요일 제2학생 식당 메뉴\n' + '◎중식 든든 ' + food_two[13].get_text() + '◎\n'
                         + food_two[8].get_text() + ' ' + food_two[18].get_text() + ' ' + food_two[23].get_text() + ' ' +
                         food_two[28].get_text() + ' ' +
                         food_two[33].get_text() + '\n')
            messages += ('◎중식 푸짐 4200원◎\n' + food_two[39].get_text() + ' ' + food_two[44].get_text() + ' ' + food_two[
                49].get_text() + ' ' + food_two[54].get_text() + ' ' +
                         food_two[59].get_text() + ' ' + food_two[65].get_text() + '\n')
            messages += ('◎석식 푸짐 3500◎\n' + food_two[98].get_text() + ' ' + food_two[103].get_text() + ' ' + food_two[
                108].get_text() + ' ' + food_two[113].get_text() + ' ' +
                         food_two[118].get_text() + ' ' + food_two[123].get_text() + '\n')
            messages += '◎간단 메뉴 + 공깃밥◎\n계란라면 2800원\n떡계란라면 치즈계란라면\n물만두계란라면 3200원\n'
            messages += '◎운영시간 - 중식 11:00~14:00 석식 17:00~19:00 (18:40분까지 주문가능)◎'

            return parser.food_parser(messages)

        elif t[r] == '화':
            messages += (t[r] + '요일 제2학생 식당 메뉴\n' + '◎든든 ' + food_two[14].get_text() + '◎\n'
                         + food_two[9].get_text() + ' ' + food_two[19].get_text() + ' ' + food_two[24].get_text() + ' ' +
                         food_two[29].get_text() + ' ' +
                         food_two[34].get_text() + '\n')
            messages += (
            '◎푸짐 4200원◎\n' + food_two[40].get_text() + ' ' + food_two[45].get_text() + ' ' + food_two[50].get_text() + ' ' +
            food_two[55].get_text() + ' ' +
            food_two[60].get_text() + ' ' + food_two[65].get_text() + '\n')
            messages += ('◎석식 푸짐 3500◎\n' + food_two[99].get_text() + ' ' + food_two[104].get_text() + ' ' + food_two[
                109].get_text() + ' ' + food_two[114].get_text() + ' ' +
                         food_two[119].get_text() + ' ' + food_two[124].get_text() + '\n')
            messages += '◎간단 메뉴 + 공깃밥◎\n계란라면 2800원\n떡계란라면 치즈계란라면\n물만두계란라면 3200원\n'
            messages += '◎운영시간 - 중식 11:00~14:00 석식 17:00~19:00 (18:40분까지 주문가능)◎'
            return parser.food_parser(messages)

        elif t[r] == '수':
            messages += (t[r] + '요일 제2학생 식당 메뉴\n' + '◎든든 ' + food_two[15].get_text() + '◎\n'
                         + food_two[10].get_text() + ' ' + food_two[20].get_text() + ' ' + food_two[25].get_text() + ' ' +
                         food_two[30].get_text() + ' ' +
                         food_two[35].get_text() + '\n')
            messages += (
            '◎푸짐 4200원◎\n' + food_two[41].get_text() + ' ' + food_two[46].get_text() + ' ' + food_two[51].get_text() + ' ' +
            food_two[56].get_text() + ' ' +
            food_two[61].get_text() + ' ' + food_two[66].get_text() + '\n')
            messages += ('◎석식 푸짐 3500◎\n' + food_two[100].get_text() + ' ' + food_two[105].get_text() + ' ' + food_two[
                110].get_text() + ' ' + food_two[115].get_text() + ' ' +
                         food_two[120].get_text() + ' ' + food_two[125].get_text() + '\n')
            messages += '◎간단 메뉴 + 공깃밥◎\n계란라면 2800원\n떡계란라면 치즈계란라면\n물만두계란라면 3200원\n'
            messages += '◎운영시간 - 중식 11:00~14:00 석식 17:00~19:00 (18:40분까지 주문가능)◎'

            return parser.food_parser(messages)

        elif t[r] == '목':
            messages += (t[r] + '요일 제2학생 식당 메뉴◎\n' + '◎든든 ' + food_two[16].get_text() + '◎\n'
                         + food_two[11].get_text() + ' ' + food_two[21].get_text() + ' ' + food_two[26].get_text() + ' ' +
                         food_two[31].get_text() + ' ' +
                         food_two[36].get_text() + '\n')
            messages += (
            '◎푸짐 4200원◎\n' + food_two[42].get_text() + ' ' + food_two[47].get_text() + ' ' + food_two[52].get_text() + ' ' +
            food_two[57].get_text() + ' ' +
            food_two[62].get_text() + ' ' + food_two[67].get_text() + '\n')
            messages += ('◎석식 푸짐 3500◎\n' + food_two[101].get_text() + ' ' + food_two[106].get_text() + ' ' + food_two[
                111].get_text() + ' ' + food_two[116].get_text() + ' ' +
                         food_two[121].get_text() + ' ' + food_two[126].get_text() + '\n')
            messages += '◎간단 메뉴 + 공깃밥◎\n계란라면 2800원\n떡계란라면 치즈계란라면\n물만두계란라면 3200원\n'
            messages += '◎운영시간 - 중식 11:00~14:00 석식 17:00~19:00 (18:40분까지 주문가능)◎'

            return parser.food_parser(messages)

        elif t[r] == '금':
            messages += (t[r] + '요일 제2학생 식당 메뉴\n' + '◎든든 ' + food_two[17].get_text() + '◎\n'
                         + food_two[12].get_text() + ' ' + food_two[22].get_text() + ' ' + food_two[27].get_text() + ' ' +
                         food_two[32].get_text() + ' ' +
                         food_two[37].get_text() + '\n')
            messages += (
            '◎푸짐 4200원◎\n' + food_two[43].get_text() + ' ' + food_two[48].get_text() + ' ' + food_two[53].get_text() + ' ' +
            food_two[58].get_text() + ' ' +
            food_two[63].get_text() + ' ' + food_two[68].get_text() + '\n')
            messages += ('◎석식 푸짐 3500◎\n' + food_two[102].get_text() + ' ' + food_two[107].get_text() + ' ' + food_two[
                112].get_text() + ' ' + food_two[117].get_text() + ' ' +
                         food_two[122].get_text() + ' ' + food_two[127].get_text() + '\n')
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
    global food_two, food_two_idx
    if(food_two_idx == 0):
        driver.get('http://www.seoultech.ac.kr/life/student/food/')
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        food_two = soup.select(".dts_design td", limit=130)

    messages = ''
    try:
        messages += ('월요일 제2학생 식당 메뉴\n' + '◎중식 든든 ' + food_two[13].get_text() + '◎\n'
                     + food_two[8].get_text() + ' ' + food_two[18].get_text() + ' ' + food_two[23].get_text() + ' ' +
                     food_two[28].get_text() + ' ' +
                     food_two[33].get_text() + '\n')
        messages += (
        '◎중식 푸짐 4200원◎\n' + food_two[39].get_text() + ' ' + food_two[44].get_text() + ' ' + food_two[49].get_text() + ' ' +
        food_two[54].get_text() + ' ' +
        food_two[59].get_text() + ' ' + food_two[65].get_text() + '\n')
        messages += (
        '◎석식 푸짐 3500◎\n' + food_two[98].get_text() + ' ' + food_two[103].get_text() + ' ' + food_two[108].get_text() + ' ' +
        food_two[113].get_text() + ' ' +
        food_two[118].get_text() + ' ' + food_two[123].get_text() + '\n')

        messages += ('\n화요일 제2학생 식당 메뉴\n' + '◎든든 ' + food_two[14].get_text() + '◎\n'
                     + food_two[9].get_text() + ' ' + food_two[19].get_text() + ' ' + food_two[24].get_text() + ' ' +
                     food_two[29].get_text() + ' ' +
                     food_two[34].get_text() + '\n')
        messages += (
        '◎푸짐 4200원◎\n' + food_two[40].get_text() + ' ' + food_two[45].get_text() + ' ' + food_two[50].get_text() + ' ' +
        food_two[55].get_text() + ' ' +
        food_two[60].get_text() + ' ' + food_two[65].get_text() + '\n')
        messages += (
        '◎석식 푸짐 3500◎\n' + food_two[99].get_text() + ' ' + food_two[104].get_text() + ' ' + food_two[109].get_text() + ' ' +
        food_two[114].get_text() + ' ' +
        food_two[119].get_text() + ' ' + food_two[124].get_text() + '\n')

        messages += ('\n수요일 제2학생 식당 메뉴\n' + '◎든든 ' + food_two[15].get_text() + '◎\n'
                     + food_two[10].get_text() + ' ' + food_two[20].get_text() + ' ' + food_two[25].get_text() + ' ' +
                     food_two[30].get_text() + ' ' +
                     food_two[35].get_text() + '\n')
        messages += (
        '◎푸짐 4200원◎\n' + food_two[41].get_text() + ' ' + food_two[46].get_text() + ' ' + food_two[51].get_text() + ' ' +
        food_two[56].get_text() + ' ' +
        food_two[61].get_text() + ' ' + food_two[66].get_text() + '\n')
        messages += ('◎석식 푸짐 3500◎\n' + food_two[100].get_text() + ' ' + food_two[105].get_text() + ' ' + food_two[
            110].get_text() + ' ' + food_two[115].get_text() + ' ' +
                     food_two[120].get_text() + ' ' + food_two[125].get_text() + '\n')

        messages += ('\n목요일 제2학생 식당 메뉴◎\n' + '◎든든 ' + food_two[16].get_text() + '◎\n'
                     + food_two[11].get_text() + ' ' + food_two[21].get_text() + ' ' + food_two[26].get_text() + ' ' +
                     food_two[31].get_text() + ' ' +
                     food_two[36].get_text() + '\n')
        messages += (
        '◎푸짐 4200원◎\n' + food_two[42].get_text() + ' ' + food_two[47].get_text() + ' ' + food_two[52].get_text() + ' ' +
        food_two[57].get_text() + ' ' +
        food_two[62].get_text() + ' ' + food_two[67].get_text() + '\n')
        messages += ('◎석식 푸짐 3500◎\n' + food_two[101].get_text() + ' ' + food_two[106].get_text() + ' ' + food_two[
            111].get_text() + ' ' + food_two[116].get_text() + ' ' +
                     food_two[121].get_text() + ' ' + food_two[126].get_text() + '\n')

        messages += ('\n금요일 제2학생 식당 메뉴\n' + '◎든든 ' + food_two[17].get_text() + '◎\n'
                     + food_two[12].get_text() + ' ' + food_two[22].get_text() + ' ' + food_two[27].get_text() + ' ' +
                     food_two[32].get_text() + ' ' +
                     food_two[37].get_text() + '\n')
        messages += (
        '◎푸짐 4200원◎\n' + food_two[43].get_text() + ' ' + food_two[48].get_text() + ' ' + food_two[53].get_text() + ' ' +
        food_two[58].get_text() + ' ' +
        food_two[63].get_text() + ' ' + food_two[68].get_text() + '\n')
        messages += ('◎석식 푸짐 3500◎\n' + food_two[102].get_text() + ' ' + food_two[107].get_text() + ' ' + food_two[
            112].get_text() + ' ' + food_two[117].get_text() + ' ' +
                     food_two[122].get_text() + ' ' + food_two[127].get_text() + '\n')
        messages += '◎간단 메뉴 + 공깃밥◎\n계란라면 2800원\n떡계란라면 치즈계란라면\n물만두계란라면 3200원\n'
        messages += '◎운영시간 - 중식 11:00~14:00 석식 17:00~19:00 (18:40분까지 주문가능)◎'

        return parser.food_parser(messages)
    except:
        return ('식당 메뉴가 업로드 되지 않았습니다.')    

# kb 학사 전체
def KB_All():
    global kb
    if (kb_idx == 0):
        driver.get('http://domi.seoultech.ac.kr/support/food/?foodtype=kb')
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        kb = soup.findAll("td", limit=8)
        
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
    global sung
    if(sung_idx==0):
        driver.get('http://domi.seoultech.ac.kr/support/food/?foodtype=sung')
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        sung = soup.findAll("td", limit=8)
        
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
    global surim
    if(surim_idx == 0):
        driver.get('http://domi.seoultech.ac.kr/support/food/?foodtype=surim')
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        surim = soup.findAll("td", limit=8)
        
    messages = ''

    messages += ('◎월요일 학식 메뉴◎' + surim[1].get_text())
    messages += ('◎화요일 학식 메뉴◎' + surim[2].get_text())
    messages += ('◎수요일 학식 메뉴◎' + surim[3].get_text())
    messages += ('◎목요일 학식 메뉴◎' + surim[4].get_text())
    messages += ('◎금요일 학식 메뉴◎' + surim[5].get_text())
    messages += ('◎토요일 학식 메뉴◎' + surim[6].get_text())
    messages += ('◎일요일 학식 메뉴◎' + surim[7].get_text())
    return parser.dom_parser(messages)
