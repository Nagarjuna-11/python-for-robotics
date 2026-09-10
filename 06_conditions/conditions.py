# Conditional Statements in Python
# Python for Robotics
# Chapter 06: Conditions


# ==================================================
# 1. Simple if Statement
# ==================================================

battery = 80

if battery > 50:
    print("Battery level is good")


# ==================================================
# 2. if-else Statement
# ==================================================

battery = 30

if battery > 20:
    print("\nRobot can continue working")
else:
    print("\nRobot needs charging")


# ==================================================
# 3. if-elif-else Statement
# ==================================================

battery = 45

if battery > 70:
    print("\nBattery status: Excellent")
elif battery > 40:
    print("\nBattery status: Good")
elif battery > 20:
    print("\nBattery status: Low")
else:
    print("\nBattery status: Critical")


# ==================================================
# 4. Checking Robot Speed
# ==================================================

speed = 2.5

if speed > 3:
    print("\nRobot is moving too fast")
else:
    print("\nRobot speed is within the limit")


# ==================================================
# 5. Checking Distance
# ==================================================

distance = 5

if distance > 2:
    print("\nPath is clear")
else:
    print("\nObstacle may be nearby")


# ==================================================
# 6. Checking Obstacle Distance
# ==================================================

obstacle_distance = 0.8

if obstacle_distance < 1:
    print("\nObstacle detected!")
else:
    print("\nNo nearby obstacle")


# ==================================================
# 7. Using Comparison Operators
# ==================================================

battery = 75

print("\nBattery Comparisons")

if battery == 75:
    print("Battery is exactly 75%")


if battery >= 50:
    print("Battery is at least 50%")


if battery != 0:
    print("Robot has some battery remaining")


# ==================================================
# 8. Checking Robot Movement
# ==================================================

robot_speed = 2.0

if robot_speed > 0:
    print("\nRobot is moving")
else:
    print("\nRobot is stopped")


# ==================================================
# 9. Checking Battery and Distance
# ==================================================

battery = 80
distance = 5

if battery > 20 and distance > 1:
    print("\nRobot can move")
else:
    print("\nRobot cannot move")


# ==================================================
# 10. Using OR
# ==================================================

battery = 15
obstacle_distance = 5

if battery < 20 or obstacle_distance < 1:
    print("\nRobot should stop")
else:
    print("\nRobot can continue")


# ==================================================
# 11. Using NOT
# ==================================================

obstacle_detected = False

if not obstacle_detected:
    print("\nPath is clear")


# ==================================================
# 12. Nested Conditions
# ==================================================

battery = 80
distance = 5

if battery > 20:

    if distance > 1:
        print("\nRobot is ready to move")
    else:
        print("\nObstacle detected")

else:
    print("\nBattery is too low")


# ==================================================
# 13. Robot Charging Status
# ==================================================

battery = 25

if battery < 20:
    print("\nBattery critically low")
elif battery < 50:
    print("\nBattery is low")
else:
    print("\nBattery level is sufficient")


# ==================================================
# 14. Robot Temperature
# ==================================================

temperature = 45

if temperature > 60:
    print("\nWarning: Robot temperature is high")
elif temperature > 40:
    print("\nRobot temperature is slightly high")
else:
    print("\nRobot temperature is normal")


# ==================================================
# 15. Sensor Status
# ==================================================

sensor_distance = 3.5

if sensor_distance < 1:
    print("\nObstacle detected")
elif sensor_distance < 3:
    print("\nObstacle is nearby")
else:
    print("\nPath is clear")


# ==================================================
# 16. Taking Battery Input
# ==================================================

battery = int(input("\nEnter battery percentage: "))

if battery > 50:
    print("Battery level is good")
elif battery > 20:
    print("Battery level is low")
else:
    print("Battery level is critical")


# ==================================================
# 17. Taking Distance Input
# ==================================================

distance = float(input("\nEnter distance from obstacle: "))

if distance < 1:
    print("STOP! Obstacle is too close")
elif distance < 3:
    print("Warning! Obstacle is nearby")
else:
    print("Path is clear")


# ==================================================
# 18. Robot Movement Decision
# ==================================================

battery = int(input("\nEnter battery level: "))
distance = float(input("Enter distance from obstacle: "))

if battery > 20 and distance > 1:
    print("Robot can move")
else:
    print("Robot should stop")


# ==================================================
# 19. Robot Operating Mode
# ==================================================

battery = int(input("\nEnter battery percentage: "))

if battery >= 80:
    print("Operating Mode: Normal")
elif battery >= 50:
    print("Operating Mode: Energy Saving")
elif battery >= 20:
    print("Operating Mode: Low Power")
else:
    print("Operating Mode: Charging Required")


# ==================================================
# 20. Final Warehouse Robot Decision
# ==================================================

battery = int(input("\nEnter robot battery level: "))
obstacle_distance = float(input("Enter obstacle distance: "))

print("\n==============================")
print("     WAREHOUSE ROBOT")
print("==============================")

if battery <= 20:
    print("Status: STOP")
    print("Reason: Battery is too low")

elif obstacle_distance < 1:
    print("Status: STOP")
    print("Reason: Obstacle detected")

else:
    print("Status: MOVING")
    print("Battery:", battery, "%")
    print("Obstacle Distance:", obstacle_distance, "m")

print("==============================")
