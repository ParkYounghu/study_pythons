# 섭씨 온도 3개를 받아 평균을 반환하는 함수 avg_celsius(t1, t2, t3) 를 작성하시오.

# def _K(C):
#     K = (C - 32) * 5 / 9
#     return K

# C1 = 113
# C2 = 104
# C3 = 95

# def avg_C(t1, t2, t3):
#     avg = (t1 + t2 + t3) / 3
#     return avg

# t1 = _K(C1)
# t2 = _K(C2)
# t3 = _K(C3)

# average = avg_C(t1, t2, t3)
# print(average)

# 이름과 좋아하는 언어 2개를 받아 아래 형식으로 출력하는 함수를 작성하시오.
# 홍길동님의 선호 언어는 Python, Java 입니다.

# # 1. 언어 2개를 하나의 문자열로 합치는 함수
# def join_languages(A, B):
#     return f"{A}, {B}"


# # 2. 이름과 언어 문자열을 이용해 문장 생성
# def make_sentence(N, L):
#     return f"{N}님의 선호 언어는 {L} 입니다."


# # 3. 최종 출력 함수
# def print_favorites(N, A, B):
#     langs = join_languages(A, B)    # 함수 1 사용
#     sentence = make_sentence(N, langs)   # 함수 2 사용
#     print(sentence)                         # 최종 출력


# # 사용 예시
# print_favorites("홍길동", "Python", "Java")  # 함수 1,2,3 모두 사용됨

# 🔹 문제 3
# 점수 리스트를 받아 60점 이상 점수만 누적한 합계를 반환하는 함수를 작성하시오.


# # 1. 점수가 60점 이상인지 확인하는 함수
# def is_pass(score):
#     return score >= 60


# # 2. 60점 이상 점수만 새로운 리스트로 필터링하는 함수
# def filter_pass(scores):
#     passed = []
#     for s in scores:
#         if is_pass(s):          # 함수 1 사용
#             passed.append(s)
#     return passed


# # 3. 리스트 숫자들의 합을 구하는 함수
# def sum_scores(score_list):
#     total = 0
#     for s in score_list:
#         total += s
#     return total


# # 4. 최종적으로 60점 이상만 합산해 반환하는 함수
# def sum_pass_scores(scores):
#     filtered = filter_pass(scores)      # 함수 2 사용
#     total = sum_scores(filtered)        # 함수 3 사용
#     return total


# scores = [30, 67, 88, 55, 92, 40]
# result = sum_pass_scores(scores)
# print("60점 이상 합계:", result)


# 🔹 문제 4
# 문자열 두 개를 받아 하나의 문장으로 이어 붙이는 함수 combine(str1, str2) 작성.

# def combine(str1, str2):
#     # str1 앞뒤 공백 제거
#     i = 0
#     while i < len(str1) and str1[i] == " ":
#         i += 1
#     j = len(str1) - 1
#     while j >= 0 and str1[j] == " ":
#         j -= 1
#     part1 = []
#     for k in range(i, j + 1):
#         part1 += [str1[k]]

#     # str2 앞뒤 공백 제거
#     i = 0
#     while i < len(str2) and str2[i] == " ":
#         i += 1
#     j = len(str2) - 1
#     while j >= 0 and str2[j] == " ":
#         j -= 1
#     part2 = []
#     for k in range(i, j + 1):
#         part2 += [str2[k]]

#     # 두 리스트 합치기 + 띄어쓰기
#     result_list = []
#     for c in part1:
#         result_list += [c]
#     result_list += [" "]
#     for c in part2:
#         result_list += [c]

#     # 리스트 → 문자열 변환
#     result_str = ""
#     for c in result_list:
#         result_str += c

#     return result_str

# # 테스트
# output = combine("   Hello   ", "   World     ")
# print(output)

temp = [95, 104, 113]
# 1. 화씨 → 섭씨 변환
def to_c(f):
    return (f - 32) * 5 // 9  # 정수 계산

# 2. 리스트 길이 구하기
def get_len(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

# 3. 화씨 리스트 → 섭씨 리스트 변환
def convert_list():
    f_list = [95, 104, 113]  # 고정
    c_list = []
    for i in range(get_len(f_list)):   # 함수 2 사용
        c_list += [to_c(f_list[i])]    # 함수 1 사용
    return c_list

# 테스트
celsius_list = convert_list()
print(celsius_list)
