########################################################################
# #100DaysofCode                                      By Jonathan Rhau #
#                                                                      #
#                       Day 2 - Tip Calculator                         #
#                                                                      #
########################################################################

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the Tip Calculator.\n")

bill = float(input("What was the total bill? "))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100 + 1
n_people = int(input("How many people to split the bill? "))

amount_per_person = bill * tip / n_people

print(f"Each person should pay: ${round(amount_per_person,2):0.2f}\n")
