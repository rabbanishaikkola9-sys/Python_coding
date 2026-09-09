class employee:
    company="ITC"
    def show(self):
        print(f"The name is {self.name } and the salary is {self.salary}")
class programmer:
    company="ITCinfotech"
    def show(self):
        print(f"The name is {self.name } and the salary is {self.salary}")
    def showlang(self):
        print(f"The name is {self.name } and he is good at {self.lang}")
a=employee()
b=programmer()
print(a.company)
print(b.company)