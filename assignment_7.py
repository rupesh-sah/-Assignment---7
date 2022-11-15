'''            Assignment - 7 Full Stack Web Development using Python MySirG
                      
                      Match Case '''
# (Q.1)Write a python script to display the number of days in a given month number.

print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month_name = input("Input the name of Month: ")

if month_name == "February":
	print("No. of days: 28/29 days")
elif month_name in ("April", "June", "September", "November"):
	print("No. of days: 30 days")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
	print("No. of days: 31 day")
else:
	print("Wrong month name") 

''' (Q.2) Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division'''

#Addition
add = 5 + 2
print ("Addition: %d" %add)
 
#Subtraction
sub = 5 - 2
print ("Subtraction: %d" %sub)
 
#Multiplication
mul = 5 * 2
print ("Multiplication: %d" %mul)
 
#Division
div = 5 / 2
print ("Division: %.2f" %div)
	

'''(Q.3) Write a menu driven program with the following options:
  a. Check whether a given set of three numbers are lengths of an isosceles
    triangle or not
  b. Check whether a given set of three numbers are lengths of sides of a right
    angled triangle or not
  c. Check whether a given set of three numbers are equilateral triangle or not
  d. Exit.'''

print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
	print("Equilateral triangle")
elif x==y or y==z or z==x:
	print("isosceles triangle")
else:
	print("Scalene triangle")

'''(Q.4) Write a program which takes user’s age and display the category of person. Age
below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen.'''

age = int(input("Please enter your age:"))
if age <= 10:
	print('You are kids')
elif age >= 10 and age <= 20:
	print('you are Teen')
elif age >= 20 and age <= 40:
	print('you are young')
else:
	print('Senior Citizen')

'''(Q.5) 5. Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number.'''

num1 = int(input("Enter The Number "))

if (num1 % 2) == 0:
  print("Saurabh Shukla is Even".format(num1))
elif (num1 < 0):
    print(" Prateek Jain is negative odd".format(num1))
else:
  print("Aditya Choudhary is Odd".format(num1))

'''(Q.6)Write a python program to check whether a given string is a multiword string or single
word string using match case statement'''
'''(Q.7) Write a python program to check whether a given number is positive, negative or
zero using match case statement'''

num = float(input("Input a number: "))
if num > 0:
   print("It is positive number")
elif num == 0:
   print("It is Zero")
else:
   print("It is a negative number")

'''(Q.8) Write a python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement'''

''' (Q.9) Write a python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year'''
   
# User enters the year
year = int(input("Enter Year: "))

# Leap Year Check
if year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")
elif year % 400 ==0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

'''(Q.10). Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday'''

print("List of colour: Yellow, Blue, Orange, Black, Red, All other colours ")
colour_name = input("Input the name of colour name: ")

if colour_name == "Yellow":
	print("Yellow - Monday")
elif colour_name == "Blue":
	print("Blue - Tuesday")
elif colour_name == "Orange":
	print("Orange - Wednesday")
elif colour_name == "White":
	print("White - Thursday")
elif colour_name == "Black":
	print("Black - Friday")
elif colour_name == "Red":
	print("Red - Saturday")
else:
	print("All other colours - Sunday") 


    