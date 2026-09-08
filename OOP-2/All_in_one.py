class college():
    college_name="Govt polytechnic Dharmavaram"
    def __init__(s,name,age,gender):
        s.name=name
        s.age=age
        s.gender=gender
    def display(s):
        print(s.name,s.age,s.gender)

# Creating the objects for the class college
student1= college("Rabbani",18,"Male")
student2= college("Ganesh",18,"Male")
student3= college("Bhanoday",18,"Male")
student1.display()
student2.display()
student3.display()