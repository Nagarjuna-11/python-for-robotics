# Input and Output in Python
# Python for Robotics
# Chapter 04: Input and Output


# ==================================================
# 1. Basic print() Statements
# ==================================================

print("Hello, World!")
print("Welcome to Python")
print("Learning Python for Robotics")
print("Building a foundation for ROS 2")


# ==================================================
# 2. Printing Text
# ==================================================

print("\nRobot Information")
print("Robot Name")
print("Robot Model")
print("Robot Location")
print("Robot Status")


# ==================================================
# 3. Printing Variables
# ==================================================

robot_name = "WarehouseBot"
robot_model = "WB-01"
robot_location = "Warehouse A"
robot_status = "Ready"

print("\nRobot Details")
print("Name:", robot_name)
print("Model:", robot_model)
print("Location:", robot_location)
print("Status:", robot_status)


# ==================================================
# 4. Printing Different Data Types
# ==================================================

battery_level = 80
robot_speed = 2.5
is_moving = True
sensor_name = "LiDAR"

print("\nRobot Data")
print("Battery Level:", battery_level)
print("Robot Speed:", robot_speed)
print("Is Moving:", is_moving)
print("Sensor:", sensor_name)


# ==================================================
# 5. Printing Multiple Values
# ==================================================

name = "WarehouseBot"
battery = 75
speed = 2.0

print("\nMultiple Values")
print(name, battery, speed)


# ==================================================
# 6. Using sep Parameter
# ==================================================

robot_name = "WarehouseBot"
location = "Warehouse A"
status = "Ready"

print("\nUsing sep")
print(robot_name, location, status, sep=" | ")


# ==================================================
# 7. Using end Parameter
# ==================================================

print("\nUsing end")

print("Robot", end=" ")
print("is", end=" ")
print("ready")


# ==================================================
# 8. Taking Basic User Input
# ==================================================

print("\nEnter Robot Information")

robot_name = input("Robot Name: ")

print("Robot Name:", robot_name)


# ==================================================
# 9. Taking Multiple Inputs
# ==================================================

robot_name = input("\nEnter robot name: ")
robot_location = input("Enter robot location: ")

print("\nRobot Information")
print("Name:", robot_name)
print("Location:", robot_location)


# ==================================================
# 10. Taking Sensor Information
# ==================================================

sensor_name = input("\nEnter sensor name: ")
sensor_location = input("Enter sensor location: ")

print("\nSensor Information")
print("Sensor Name:", sensor_name)
print("Sensor Location:", sensor_location)


# ==================================================
# 11. Taking Operator Information
# ==================================================

operator_name = input("\nEnter operator name: ")
robot_name = input("Enter robot name: ")

print("\nOperator Information")
print("Operator:", operator_name)
print("Robot:", robot_name)


# ==================================================
# 12. Formatted Output Using f-Strings
# ==================================================

robot_name = "WarehouseBot"
battery = 85
speed = 2.5

print("\nFormatted Output")

print(f"Robot Name: {robot_name}")
print(f"Battery Level: {battery}%")
print(f"Robot Speed: {speed} m/s")


# ==================================================
# 13. Combining Text and Variables
# ==================================================

robot_name = "WarehouseBot"
location = "Storage Area"
task = "Moving Boxes"

print("\nRobot Task Information")

print("The robot", robot_name, "is currently in", location)
print("Current task:", task)


# ==================================================
# 14. Displaying Robot Status
# ==================================================

robot_name = "WarehouseBot"
location = "Loading Area"
status = "Ready"

print("\n==============================")
print("        ROBOT STATUS")
print("==============================")

print("Robot Name :", robot_name)
print("Location   :", location)
print("Status     :", status)

print("==============================")


# ==================================================
# 15. Displaying Sensor Status
# ==================================================

sensor_name = "LiDAR"
sensor_type = "Distance Sensor"
sensor_location = "Front of Robot"

print("\n==============================")
print("       SENSOR STATUS")
print("==============================")

print("Sensor Name :", sensor_name)
print("Sensor Type :", sensor_type)
print("Location    :", sensor_location)

print("==============================")


# ==================================================
# 16. Simple Robot Configuration
# ==================================================

robot_name = input("\nEnter robot name: ")
robot_model = input("Enter robot model: ")
robot_task = input("Enter robot task: ")

print("\n==============================")
print("     ROBOT CONFIGURATION")
print("==============================")

print(f"Robot Name : {robot_name}")
print(f"Robot Model: {robot_model}")
print(f"Robot Task : {robot_task}")

print("==============================")


# ==================================================
# 17. Simple Sensor Configuration
# ==================================================

sensor_name = input("\nEnter sensor name: ")
sensor_type = input("Enter sensor type: ")
sensor_location = input("Enter sensor location: ")

print("\n==============================")
print("    SENSOR CONFIGURATION")
print("==============================")

print(f"Sensor Name     : {sensor_name}")
print(f"Sensor Type     : {sensor_type}")
print(f"Sensor Location : {sensor_location}")

