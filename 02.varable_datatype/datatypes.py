# Variables and Data Types
# Python for Robotics
# Chapter 02: Variables and Data Types


# --------------------------------------------------
# 1. String
# --------------------------------------------------

robot_name = "WarehouseBot"
robot_model = "WB-01"
location = "Warehouse"

print("Robot Name:", robot_name)
print("Robot Model:", robot_model)
print("Location:", location)

print("Type of robot_name:", type(robot_name))


# --------------------------------------------------
# 2. Integer
# --------------------------------------------------

battery_level = 75
number_of_wheels = 4
sensor_count = 3

print("\nBattery Level:", battery_level)
print("Number of Wheels:", number_of_wheels)
print("Number of Sensors:", sensor_count)

print("Type of battery_level:", type(battery_level))


# --------------------------------------------------
# 3. Float
# --------------------------------------------------

robot_speed = 2.5
distance_travelled = 15.75
battery_voltage = 12.6

print("\nRobot Speed:", robot_speed, "m/s")
print("Distance Travelled:", distance_travelled, "m")
print("Battery Voltage:", battery_voltage, "V")

print("Type of robot_speed:", type(robot_speed))


# --------------------------------------------------
# 4. Boolean
# --------------------------------------------------

is_moving = True
obstacle_detected = False
is_charging = False

print("\nIs Robot Moving:", is_moving)
print("Obstacle Detected:", obstacle_detected)
print("Is Charging:", is_charging)

print("Type of is_moving:", type(is_moving))


# --------------------------------------------------
# 5. Multiple Variables
# --------------------------------------------------

length = 1.2
width = 0.8
height = 0.6

print("\nRobot Dimensions")
print("Length:", length, "m")
print("Width:", width, "m")
print("Height:", height, "m")


# --------------------------------------------------
# 6. Changing the Value of a Variable
# --------------------------------------------------

battery_level = 75

print("\nInitial Battery:", battery_level)

battery_level = 60

print("Updated Battery:", battery_level)

battery_level = 45

print("Current Battery:", battery_level)


# --------------------------------------------------
# 7. Checking Data Types
# --------------------------------------------------

name = "WarehouseBot"
battery = 75
speed = 2.5
moving = True

print("\nData Types")

print("name:", type(name))
print("battery:", type(battery))
print("speed:", type(speed))
print("moving:", type(moving))


# --------------------------------------------------
# 8. Simple Robot Status
# --------------------------------------------------

robot_name = "WarehouseBot"
battery_level = 80
robot_speed = 1.5
obstacle_detected = False

print("\nRobot Status")
print("Name:", robot_name)
print("Battery:", battery_level, "%")
print("Speed:", robot_speed, "m/s")
print("Obstacle Detected:", obstacle_detected)
