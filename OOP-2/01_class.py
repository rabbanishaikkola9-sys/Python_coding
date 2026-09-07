class Employee:
     # class attribute
    age=18 # class attribute
    lang="Python" # class attribute
    sex="Male" # class attribute
obj1=Employee()
obj1.name="rabbani"# instance or object attribute
print(obj1.name,obj1.age,obj1.lang,obj1.sex)
obj2=Employee()
obj2.name="rohan"# instance or object attribute
print(obj2.name,obj2.age,obj2.lang,obj2.sex)
# here the age ,lang, sex are the class atribute as they belong directly to the class employee and the name is the object attribute as it is done by the object 