from .decorators import bot
from . import functions


# myvenv\Scripts\activate
# cd 프로젝트 경로
# python manage.py runserver 0:8000

@bot
def on_init(request):
    return {'type' : 'buttons',
            'buttons' : ['오늘 식단표','이번주 식단표','버스 정류장','공릉동 미세먼지']
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
				'buttons':['KB 학사 학식 메뉴','성림 학사 학식 메뉴', '수림 학사 학식 메뉴','제2 학생 식당 메뉴','테크노 파크 식단']
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

    elif content.startswith('버스 정류장'):
        return ({
			'message':{
				'text':'장소를 골라주세요.'
			},
			'keyboard':{
				'type':'buttons',
				'buttons':['공릉역 2번 출구', '과기대 붕어방','정문 13번 공릉방향','과기대 정문','정문(교촌치킨)','1번 출구 석계역','4번 출구 석계역']
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

    elif content.startswith('테크노 파크 식단'):
        response = functions.TechPark()

    elif content.startswith('케이비'):
        response = functions.KB_All()

    elif content.startswith('수림'):
        response = functions.Surim_All()

    elif content.startswith('성림'):
        response = functions.Sungrim_All()

    elif content.startswith('공릉역 2번 출구'):
        response = functions.bus_Gongneung()

    elif content.startswith('과기대 붕어방'):
        response = functions.bus_bnag()
    
    elif content.startswith('과기대 정문'):
        response = functions.front_door()

    elif content.startswith('정문(교촌치킨)'):
        response = functions.front_door_gs()
	
    elif content.startswith('정문 13번 공릉방향'):
        response = functions.front_door_13()
	
    elif content.startswith('1번 출구 석계역'):
        response = functions.seok_1()
	
    elif content.startswith('4번 출구 석계역'):
        response = functions.seok_2()
	
    elif content.startswith('공릉동 미세먼지'):
        response = functions.check_dust()
	
    else:
        response = ('지원하는 명령어가 아닙니다.')
    
    #elif content.startswith('도서관 열람실 좌석 현황'):
    #    response = functions.Library_seat()

    return {
        'message': {
            'text': response,
        },
        'keyboard': {
            'type': 'buttons',
            'buttons' : ['오늘 식단표','이번주 식단표','버스 정류장','공릉동 미세먼지']
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
