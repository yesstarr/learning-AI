# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10,20,30]

subway = ["유재석","조세호","박명수"]

print(subway.index("조세호"))

subway.append("하하")
#append = 뒤에 더해주는 것
print(subway)

subway.insert(1,"정형돈")
#insert 말그대로 삽입하는 것 삽입당한 위치를 기준으로 뒤에 있는 것들은 한칸씩 밀리게됨
print(subway)

print(subway.pop())
#pop은 맨뒤에 사람빼는 것
print(subway)

subway.append("유재석")
print(subway.count("유재석"))

num_list = [5,2,4,3,1]
num_list.sort()#정렬하기
print(num_list)

num_list.reverse() #반대로
print(num_list)

num_list.clear() #다 지우기
print(num_list)

mix_list=["조세호",20,True]
num_list.extend(mix_list)
print(num_list)