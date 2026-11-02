
# ============================================================
# MINI PROJECT 1: WAREHOUSE ROBOT SIMULATOR
# Python for Robotics
#
# Concepts used:
# Variables, data types, operators, input/output,
# conditions, loops, functions, lists, dictionaries,
# and classes.
# ============================================================


# ============================================================
# SECTION 1: CREATING THE ROBOT CLASS
# ============================================================

class WarehouseRobot:

    def __init__(self, name, battery):

        # Robot information
        self.name = name

        # Battery percentage
        self.battery = battery

        # Initial robot position
        self.x = 0
        self.y = 0

        # Initial robot status
        self.status = "Ready"

        # Store completed tasks
        self.completed_tasks = []


    # ========================================================
    # SECTION 2: DISPLAY ROBOT INFORMATION
    # ========================================================

    def show_status(self):

        print("\n========== ROBOT STATUS ==========")

        print("Robot Name:", self.name)

        print("Battery:", self.battery, "%")

        print("Position:", self.x, self.y)

        print("Status:", self.status)

        print("Completed Tasks:", self.completed_tasks)

        print("================================")


    # ========================================================
    # SECTION 3: MOVE FORWARD
    # ========================================================

    def move_forward(self, distance):

        # Check whether battery is available.

        if self.battery <= 0:

            print("Robot battery is empty!")

            self.status = "Stopped"

            return

        # Move the robot along the X-axis.

        self.x = self.x + distance

        # Reduce battery based on movement.

        self.battery = self.battery - distance

        # Prevent negative battery values.

        if self.battery < 0:

            self.battery = 0

        self.status = "Moving"

        print("\nRobot moved forward.")

        print("New position:", self.x, self.y)

        print("Battery:", self.battery, "%")


    # ========================================================
    # SECTION 4: MOVE BACKWARD
    # ========================================================

    def move_backward(self, distance):

        if self.battery <= 0:

            print("Robot battery is empty!")

            self.status = "Stopped"

            return

        # Move the robot backward.

        self.x = self.x - distance

        # Reduce battery.

        self.battery = self.battery - distance

        if self.battery < 0:

            self.battery = 0

        self.status = "Moving"

        print("\nRobot moved backward.")

        print("New position:", self.x, self.y)

        print("Battery:", self.battery, "%")


    # ========================================================
    # SECTION 5: MOVE TO A SPECIFIC POSITION
    # ========================================================

    def move_to(self, new_x, new_y):

        if self.battery <= 0:

            print("Robot battery is empty!")

            self.status = "Stopped"

            return

        # Calculate movement distance.

        distance_x = abs(new_x - self.x)

        distance_y = abs(new_y - self.y)

        total_distance = distance_x + distance_y

        # Update position.

        self.x = new_x

        self.y = new_y

        # Reduce battery.

        self.battery = self.battery - total_distance

        if self.battery < 0:

            self.battery = 0

        self.status = "Moving"

        print("\nRobot moved to the target position.")

        print("New position:", self.x, self.y)

        print("Battery:", self.battery, "%")


    # ========================================================
    # SECTION 6: CHARGE THE ROBOT
    # ========================================================

    def charge(self):

        print("\nRobot is charging...")

        self.battery = 100

        self.status = "Ready"

        print("Battery fully charged.")


    # ========================================================
    # SECTION 7: STOP THE ROBOT
    # ========================================================

    def stop(self):

        self.status = "Stopped"

        print("\nRobot stopped.")


    # ========================================================
    # SECTION 8: ASSIGN A TASK
    # ========================================================

    def complete_task(self, task_name):

        print("\nExecuting task:", task_name)

        self.completed_tasks.append(task_name)

        print("Task completed:", task_name)


# ============================================================
# SECTION 9: CREATE THE ROBOT
# ============================================================

robot = WarehouseRobot("WarehouseBot", 100)


# ============================================================
# SECTION 10: MAIN PROGRAM
# ============================================================

print("\n===================================")

print(" WAREHOUSE ROBOT SIMULATOR ")

print("===================================")


# ============================================================
# SECTION 11: MENU
# ============================================================

while True:

    print("\n========== ROBOT MENU ==========")

    print("1. Show Robot Status")

    print("2. Move Forward")

    print("3. Move Backward")

    print("4. Move to Position")

    print("5. Charge Robot")

    print("6. Stop Robot")

    print("7. Complete a Task")

    print("8. Exit")

    print("==============================")

    # Get user choice.

    choice = input("Enter your choice: ")


    # ========================================================
    # OPTION 1: SHOW STATUS
    # ========================================================

    if choice == "1":

        robot.show_status()


    # ========================================================
    # OPTION 2: MOVE FORWARD
    # ========================================================

    elif choice == "2":

        distance = float(input("Enter distance: "))

        if distance > 0:

            robot.move_forward(distance)

        else:

            print("Distance must be positive.")


    # ========================================================
    # OPTION 3: MOVE BACKWARD
    # ========================================================

    elif choice == "3":

        distance = float(input("Enter distance: "))

        if distance > 0:

            robot.move_backward(distance)

        else:

            print("Distance must be positive.")


    # ========================================================
    # OPTION 4: MOVE TO POSITION
    # ========================================================

    elif choice == "4":

        new_x = float(input("Enter target X position: "))

        new_y = float(input("Enter target Y position: "))

        robot.move_to(new_x, new_y)


    # ========================================================
    # OPTION 5: CHARGE ROBOT
    # ========================================================

    elif choice == "5":

        robot.charge()


    # ========================================================
    # OPTION 6: STOP ROBOT
    # ========================================================

    elif choice == "6":

        robot.stop()


    # ========================================================
    # OPTION 7: COMPLETE TASK
    # ========================================================

    elif choice == "7":

        task_name = input("Enter task name: ")

        robot.complete_task(task_name)


    # ========================================================
    # OPTION 8: EXIT
    # ========================================================

    elif choice == "8":

        print("\nExiting Warehouse Robot Simulator.")

        break


    # ========================================================
    # INVALID OPTION
    # ========================================================

    else:

        print("Invalid choice. Please try again.")


# ============================================================
# END OF MINI PROJECT
# ============================================================
