from .decorators import bot
from . import functions


# myvenv\Scripts\activate
# cd 프로젝트 경로
# python manage.py runserver 0:8000

@bot
def on_init(request):
    return {
        'type': 'text',
        'keyboard': {
            'type': 'buttons',      
            'buttons' : ['오늘 식단표','이번주 식단표','도서관 열람실 좌석 현황','네이버 실시간 검색어']
        }
 }

@bot
def on_message(request):
    user_key = request.JSON['user_key']
    type = request.JSON['type']
    content = request.JSON['content']  # photo 타입일 경우에는 이미지 URL

    if content.startswith('명령어'):
        response = ('명령어는 " " 안에 있는 단어를 입력 하시면 됩니다. ex) -> 수림\n●명령어 리스트● \n' \
                   '1.이번주 학식 메뉴 \n"케이비, 성림, 수림"\n' \
                   '2.학교 교통 노선 \n"지하철, 버스"' \
                   '\n3.네이버 실시간 검색\n"실시간,네이버"\n4.음악 검색 \n"뮤직 노래제목"' \
                   ' ex)뮤직 노력')
    elif content.startswith('오늘 식단표'):
        return ({
			'message':{
				'text':'장소를 골라주세요.'
			},
			'keyboard':{
				'type':'buttons',
				'buttons':['KB 학사 학식 메뉴','성림 학사 학식 메뉴', '수림 학사 학식 메뉴','제2 학생 식당 메뉴','내일 제2 학생 식당 메뉴']
			}
		})

    elif content.startswith('이번주 식단표'):
        return ({
			'message':{
				'text':'장소를 골라주세요.'
			},
			'keyboard':{
				'type':'buttons',
				'buttons':['케이비','성림', '수림','제2 학생 식당']
			}
		})
   

    elif content.startswith('도서관 열람실 좌석 현황'):
        response = functions.Library_seat()

    elif content.startswith('KB 학사 학식 메뉴'):
        response = functions.Kb_Dormitory()

    elif content.startswith('성림 학사 학식 메뉴'):
        response = functions.Sungrim_Dormitory()

    elif content.startswith('수림 학사 학식 메뉴'):
        response = functions.Surim_Dormitory()

    elif content.startswith('제2 학생 식당 메뉴'):
        response = functions.Food_two()

    elif content.startswith('제2 학생 식당'):
        response = functions.Food_two_tomorrow()

    elif content.startswith('도서관 열람실 좌석 현황'):
        response = functions.Library_seat()

    elif content.startswith('케이비'):
        response = functions.KB_All()

    elif content.startswith('수림'):
        response = functions.Surim_All()

    elif content.startswith('성림'):
        response = functions.Sungrim_All()

    elif content.startswith('지하철'):
        response = ('●7호선 공릉역 2번 출구●\n' \
                   '마을버스 03번, 13번(교내 경유)\n' \
                   '●1, 6호선 석계역 1,4,6번 출구●\n' \
                   '마을버스 03번, 13번(교내 경유)')

    elif content.startswith('버스'):
        response = ('●지선버스(초록버스)●\n1136번,1141번,1224번,1227번\n' \
                   '●마을버스 - 03번●\n' \
                   '●교내 경유 마을버스 - 13번●\n' \
                   '정문-다산관-붕어방-다산관-주차로터리')

    elif content.startswith('네이버 실시간 검색어'):
        response = ('네이버 실시간 검색어\n {}'.format(functions.naver_rank()))

    else:
        response = ('지원하는 명령어가 아닙니다.')

    return {
        'message': {
            'text': response,
        },
        'keyboard': {
            'type': 'buttons',
            'buttons' : 'buttons' : ['오늘 식단표','이번주 식단표','도서관 열람실 좌석 현황','네이버 실시간 검색어']
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
