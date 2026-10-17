 # Loop Control Statements in Python
# Python for Robotics
# Chapter 08: Loop Control Statements


# ==================================================
# 1. Using break
# ==================================================

print("Example 1: Break Statement")

for number in range(1, 11):
    if number == 5:
        break

    print(number)


# ==================================================
# 2. Breaking a Loop at a Specific Number
# ==================================================

print("\nExample 2: Stop at Number 7")

for number in range(1, 11):
    print(number)

    if number == 7:
        break


# ==================================================
# 3. Using continue
# ==================================================

print("\nExample 3: Continue Statement")

for number in range(1, 11):
    if number == 5:
        continue

    print(number)


# ==================================================
# 4. Printing Only Odd Numbers Using continue
# ==================================================

print("\nExample 4: Odd Numbers")

for number in range(1, 11):
    if number % 2 == 0:
        continue

    print(number)


# ==================================================
# 5. Skipping Multiples of 3
# ==================================================

print("\nExample 5: Skip Multiples of 3")

for number in range(1, 16):
    if number % 3 == 0:
        continue

    print(number)


# ==================================================
# 6. Breaking a While Loop
# ==================================================

print("\nExample 6: Break in While Loop")

count = 1

while count <= 10:
    if count == 6:
        break

    print(count)
    count += 1


# ==================================================
# 7. Continue in a While Loop
# ==================================================

print("\nExample 7: Continue in While Loop")

count = 0

while count < 10:
    count += 1

    if count == 5:
        continue

    print(count)


# ==================================================
# 8. Robot Stops at a Specific Position
# ==================================================

print("\nExample 8: Robot Position")

for position in range(1, 11):
    if position == 6:
        print("Target position reached!")
        break

    print("Robot position:", position)


# ==================================================
# 9. Robot Skips Selected Positions
# ==================================================

print("\nExample 9: Skipping Positions")

for position in range(1, 11):
    if position == 4 or position == 7:
        continue

    print("Robot position:", position)


# ==================================================
# 10. Stopping Robot Movement
# ==================================================

print("\nExample 10: Stop Robot")

for step in range(1, 11):
    print("Robot movement step:", step)

    if step == 5:
        print("Stop command received!")
        break


# ==================================================
# 11. Skipping Sensor Readings
# ==================================================

print("\nExample 11: Sensor Readings")

for reading in range(1, 11):
    if reading == 3 or reading == 8:
        print("Invalid sensor reading skipped")
        continue

    print("Sensor reading:", reading)


# ==================================================
# 12. Stopping When Battery Becomes Low
# ==================================================

print("\nExample 12: Battery Monitoring")

battery = 100

while battery > 0:
    print("Battery level:", battery, "%")

    battery -= 20

    if battery <= 40:
        print("Battery is low. Stopping simulation.")
        break


# ==================================================
# 13. Skipping Warehouse Sections
# ==================================================

print("\nExample 13: Warehouse Inspection")

for section in range(1, 11):
    if section == 4:
        print("Section 4 is under maintenance")
        continue

    print("Inspecting warehouse section:", section)


# ==================================================
# 14. Stopping at an Obstacle
# ==================================================

print("\nExample 14: Obstacle Detection")

for distance in range(5, 0, -1):
    print("Obstacle distance:", distance, "meters")

    if distance == 2:
        print("Obstacle too close! Robot stopped.")
        break


# ==================================================
# 15. Skipping Empty Task Numbers
# ==================================================

print("\nExample 15: Warehouse Tasks")

for task in range(1, 11):
    if task == 3 or task == 6:
        continue

    print("Executing warehouse task:", task)


# ==================================================
# 16. Using break with a While Loop
# ==================================================

print("\nExample 16: Robot Search")

position = 0

while True:
    print("Searching position:", position)

    if position == 5:
        print("Target found!")
        break

    position += 1


# ==================================================
# 17. Skipping Even Numbers
# ==================================================

print("\nExample 17: Odd Number Processing")

for number in range(1, 21):
    if number % 2 == 0:
        continue

    print("Processing:", number)


# ==================================================
# 18. Stopping Sensor Scanning
# ==================================================

print("\nExample 18: Sensor Scanning")

scan = 1

while scan <= 10:
    print("Scanning environment:", scan)

    if scan == 5:
        print("Scanning completed.")
        break

    scan += 1


# ==================================================
# 19. Using pass
# ==================================================

print("\nExample 19: Pass Statement")

for number in range(1, 6):
    if number == 3:
        pass

    print(number)


# ==================================================
# 20. Pass in a Conditional Block
# ==================================================

print("\nExample 20: Pass in Conditions")

robot_status = "Ready"

if robot_status == "Ready":
    pass

print("Robot status:", robot_status)


# ==================================================
# 21. Skipping a Robot Task
# ==================================================

print("\nExample 21: Task Processing")

for task in range(1, 8):
    if task == 4:
        print("Task 4 skipped")
        continue

    print("Processing task:", task)


# ==================================================
# 22. Stopping Robot at Target Distance
# ==================================================

print("\nExample 22: Target Distance")

distance = 0

while distance <= 20:
    print("Distance travelled:", distance, "meters")

    if distance == 10:
        print("Target distance reached!")
        break

    distance += 2


# ==================================================
# 23. Warehouse Robot Route
# ==================================================

print("\nExample 23: Warehouse Route")

for checkpoint in range(1, 11):
    if checkpoint == 5:
        print("Blocked checkpoint detected!")
        break

    print("Moving towards checkpoint:", checkpoint)


# ==================================================
# 24. Final Warehouse Robot Simulation
# ==================================================

print("\n================================")
print("   WAREHOUSE ROBOT SIMULATION")
print("================================")

battery = 100

for step in range(1, 11):

    if step == 4:
        print("Obstacle detected. Skipping this step.")
        continue

    print("Movement step:", step)

    battery -= 10

    print("Battery remaining:", battery, "%")

    if battery <= 50:
        print("Battery threshold reached. Robot stopping.")
        break

print("Simulation ended.")

print("================================")
