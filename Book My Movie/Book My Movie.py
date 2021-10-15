from Price import *
import CinemaHall



print('Lets Start With Creating The Sitting Space For The Cinema Hall')
try:
    rows = int(input("Enter the number of rows:"))
    seats = int(input("Enter the number of seats per row:"))
    sc=CinemaHall.Theatre(rows,seats)
except:
    print('Please Provide Number As Input')
    exit()


print('WELCOME TO THE SHARON K Theatre!!')
print('Which Movie Do You Want To Watch ?\n Enter Movie Name :-')
s=input()
print('Auditorium 1 Available For',s.upper(),'Kindly Book Your Seat ')

def Menu():
    print('1: Show the Seats')
    print('2: Buy a Ticket')
    print('3: Show Statistics')
    print('4: Show Booked Ticket User Info')
    print('0: Exit')
    print('----------')
    print('Enter Your Choice ?')
    choice=input()
    if choice=='1':
        sc.Print_Cinema()
        Menu()
    elif choice=='2':
        sc.Buy_Ticket()
        Menu()
    elif choice=='3':
        sc.Statistics_Menu()
        Menu()
    elif choice=='4':
        sc.Booked_Ticket_User_Info()
        Menu()
    elif choice=='0':
        print('Thank You For Visiting Sharon K Cinemas | We Love To Have You Again.')
        exit()
    else:
        print('Kindly Choose From the Given Options.')
        Menu()

Menu()
