class Employee:
     # class attribute
    age=18 # class attribute
    lang="Python" # class attribute
    sex="Male" # class attribute
rabbani=Employee()
rabbani.name="rabbani"# instance or object attribute
print(rabbani.name,rabbani.age,rabbani.lang,rabbani.sex)
rohan=Employee()
rohan.name="Rohan roro robinson"# instance or object attribute
print(rohan.name,rohan.age,rohan.lang,rohan.sex)
# here the age ,lang, sex are the class atribute as they belong directly to the class employee and the name is the object attribute as it is done by the object made for the class