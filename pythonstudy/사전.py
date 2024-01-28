# cabinet = {3:"유재석",100:"김태호"}
# #3번키를 유재석이 받았다,100번키를 김태호가 받았다
# print(cabinet[3]) 
# print(cabinet[100])

# print(cabinet.get(3))
# # print(cabinett[5])
# #오류,컴파일 종료

# print(cabinet.get(5))
# #none

# print(cabinet.get(5,"사용 가능"))

# print(3 in cabinet) # True
# print(5 in cabinet) # False

cabinet = { "A-3" : "유재석","B- 100":"김태호"}
print(cabinet["A-3"])
print(cabinet)
cabinet["A-3"] = "김종국" # replace
cabinet["C-20"] = "조세호"
print(cabinet)

#간 손님
del cabinet["A-3"] #지울수있므
print(cabinet)
#key만 출력
print(cabinet.keys())

#value만 출력
print(cabinet.values())

#둘다 출력
print(cabinet.items())

#목욕탕 폐점
cabinet.clear()
print (cabinet)