print("==============================")# Input and Output in Python
# Python for Robotics
# Chapter 04: Input and Output


# ==================================================
# 1. Basic print() Statements
# ==================================================

print("Hello, World!")
print("Welcome to Python")
print("Learning Python for Robotics")
print("Building a foundation for ROS 2")


# ==================================================
# 2. Printing Text
# ==================================================

print("\nRobot Information")
print("Robot Name")
print("Robot Model")
print("Robot Location")
print("Robot Status")


# ==================================================
# 3. Printing Variables
# ==================================================

robot_name = "WarehouseBot"
robot_model = "WB-01"
robot_location = "Warehouse A"
robot_status = "Ready"

print("\nRobot Details")
print("Name:", robot_name)
print("Model:", robot_model)
print("Location:", robot_location)
print("Status:", robot_status)


# ==================================================
# 4. Printing Different Data Types
# ==================================================

battery_level = 80
robot_speed = 2.5
is_moving = True
sensor_name = "LiDAR"

print("\nRobot Data")
print("Battery Level:", battery_level)
print("Robot Speed:", robot_speed)
print("Is Moving:", is_moving)
print("Sensor:", sensor_name)


# ==================================================
# 5. Printing Multiple Values
# ==================================================

name = "WarehouseBot"
battery = 75
speed = 2.0

print("\nMultiple Values")
print(name, battery, speed)


# ==================================================
# 6. Using sep Parameter
# ==================================================

robot_name = "WarehouseBot"
location = "Warehouse A"
status = "Ready"

print("\nUsing sep")
print(robot_name, location, status, sep=" | ")


# ==================================================
# 7. Using end Parameter
# ==================================================

print("\nUsing end")

print("Robot", end=" ")
print("is", end=" ")
print("ready")


# ==================================================
# 8. Taking Basic User Input
# ==================================================

print("\nEnter Robot Information")

robot_name = input("Robot Name: ")

print("Robot Name:", robot_name)


# ==================================================
# 9. Taking Multiple Inputs
# ==================================================

robot_name = input("\nEnter robot name: ")
robot_location = input("Enter robot location: ")

print("\nRobot Information")
print("Name:", robot_name)
print("Location:", robot_location)


# ==================================================
# 10. Taking Sensor Information
# ==================================================

sensor_name = input("\nEnter sensor name: ")
sensor_location = input("Enter sensor location: ")

print("\nSensor Information")
print("Sensor Name:", sensor_name)
print("Sensor Location:", sensor_location)


# ==================================================
# 11. Taking Operator Information
# ==================================================

operator_name = input("\nEnter operator name: ")
robot_name = input("Enter robot name: ")

print("\nOperator Information")
print("Operator:", operator_name)
print("Robot:", robot_name)


# ==================================================
# 12. Formatted Output Using f-Strings
# ==================================================

robot_name = "WarehouseBot"
battery = 85
speed = 2.5

print("\nFormatted Output")

print(f"Robot Name: {robot_name}")
print(f"Battery Level: {battery}%")
print(f"Robot Speed: {speed} m/s")


# ==================================================
# 13. Combining Text and Variables
# ==================================================

robot_name = "WarehouseBot"
location = "Storage Area"
task = "Moving Boxes"

print("\nRobot Task Information")

print("The robot", robot_name, "is currently in", location)
print("Current task:", task)


# ==================================================
# 14. Displaying Robot Status
# ==================================================

robot_name = "WarehouseBot"
location = "Loading Area"
status = "Ready"

print("\n==============================")
print("        ROBOT STATUS")
print("==============================")

print("Robot Name :", robot_name)
print("Location   :", location)
print("Status     :", status)

print("==============================")


# ==================================================
# 15. Displaying Sensor Status
# ==================================================

sensor_name = "LiDAR"
sensor_type = "Distance Sensor"
sensor_location = "Front of Robot"

print("\n==============================")
print("       SENSOR STATUS")
print("==============================")

print("Sensor Name :", sensor_name)
print("Sensor Type :", sensor_type)
print("Location    :", sensor_location)

print("==============================")


# ==================================================
# 16. Simple Robot Configuration
# ==================================================

robot_name = input("\nEnter robot name: ")
robot_model = input("Enter robot model: ")
robot_task = input("Enter robot task: ")

print("\n==============================")
print("     ROBOT CONFIGURATION")
print("==============================")

print(f"Robot Name : {robot_name}")
print(f"Robot Model: {robot_model}")
print(f"Robot Task : {robot_task}")

print("==============================")


# ==================================================
# 17. Simple Sensor Configuration
# ==================================================

sensor_name = input("\nEnter sensor name: ")
sensor_type = input("Enter sensor type: ")
sensor_location = input("Enter sensor location: ")

print("\n==============================")
print("    SENSOR CONFIGURATION")
print("==============================")

print(f"Sensor Name     : {sensor_name}")
print(f"Sensor Type     : {sensor_type}")
print(f"Sensor Location : {sensor_location}")

print("==============================")
