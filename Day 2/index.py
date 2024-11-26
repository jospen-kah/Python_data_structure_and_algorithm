from datetime import datetime

# Making use of strings

#first_name = input( "Enter Your First name: ")
#second_name = input("Enter Your Second name: ")
#last_name = input("Enter Your Last name: ")

""" Displaying all the names as one full name"""
#print(f"Your full name is {first_name} {second_name} {last_name} ")

# Determing your age in Days
yob = int(input("enter your age in the format YYYY: "))

current_year  = datetime.now().year
num_years = current_year - yob

years_in_days = num_years * 365 
print(f"A person born in the {yob} is {years_in_days}days old")
