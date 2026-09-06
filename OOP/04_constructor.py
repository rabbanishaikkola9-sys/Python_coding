class Employee:
    language="py" # This is the class attribute
    Gender="male"
    salary=120000
    def __init__(self,name,salary,language): # dunder method which is automatically called 
        print("I am creating an object")
        self.name=name
        self.salary=salary
        self.language=language
    @staticmethod
    def greeteveryone():
        print("Good morning everyone")

    def getInfo(hey):
        print(f"The language is {hey.language} and the salary is {hey.salary}")
rabbani=Employee("rabbani",120000,"python")
rohan=Employee()
print(rabbani.language ,rabbani.salary)