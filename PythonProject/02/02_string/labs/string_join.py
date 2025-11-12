# 02/02_string/labs/string_join.py

# 회사 이름이 저장된 리스트
companies = ['NAVER', 'KAKAO', 'SK', 'SAMSUNG']

# 1. 구분자 ';'를 사용하여 리스트의 요소들을 하나의 문자열로 합칩니다.
# join() 메서드는 '구분자'.join(리스트) 형태로 사용합니다.
separator = ';'
companystring = separator.join(companies)

# 2. 요구 사항에 맞게 결과 문자열을 출력합니다.
print(companystring)

# 출력 결과:
# NAVER;KAKAO;SK;SAMSUNG