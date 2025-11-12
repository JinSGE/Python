class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        print('[INFO] 오브젝트가 생성되었습니다.')

    def printname(self):
        print(f"{self.firstname}, {self.lastname}")

class Student(Person):
    def __init__(self, fname, lname,year):
        # Person.__init__(self, fname, lname)
        super().__init__(fname, lname)
        self.graduationyear = year

    def say(self):
        print('yeah~')

# x = Person("SungEun", "Jin") # 오브젝트 1
y = Student(fname="Jin", lname="Mr", year=2025) # 오브젝트 2
print('*'*10)
y.printname()
print(y.graduationyear)
y.say()