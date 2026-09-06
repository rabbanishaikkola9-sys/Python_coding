class Employee:
    language="py" # This is the class attribute
    Gender="male"
harry=Employee()
harry.name="Harry" # This is the instance /Object attribute
print(harry.name,harry.language)
rohan=Employee()
rohan.name="Rohan"
print(rohan.name)
print(rohan.Gender,rohan.language)
# here the name is obj attr nd the salary nd language are class attr as they directly belong to this class
