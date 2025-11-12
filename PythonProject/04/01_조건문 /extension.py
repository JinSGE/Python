# 04_제어구문/02_조건문/extension.py

# 파일 이름 리스트
filenames = ['intra.h', 'intra.c', 'input.txt', 'run.py']

# 1. 리스트 컴프리헨션과 endswith()를 사용하여 확장자 필터링
# endswith()에 튜플을 전달하여 여러 확장자를 한 번에 검사할 수 있습니다.
results = [
    filename for filename in filenames
    if filename.endswith(('.h', '.c'))
]

# 결과 출력
print(results)
# 출력: ['intra.h', 'intra.c']