print(5)
print(-10)
print(3.14)
print(5>10)
print(True)
print(not (5>10))

animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >=3

print("우리집 "+animal+"의 이름은 "+ name+"이에요")
print(name + "는 " +str(age)+"살이며, "+hobby+"을 아주 좋아해요")
# 정수형을 문자형으로 바꿔줄땐 str로 감싸준다
# print(name + "는 어른일까요?" + str(is_adult))
# 불릿형을 문자형으로 바꿔줄땐 str로 감싸준다
print(name ,"는 어른일까요?" ,is_adult)
# +대신에 ,를 넣어줄수있는데, 이때는 str로 안감싸줘도됨  
# 컨트롤 + / 로 전체 주석 가능

print(2**3) # 2의 3승
print(5//3) #몫
print(abs(-5)) #5, abs는 절댓값
print(pow(4,2))#4의 2승
print(max(5,12)) # 12
print(min(5,12))#5
print(round(3.14))#3 round == 반올림

from math import *
print(floor(4.99)) #4 floor == 내림
print(ceil(3.14)) #4 올림
print(sqrt(16)) #4 제곱근

