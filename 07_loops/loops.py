# Loops in Python
# Python for Robotics
# Chapter 07: Loops


# ==================================================
# 1. Simple for Loop
# ==================================================

print("Simple For Loop")

for i in range(5):
    print(i)
      

# ==================================================
# 2. Printing Numbers from 1 to 10
# ==================================================

print("\nNumbers from 1 to 10")

for number in range(1, 11):
    print(number)


# ==================================================
# 3. Printing Even Numbers
# ==================================================

print("\nEven Numbers")

for number in range(2, 11, 2):
    print(number)


# ==================================================
# 4. Printing Odd Numbers
# ==================================================

print("\nOdd Numbers")

for number in range(1, 11, 2):
    print(number)


# ==================================================
# 5. Counting Down
# ==================================================

print("\nCountdown")

for number in range(10, 0, -1):
    print(number)

print("Robot Started")


# ==================================================
# 6. Repeating a Message
# ==================================================

print("\nRobot Messages")

for i in range(5):
    print("WarehouseBot is ready")


# ==================================================
# 7. Robot Inspection
# ==================================================

print("\nRobot Inspection")

for inspection in range(1, 6):
    print("Performing inspection:", inspection)


# ==================================================
# 8. Sensor Scanning
# ==================================================

print("\nSensor Scanning")

for scan in range(1, 6):
    print("Performing sensor scan:", scan)


# ==================================================
# 9. Robot Movement
# ==================================================

print("\nRobot Movement")

for step in range(1, 6):
    print("Robot moved to step:", step)


# ==================================================
# 10. Robot Distance
# ==================================================

print("\nRobot Distance")

for distance in range(0, 11, 2):
    print("Distance travelled:", distance, "meters")


# ==================================================
# 11. Robot Battery Readings
# ==================================================

print("\nBattery Readings")

battery = 100

for reading in range(5):
    print("Battery:", battery, "%")
    battery -= 10


# ==================================================
# 12. Simple while Loop
# ==================================================

print("\nSimple While Loop")

count = 1

while count <= 5:
    print("Count:", count)
    count += 1


# ==================================================
# 13. Robot Position Using while Loop
# ==================================================

print("\nRobot Position")

position = 0

while position <= 10:
    print("Robot position:", position, "meters")
    position += 2


# ==================================================
# 14. Battery Simulation Using while Loop
# ==================================================

print("\nBattery Simulation")

battery = 100

while battery > 0:
    print("Battery:", battery, "%")
    battery -= 20


# ==================================================
# 15. Sensor Reading Using while Loop
# ==================================================

print("\nSensor Readings")

reading = 1

while reading <= 5:
    print("Sensor reading number:", reading)
    reading += 1


# ==================================================
# 16. Warehouse Sections
# ==================================================

print("\nWarehouse Inspection")

for section in range(1, 6):
    print("Inspecting warehouse section:", section)


# ==================================================
# 17. Repeated Warehouse Tasks
# ==================================================

print("\nWarehouse Tasks")

for task in range(1, 6):
    print("Performing warehouse task:", task)


# ==================================================
# 18. Robot Movement with Position
# ==================================================

print("\nRobot Movement Simulation")

position = 0

for movement in range(1, 6):
    position += 2

    print("Movement:", movement)
    print("Current position:", position, "meters")


# ==================================================
# 19. Robot Battery Charging
# ==================================================

print("\nBattery Charging")

battery = 20

while battery <= 100:
    print("Battery:", battery, "%")
    battery += 20


# ==================================================
# 20. Robot Travel Simulation
# ==================================================

print("\nRobot Travel")

distance = 0

while distance <= 20:
    print("Robot travelled:", distance, "meters")
    distance += 5


# ==================================================
# 21. Temperature Readings
# ==================================================

print("\nTemperature Readings")

for reading in range(1, 6):
    temperature = 25 + reading

    print("Reading:", reading)
    print("Temperature:", temperature, "°C")


# ==================================================
# 22. Sensor Data Collection
# ==================================================

print("\nSensor Data Collection")

for reading in range(1, 6):
    distance = reading * 2

    print("Reading:", reading)
    print("Sensor Distance:", distance, "meters")


# ==================================================
# 23. Multiplication Table
# ==================================================

print("\nMultiplication Table")

number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# ==================================================
# 24. Multiple Robot Movements
# ==================================================

print("\nMultiple Robot Movements")

position = 0

for movement in range(1, 11):
    position += 1

    print(
        "Movement:",
        movement,
        "| Position:",
        position,
        "meters"
    )


# ==================================================
# 25. Robot Battery Monitoring
# ==================================================

print("\nRobot Battery Monitoring")

battery = 100

for reading in range(1, 11):
    print(
        "Reading:",
        reading,
        "| Battery:",
        battery,
        "%"
    )

    battery -= 5


# ==================================================
# 26. Warehouse Robot Task Counter
# ==================================================

print("\nWarehouse Robot Tasks")

completed_tasks = 0

for task in range(1, 6):
    print("Completed task:", task)
    completed_tasks += 1

print("Total completed tasks:", completed_tasks)


# ==================================================
# 27. Robot Route Simulation
# ==================================================

print("\nRobot Route Simulation")

position = 0

for step in range(1, 11):
    position += 3

    print(
        "Step:",
        step,
        "| Robot position:",
        position,
        "meters"
    )


# ==================================================
# 28. Final Warehouse Robot Simulation
# ==================================================

print("\n================================")
print("    WAREHOUSE ROBOT SIMULATION")
print("================================")

position = 0
battery = 100

for step in range(1, 6):

    position += 2
    battery -= 10

    print("\nStep:", step)
    print("Position:", position, "meters")
    print("Battery:", battery, "%")

print("\nRobot completed the simulation.")

print("================================")
