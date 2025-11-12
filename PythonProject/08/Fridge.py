class Fridge:
    def __init__(self):
        self.isOpened = False
        self.foods = []

    def open(self):
        self.isOpened = True
        print("[INFO] 냉장고 문 열음.")

    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing)
            print(f"[ OK ] 냉장고 속에 {thing} 음식 넣음.")
        else:
            print("[FAIL] 냉장고 문이 닫혀 있음.")

    def close(self):
        self.isOpened = False
        print("[INFO] 냉장고 문을 닫음.")

    def show_foods(self):
        print(f"[INFO] 냉장고 음식 리스트: {self.foods}")


class Food:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
