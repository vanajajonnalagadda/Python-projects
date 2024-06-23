import random
from datetime import datetime


v="""
1.User details
2.source and destination station
3.Train number and seats availability
4.Price
5.Book ticket and PNR (Passenger Name Record) generate
6.Generate bill
7.Exit
"""

users = {"Vanaja":123,"Anusri":456}
User_details = []
# Store booking details with PNR numbers
bookings={}

trains={
      ("Rjy","Vizag"):   {"Konark":{"number":11019, "seats_available":39,"price":120},
                       "Falaknuma":{"number":12704, "seats_available":57,"price":200},
                       "Ratnachal":{"number":12718, "seats_available":104,"price":350}},

      ("Vizag","Hyd"):   {"Duronto":{"number":22203, "seats_available":72,"price":400},
                       "East_coast":{"number":18645, "seats_available":0,"price":300},
                         "Godavari":{"number":12727, "seats_available":50,"price":450}}
   } 
               
Source=" " 
Destination=" "


def user_authentication():
   user = input("Enter your name: ")

   if user in users.keys():
      password=input("Enter the password: ")

      if password != str(users[user]):
         print("invalid password!")
         return False
      else:
         return True
      
   else:
      print("User not found!")
      return False
   



def generate_pnr():
# Generating a unique PNR number
   return f"PNR{random.randint(100000, 999999)}"


def book_ticket_and_generate_pnr():
   global Source, Destination
   if not Source or not Destination:
      print("Please enter source and destination stations first.")
      return
   else:
      train_name=input("Enter the train name: ")
      print(" ") 
      if (Source,Destination)  in trains:
         if train_name in trains[(Source, Destination)]:
            NumSeats = int(input("Enter the number of seats you want to book: "))
            if NumSeats <= trains[(Source, Destination)][train_name ]["seats_available"]:
               trains[(Source, Destination)][train_name]["seats_available"] -= NumSeats
               pnr = generate_pnr()
               now = datetime.now() 
               bookings[pnr] = {
                  "Route":(Source, Destination),
                  "Train": train_name,
                  "Num_seats": NumSeats,
                  "Price": trains[(Source, Destination)][train_name]["price"] * NumSeats,
                  "Date": now.strftime("%Y-%m-%d"),
                  "Time": now.strftime("%H:%M:%S"),
                  "Day": now.strftime("%A"),
                }
               print(f"Successfully booked {NumSeats} seats on {train_name}.")
               print(" ")
               print(f"Remaining seats: {trains[(Source, Destination)][train_name]['seats_available']}")
               print(" ")
               print(f"Your PNR is {pnr}. Please keep it for future reference.")
               print(" ")
                     
            else:
               print(f"Sorry, only {trains[(Source, Destination)][train_name]['seats_available']} seats are available!")
         else:
            print(f"No train named {train_name} is available for the specified route.")
      else: 
            print("No such trains available for the specified route.")
            print(" ")


def generate_bill():
   if not bookings:
      print("No bookings available to generate a bill.")
      return
    
   
   now = datetime.now()
   current_date = now.strftime("%Y-%m-%d")
   current_time = now.strftime("%H:%M:%S")
   current_day = now.strftime("%A")
   print(" ")
   print(20*"=", "Welcome to Railway Reservation Portal" , 21*"=")
   print(80*"=")
   print(f"{current_date}  {current_time}  {current_day}".rjust(75))
   print(80*"-")
   total_price = 0
   for pnr, details in bookings.items():
      print(f"\nPNR: {pnr}")
      print(f"Route: {details['Route'][0]} ---> {details['Route'][1]}")
      print(f"Train Name: {details['Train']}")
      print(f"Number of Seats: {details['Num_seats']}")
      print(f"Price per Ticket: {details['Price'] / details['Num_seats']}")
      print(f"Total Price: {details['Price']}")

      total_price += details['Price']
      print(80*"-")
    
   print(f"\nGrand Total: {total_price}\n")
   print(80*"-")
   print(33*"-","Happy Journey", 32*"-")
      


def main_menu():
   global Source, Destination
   print(v)
   while True:
      option = int(input("Enter the option: "))

      if option==1:
         Gen=["Male","Female","Other"]
         Gender=(input("Enter your gender: "))
               
         if Gender not in Gen:
            print("you entered wrong!" ) 
         else:
            Age=int(input("Enter your age: "))
            Email_address=(input("Enter your Email_address: "))
            Contact_No=int(input("Enter your Contact_No: "))

            s=[Age,Gender,Email_address,Contact_No]
            User_details.append(s)
            print("User details saved successfully!")
            print(" ")
            

      elif option==2:
         Source=input("Enter your source station: ")
         Destination=input ("Enter your destination station: ")
         print(f"Source and destination set to {Source} ---> {Destination}")
         
         print(" ") 
         print("Available trains:")
         print(" ")

         if (Source, Destination) in trains:
            print(trains[(Source, Destination)])
            print(" ")
         else:
            print("No trains available")
            print(" ")
               


      elif option==3:
         train_name=(input("Enter the train name: "))
         print(" ")
         if not Source or not Destination:
            print("Please enter source and destination stations first.")
            print(" ")
         else:
            print("Available Trains and Seats: ")
            print(" ")

         if (Source, Destination) in trains and train_name in trains[(Source, Destination)]:
            details=trains[(Source, Destination)][train_name]
               
            print(f"Train:{train_name}\nTrain_number:{details['number']}\nSeats_availability:{details['seats_available']}")
            print(" ")
         else:
            print("No such trains available for the specified route.")
            print(" ")
               



      elif option==4:
         train_name=input("Enter the train name:  ")
         print(" ") 
               
         if not Source or not Destination:
            print("Please enter source and destination stations first.")
         else:
            print("Available trains and prices. ") 
            print(" ") 


               
            if (Source,Destination)  in trains:
               if train_name in trains[(Source, Destination)]:
                  details=trains[(Source, Destination)][train_name]
                  print(f"Train: {train_name}\nTrain Number: {details['number']}\nPrice: {details['price']}")
                  print(" ")
               else: 
                  print(f"No train named {train_name} is available for the specified route.")
                  print(" ")
            else: 
               print("No such trains available for the specified route.")
               print(" ")
               



      elif option==5:
         book_ticket_and_generate_pnr()
         print(" ")

      elif option == 6:
         generate_bill()  
         print(" ")

      elif option==7:
         break

      else:
         print("Invalid option! Please try again.")


   # Authenticate user
if user_authentication():
   # Start main menu loop
   main_menu()  
else:
   print("Authentication failed!")




