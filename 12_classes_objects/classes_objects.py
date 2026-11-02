
# ============================================================
# CHAPTER 12: CLASSES AND OBJECTS
# Python for Robotics
# ============================================================

# A class is a blueprint for creating objects.
# An object represents a particular instance of a class.
#
# For example:
# Robot is a class.
# WarehouseBot and DeliveryBot can be objects.


# ============================================================
# SECTION 1: CREATING A CLASS
# ============================================================

class Robot:
    pass


# We have created a class named Robot.
# pass means that the class is currently empty.


# ============================================================
# SECTION 2: CREATING OBJECTS
# ============================================================

# An object is created by calling the class.

robot1 = Robot()
robot2 = Robot()

print("Robot 1:", robot1)
print("Robot 2:", robot2)


# ============================================================
# SECTION 3: THE __init__() METHOD
# ============================================================

# __init__() is a special method.
# It runs automatically when an object is created.
#
# We use it to initialize object data.


class Robot:

    def __init__(self):
        print("A robot object has been created.")


robot1 = Robot()
robot2 = Robot()


# ============================================================
# SECTION 4: UNDERSTANDING self
# ============================================================

# self refers to the current object.
#
# self.name means the name belonging to this object.


class Robot:

    def __init__(self):
        self.name = "WarehouseBot"


robot1 = Robot()

print("Robot name:", robot1.name)


# ============================================================
# SECTION 5: OBJECT ATTRIBUTES
# ============================================================

# Attributes are variables that belong to an object.

class Robot:

    def __init__(self):
        self.name = "WarehouseBot"
        self.battery = 100
        self.speed = 2.5
        self.status = "Ready"


robot1 = Robot()

print("Name:", robot1.name)
print("Battery:", robot1.battery)
print("Speed:", robot1.speed)
print("Status:", robot1.status)


# ============================================================
# SECTION 6: PASSING VALUES TO THE CLASS
# ============================================================

# We can pass values while creating an object.
#
# These values are received by __init__().


class Robot:

    def __init__(self, name, battery):
        self.name = name
        self.battery = battery


robot1 = Robot("WarehouseBot", 90)
robot2 = Robot("DeliveryBot", 75)

print("Robot 1:", robot1.name)
print("Battery 1:", robot1.battery)

print("Robot 2:", robot2.name)
print("Battery 2:", robot2.battery)


# ============================================================
# SECTION 7: EACH OBJECT HAS ITS OWN DATA
# ============================================================

class Robot:

    def __init__(self, name, battery):
        self.name = name
        self.battery = battery


robot1 = Robot("WarehouseBot", 90)
robot2 = Robot("DeliveryBot", 75)

# Change the battery of robot1.

robot1.battery = 60

print("Robot 1 battery:", robot1.battery)
print("Robot 2 battery:", robot2.battery)


# ============================================================
# SECTION 8: MODIFYING OBJECT ATTRIBUTES
# ============================================================

class Robot:

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed


robot1 = Robot("WarehouseBot", 2.5)

print("Original speed:", robot1.speed)

robot1.speed = 4.0

print("Updated speed:", robot1.speed)


# ============================================================
# SECTION 9: CREATING METHODS
# ============================================================

# A method is a function defined inside a class.
#
# Methods describe what an object can do.


class Robot:

    def __init__(self, name):
        self.name = name

    def move(self):
        print(self.name, "is moving.")


robot1 = Robot("WarehouseBot")

robot1.move()


# ============================================================
# SECTION 10: METHODS WITH PARAMETERS
# ============================================================

class Robot:

    def __init__(self, name):
        self.name = name

    def move(self, distance):
        print(self.name, "moved", distance, "meters.")


robot1 = Robot("WarehouseBot")

robot1.move(5)
robot1.move(10)


# ============================================================
# SECTION 11: METHODS MODIFYING OBJECT DATA
# ============================================================

class Robot:

    def __init__(self, name, battery):
        self.name = name
        self.battery = battery

    def charge(self):
        self.battery = 100


robot1 = Robot("WarehouseBot", 40)

print("Before charging:", robot1.battery)

robot1.charge()

print("After charging:", robot1.battery)


# ============================================================
# SECTION 12: REDUCING BATTERY
# ============================================================

class Robot:

    def __init__(self, name, battery):
        self.name = name
        self.battery = battery

    def use_battery(self, amount):
        self.battery = self.battery - amount


robot1 = Robot("WarehouseBot", 100)

robot1.use_battery(10)

print("Battery after first movement:", robot1.battery)

robot1.use_battery(20)

print("Battery after second movement:", robot1.battery)


# ============================================================
# SECTION 13: METHODS RETURNING VALUES
# ============================================================

class Robot:

    def __init__(self, name, battery):
        self.name = name
        self.battery = battery

    def get_battery(self):
        return self.battery


robot1 = Robot("WarehouseBot", 80)

current_battery = robot1.get_battery()

print("Current battery:", current_battery)


