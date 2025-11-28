# 내장 modules


# 날짜와 시간
from datetime import datetime, date
now = datetime.now()
print( now,type(now)) # 오늘 날짜와 시간
print(now.strftime('%Y년 %m월 %d일 %H시 %M분 %S초'))
print(now.strftime('%Y년 %m월 %p %d일 %I시 %M분 %S초 %f'))

print(now.date()) #오늘 날짜
start = date(2025, 11, 19 )
today = date(2025, 11, 28 )
print( today - start)
# 시간 그자체
import time

print(time.time()) # 1970년 1월 1일 자정부터 몇초가 지났는가 (초 단위)

before = time.time() 
# 시간을 측정하고 싶은 코드 작성
for i in range(10) :
    print(i)
    #pass
    # time.sleep(0.5) # 일시정지 (초 단위) 
after = time.time()
print (f'걸린시간 :{after - before}')


import random
print(random.random()) # 0 M= rnd <1
print(random.randint(1,6)) # 1~6 사이의 무작위 정수

a = [1,2,3,4,5]
print(random.choice(a)) # 시퀀스 객체에서 무작위 선택
random.shuffle(a)
print(a)
