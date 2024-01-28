python = "Python is Amazing"
print(python.lower())#소문자로 출력
print(python.upper())#대문자로 출력
print(python)

print(python[0].isupper()) #첫번째꺼 대문자임?
print(len(python)) #길이
print(python.replace("Python","Java")) #글자 찾아서 변환

index = python.index("n") #위치 찾기, 맨 처음으로 n이 나오는 위치만 찾아줌
print(index)
index = python.index("n",index + 1) #그 뒤에 있는것도 찾아줌
print(index)

print(python.find("n"))

print(python.find("Java")) # 없으면 -1 반환
#print(python.index("Java")) 그냥 오류
print(python.count("n"))
