# second = "Programming"
# first = "Welcome to Python Strings" + second   # 오류 발생 , 중괄호 제거

# print(first)

# 아래 코드는 first가 문자열인데, while 조건에서 비교 연산을 수행하려고 한다.
#  발생하는 오류를 설명하고, 정상 작동하도록 수정하시오.
# first = "Hello Python"

# while first > 0:
#     print(first)
#     first = first - 1
# 문자열은 크기 비교가 불가능하므로, while 조건에서 비교 연산을 수행할 수 없다.


# 이를 해결하기 위해 first를 정수형 변수로 변경하여 비교 연산이 가능

# first = 5

# while first > 0:
#     print(first)
#     first = first - 1

# 문자열을 지우고 싶다면

# first = "Hello Python"

# while len(first) > 0:
#     print(first)
#     first = first[:-1]   # 뒤에서 한 글자씩 제거

# 문자열을 반복하고 싶고, 반복 횟수를 제어하려면

# first = "Hello Python"
# count = len(first)

# while count > 0:
#     print(first)
#     count -= 1

# 아래 코드의 오류를 찾고 올바르게 수정하시오.
# kor = [70, 80, 90, 40, 50]
# eng = [90, 80, 70, 70, 60]
# sum_all = 0

# for k in kor:
#     sum_all = sum_all + kor + eng     # 오류 위치 : kor 과 eng 는 리스트라서 숫자와 더할 수 없다.

# 따라서 인덱스를 활용

# kor = [70, 80, 90, 40, 50]
# eng = [90, 80, 70, 70, 60]
# sum_all = 0

# for index in range(len(kor)):
#     sum_all += kor[index] + eng[index]

# print(sum_all)

# 아래 코드에서 IndexError가 발생한다.
#  오류 원인을 설명하고 올바른 코드를 작성하시오.
# kor = [70, 80, 90, 40, 50]
# eng = [90, 80, 70, 70, 60]

# sum_total = 0

# for i in range(0, 10):    # 오류 발생 
#     sum_total = sum_total + kor[i] + eng[i]

# 아래 코드에서 IndexError가 발생한다.
#  오류 원인을 설명하고 올바른 코드를 작성하시오.

#  kor와 eng 리스트 길이가 5이므로 range(5)를 쓰거나 range(0,5)를 쓴다

kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]

sum_total = 0

for i in range(0, 5):
    sum_total = sum_total + kor[i] + eng[i] 

print(sum_total)
