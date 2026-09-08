class Calculator:
    @staticmethod
    def hello():
        print("Hello there !!! ")
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"The square of the {self.n} is {self.n**2}")
    def cube(self):
        print(f"The cube of the {self.n} is {self.n**3}")
    def squareroot(self):
        print(f"The squareroot of the {self.n} is {self.n**(1/2)}")
a=Calculator(25)
a.hello()
a.square()
a.cube()
a.squareroot()