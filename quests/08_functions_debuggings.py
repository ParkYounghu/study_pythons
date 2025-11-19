# ✅ 문제 1 — return 누락 오류
# 아래 함수는 섭씨 변환 후 값을 반환해야 한다.
#  현재 코드에서 발생하는 오류를 찾고 수정하시오.
# def to_celsius(temp):
#     celsius = (temp - 32) * 5 / 9
#     return celsius          #return 누락

# result = to_celsius(77)
# print(result)

# ✅ 문제 2 — 매개변수 이름 오류
# 아래 프로그램은 실행 시 오류가 발생한다.
#  오류 위치를 찾고 올바르게 수정하시오.
# def convert(temp):
#     return (temp - 3) * 5 / 9   # 오타: temps

# print(convert(95))

# ✅ 문제 3 — 함수 호출 인자 오류
# 아래 코드는 함수 호출이 잘못되어 있다.
#  오류를 설명하고 고치시오.
# def to_celsius(temp):
#     return (temp - 32) * 5 / 9

# temp = 212 # 함수에 들어갈 temp값 고정
# value = to_celsius(temp) # 오류: 함수 호출에 필요한 temp 작성
# print(value)

# ✅ 문제 4 — 타입 오류(TypeError)
# 아래 코드는 문자열을 함수에 전달하여 오류가 발생한다.
#  이 오류가 왜 발생하는지 설명하고 해결하시오.
# def to_celsius(temp):
#     return (temp - 3) * 5 / 9

# print(to_celsius(77))  # 타입 에러 / print(to_celsius(77)) 로 수정

# ✅ 문제 5 — 반복 구조 + 함수 사용 오류
# 아래 코드는 여러 값을 함수로 변환하려 하지만 오류가 발생한다.
#  오류 원인을 찾고 고치시오.(Option : for 문을 함수화)

def to_celsius(temp):
    return (temp - 32) * 5 / 9     # 섭씨 온도 공식 수정 (3 -> 32)

temps = [77, 95, 50]  # for문 대신 리스트 내포 사용

def t(temp):          # temps 를 temp로 수정, for 대신 def를 써서 문자 이용해서 함수화
    result = to_celsius(temp)
    return result
    results.append(result)         # results에 값을 추가
results = [t(temp) for temp in temps]  # 리스트 내포로 함수 호출
print(results)