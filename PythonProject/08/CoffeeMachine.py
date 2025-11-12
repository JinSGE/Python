import sys
import subprocess

# --- tkinter 설치 확인 및 자동 설치 ---
try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    print("tkinter 모듈이 없습니다. 설치를 시도합니다...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "tk"])
    import tkinter as tk
    from tkinter import messagebox


# ---------------------- Coffee 클래스 ----------------------
class Coffee:
    def __init__(self):
        # 자판기 기본 속성
        self.total_amount = 10             # 커피 개수
        self.total_amount_price = 5000     # 자판기 보유 금액
        self.coffee_price = 300            # 커피 한 잔 가격

        # 사용자 입력 관련 속성
        self.put_price = 0
        self.req_coffee_nums = 0

        # 결과 관련 속성
        self.remaining_price = 0
        self.remaining_coffee_nums = 0

    # 사용자 입력 요청
    def request(self, put_price, req_coffee_nums):
        self.put_price = put_price
        self.req_coffee_nums = req_coffee_nums
        return self.get(self.put_price, self.req_coffee_nums)

    # 커피 제공 로직
    def get(self, put_price, req_coffee_nums):
        total_cost = self.coffee_price * req_coffee_nums

        # 재고 부족
        if req_coffee_nums > self.total_amount:
            return "❌ 커피 재고가 부족합니다."

        # 돈이 충분한 경우
        if put_price >= total_cost:
            self.remaining_price = put_price - total_cost
            self.total_amount -= req_coffee_nums
            self.total_amount_price += total_cost
            msg = f"☕ 커피 {req_coffee_nums}개 나왔습니다!\n거스름돈: {self.remaining_price}원"
        else:
            # 돈이 불충분한 경우
            affordable_coffee = put_price // self.coffee_price

            if affordable_coffee == 0:
                self.remaining_price = put_price
                msg = f"❌ 돈이 부족합니다. {self.remaining_price}원을 돌려드립니다."
            else:
                spent = affordable_coffee * self.coffee_price
                self.remaining_price = put_price - spent
                self.total_amount -= affordable_coffee
                self.total_amount_price += spent
                msg = f"☕ 돈이 부족하여 {affordable_coffee}개만 드립니다.\n거스름돈: {self.remaining_price}원"

        return msg

    # 자판기 정보 출력
    def info(self):
        return f"자판기 남은 커피: {self.total_amount}개\n자판기 남은 금액: {self.total_amount_price}원"

    # 상태 점검
    def check_amount(self):
        if self.total_amount <= 0:
            return "⚠️ 커피 재고가 없습니다."
        if self.total_amount_price <= 0:
            return "⚠️ 자판기 금액이 부족합니다."
        return "✅ 정상 작동 중입니다."


# ---------------------- Tkinter GUI ----------------------
class CoffeeMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("☕ 커피 자판기 프로그램")
        self.root.geometry("400x400")

        self.machine = Coffee()

        # 제목
        tk.Label(root, text="커피 자판기", font=("Arial", 18, "bold")).pack(pady=10)

        # 돈 입력
        tk.Label(root, text="넣을 금액:").pack()
        self.money_entry = tk.Entry(root)
        self.money_entry.pack()

        # 커피 개수 입력
        tk.Label(root, text="원하는 커피 개수:").pack()
        self.num_entry = tk.Entry(root)
        self.num_entry.pack()

        # 버튼
        tk.Button(root, text="커피 요청", command=self.request_coffee, bg="#6fa8dc").pack(pady=10)
        tk.Button(root, text="자판기 정보 보기", command=self.show_info, bg="#f6b26b").pack(pady=5)
        tk.Button(root, text="자판기 상태 점검", command=self.check_machine, bg="#93c47d").pack(pady=5)

        # 결과 표시
        self.result_label = tk.Label(root, text="", fg="blue", font=("Arial", 12))
        self.result_label.pack(pady=20)

    def request_coffee(self):
        try:
            put_price = int(self.money_entry.get())
            req_nums = int(self.num_entry.get())
            result = self.machine.request(put_price, req_nums)
            self.result_label.config(text=result)
        except ValueError:
            messagebox.showerror("입력 오류", "숫자만 입력해주세요.")

    def show_info(self):
        info = self.machine.info()
        messagebox.showinfo("자판기 정보", info)

    def check_machine(self):
        status = self.machine.check_amount()
        messagebox.showinfo("자판기 점검", status)


# 프로그램 실행
if __name__ == "__main__":
    root = tk.Tk()
    app = CoffeeMachineApp(root)
    root.mainloop()
