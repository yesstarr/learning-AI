# print("백문이 불여일견 
# 백견이 불여일타")
print("백문이 불여일견 \n 백견이 불여일타")
#저는 "나도코딩" 입니다
print('저는"나도코딩"입니다.')
print("저는 \"나도코딩\" 입니다.")
#\쓸때는 \\

#\r : 커서 맨앞으로 이동
print("Red apple\rPine")

# \b : 백스페이스 (한글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")

#quiz 사이트별로 비밀번호만들기 

# url = "http://naver.com"
# newurl = url[7:12]
# cnt = url.count("e")
# print("생성된 비밀번호 : %s %d %d !" %(newurl[0:3],len[newurl],cnt))
# url = "http://naver.com"
# my_str = url.replace("http://","")
# print(my_str)
# my_str =my_str[:my_str.index(".")] 
# print(my_str)
# password = my_str[:3] + str(len(my_str)) +str(my_str.count("e")) +"!"
# print("{0}의 비밀번호는 {1}입니다. " .format(url,password))

url = "http://naver.com"
newurl = url.replace("http://","")
newurl = newurl[:newurl.index(".")]
print(newurl)
password = newurl[:3]+str(len(newurl))+str(newurl.count("e"))+"!"
print("생성된 비밀번호 : {0}" .format(password))
