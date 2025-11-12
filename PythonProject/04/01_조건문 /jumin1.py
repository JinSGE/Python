# 04_제어구문/01_조건문/jumin.py

# 1. 사용자로부터 주민등록번호를 입력받습니다.
# 예시 입력: 821010-165210
jumin_number = input("주민등록번호: ")

# 2. 성별 코드와 지역 코드 추출
# 성별 코드(G)는 뒤 7자리 중 첫 번째 (인덱스 7).
gender_code = int(jumin_number[7])

# 지역 코드(ZZ)는 뒤 7자리 중 두 번째와 세 번째 (인덱스 8~9).
region_code = int(jumin_number[8:10])

# --- 성별 분석 ---
if gender_code == 1 or gender_code == 3:
    gender = '남자'
elif gender_code == 2 or gender_code == 4:
    gender = '여자'
else:
    # 5~8 등 다른 번호가 들어올 경우 처리 (예: 외국인 등록번호)
    gender = '알 수 없음'

print(f"성별: {gender}")

# --- 출생지 (지역 코드) 분석 ---
region = ""

if 0 <= region_code <= 8:
    region = '서울'
elif 9 <= region_code <= 12:
    region = '부산'
elif 13 <= region_code <= 15:
    region = '인천'
elif 16 <= region_code <= 25:
    region = '경기도'
elif 26 <= region_code <= 34:
    region = '강원도'
elif 35 <= region_code <= 39:
    region = '충청북도'
elif region_code == 40:
    region = '대전광역시'
elif 41 <= region_code <= 47:
    region = '충청남도'
elif 48 <= region_code <= 55:
    # 주어진 예시 (165210)의 지역 코드(65)와 일치하는 부분은 48~55가 아니라 56~64(전라북도), 65~66(광주) 등
    # 문제 이미지의 표와 '참고' 코드의 지역 범위를 따릅니다.
    # 이미지의 '참고' 코드에 따라 48~55는 '전라북도'로 가정합니다.
    region = '전라북도'
elif 56 <= region_code <= 64:
    region = '전라남도'
elif region_code == 65 or region_code == 66:
    region = '광주광역시'
elif 67 <= region_code <= 69:
    region = '대구광역시'
elif 70 <= region_code <= 80:
    region = '경상북도'
elif 81 <= region_code <= 99:
    # 81~99 중 85는 별도 처리 (85는 울산광역시)
    if region_code == 85:
        region = '울산광역시'
    else:
        region = '경상남도'
else:
    # 85(울산)를 제외한 81~99가 경상남도, 05가 울산광역시로 분리되는 표 기준
    # 이미지의 '참고' 코드에 따라 최종 else 처리
    region = '출생지: 외국인!' # 또는 '알 수 없음'

print(f"지역: {region}")

# 예시 입력 821010-165210 (성별 코드: 1, 지역 코드: 65)
# 출력:
# 성별: 남자
# 지역: 광주광역시