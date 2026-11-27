student_name = "Dominion Nwajei"
university = "covenant university"
total_allowance = 20000
food_expenses = 15000
transport_expenses = 3000

total_expenses = food_expenses + transport_expenses
total_allowance -= total_expenses

print(f"\n                 DATA FOR {student_name.upper()}\n ============================================================ \n")

print(f"                 Student Name: {student_name}.\n")
print(f"                 University: {university}.\n")
print(f"                 Total Allowance is {total_allowance:,}.\n")
print(f"                 Total Expenses is {total_expenses:,}.\n")
