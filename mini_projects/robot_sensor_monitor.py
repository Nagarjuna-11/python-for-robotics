
# ============================================================
# MINI PROJECT 2: ROBOT SENSOR MONITORING SYSTEM
# ============================================================
# Objective:
# Simulate a robot monitoring its ultrasonic and LiDAR sensors.
# The robot checks sensor readings and detects obstacles.
# ============================================================


# SECTION 1: IMPORT MODULE

import random


# SECTION 2: CREATE SENSOR CLASS

class RobotSensor:

    def __init__(self, sensor_name, sensor_type):

        self.sensor_name = sensor_name
        self.sensor_type = sensor_type
        self.distance = 0

    def update_reading(self):

        # Simulate a sensor reading between 10 and 200 cm
        self.distance = random.randint(10, 200)

    def display_reading(self):

        print(self.sensor_name, ":", self.distance, "cm")


# SECTION 3: CREATE ROBOT CLASS

class Robot:

    def __init__(self, robot_name):

        self.robot_name = robot_name

        # Create two sensor objects
        self.ultrasonic = RobotSensor(
            "Ultrasonic Sensor", "Distance Sensor"
        )

        self.lidar = RobotSensor(
            "LiDAR Sensor", "Laser Sensor"
        )

        self.status = "STOPPED"

    # SECTION 4: READ SENSOR DATA

    def read_sensors(self):

        print("\nReading sensor data...")

        self.ultrasonic.update_reading()
        self.lidar.update_reading()

        self.ultrasonic.display_reading()
        self.lidar.display_reading()

    # SECTION 5: CHECK FOR OBSTACLES

    def check_obstacles(self):

        ultrasonic_distance = self.ultrasonic.distance
        lidar_distance = self.lidar.distance

        print("\nObstacle Detection:")

        # Check ultrasonic sensor
        if ultrasonic_distance <= 30:

            print("Ultrasonic Sensor: Obstacle very close!")

        elif ultrasonic_distance <= 80:

            print("Ultrasonic Sensor: Obstacle detected nearby.")

        else:

            print("Ultrasonic Sensor: Path is clear.")

        # Check LiDAR sensor
        if lidar_distance <= 30:

            print("LiDAR Sensor: Obstacle very close!")

        elif lidar_distance <= 80:

            print("LiDAR Sensor: Obstacle detected nearby.")

        else:

            print("LiDAR Sensor: Path is clear.")

    # SECTION 6: MAKE MOVEMENT DECISION

    def make_decision(self):

        ultrasonic_distance = self.ultrasonic.distance
        lidar_distance = self.lidar.distance

        print("\nRobot Decision:")

        # If either sensor detects a close obstacle, stop
        if ultrasonic_distance <= 30 or lidar_distance <= 30:

            self.status = "STOPPED"

            print("Obstacle too close!")
            print("Robot must STOP.")

        # If an obstacle is nearby, move slowly
        elif ultrasonic_distance <= 80 or lidar_distance <= 80:

            self.status = "SLOW"

            print("Obstacle nearby.")
            print("Robot should move slowly.")

        # Otherwise, move normally
        else:

            self.status = "MOVING"

            print("No nearby obstacles.")
            print("Robot can move normally.")

    # SECTION 7: DISPLAY ROBOT STATUS

    def display_status(self):

        print("\n------------------------------")
        print("ROBOT STATUS")
        print("------------------------------")

        print("Robot Name:", self.robot_name)
        print("Current Status:", self.status)

        print("------------------------------")


# SECTION 8: CREATE ROBOT OBJECT

robot = Robot("WarehouseBot")


# SECTION 9: MAIN MENU

while True:

    print("\n================================")
    print(" ROBOT SENSOR MONITORING SYSTEM ")
    print("================================")

    print("1. Read Sensor Data")
    print("2. Detect Obstacles")
    print("3. Make Movement Decision")
    print("4. Display Robot Status")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        robot.read_sensors()

    elif choice == "2":

        # Read sensors before checking obstacles
        robot.read_sensors()
        robot.check_obstacles()

    elif choice == "3":

        # Read sensors before making a decision
        robot.read_sensors()
        robot.make_decision()
        robot.display_status()

    elif choice == "4":

        robot.display_status()

    elif choice == "5":

        print("\nShutting down Sensor Monitoring System.")
        print("Thank you!")

        break

    else:

        print("\nInvalid choice. Please try again.")
