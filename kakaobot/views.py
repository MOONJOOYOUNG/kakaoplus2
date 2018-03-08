from .decorators import bot
from . import functions


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
        response = '명령어는 "" 안에 있는 단어를 입력 하시면 됩니다. ex) -> 수림\n●명령어 리스트● \n1.오늘의 학식 메뉴 "케이비" "성림" "수림"\n' \
                   '이번주학식"이번주kb,이번주성림,이번주수림"' \
                   '\n2.네이버 실시간 검색(실시간,네이버)'
    #\n2.과기대 근처 밥집(밥집)\n3.오늘의 추천 식당(추천)
    elif content.startswith('kb') | content.startswith('케이비'):
        response = functions.Kb_Dormitory()

    elif content.startswith('성림'):
        response = functions.Sungrim_Dormitory()

    elif content.startswith('수림'):
        response = functions.Surim_Dormitory()

    elif content.startswith('밥집'):
        response = "과기대 근처 밥집 리스트 입니다.\n{}".format(functions.FoodList())

    elif content.startswith('추천'):
        response = "오늘의 추천 식당은 " + functions.NearCampus() + " 입니다."

    elif content.startswith('이번주kb') | content.startswith('이번주케이비'):
        response = functions.KB_All()

    elif content.startswith('이번주수림'):
        response = functions.Surim_All()

    elif content.startswith('이번주성림'):
        response = functions.Sungrim_All()

    elif content.startswith('A노선') | content.startswith('a노선'):
        response = 'A노선 7회 운행 대전75바2845\n' \
                   '●노선 정보●\n' \
                   '로얄빌(동캠)→학술정보센터(동캠)→학생회관(동캠)→학술정보센터(동캠)→동문입구(서캠)→도서정보센터(서캠)→로얄빌(동캠)→학술정보센터(동캠)→학생회관(동캠)' \
                   '\n●배차 시간●\n08:30   09:30   10:30   13:30   16:00   16:30   17:30 \n●각 정류장별 2~4분 소요●'

    elif content.startswith('B노선') | content.startswith('b노선'):
        response = 'B노선 9회 운행 대전75바2845\n' \
                   '●노선 정보●\n' \
                   '학생회관(동캠)→학술정보센터(동캠)→동문입구(서캠)→도서정보센터(서캠)→학술정보센터(동캠)→학생회관(동캠)' \
                   '\n●배차 시간●\n09:00   10:00   11:00   11:30  14:00   14:30   15:00   15:30   17:00 \n●각 정류장별 2~4분 소요●'

    elif content.startswith('혼밥'):
        response = functions.alone()

    elif content.startswith('뮤직 '):
        query = content[3:]
        response = '멜론 "{}" 검색결과\n\n'.format(query) + functions.melon_search(query)

    elif content.startswith('학식'):
        response = "서캠, 동캠, 기숙사 입력시 해당되는 곳의 오늘의 학식 정보를 알수 있습니다."

    elif content.startswith('실시간') | content.startswith('네이버'):
        response = '네이버 실시간 검색어\n {}'.format(functions.naver_rank())

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

