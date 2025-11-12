# 02/02_string/labs/resolution_split.py

# 영상 해상도 문자열 할당
my_resolution = '1920x1080'

# 1. 문자열을 'x' 문자를 기준으로 분리합니다.
# split() 메서드는 결과를 요소로 갖는 리스트를 반환합니다.
# ['1920', '1080']
resolution_parts = my_resolution.split('x')

# 2. 리스트에서 너비(width)와 높이(height)를 추출합니다.
# 리스트의 첫 번째 요소 (인덱스 0)는 너비입니다.
width_str = resolution_parts[0]
# 리스트의 두 번째 요소 (인덱스 1)는 높이입니다.
height_str = resolution_parts[1]

# 3. 추출한 너비와 높이를 요구 사항에 맞게 출력합니다.
# 원래 문자열이지만, 숫자로 인식될 수 있도록 변수 이름을 지정했습니다.
print(f"width  = {width_str}")
print(f"height = {height_str}")

# 출력 결과:
# width = 1920
# height = 1080