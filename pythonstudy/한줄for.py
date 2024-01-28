# #출석번호 1 2 3 4 앞에 20220400을 붙이기로 함
# students = [1,2,3,4,5]
# print(students)
# students = [i+202204000 for i in students]
# print(students)

# students = ["Iron man","Thor","I am groot"]
# students = [len(i) for i in students]
# print(students)

# students = ["Iron man","Thor","I am groot"]
# students = [i.upper() for i in students]
# print(students)

#Quiz
from random import *

cnt = 0
for number in range(1,51) :
    min = randrange(5,51)
    if min <= 15 :
        ok = "O"
        cnt+=1
    else:
        ok = " "

    print("[{2}] {0}번째 손님  소요시간 : {1}분" .format(number,min,ok))
    if number == 50 :
        print("총 탑승 승객 : {0}분" .format(cnt))
