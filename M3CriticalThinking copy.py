# Module 3: Critical Thinking Assignment Part 1 and 2
# Brenda Nieves 4/11/2024

# Program 1: Tip and Sales Tax Meal Cost Caculator
print("\nProgram 1: Tip and Sales Tax Meal Cost Calculator \n")

# Ask for the charge for the food
food_cost = float(input("Please enter the cost of the food: $"))

# Tip and sales tax Calculation
tip = food_cost * 0.18
sales_tax = food_cost * 0.07

# Total cost Calculation
total_cost = food_cost + tip + sales_tax

# Display the results
print(f"Subtotal: ${food_cost:.2f}")
print(f"18% Tip: ${tip:.2f}")
print(f"7% Sales Tax: ${sales_tax:.2f}")
print(f"Grand Total: ${total_cost:.2f}")

print("\n________________________________________\n")
print("\nProgram 2: Alarm Clock Calculation\n")

# User enter current time and hours to wait 
current_time = int(input("Enter the current time: "))
wait_hours = int(input("How many hours would you like to wait: "))

# Alarm time calculation
alarm_24time = (current_time + wait_hours) % 24

# Alarm time result
print(f"Alarm will ring at {alarm_24time:02}:00.")


