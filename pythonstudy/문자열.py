sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

yesung = "991014-1234567"

print("성별 : " + yesung[7])
print("연 : " + yesung[0:2]+"년") # index 0부터 1까지 
print("월 : " + yesung[2:4] + "월")
print("일 : " +yesung[4:6]+ "일")

print("생년월일 : " + yesung[:6]) #처음부터 6까지
print("뒤 7자리 : " +yesung[7:])#7부터 끝까지
print("뒤 7자리 (뒤에부터) " + yesung [-7:])#맨 뒤에서 7번쨰부터 끝까지