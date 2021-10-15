
import Userinfo
from Price import *

class Theatre:
    def __init__(self,rows,seats):
        self.rows=rows
        self.seats=seats
        self.ticketpurchased=0
        self.ticketpercentage=0
        self.currentincome=0
        self.totalseats=self.rows*seats
        self.totalincome =0
        self.users={}
        self.a = [['S' for i in range(self.rows+1)] for j in range(self.seats-1)]
        if self.totalseats<=60:
            self.totalincome=self.totalseats*10
        else:
            if rows%2:
                self.totalincome=(self.rows//2)*self.seats*10 + (self.rows//2)*self.seats*8
            else:
                r=self.rows//2
                y=self.rows-r
                self.totalincome=r*self.seats*10 + y*self.seats*8

    def Print_Cinema(self):
        m = 0
        b = 0
        print(end="  ")
        for i in range(1,self.seats+1) :
            b = b + 1
            print(b, end=" ")
        print()
        for j in self.a:
            m = m + 1
            print(m, end=" ") 
            print(" ".join(j), sep=",")


    def Buy_Ticket(self):
        try:
            print('Enter the row-seat number ?')
            print('For Example 1-3 = Row 1 and Seat 3')
            r,s=input().split('-')
            self.BookSeat(int(r),int(s))
        except:
            print('No Option For This Seat Sorry.')

    def BookSeat(self,r,s):
        if self.a[r-1][s-1]!='B':
            print('Seat Available! Want to Book ? \n Press "Y" for yes OR Press "N" for no')
            res=input()
            if res.lower()=='y':
                price=Ticekt_Price(r,s,self.totalseats,self.rows)
                print(f'Price for your seat is: {price}$ \n Press "Y" to Continue OR Press "N" for Exit')
                resp=input()
                if resp.lower()=='y':
                    name = input("Enter the Name: ")
                    age = input("Enter the Age: ")
                    gender = input("Enter the Gender: ")
                    phone = input("Enter the Phone NO: ")
                    newobj = Userinfo.User_Info()
                    newobj.add_Details(name,age,gender,phone,price)
                    user=newobj.Create_User((r,s))
                    self.users.update(user)
                    for i in range(len(self.a)) :
                        for j in range(len(self.a[i])):
                            if i==r-1 and j==s-1:
                                self.a[i][j]='B'
                                print(f'Ticket Booked, Your Seat No is {r,s}')
                                self.ticketpurchased=self.ticketpurchased+1
                                self.ticketpercentage=round((self.ticketpurchased/self.totalseats)*100, 2)
                                self.currentincome=self.currentincome+price
                                return
                else:
                    return None
            else:
                return None
        else:
            print('Sorry for Inconvenience Seat Is Already Booked. Kindly Choose Another One')

    def Booked_Ticket_User_Info(self):
        if self.users !={}:
            for i in self.users:
                print('Seat No:''User Details:',self.users[i])
        else:
            print('0 Users Booked Tickets Till Now.')

    def Statistics_Menu(self):
        print('Number of Purchased Tickets : ',self.ticketpurchased)
        print('Percentage of Tickets Booked : ',self.ticketpercentage,'%')
        print('Current Income : ',self.currentincome,'$')
        print('Total Income : ',self.totalincome,'$')
