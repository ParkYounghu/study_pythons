# ✅ 중급 난이도 문제 1 — 문자열과 f-string 활용
# second 문자열에 "Python"이 포함되어 있는지 확인하고,
#  "Welcome!"과 합쳐서 출력하는 코드를 작성하시오.
# 조건: f-string 사용


# 출력 예시: "Welcome! Python is fun"

# first = "Python is fun"
# second = "Python"
# # # 여기에 코드 작성


# if second in first:
#     print(f"Welcome! {first}")

# ✅ 중급 난이도 문제 2 — while 반복문 응용
# first 변수가 5부터 1까지 감소하도록 while문을 작성하고,
#  first == 2일 때만 "special"을 출력하도록 코드를 작성하시오.
# first = 5
# # 여기에 코드 작성


# while first >= 1:
#     print(f"while 값 : {first}")
#     if first == 2:
#         print("special, break 실행")
#         break
#     first -= 1
# print("while 종료")


# ✅ 중급 난이도 문제 3 — 리스트 합계 및 평균 계산
# kor와 eng 리스트가 주어졌을 때,
# 각 학생 점수의 총합을 total_scores 리스트로 저장


# 각 학생 점수 평균을 avg_scores 리스트로 저장


# kor = [70, 80, 90, 40, 50]
# eng = [90, 80, 70, 70, 60]

# # 여기에 코드 작성

# kor = [70, 80, 90, 40, 50]
# eng = [90, 80, 70, 70, 60]

# total_scores = []
# avg_scores = []

# for k, e in zip(kor, eng):
#     total = k + e
#     total_scores.append(total)
#     avg_scores.append(total / 2)

# print(f"total_scores = {total_scores}")
# print(f"avg_scores = {avg_scores}")


# kor 리스트에서 60점 이상인 점수만 누적 합계를 계산하고 출력하시오.
# 조건: for문 사용, 60점 미만은 제외


kor = [70, 80, 90, 40, 50]

# 여기에 코드 작성
# 출력 예시: 누적합 = 240

sum4 = 0

for score in kor :
    if score >= 60:
        sum4 = score + sum4
누적합 = sum4

print(f"누적합: {누적합}")


