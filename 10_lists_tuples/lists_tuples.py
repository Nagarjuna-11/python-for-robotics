```python
# ============================================================
# CHAPTER 10: LISTS AND TUPLES
# Repository: python-for-robotics
# Goal: Learn to store and manage collections of data.
# ============================================================


# ============================================================
# SECTION 1: WHAT IS A LIST?
# ============================================================

# A list stores multiple values in a single variable.
# Lists use square brackets [].

robot_sensors = ["Lidar", "Camera", "Ultrasonic", "GPS"]

print("Robot sensors:", robot_sensors)


# ============================================================
# SECTION 2: DIFFERENT TYPES OF DATA IN A LIST
# ============================================================

# A list can contain strings, integers, floats, and booleans.

robot_data = ["WarehouseBot", 101, 85.5, True]

print("Robot data:", robot_data)


# ============================================================
# SECTION 3: ACCESSING LIST ELEMENTS
# ============================================================

# List indexing starts from 0.
#
# Index:       0          1           2
# Example:  ["Lidar", "Camera", "Ultrasonic"]

sensors = ["Lidar", "Camera", "Ultrasonic"]

print("First sensor:", sensors[0])
print("Second sensor:", sensors[1])
print("Third sensor:", sensors[2])


# ============================================================
# SECTION 4: NEGATIVE INDEXING
# ============================================================

# Negative indexing starts from the end of the list.
# Index -1 means the last element.

sensor_names = ["Lidar", "Camera", "GPS", "IMU"]

print("Last sensor:", sensor_names[-1])
print("Second-last sensor:", sensor_names[-2])
print("First sensor:", sensor_names[-4])


# ============================================================
# SECTION 5: FINDING THE LENGTH OF A LIST
# ============================================================

# len() returns the number of elements in a list.

robot_tasks = ["Move", "Scan", "Pick", "Place", "Return"]

print("Robot tasks:", robot_tasks)
print("Number of tasks:", len(robot_tasks))


# ============================================================
# SECTION 6: CHANGING A LIST ELEMENT
# ============================================================

# Lists are mutable.
# Mutable means we can change their contents after creation.

motor_speeds = [20, 30, 40]

print("Original motor speeds:", motor_speeds)

motor_speeds[0] = 25

print("Updated motor speeds:", motor_speeds)

motor_speeds[2] = 50

print("Final motor speeds:", motor_speeds)


# ============================================================
# SECTION 7: ADDING ELEMENTS USING APPEND()
# ============================================================

# append() adds one element to the end of a list.

robot_tasks = ["Move", "Scan"]

print("Before append:", robot_tasks)

robot_tasks.append("Pick")
robot_tasks.append("Place")

print("After append:", robot_tasks)


# ============================================================
# SECTION 8: INSERTING ELEMENTS USING INSERT()
# ============================================================

# insert(index, value) adds an element at a specific position.

robot_tasks = ["Move", "Pick", "Place"]

print("Before insertion:", robot_tasks)

robot_tasks.insert(1, "Scan")

print("After insertion:", robot_tasks)


# ============================================================
# SECTION 9: REMOVING ELEMENTS USING REMOVE()
# ============================================================

# remove() removes the first matching value.
# The value must exist in the list.

robot_tasks = ["Move", "Scan", "Pick", "Place"]

print("Before removal:", robot_tasks)

robot_tasks.remove("Scan")

print("After removing Scan:", robot_tasks)


# ============================================================
# SECTION 10: REMOVING ELEMENTS USING POP()
# ============================================================

# pop() removes and returns an element.
# Without an index, it removes the last element.

robot_tasks = ["Move", "Scan", "Pick", "Place"]

print("Original tasks:", robot_tasks)

completed_task = robot_tasks.pop()

print("Completed task:", completed_task)
print("Remaining tasks:", robot_tasks)

# We can also remove an element using its index.

removed_task = robot_tasks.pop(1)

print("Another removed task:", removed_task)
print("Tasks after pop:", robot_tasks)


# ============================================================
# SECTION 11: CLEARING A LIST
# ============================================================

# clear() removes every element from a list.

temporary_tasks = ["Move", "Scan", "Pick"]

print("Before clearing:", temporary_tasks)

temporary_tasks.clear()

print("After clearing:", temporary_tasks)


# ============================================================
# SECTION 12: CHECKING WHETHER AN ELEMENT EXISTS
# ============================================================

# The 'in' operator checks whether a value exists in a list.

available_sensors = ["Lidar", "Camera", "GPS"]

print("Is Lidar available?", "Lidar" in available_sensors)
print("Is Radar available?", "Radar" in available_sensors)


# ============================================================
# SECTION 13: LOOPING THROUGH A LIST
# ============================================================

# A for loop can process every element in a list.

robot_tasks = ["Move", "Scan", "Pick", "Place"]

for task in robot_tasks:
    print("Executing task:", task)


# ============================================================
# SECTION 14: LIST OF SENSOR READINGS
# ============================================================

# Imagine that a robot collects distance readings
# from an ultrasonic sensor.

distance_readings = [2.5, 1.8, 3.2, 0.9, 4.1]

print("Distance readings:", distance_readings)

for distance in distance_readings:
    print("Measured distance:", distance, "meters")


# ============================================================
# SECTION 15: CALCULATING THE TOTAL OF A LIST
# ============================================================

# sum() adds all numeric elements in a list.

battery_readings = [90, 85, 80, 75, 70]

total_battery = sum(battery_readings)

print("Battery readings:", battery_readings)
print("Total of readings:", total_battery)


# ============================================================
# SECTION 16: CALCULATING THE AVERAGE
# ============================================================

# Average = sum of values / number of values.

temperature_readings = [25.5, 26.0, 25.8, 26.2]

total_temperature = sum(temperature_readings)
number_of_readings = len(temperature_readings)

average_temperature = total_temperature / number_of_readings

print("Temperature readings:", temperature_readings)
print("Average temperature:", average_temperature)


# ============================================================
# SECTION 17: FINDING THE MINIMUM AND MAXIMUM
# ============================================================

# min() returns the smallest value.
# max() returns the largest value.

distance_readings = [2.5, 1.8, 3.2, 0.9, 4.1]

print("Shortest measured distance:", min(distance_readings))
print("Longest measured distance:", max(distance_readings))


# ============================================================
# SECTION 18: LIST SLICING
# ============================================================

# Slicing extracts part of a list.
#
# Syntax:
# list_name[start:end]
#
# The start index is included.
# The end index is excluded.

robot_sensors = ["Lidar", "Camera", "GPS", "IMU", "Radar"]

print("All sensors:", robot_sensors)
print("First two sensors:", robot_sensors[0:2])
print("Sensors from index 1 to 3:", robot_sensors[1:4])
print("First three sensors:", robot_sensors[:3])
print("Sensors from index 2 onward:", robot_sensors[2:])
print("Copy of the list:", robot_sensors[:])


# ============================================================
# SECTION 19: COMBINING TWO LISTS
# ============================================================

# The + operator combines lists into a new list.

navigation_sensors = ["Lidar", "GPS"]
vision_sensors = ["Camera", "Depth Camera"]

all_sensors = navigation_sensors + vision_sensors

print("Navigation sensors:", navigation_sensors)
print("Vision sensors:", vision_sensors)
print("All sensors:", all_sensors)


# ============================================================
# SECTION 20: REPEATING A LIST
# ============================================================

# The * operator repeats the contents of a list.

status = ["Ready"]

repeated_status = status * 3

print("Repeated status:", repeated_status)


# ============================================================
# SECTION 21: SORTING A LIST
# ============================================================

# sort() arranges the list in ascending order by default.
# It changes the original list.

motor_speeds = [40, 10, 30, 20]

print("Before sorting:", motor_speeds)

motor_speeds.sort()

print("After ascending sort:", motor_speeds)

motor_speeds.sort(reverse=True)

print("After descending sort:", motor_speeds)


# ============================================================
# SECTION 22: REVERSING A LIST
# ============================================================

# reverse() reverses the current order of the list.
# It does not sort the values.

robot_tasks = ["Move", "Scan", "Pick", "Place"]

print("Original task order:", robot_tasks)

robot_tasks.reverse()

print("Reversed task order:", robot_tasks)


# ============================================================
# SECTION 23: COPYING A LIST
# ============================================================

# Use copy() to create a separate copy of a list.

original_sensors = ["Lidar", "Camera", "GPS"]

copied_sensors = original_sensors.copy()

copied_sensors.append("IMU")

print("Original sensors:", original_sensors)
print("Copied sensors:", copied_sensors)


# ============================================================
# SECTION 24: INTRODUCTION TO TUPLES
# ============================================================

# A tuple stores multiple values like a list.
# Tuples use parentheses ().
# Tuples cannot be modified after creation.

robot_position = (10, 20, 5)

print("Robot position:", robot_position)
print("X coordinate:", robot_position[0])
print("Y coordinate:", robot_position[1])
print("Z coordinate:", robot_position[2])


# ============================================================
# SECTION 25: LISTS VS TUPLES
# ============================================================

# Lists can be modified.
# Tuples cannot be modified.

robot_speeds = [10, 20, 30]

robot_speeds[0] = 15

print("Modified list:", robot_speeds)


robot_position = (10, 20, 5)

print("Tuple position:", robot_position)

# The following line would produce a TypeError:
# robot_position[0] = 15


# ============================================================
# SECTION 26: TUPLE WITH DIFFERENT DATA TYPES
# ============================================================

robot_information = ("WarehouseBot", 101, 85.5, True)

print("Robot information:", robot_information)
print("Robot name:", robot_information[0])
print("Robot ID:", robot_information[1])
print("Battery percentage:", robot_information[2])
print("Is robot active?", robot_information[3])


# ============================================================
# SECTION 27: TUPLE UNPACKING
# ============================================================

# Tuple unpacking assigns tuple elements to separate variables.

position = (10, 20, 5)

x, y, z = position

print("X coordinate:", x)
print("Y coordinate:", y)
print("Z coordinate:", z)


# ============================================================
# SECTION 28: A TUPLE WITH ONE ELEMENT
# ============================================================

# A comma is required to create a one-element tuple.

single_value_tuple = (10,)

print("Single-element tuple:", single_value_tuple)
print("Type:", type(single_value_tuple))


# ============================================================
# SECTION 29: COUNTING AND FINDING AN ELEMENT IN A TUPLE
# ============================================================

# count() counts how many times a value appears.
# index() returns the index of the first matching value.

sensor_statuses = ("Ready", "Busy", "Ready", "Offline", "Ready")

print("Ready count:", sensor_statuses.count("Ready"))
print("Busy index:", sensor_statuses.index("Busy"))


# ============================================================
# SECTION 30: CONVERTING BETWEEN LISTS AND TUPLES
# ============================================================

# list() converts a tuple into a list.
# tuple() converts a list into a tuple.

position_tuple = (10, 20, 5)

position_list = list(position_tuple)

print("Original tuple:", position_tuple)
print("Converted list:", position_list)

position_list[0] = 15

print("Updated position list:", position_list)

updated_position_tuple = tuple(position_list)

print("Converted back to tuple:", updated_position_tuple)


# ============================================================
# SECTION 31: WAREHOUSE ROBOT SENSOR EXAMPLE
# ============================================================

# A warehouse robot collects several distance measurements.

distances = [3.5, 2.8, 1.9, 0.7, 2.2]

print("Warehouse robot distance measurements:")

for distance in distances:
    print(distance, "meters")

closest_obstacle = min(distances)
farthest_obstacle = max(distances)
average_distance = sum(distances) / len(distances)

print("Closest obstacle:", closest_obstacle, "meters")
print("Farthest obstacle:", farthest_obstacle, "meters")
print("Average measured distance:", average_distance, "meters")


# ============================================================
# SECTION 32: WAREHOUSE ROBOT TASK QUEUE
# ============================================================

# A task queue stores the tasks that the robot must perform.

task_queue = ["Move to shelf A", "Scan barcode", "Pick package"]

print("Initial task queue:", task_queue)

task_queue.append("Move to packing station")

print("Updated task queue:", task_queue)

next_task = task_queue.pop(0)

print("Next task to execute:", next_task)
print("Remaining task queue:", task_queue)


# ============================================================
# SECTION 33: ROBOT POSITION AND SENSOR DATA
# ============================================================

# A tuple can represent a fixed 3D position.
# A list can store multiple sensor readings.

robot_position = (12.5, 8.0, 0.0)

lidar_readings = [4.2, 3.8, 2.1, 1.5, 3.0]

print("Robot's 3D position:", robot_position)
print("Lidar readings:", lidar_readings)

print("Robot X position:", robot_position[0])
print("Robot Y position:", robot_position[1])
print("Robot Z position:", robot_position[2])


# ============================================================
# SECTION 34: FINAL MINI PROJECT
# WAREHOUSEBOT DATA COLLECTION
# ============================================================

print("\n===== WAREHOUSEBOT DATA COLLECTION =====")

robot_name = "WarehouseBot"

# Store the robot's sensor names in a list.
sensors = ["Lidar", "Camera", "Ultrasonic"]

# Store measured distances in a list.
distances = [3.0, 2.5, 1.2, 0.8, 2.7]

# Store the robot's fixed position in a tuple.
position = (15, 8, 0)

print("Robot name:", robot_name)
print("Available sensors:", sensors)
print("Robot position:", position)

print("\nDistance measurements:")

for distance in distances:
    print(distance, "meters")

print("\nSensor count:", len(sensors))
print("Number of distance readings:", len(distances))
print("Closest obstacle:", min(distances), "meters")
print("Farthest obstacle:", max(distances), "meters")

average_distance = sum(distances) / len(distances)

print("Average distance:", average_distance, "meters")

print("\n===== DATA COLLECTION COMPLETE =====")


# ============================================================
# END OF CHAPTER 10
# ============================================================
```
