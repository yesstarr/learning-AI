# print("a"+"b")
# print("a","b")

print("나는 %d살입니다." %20)
print("나는 %s을 좋아해요" %"파이썬")
# c언어와 달리 , 로 구분하는게 아닌 걍 %갈기셈
print("Apple 은 %c로 시작해요." %"A")
# %s 로 하면 다 됨
print("나는 %s색과 %s색을 좋아해요." %("파란","빨간"))

print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요" .format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아해요" .format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요" .format("파란","빨간"))

print("나는{age}살이며,{color}색을 좋아해요." .format(age = 20,color="빨간"))


#파이썬 버젼 3.6 이상
age = 20
color = "빨간"
print(f"나는{age}살이며,{color}색을 좋아해요.")
#f 를 쓰고 시작하면 변수 가져다가 쓸 수 있음