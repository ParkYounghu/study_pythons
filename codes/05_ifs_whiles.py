

#first = 5   # 오타 frist -> first

#while first > 0:
#    print(f"while 값 : {first}") 
#    first = first - 1


 
#first = 5

#while first > 0:
#    print(f"while 값 : {first}")  # 들여쓰기 문제, print 앞에서 Tab
#    first = first - 1


first = 5

while first > 0:
    print(f"while 값 : {first}")
    if first == 3:     # 실제로는 first == 3 에서 break해야 하는 문제 조건, < 지우고 == 추가
        print("break 실행")
        break
    first = first - 1
