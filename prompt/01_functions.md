너는 코딩을 마스터한 20년차 베테랑 개발자야. 내가 지금 json 형식으로 코딩 문제를 줄건데, 이거를 visual studio code 에 py 파일로 넣을 수 있는 형식으로 문제를 풀이해줘



{

  "problem_info": {

    "title": "리스트를 이용한 사칙연산 함수 구현",

    "description": "두 개의 숫자 리스트를 이용해 사칙연산(+, -, *, /)을 수행하는 함수를 구현하시오.",

    "level": "Basic",

    "language": "Python"

  },

  "requirements": [

    "테스트 데이터는 리스트(list)로만 제공될 것",

    "테스트 데이터 개수는 총 10개",

    "변수명은 소문자 + 언더바(_) 조합(snake_case)을 사용할 것",

    "함수는 두 숫자를 입력받아 덧셈, 뺄셈, 곱셈, 나눗셈 결과를 튜플 등으로 모두 반환할 것",

    "0으로 나누는 경우 결과값으로 'division_error' 문자열을 반환할 것"

  ],

  "code_template": "def calculate_all(num1, num2):\n    # 여기에 사칙연산 구현\n    # return (덧셈, 뺄셈, 곱셈, 나눗셈)\n    pass\n\n\n# 테스트 리스트 (10개)\ntest_a = [10, 25, 40, 12, 7, 9, 16, 100, 3, 81]\ntest_b = [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]\n\n# 테스트 실행\nfor i in range(10):\n    a = test_a[i]\n    b = test_b[i]\n    result = calculate_all(a, b)\n    print(f\"{a}, {b} => {result}\")",

  "test_dataset": {

    "input_a": [10, 25, 40, 12, 7, 9, 16, 100, 3, 81],

    "input_b": [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]

  },

  "expected_behavior": {

    "return_format": "(add, sub, mul, div)",

    "exception_handling": {

      "condition": "denominator == 0",

      "return_value": "division_error"

    }

  }

}