# ============================================================
# SECTION 14: CALCULATING ROBOT SPEED
# ============================================================

class Robot:

    def __init__(self, name):
        self.name = name

    def calculate_speed(self, distance, time):
        speed = distance / time
        return speed


robot1 = Robot("WarehouseBot")

speed = robot1.calculate_speed(10, 5)

print("Robot speed:", speed, "m/s")


# ============================================================
# SECTION 15: ROBOT POSITION
# ============================================================

class Robot:

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def show_position(self):
        print("Robot:", self.name)
        print("X:", self.x)
        print("Y:", self.y)


robot1 = Robot("WarehouseBot", 10, 20)

robot1.show_position()


# ============================================================
# SECTION 16: MOVING A ROBOT
# ============================================================

class Robot:

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def move_forward(self, distance):
        self.x = self.x + distance

    def move_backward(self, distance):
        self.x = self.x - distance


robot1 = Robot("WarehouseBot", 0, 0)

robot1.move_forward(5)

print("Position after moving forward:", robot1.x)

robot1.move_backward(2)

print("Position after moving backward:", robot1.x)


# ============================================================
# SECTION 17: MOVING TO A NEW POSITION
# ============================================================

class Robot:

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y


robot1 = Robot("WarehouseBot", 0, 0)

robot1.move_to(15, 25)

print("New X position:", robot1.x)
print("New Y position:", robot1.y)


# ============================================================
# SECTION 18: CREATING A SENSOR CLASS
# ============================================================

class Sensor:

    def __init__(self, name, reading):
        self.name = name
        self.reading = reading

    def show_reading(self):
        print(self.name, "reading:", self.reading)


lidar = Sensor("Lidar", 3.5)
ultrasonic = Sensor("Ultrasonic", 1.2)

lidar.show_reading()
ultrasonic.show_reading()


# ============================================================
# SECTION 19: UPDATING SENSOR READINGS
# ============================================================

class Sensor:

    def __init__(self, name, reading):
        self.name = name
        self.reading = reading

    def update_reading(self, new_reading):
        self.reading = new_reading


lidar = Sensor("Lidar", 3.5)

print("Old reading:", lidar.reading)

lidar.update_reading(2.8)

print("New reading:", lidar.reading)


# ============================================================
# SECTION 20: MULTIPLE ROBOT OBJECTS
# ============================================================

class Robot:

    def __init__(self, name, battery):
        self.name = name
        self.battery = battery

    def show_status(self):
        print(self.name, "battery:", self.battery, "%")


robot1 = Robot("WarehouseBot", 90)
robot2 = Robot("DeliveryBot", 75)
robot3 = Robot("CleaningBot", 60)

robot1.show_status()
robot2.show_status()
robot3.show_status()


# ============================================================
# SECTION 21: ASSIGNING TASKS
# ============================================================

class Robot:

    def __init__(self, name):
        self.name = name
        self.task = "Idle"

    def assign_task(self, new_task):
        self.task = new_task

    def show_task(self):
        print(self.name, "current task:", self.task)


robot1 = Robot("WarehouseBot")

robot1.show_task()

robot1.assign_task("Pick package")

robot1.show_task()


# ============================================================
# SECTION 22: ROBOT STATUS
# ============================================================

class Robot:

    def __init__(self, name, battery):
        self.name = name
        self.battery = battery
        self.status = "Ready"

    def start(self):
        self.status = "Moving"

    def stop(self):
        self.status = "Stopped"

    def show_status(self):
        print("Robot:", self.name)
        print("Battery:", self.battery)
        print("Status:", self.status)


robot1 = Robot("WarehouseBot", 85)

robot1.show_status()

robot1.start()

robot1.show_status()

robot1.stop()

robot1.show_status()


# ============================================================
# SECTION 23: FINAL MINI PROJECT
# WAREHOUSE ROBOT
# ============================================================

class WarehouseRobot:

    def __init__(self, name, battery, x, y):
        self.name = name
        self.battery = battery
        self.x = x
        self.y = y
        self.status = "Ready"

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.battery = self.battery - 5
        self.status = "Moving"

    def charge(self):
        self.battery = 100
        self.status = "Charging"

    def stop(self):
        self.status = "Stopped"

    def show_details(self):
        print("\nRobot name:", self.name)
        print("Battery:", self.battery, "%")
        print("Position:", self.x, self.y)
        print("Status:", self.status)


# Create a robot object.

robot1 = WarehouseRobot("WarehouseBot", 100, 0, 0)

print("===== INITIAL ROBOT STATUS =====")

robot1.show_details()


# Move the robot.

print("\n===== ROBOT MOVEMENT =====")

robot1.move_to(10, 20)

robot1.show_details()


# Stop the robot.

print("\n===== ROBOT STOPPED =====")

robot1.stop()

robot1.show_details()


# Charge the robot.

print("\n===== ROBOT CHARGING =====")

robot1.charge()

robot1.show_details()


# ============================================================
# END OF CHAPTER 12
# ============================================================
