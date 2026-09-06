# .Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways. 
from random import randint
class Train:
    def __init__(self,TrainNo):
        self.TrainNo=TrainNo
    def book(self,fro,to):
        print(f"Ticket is booked {self.TrainNo} from {fro} to {to}")
    def getstatus(self):
         print(f"The train {self.TrainNo} has been delayed for 2 hours please bear some delay and sorry for inconvinience")
    def getfare(self,fro,to):
        print(f"The price is {randint(30,100)} from {fro} to {to}")

t=Train(17215)
t.book("Anantapur","Dharmavaram")
t.getstatus()
t.getfare("Anantapur","Dharmavaram")
