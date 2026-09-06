class Employee:
    language="py" # This is the class attribute
    Gender="male"
    salary=120000
    @staticmethod
    def greeteveryone():
        print("Good morning everyone")

    def getInfo(hey):
        print(f"The language is {hey.language} and the salary is {hey.salary}")
rabbani=Employee()
rabbani.name="Harry" # This is the instance /Object attribute
print(rabbani.name,rabbani.language)
rohan=Employee()
rohan.name="Rohan"
print(rohan.name)
print(rohan.Gender,rohan.language)
# here the name is obj attr nd the salary nd language are class attr as they directly belong to this class
rabbani.getInfo()
rabbani.greeteveryone()