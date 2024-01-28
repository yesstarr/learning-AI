#아이디 20명 아이디는 숫자로,
#20명이 작성, 댓글내용과 상관없이 무작위로 추첨, 중복 불가
#random모듈의 shuffle과 sample활용
from random import *
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

users = range(1,21) # 1부터 2-까지
users = list(users)

shuffle(lst)

shuffle(users)

print("-- 당첨자 발표 --")

winners = sample(users,4) # 3명은 커피, 1명은 치킨
print("커피당첨자 : {0}" .format(winners[0]))
print("치킨 당첨자 : {0}" .format(winners[1:]))

