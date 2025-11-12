from Fridge import Fridge, Food

# 객체 생성
f = Fridge()
apple = Food("사과")
banana = Food("바나나")
orange = Food("오렌지")

# 냉장고 사용
f.open() # 문 열기
f.put(apple) # 사과 넣기
f.put(banana) # 바나나 넣기
f.put(orange) # 오렌지 넣기
f.close() # 문 닫기
f.show_foods() # 냉장고 음식 리스트
