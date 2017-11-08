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

    if content.startswith('명령어'):
        response = '명령어는 () 안에 있는 단어를 입력 하시면 됩니다.\n명령어 기능 1.오늘의 학식 메뉴(서캠,동캠,기숙사) 다음날 학식(내일서캠,내일동캠,내일기숙사)' \
                   '2.우송대 근처 맛집(맛집) 3.오늘의 추천 식당(추천) 4.네이버 실시간 검색(실시간,네이버) 5.노래찾기(뮤직 노래제목)'

    elif content.startswith('서캠'):
        response = functions.WestCampus()

    elif content.startswith('동캠'):
        response = functions.EastCampus()

    elif content.startswith('기숙사'):
        response = functions.Dormitory()

    elif content.startswith('맛집'):
        response = "우송대 근처 맛집 리스트 입니다.\n {}".format(functions.FoodList())

    elif content.startswith('추천'):
        response = "오늘의 추천 식당은 " + functions.NearCampus() + " 입니다."

    elif content.startswith('내일서캠'):
        response = functions.TommorrowWestCampus()

    elif content.startswith('내일동캠'):
        response = functions.TommorrowEastCampus()

    elif content.startswith('내일기숙사'):
        response = functions.TommorrowDormitory()

    elif content.startswith('혼밥'):
        response = functions.alone()

    elif content.startswith('뮤직 '):
        query = content[3:]
        response = '멜론 "{}" 검색결과\n\n'.format(query) + functions.melon_search(query)

    elif content.startswith('안형선') | content.startswith('형선'):
        response = '게임멀티미디어학과 11학번 안형선(26 빠른93) 키 181cm 몸무게 102kg 여친구함. 현 경동택배 R&D 근무 연봉 3100'

    elif content.startswith('학식'):
        response = "서캠, 동캠, 기숙사 입력시 해당되는 곳의 오늘의 학식 정보를 알수 있습니다."

    elif content.startswith('실시간') | content.startswith('네이버'):
        response = '네이버 실시간 검색어\n {}'.format(functions.naver_rank())

    elif content.startswith('최정헌') | content.startswith('정헌'):
        response = '최정헌(26) 게임멀티미디어 11학번 학회장출신 파파스에서 안형선한테 외모대결 패배 일명 빵떡사건'

    else:
        response = '지원하는 명령어가 아닙니다. "명령어" 입력 시 지원되는 기능을 볼 수 있습니다.'

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

