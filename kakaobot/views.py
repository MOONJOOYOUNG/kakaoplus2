from django.shortcuts import render
from .decorators import bot
from . import functions
import requests
from bs4 import BeautifulSoup

# myvenv\Scripts\activate
# cd 프로젝트 경로
# python manage.py runserver 0:8000

@bot
def on_init(request):
    return {'type': 'text' }

@bot
def on_message(request):
    user_key = request.JSON['user_key']
    type = request.JSON['type']
    content = request.JSON['content']  # photo 타입일 경우에는 이미지 URL

    if content.startswith('뮤직 '):
        query = content[3:]
        response = '멜론 "{}" 검색결과\n\n'.format(query) + functions.melon_search(query)

    elif content.startswith('명령어') | content.startswith('명령'):
        response = '명령어 기능 1.오늘의 학식 메뉴(서캠,동캠,기숙사) 2.우송대 근처 맛집(맛집) 3.네이버 실시간 검색(실시간) 4.음악찾기(뮤직 노래제목)'

    elif content.startswith('안형선') | content.startswith('형선'):
        response = '게임멀티미디어학과 11학번 안형선(26 빠른93) 키 181cm 몸무게 102kg 여친구함. 현 경동택배 R&D 근무 연봉 3100'

    elif content.startswith('서캠') | content.startswith('서'):
        response = functions.WestCampus()

    elif content.startswith('동캠') | content.startswith('동'):
        response = functions.EastCampus()

    elif content.startswith('기숙사') | content.startswith('긱사'):
        response = functions.Dormitory()

    elif content.startswith('맛집'):
        response = "오늘의 추천 식당은 " + functions.NearCampus() + "입니다."

    elif content.startswith('혼밥'):
        response = functions.alone()

    elif content.startswith('학식'):
        response = "서캠(서), 동캠(동), 기숙사(긱사) 입력시 해당되는 곳의 오늘의 학식 정보를 알수 있습니다."

    elif content.startswith('실시간'):
        response = '네이버 실시간 검색어\n {}'.format(functions.naver_rank())

    else:
        response = '지원하는 명령어가 아닙니다. "명령어" or "명령" 입력 시 지원되는 기능을 볼 수 있습니다.'

    return {
        'message': {
            'text': response,
        }
    }

@bot
def on_added(request):
    user_key = request.JSON['user_key']

@bot
def on_block(request, user_key):
    pass
@bot
def on_leave(request, user_key):
    pass


# Create your views here.

