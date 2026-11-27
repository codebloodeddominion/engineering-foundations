# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# height = float(input("Enter your height in metres: "))

# print("\nYOUR INFORMATION")
# print(f"Name: {name}")
# print(f"Age: {age}")
# print(f"Height: {height} metres")

# print("\nDATA TYPES")
# print(type(name))
# print(type(age))
# print(type(height))

student_name = input("Enter your full name: ")
university = input(("Enter your University name: "))
total_allowance = int(input("Enter your total allowance: "))
food_expenses = int(input("Enter your total food expense: "))
transport_expenses = int(input("Enter your total transport expense: "))

total_expenses = food_expenses + transport_expenses
remaining_allowance = total_allowance - total_expenses

print(f"\n{'=' * 55}")
print(f"       EXPENSE REPORT FOR {student_name.upper()}")
print(f"{'=' * 55}")

print(f"Student Name: {student_name.title()}")
print(f"University: {university.title()}")

print(f"\nTotal Allowance: ₦{total_allowance:,}")
print(f"Food Expenses: ₦{food_expenses:,}")
print(f"Transport Expenses: ₦{transport_expenses:,}")
print(f"Total Expenses: ₦{total_expenses:,}")
print(f"Remaining Allowance: ₦{remaining_allowance:,}")

print(f"{'=' * 55}")