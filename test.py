# print("Enter the amount of money between 0 to 99: ")
# total_price = int(input())
# while total_price < 0 or total_price > 99:
#   print("Invalid input, please enter again: ")
#   total_price = int(input())

# quarters = int(total_price / 25)
# dims = int((total_price % 25) / 10)
# nickels = int((total_price % 25) % 10 / 5)
# cents = int((total_price % 25) % 10 % 5)
# print("quaters: ",quarters)
# print("dims: ", dims)
# print("nickels: ", nickels)
# print("cents: ", cents)
_______________________________________________________________________
#print("Enter the price of the item: ")
#price = float(input())

#print("Enter the wight of the item in kilograms and grams separately: ")
#print("kg: ")
#kg = int(input())
#print("grams: ")
#grams = int(input())

# weight = grams + (kg * 1000)

# price_per_gram = price / weight 

# print("The price per gram is: $", round(price_per_gram, 2))
____________________________________________________________________________________________________
# projects = ["Data Science", "Quality Assurance", "Software Testing", "Big Data"]
# investment_amount = []
# investment_sum = 0 

# for project in projects:
#   print("Enter the amount invested in ", project, "project: ")
#   amount = float(input())
#   investment_amount.append(amount)
#   investment_sum += amount



# print("Project" + " " * 10 + "Percentage")
# for project in projects:
#   print(project + " " * 10 + str(round(investment_amount[projects.index(project)] / investment_sum * 100, 2)) + "%")

# print("Total amount invested: $", investment_sum)
# print("Average amount invested: $", (investment_sum / len(projects)))


_______________________________________________________________
print("Enter number of miles: ")
miles = int(input())
print("Enter the number of yards: ")
yards = int(input())
print("Enter the number of feet: ")
feet = int(input())
print("Enter the number of inches: ")
inches = int(input())

total_inches = inches + feet * 12 + yards * 36 + miles * 63360
total_meters = total_inches / 39.37

kilometers = int((total_meters / 1000))
meters = int((total_meters % 1000))
centimeters = round(((total_meters * 100) % 100), 2)

print("Metric length: ")
print(kilometers, " Kilometers")
print(meters, " Meters")
print(centimeters, " Centimeters")





    
    



  



