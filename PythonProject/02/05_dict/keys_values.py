# 02/05_dict/keys_values.py

# 아이스크림 딕셔너리
icecream = {
    'Tankboy': 1200,
    'Pollapo': 1200,
    'Ppangppare': 1800,
    'Worldcorn': 1500,
    'Melona': 1000,
    'Heathunting': 1200
}

# 1. 딕셔너리의 key만 추출하여 리스트를 생성합니다.
# .keys() 메서드는 dict_keys 객체를 반환하며, 이를 list()로 감싸 리스트로 변환합니다.
dict_keys = list(icecream.keys())

# 2. 딕셔너리의 value만 추출하여 리스트를 생성합니다.
# .values() 메서드는 dict_values 객체를 반환하며, 이를 list()로 감싸 리스트로 변환합니다.
dict_values = list(icecream.values())

# 결과를 출력합니다.
print(f"dict_keys({dict_keys})")
print(f"dict_values({dict_values})")

# 출력 결과 (순서는 Python 버전 및 환경에 따라 다를 수 있음):
# dict_keys(['Tankboy', 'Pollapo', 'Ppangppare', 'Worldcorn', 'Melona', 'Heathunting'])
# dict_values([1200, 1200, 1800, 1500, 1000, 1200])