from random import *

print(random()) #0.0 ~ 1.0 미만의 임의의 값 생성
print(random()*10)
print(int(random()*10)) #인트형으로
print(int(random()*10)+1) # 1~10이하의 임의의 값 생성

print(int(random()*45)+1) #1부터 45 이하의 임의의 값 생성
print(int(random()*45)+1) #1부터 45 이하의 임의의 값 생성
print(int(random()*45)+1) #1부터 45 이하의 임의의 값 생성
print(int(random()*45)+1) #1부터 45 이하의 임의의 값 생성
print(int(random()*45)+1) #1부터 45 이하의 임의의 값 생성
print(int(random()*45)+1) #1부터 45 이하의 임의의 값 생성

print(randrange(1,46)) #1부터 45이하의 임의의 값 생성

print(randint(1,45)) #1부터 45 이하의 임의의 값 생성

#quiz 오프라인 1번 온라인 3번, 월별 날짜 28일 이내, 1~3일 제외

day = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 "+str(day)+"일로 선정되었습니다")
print("오프라인 스터디 모임 날짜는 매월",day,"일로 선정되었습니다")