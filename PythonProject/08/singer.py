# class Singer:
#
#     eyes = 2
#
#     def sing(self):
#         print("lalala~")
#         self.eyes = 3
#
# teaji = Singer()
# print(teaji.eyes)
# teaji.sing()
#
# ricky = Singer()
# print(ricky.eyes)
# ricky.sing()

class Person:

    eyes = 2
    nose = 1

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print(f"내 이름은 {self.name}")
        print(f"내 나이는 {self.age}")
        print(f"내 눈은 {self.eyes}개")
        print(f"내 코는 {self.nose}개")

p1 = Person("JOHN", 25)
# p1.age = 30
# print(p1.age)
p1.myfunc()