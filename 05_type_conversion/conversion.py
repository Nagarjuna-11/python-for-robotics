# Type Conversion in Python
# Python for Robotics
# Chapter 05: Type Conversion


# ==================================================
# 1. Introduction to Type Conversion
# ==================================================

# Type conversion means changing a value
# from one data type to another.

value = "100"

print("Original Value:", value)
print("Original Type:", type(value))


# ==================================================
# 2. String to Integer
# ==================================================

number_text = "50"

number = int(number_text)

print("\nString to Integer")
print("Original:", number_text)
print("Original Type:", type(number_text))
print("Converted:", number)
print("Converted Type:", type(number))


# ==================================================
# 3. String to Float
# ==================================================

distance_text = "25.5"

distance = float(distance_text)

print("\nString to Float")
print("Original:", distance_text)
print("Original Type:", type(distance_text))
print("Converted:", distance)
print("Converted Type:", type(distance))


# ==================================================
# 4. Integer to Float
# ==================================================

battery = 75

battery_float = float(battery)

print("\nInteger to Float")
print("Original:", battery)
print("Original Type:", type(battery))
print("Converted:", battery_float)
print("Converted Type:", type(battery_float))


# ==================================================
# 5. Float to Integer
# ==================================================

speed = 2.8

speed_integer = int(speed)

print("\nFloat to Integer")
print("Original:", speed)
print("Original Type:", type(speed))
print("Converted:", speed_integer)
print("Converted Type:", type(speed_integer))


# ==================================================
# 6. Integer to String
# ==================================================

battery = 80

battery_text = str(battery)

print("\nInteger to String")
print("Original:", battery)
print("Original Type:", type(battery))
print("Converted:", battery_text)
print("Converted Type:", type(battery_text))


# ==================================================
# 7. Float to String
# ==================================================

robot_speed = 2.5

speed_text = str(robot_speed)

print("\nFloat to String")
print("Original:", robot_speed)
print("Original Type:", type(robot_speed))
print("Converted:", speed_text)
print("Converted Type:", type(speed_text))


# ==================================================
# 8. Integer to Boolean
# ==================================================

value = 1

boolean_value = bool(value)

print("\nInteger to Boolean")
print("Value:", value)
print("Converted Value:", boolean_value)
print("Type:", type(boolean_value))


# ==================================================
# 9. Zero to Boolean
# ==================================================

value = 0

boolean_value = bool(value)

print("\nZero to Boolean")
print("Value:", value)
print("Converted Value:", boolean_value)
print("Type:", type(boolean_value))


# ==================================================
# 10. String to Boolean
# ==================================================

text = "Robot"

boolean_value = bool(text)

print("\nString to Boolean")
print("Value:", text)
print("Converted Value:", boolean_value)
print("Type:", type(boolean_value))


# ==================================================
# 11. Empty String to Boolean
# ==================================================

text = ""

boolean_value = bool(text)

print("\nEmpty String to Boolean")
print("Value:", text)
print("Converted Value:", boolean_value)
print("Type:", type(boolean_value))


# ==================================================
# 12. Converting Robot Battery Data
# ==================================================

battery_text = "85"

battery = int(battery_text)

print("\nRobot Battery")
print("Battery:", battery, "%")
print("Data Type:", type(battery))


# ==================================================
# 13. Converting Robot Distance Data
# ==================================================

distance_text = "12.75"

distance = float(distance_text)

print("\nRobot Distance")
print("Distance:", distance, "meters")
print("Data Type:", type(distance))


# ==================================================
# 14. Converting Robot Speed Data
# ==================================================

speed_text = "2.5"

speed = float(speed_text)

print("\nRobot Speed")
print("Speed:", speed, "m/s")
print("Data Type:", type(speed))


# ==================================================
# 15. Converting User Input to Integer
# ==================================================

battery = input("\nEnter battery level: ")

battery = int(battery)

print("Battery Level:", battery, "%")
print("Data Type:", type(battery))


# ==================================================
# 16. Converting User Input to Float
# ==================================================

distance = input("\nEnter distance travelled: ")

distance = float(distance)

print("Distance:", distance, "meters")
print("Data Type:", type(distance))


# ==================================================
# 17. Converting Multiple Robot Inputs
# ==================================================

robot_name = input("\nEnter robot name: ")
battery = input("Enter battery level: ")
speed = input("Enter robot speed: ")

battery = int(battery)
speed = float(speed)

print("\nRobot Information")
print("Robot Name:", robot_name)
print("Battery:", battery, "%")
print("Speed:", speed, "m/s")


# ==================================================
# 18. Robot Distance and Time
# ==================================================

distance = input("\nEnter distance travelled: ")
time = input("Enter time taken: ")

distance = float(distance)
time = float(time)

print("\nMovement Information")
print("Distance:", distance, "meters")
print("Time:", time, "seconds")


# ==================================================
# 19. Calculating Robot Speed
# ==================================================

distance = input("\nEnter distance travelled: ")
time = input("Enter time taken: ")

distance = float(distance)
time = float(time)

speed = distance / time

print("\nRobot Speed Calculation")
print("Distance:", distance, "m")
print("Time:", time, "seconds")
print("Speed:", speed, "m/s")


# ==================================================
# 20. Calculating Remaining Battery
# ==================================================

starting_battery = input("\nEnter starting battery: ")
battery_used = input("Enter battery used: ")

starting_battery = int(starting_battery)
battery_used = int(battery_used)

remaining_battery = starting_battery - battery_used

print("\nBattery Information")
print("Starting Battery:", starting_battery, "%")
print("Battery Used:", battery_used, "%")
print("Remaining Battery:", remaining_battery, "%")


# ==================================================
# 21. Converting Robot Dimensions
# ==================================================

length = input("\nEnter robot length: ")
width = input("Enter robot width: ")
height = input("Enter robot height: ")

length = float(length)
width = float(width)
height = float(height)

print("\nRobot Dimensions")
print("Length:", length, "m")
print("Width:", width, "m")
print("Height:", height, "m")


# ==================================================
# 22. Final Robot Configuration
# ==================================================

robot_name = input("\nEnter robot name: ")
battery = input("Enter battery percentage: ")
speed = input("Enter maximum speed: ")
distance = input("Enter operating range: ")

battery = int(battery)
speed = float(speed)
distance = float(distance)

print("\n================================")
print("       ROBOT CONFIGURATION")
print("================================")

print("Robot Name     :", robot_name)
print("Battery Level  :", battery, "%")
print("Maximum Speed  :", speed, "m/s")
print("Operating Range:", distance, "m")

print("================================")
