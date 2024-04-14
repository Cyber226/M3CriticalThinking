# Module 3: Critical Thinking Assignment Part 1 of 2
# Brenda Nieves 4/11/2024

# Program 1: Tip and Sales Tax Meal Cost Calculator
print("\nProgram 1: Tip and Sales Tax Meal Cost Calculator \n")

# Ask for the charge for the food
food_cost = float(input("Please enter the cost of the food: $"))

# Tip and sales tax Calculation
tip = food_cost * 0.18
sales_tax = food_cost * 0.07

# Total Cost Calculation
total_cost = food_cost + tip + sales_tax

# Display the results
print(f"Subtotal: ${food_cost:.2f}")
print(f"18% Tip: ${tip:.2f}")
print(f"7% Sales Tax: ${sales_tax:.2f}")
print(f"Grand Total: ${total_cost:.2f}")
