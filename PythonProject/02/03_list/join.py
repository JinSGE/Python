# 02/03_list/join.py

# 종목 코드 리스트
items = ['000600', '034560', '003540', '039490']

# 1. 구분자(Delimiter)인 세미콜론을 지정합니다.
separator = ':'

# 2. join() 메서드를 사용하여 리스트 요소를 구분자로 연결합니다.
result_string = separator.join(items)

# 결과를 출력합니다.
print(result_string)

# 출력 결과:
# 000600:034560:003540:039490