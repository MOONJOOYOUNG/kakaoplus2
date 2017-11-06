from django.test import TestCase

# Create your tests here.
import datetime
utcnow = datetime.datetime.utcnow()
time_gap = datetime.timedelta(hours=9)
kor_time = utcnow + time_gap

print(kor_time)

now = datetime.datetime.now()
nowdate = now.strftime('%m-%d')
messages = ''

t = ['월', '화', '수', '목', '금', '토', '일']
r = kor_time.weekday()

print(t[r])