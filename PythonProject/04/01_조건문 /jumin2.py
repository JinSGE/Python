# 04_제어구문/02_조건문/jumin2.py

# 1. 사용자로부터 주민등록번호를 입력.
# 예시 입력: 821010-1635210
jumin_input = input("주민등록번호: ")

# 2. 주민등록번호에서 숫자 13자리만 추출.
# 하이픈(-)을 제거하고 숫자로만 구성된 문자열 생성.
# string == 821010-1635210 ==> string == 8210101635210
jumin_number = jumin_input.replace('-', '')

# 유효성 검사를 위한 가중치(Weights) 리스트 생성.
weights = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

# 3. (1차 계산) 앞 12자리와 가중치를 곱하고 모두 더함.
total_sum = 0

# i는 인덱스 (0 ~ 11), weights[i]는 가중치, jumin_number[i]는 주민번호 숫자

for i in range(12):
    # 주민번호 숫자는 문자열이므로, int()로 변환하여 계산.
    digit = int(jumin_number[i])
    total_sum += digit * weights[i]

# 4. (2차 계산) 합산 결과를 11로 나눈 나머지를 구합니다.
remainder = total_sum % 11

# 5. (3차 계산) 11에서 나머지를 뺀 값을 검증 번호로 설정.
# 만약 10이 나오면, 검증 번호는 0이 됩니다.
verification_number = 11 - remainder

# 결과가 10 이상이면, 10의 자리는 버리고 1의 자리만 취합니다.
if verification_number >= 10:
    verification_number = verification_number % 10 # 10 -> 0, 11 -> 1 등

# 6. 최종 검증: 계산된 검증 번호와 주민등록번호의 마지막 자리(13번째 자리)를 비교.
# 주민등록번호의 마지막 자리(검증 번호) 추출
last_digit = int(jumin_number[12])

# 최종 판정
if verification_number == last_digit:
    result_message = "유효하다"
else:
    result_message = "유효하지 않다"

# 7. 결과 출력
print(f"유효성 검사 결과: {result_message}")

# 예시 입력: 821010-1635210
# 예시 출력: 유효하지 않다.
# (total_sum=128, remainder=7, verification_number=4, last_digit=0 이므로 불일치)