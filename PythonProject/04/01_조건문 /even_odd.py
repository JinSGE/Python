# 04_제어구문/01_조건문/even_odd.py

# 1. 사용자로부터 두 개의 숫자를 입력받습니다.
# 입력 예: 10, 7
input_1 = int(input("입력 1: "))
input_2 = int(input("입력 2: "))

# 2. 두 숫자 중 큰 숫자를 찾습니다.
if input_1 >= input_2:
    larger_number = input_1
else:
    larger_number = input_2

# 큰 수 출력
print(f"큰 수: {larger_number}")

# 3. 큰 숫자가 홀수(odd)인지 짝수(even)인지 판별합니다.
# 숫자를 2로 나눈 나머지(%)가 0이면 짝수, 1이면 홀수입니다.
if larger_number % 2 == 0:
    odd_even = "even number"
else:
    odd_even = "odd number"

# 홀짝 결과 출력
print(f"홀짝수: {odd_even}")

# 입력 1: 10, 입력 2: 7 일 경우 출력:
# 큰 수: 10
# 홀짝수: even number