# Operators in Python
# Python for Robotics
# Chapter 03: Operators


# --------------------------------------------------
# 1. Arithmetic Operators
# --------------------------------------------------

a = 20
b = 5

print("Arithmetic Operators")

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)


# --------------------------------------------------
# 2. Arithmetic Operations with Robot Data
# --------------------------------------------------

battery_start = 100
battery_used = 25

battery_remaining = battery_start - battery_used

print("\nRobot Battery")
print("Starting Battery:", battery_start, "%")
print("Battery Used:", battery_used, "%")
print("Remaining Battery:", battery_remaining, "%")


# --------------------------------------------------
# 3. Comparison Operators
# --------------------------------------------------

battery = 75

print("\nComparison Operators")

print("Battery > 50:", battery > 50)
print("Battery < 50:", battery < 50)
print("Battery == 75:", battery == 75)
print("Battery != 75:", battery != 75)
print("Battery >= 75:", battery >= 75)
print("Battery <= 75:", battery <= 75)


# --------------------------------------------------
# 4. Comparing Robot Speed
# --------------------------------------------------

robot_speed = 2.5
maximum_speed = 3.0

print("\nRobot Speed")

print("Robot speed:", robot_speed, "m/s")
print("Maximum speed:", maximum_speed, "m/s")

print("Speed is below maximum:", robot_speed < maximum_speed)
print("Speed is equal to maximum:", robot_speed == maximum_speed)
print("Speed is above maximum:", robot_speed > maximum_speed)


# --------------------------------------------------
# 5. Logical AND Operator
# --------------------------------------------------

battery = 80
distance = 5

print("\nLogical AND")

print("Battery > 20 AND Distance > 1:")
print(battery > 20 and distance > 1)


# --------------------------------------------------
# 6. Logical OR Operator
# --------------------------------------------------

battery = 15
obstacle_distance = 0.5

print("\nLogical OR")

print("Battery is low OR obstacle is close:")
print(battery < 20 or obstacle_distance < 1)


# --------------------------------------------------
# 7. Logical NOT Operator
# --------------------------------------------------

obstacle_detected = False

print("\nLogical NOT")

print("Obstacle Detected:", obstacle_detected)
print("Obstacle Not Detected:", not obstacle_detected)


# --------------------------------------------------
# 8. Assignment Operators
# --------------------------------------------------

battery = 100

print("\nAssignment Operators")

print("Initial Battery:", battery)

battery += 10
print("After += 10:", battery)

battery -= 20
print("After -= 20:", battery)

battery *= 2
print("After *= 2:", battery)

battery /= 2
print("After /= 2:", battery)


# --------------------------------------------------
# 9. Modulus Operator for Robot Wheels
# --------------------------------------------------

total_wheels = 8
robots = 2

wheels_per_robot = total_wheels % robots

print("\nModulus Example")
print("Total Wheels:", total_wheels)
print("Number of Robots:", robots)
print("Remainder:", wheels_per_robot)


# --------------------------------------------------
# 10. Simple Robot Calculation
# --------------------------------------------------

distance = 20
time = 5

speed = distance / time

print("\nRobot Speed Calculation")
print("Distance:", distance, "m")
print("Time:", time, "seconds")
print("Speed:", speed, "m/s")


# --------------------------------------------------
# 11. Combining Operators
# --------------------------------------------------

battery = 75
distance = 10
speed = 2

robot_ready = battery > 20 and distance > 0 and speed > 0

print("\nRobot Readiness")
print("Battery:", battery, "%")
print("Distance:", distance, "m")
print("Speed:", speed, "m/s")
print("Robot Ready:", robot_ready)
