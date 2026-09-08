class Employee:
     # class attribute
    name="rehaan"
    age=18 # class attribute
    lang="Python" # class attribute
    sex="Male" # class attribute
    def getInfo(str):
        print(f"The lanaguage is {str.lang} and the age is {str.age}")
rabbani=Employee()
# Instance attribute stakes over the the class attribute
rabbani.name="rabbani"# instance or object attribute
rabbani.lang="JS"
rabbani.age=20 # prints the JS bcz the ctrl first checks the instance attribute after that it will go to the class attribute
print(rabbani.name,rabbani.age,rabbani.lang,rabbani.sex)
# Here the output will be the JS not python if JS is absent then the output will be python
print("End of the line ")
rabbani.getInfo()