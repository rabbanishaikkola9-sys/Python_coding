class Employee:
     # class attribute
    age=18 # class attribute
    lang="Python" # class attribute
    sex="Male" # class attribute
rabbani=Employee()
rabbani.name="rabbani"# instance or object attribute
rabbani.lang="JS" # prints the JS bcz the ctrl first checks the instance attribute after that it will go to the class attribute
print(rabbani.name,rabbani.age,rabbani.lang,rabbani.sex)
# Here the output will be the JS not python if JS is absent then the output will be python