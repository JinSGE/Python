milk_orders = {'101': {'milk': 1, 'yogurt': 5},
               '102': {'milk': 2},
               '103': {'milk': 1, 'yogurt': 10},
               '104': {'yogurt': 15}}

# 딕셔너리의 모든 키(호실)를 순서대로 순회.
for room_number in milk_orders.keys():

    # 현재 호실의 주문 내용(값)을 가져옵니다.
    order = milk_orders[room_number]

    # 우유 주문 수량을 확인합니다. (없으면 0으로 간주)
    milk_count = order.get('milk', 0)

    # 우유 수량이 0보다 클 때만 출력.
    if milk_count > 0:
        # 원하는 형식 "101 호 milk : 1개"에 맞춰 출력
        print(f"{room_number} 호 milk : {milk_count}개")

# 출력 결과:
# 101 호 milk : 1개
# 102 호 milk : 2개
# 103 호 milk : 1개