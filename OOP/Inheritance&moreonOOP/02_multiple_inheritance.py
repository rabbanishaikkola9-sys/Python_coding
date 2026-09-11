class employee:
    company="ITC"
    name="Rabbani"
    def show(self):
        print(f"The name is {self.name } and the salary is {self.salary}")
# class programmer:
class coder:
    language="Python"
    def printlanguages(self):
        print("Out of all the languages here is your language {self.language}")
class programmer(employee,coder):
    company="ITCinfotech"
    def showlang(self):
        print(f"The name is {self.company} and he is good at {self.language}")
    @staticmethod
    def greet():
        print("hey good morning")
a=employee()
b=programmer()
programmer.greet()
print(a.company)
print(b.company)
b.showlang()
b.printlanguages()