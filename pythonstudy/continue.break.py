absent = [2,5]
no_book =[7]
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book :
        print("수업끝")
        break
    print("{0}아, 책을 읽어봐".format(student))
