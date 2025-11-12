# 04_제어구문/02_조건문/grade.py

# 등급표: A: 81-100, B: 61-80, C: 41-60, D: 21-40, E: 0-20

# 1. 사용자로부터 점수를 입력받습니다.
# 입력 예: 83
score = int(input("score: "))

# 2. 점수에 따라 등급을 결정합니다 (내림차순으로 조건 검사).
if score >= 81:
    grade = 'A'
elif score >= 61:
    grade = 'B'
elif score >= 41:
    grade = 'C'
elif score >= 21:
    grade = 'D'
else: # 0-20 점
    grade = 'E'

# 등급 출력
print(f"grade is {grade}")
# 입력 83일 경우 출력: grade is A