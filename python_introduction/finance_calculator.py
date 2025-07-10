income = int(input("Enter your monthly income"))
expenses = int(input("Enter your total monthly espenses"))
savings = income - expenses
print("Your monthly savings are $", savings)
annsavings = savings * 12 * 0.05
print("Projected savings after one year, with interest, is: $", annsavings)