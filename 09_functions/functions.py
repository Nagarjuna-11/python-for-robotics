 # Functions in Python
# Python for Robotics
# Chapter 09: Functions


# ==================================================
# 1. A Simple Function
# ==================================================

print("Example 1: Simple Function")


def greet():
    print("Hello, Robot!")
    print("Welcome to Python for Robotics")


greet()


# ==================================================
# 2. Calling a Function Multiple Times
# ==================================================

print("\nExample 2: Multiple Function Calls")


def robot_message():
    print("WarehouseBot is ready")


robot_message()
robot_message()
robot_message()


# ==================================================
# 3. Function with One Parameter
# ==================================================

print("\nExample 3: Function with One Parameter")


def greet_robot(name):
    print("Hello,", name)


greet_robot("WarehouseBot")
greet_robot("DeliveryBot")
greet_robot("TransportBot")


# ==================================================
# 4. Function with Multiple Parameters
# ==================================================

print("\nExample 4: Multiple Parameters")


def robot_information(name, model):
    print("Robot Name:", name)
    print("Robot Model:", model)


robot_information("WarehouseBot", "WB-01")
robot_information("DeliveryBot", "DB-02")


# ==================================================
# 5. Function with Integer Arguments
# ==================================================

print("\nExample 5: Integer Arguments")


def display_battery(battery):
    print("Battery Level:", battery, "%")


display_battery(90)
display_battery(65)
display_battery(30)


# ==================================================
# 6. Function with Float Arguments
# ==================================================

print("\nExample 6: Float Arguments")


def display_speed(speed):
    print("Robot Speed:", speed, "m/s")


display_speed(1.5)
display_speed(2.5)
display_speed(3.0)


# ==================================================
# 7. Function with a Return Value
# ==================================================

print("\nExample 7: Return Statement")


def add(a, b):
    return a + b


result = add(10, 20)

print("Sum:", result)


# ==================================================
# 8. Subtracting Values
# ==================================================

print("\nExample 8: Subtraction")


def subtract(a, b):
    return a - b


result = subtract(50, 20)

print("Difference:", result)


# ==================================================
# 9. Calculating Robot Speed
# ==================================================

print("\nExample 9: Robot Speed")


def calculate_speed(distance, time):
    return distance / time


speed = calculate_speed(20, 5)

print("Distance: 20 meters")
print("Time: 5 seconds")
print("Speed:", speed, "m/s")


# ==================================================
# 10. Calculating Remaining Battery
# ==================================================

print("\nExample 10: Battery Calculation")


def remaining_battery(starting_battery, battery_used):
    return starting_battery - battery_used


remaining = remaining_battery(100, 25)

print("Remaining Battery:", remaining, "%")


# ==================================================
# 11. Function with a Default Parameter
# ==================================================

print("\nExample 11: Default Parameter")


def robot_status(name="WarehouseBot"):
    print("Robot Name:", name)


robot_status()
robot_status("DeliveryBot")


# ==================================================
# 12. Function with Multiple Return Values
# ==================================================

print("\nExample 12: Multiple Return Values")


def robot_dimensions():
    length = 1.2
    width = 0.8

    return length, width


length, width = robot_dimensions()

print("Robot Length:", length, "m")
print("Robot Width:", width, "m")


# ==================================================
# 13. Function to Display Sensor Information
# ==================================================

print("\nExample 13: Sensor Information")


def sensor_information(sensor_name, distance):
    print("Sensor:", sensor_name)
    print("Measured Distance:", distance, "meters")


sensor_information("LiDAR", 4.5)
sensor_information("Ultrasonic", 2.0)


# ==================================================
# 14. Function to Calculate Distance
# ==================================================

print("\nExample 14: Distance Calculation")


def calculate_distance(speed, time):
    return speed * time


distance = calculate_distance(2.5, 4)

print("Distance Travelled:", distance, "meters")


# ==================================================
# 15. Function with a Boolean Parameter
# ==================================================

print("\nExample 15: Robot Movement Status")


def movement_status(is_moving):
    print("Robot Moving:", is_moving)


movement_status(True)
movement_status(False)


# ==================================================
# 16. Function to Display Robot Details
# ==================================================

print("\nExample 16: Robot Details")


def display_robot(name, battery, speed):
    print("Robot Name:", name)
    print("Battery:", battery, "%")
    print("Speed:", speed, "m/s")


display_robot("WarehouseBot", 85, 2.5)


# ==================================================
# 17. Function to Calculate Average
# ==================================================

print("\nExample 17: Average Calculation")


def calculate_average(a, b, c):
    return (a + b + c) / 3


average = calculate_average(10, 20, 30)

print("Average:", average)


# ==================================================
# 18. Function to Convert Time into Distance
# ==================================================

print("\nExample 18: Robot Travel")


def travel_distance(speed, time):
    distance = speed * time
    return distance


distance = travel_distance(3, 10)

print("Travel Distance:", distance, "meters")


# ==================================================
# 19. Function for Battery Usage
# ==================================================

print("\nExample 19: Battery Usage")


def use_battery(battery, amount_used):
    return battery - amount_used


battery = use_battery(100, 15)

print("Battery Remaining:", battery, "%")


# ==================================================
# 20. Function for Robot Position
# ==================================================

print("\nExample 20: Robot Position")


def update_position(position, movement):
    return position + movement


position = update_position(10, 5)

print("New Robot Position:", position, "meters")


# ==================================================
# 21. Function to Display Warehouse Tasks
# ==================================================

print("\nExample 21: Warehouse Tasks")


def display_task(task_name):
    print("Current Task:", task_name)


display_task("Collect Package")
display_task("Move Package")
display_task("Deliver Package")


# ==================================================
# 22. Function with a Default Speed
# ==================================================

print("\nExample 22: Default Robot Speed")


def move_robot(speed=1.0):
    print("Robot moving at", speed, "m/s")


move_robot()
move_robot(2.5)


# ==================================================
# 23. Function Returning Robot Information
# ==================================================

print("\nExample 23: Return Robot Information")


def get_robot_name():
    return "WarehouseBot"


name = get_robot_name()

print("Robot Name:", name)


# ==================================================
# 24. Function to Calculate Battery Percentage
# ==================================================

print("\nExample 24: Battery Percentage")


def battery_percentage(remaining, capacity):
    return (remaining / capacity) * 100


percentage = battery_percentage(60, 100)

print("Battery Percentage:", percentage, "%")


# ==================================================
# 25. Final Warehouse Robot Example
# ==================================================

print("\n================================")
print("    WAREHOUSE ROBOT SYSTEM")
print("================================")


def display_status(name, battery, speed):
    print("Robot Name:", name)
    print("Battery:", battery, "%")
    print("Speed:", speed, "m/s")


def calculate_travel(speed, time):
    return speed * time


display_status("WarehouseBot", 80, 2.0)

distance = calculate_travel(2.0, 10)

print("Distance Travelled:", distance, "meters")

print("================================")
