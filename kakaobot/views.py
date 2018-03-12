from .decorators import bot
from . import functions


# myvenv\Scripts\activate
# cd 프로젝트 경로
# python manage.py runserver 0:8000

@bot
def on_init(request):
    return {'type' : 'buttons',
            'buttons' : ['KB 학사 식단','성림 학사 식단', '수림 학사 식단','제2 학생 식당 메뉴' ,'이번주 KB 식단','이번주 성림 식단','이번주 수림 식단']
 }

@bot
def on_message(request):
    user_key = request.JSON['user_key']
    type = request.JSON['type']
    content = request.JSON['content']  # photo 타입일 경우에는 이미지 URL

    if content.startswith('명령어'):
        if content.startswith('명령어'):
            response = '명령어는 " " 안에 있는 단어를 입력 하시면 됩니다. ex) -> 수림\n●명령어 리스트● \n' \
                       '1.오늘의 학식 메뉴 "케이비, 성림, 수림, 제2"\n' \
                       '2.이번주 학식 "이주케이비,이주성림,이주수림"' \
                       '\n3.학교 교통 노선 "지하철, 버스"' \
                       '\n4.네이버 실시간 검색 "실시간,네이버"\n5.음악 검색 "뮤직 노래제목"' \
                       '\n  ex)뮤직 박원'
    #\n2.과기대 근처 밥집(밥집)\n3.오늘의 추천 식당(추천)
    elif content.startswith('케이비') | content.startswith('KB 학사 식단'):
        response = functions.Kb_Dormitory()

    elif content.startswith('성림') | content.startswith('성림 학사 식단'):
        response = functions.Sungrim_Dormitory()

    elif content.startswith('수림') | content.startswith('수림 학사 식단'):
        response = functions.Surim_Dormitory()

    elif content.startswith('제2') | content.startswith('제2 학생 식당 메뉴'):
        response = functions.food_two()

    elif content.startswith('밥집'):
        response = "과기대 근처 밥집 리스트 입니다.\n{}".format(functions.FoodList())

    elif content.startswith('추천'):
        response = "오늘의 추천 식당은 " + functions.NearCampus() + " 입니다."

    elif content.startswith('이번주케이비') | content.startswith('이번주 KB 식단'):
        response = functions.KB_All()

    elif content.startswith('이번주수림') | content.startswith('이번주 수림 식단'):
        response = functions.Surim_All()

    elif content.startswith('이번주성림') | content.startswith('이번주 성림 식단'):
        response = functions.Sungrim_All()

    elif content.startswith('지하철'):
        response = '●7호선 공릉역 2번 출구●\n' \
                   '마을버스 03번, 13번(교내 경유)\n' \
                   '●1, 6호선 석계역 1,4,6번 출구●\n' \
                   '마을버스 03번, 13번(교내 경유)'

    elif content.startswith('버스'):
        response = '●지선버스(초록버스)●\n1136번,1141번,1224번,1227번\n' \
                   '●마을버스 - 03번●\n' \
                   '●교내 경유 마을버스 - 13번●\n' \
                   '정문-다산관-붕어방-다산관-주차로터리'

    elif content.startswith('뮤직 '):
        query = content[3:]
        response = '멜론 "{}" 검색결과\n\n'.format(query) + functions.melon_search(query)

    elif content.startswith('실시간') | content.startswith('네이버'):
        response = '네이버 실시간 검색어\n {}'.format(functions.naver_rank())

    else:
        response = '지원하는 명령어가 아닙니다. "명령어" 입력 시 지원되는 기능을 볼 수 있습니다.'

    return {
        'message': {
            'text': response,
        },
        'keyboard': {
            'type': 'buttons',
            'buttons' : ['KB 학사 식단','성림 학사 식단', '수림 학사 식단','제2 학생 식당 메뉴' ,'이번주 KB 식단','이번주 성림 식단','이번주 수림 식단']
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

