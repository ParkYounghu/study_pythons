kor = [70, 80 ,90, 40, 50]							# 리스트 선언
eng = [90, 80 ,70, 70, 60]
sum1, sum2, sum3, sum4 = 0, 0, 0, 0				    # 누적 변수 초기화

#for 단일 변수 in 리스트:
#    실행문
# score = 70

# for score in kor:									# 국어 점수 출력 및 한계 계산
#    print(score, end=' ')
#    sum1 = score + sum1
#    print("\n국어 총점:", sum1)

# for score in eng:									# 영어 점수 출력 및 한계 계산
#    print(score, end=' ')
#    sum2 += score
#    print("\n영어 총점:", sum2)

# range(5) -> [0, 1, 2, 3, 4]
for index in range(5):								# 인덱스를 이용한 국어 점수 출력 및 합계 계산
    # kor[index] + eng[index]
    sum3 += kor[index] + eng[index]
    print(f'국어와 영어 누적 합 :{sum3}')