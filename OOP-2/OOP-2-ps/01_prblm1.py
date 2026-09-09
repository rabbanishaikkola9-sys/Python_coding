# 1.Create a Class “Programmer” for storing information of few programmers working at Microsoft. 
class programmer:
    company="Microsoft"
    def __init__(self,name,age,lang):
        self.name=name
        self.age=age
        self.lang=lang
        print(f"Name is {self.name} , the Age is {self.age} and the Language is {self.lang}")
        @staticmethod
        def greet():
            print("Good morning staff")
p1=programmer("Rabbani",30,"python")
p2=programmer("Rehaan",30,"JS")
p3=programmer("Rahul",30,"Kotlin")
