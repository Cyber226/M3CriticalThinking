# Module 3: Critical Thinking Assignment Part 2 of 2
# Brenda Nieves 4/11/2024


print("\n________________________________________\n")
print("\nProgram 2: Alarm Clock Calculation\n")

# User enters current time and hours to wait 
current_time = int(input("Enter the current time: "))
wait_hours = int(input("How many hours would you like to wait: "))

# Alarm time calculation
alarm_24time = (current_time + wait_hours) % 24

# Alarm time result
print(f"Alarm will ring at {alarm_24time:02}:00.")


