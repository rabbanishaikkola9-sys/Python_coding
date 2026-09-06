class programmer:
    company="Microsoft"
    def __init__(s,name,age,lang,sex):
        s.name=name
        s.age=age
        s.lang=lang
        s.sex=sex
    def display(s):
        print(s.name,s.age,s.lang,s.sex)
prgmr1=programmer("Rabbani",21,"Python","Male")
prgmr2=programmer("Rehaan",21,"C","Male")
prgmr3=programmer("Rahul",21,"JS","Male")
prgmr1.display()
prgmr2.display()
prgmr3.display()