# 커피 자판기 프로그램 (class 미사용)

coffee_price = 300  # 커피 한 잔 가격
coffee_stock = 5  # 초기 커피 개수

print("========================")
print("==== 커피 자판기 시작 ====")
print("========================")
print("커피 한 잔은 300원입니다. (현재 커피: 5개)\n")

while True:
    # 머신 상태 출력
    print(f"[ INFO ] [머신 상태] 남은 커피 개수 : {coffee_stock}개")

    # 커피 재고 확인
    if coffee_stock == 0:
        print("[ FAIL ] 커피가 모두 소진되었습니다. 자판기 종료")
        break

    # 사용자 입력
    money = int(input("돈을 넣어주세요: "))
    coffee = int(input("원하는 커피 개수를 입력: "))

    total_price = coffee * coffee_price

    # 돈 부족한 경우
    if money < total_price:
        print("[ INFO ] 돈이 부족합니다. 커피 한 잔은 300원입니다.")
        print("[ INFO ] 커피 0개, 거스름돈:", money, "원 반환\n")
        # 계속 동작 (고장 아님)
        continue

    # 커피 재고 부족한 경우
    if coffee > coffee_stock:
        print("[ FAIL ] 커피가 부족합니다. 현재 남은 커피:", coffee_stock, "개입니다.")
        print("[ FAIL ] 자판기가 고장났습니다. 종료합니다.\n")
        break

    # 정상 거래 처리
    change = money - total_price
    coffee_stock -= coffee

    print("[  OK  ] 커피", coffee, "개를 드립니다.")
    print("[  OK  ] 거스름돈:", change, "원")
    print("[ INFO ] 남은 커피:", coffee_stock, "개\n")

print("=====================")
print("=== 프로그램 종료 ===")
print("=====================")