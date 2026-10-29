 
# ============================================================
# CHAPTER 11: DICTIONARIES AND SETS
# Repository: python-for-robotics
# Goal: Learn to organize data using dictionaries and sets.
# ============================================================


# ============================================================
# SECTION 1: WHAT IS A DICTIONARY?
# ============================================================

# A dictionary stores data in key-value pairs.
# Each key is associated with a value.
#
# Syntax:
# dictionary = {
#     "key": value
# }

robot = {
    "name": "WarehouseBot",
    "id": 101,
    "battery": 85,
    "status": "Active"
}

print("Robot information:", robot)


# ============================================================
# SECTION 2: ACCESSING DICTIONARY VALUES
# ============================================================

# We can access values using their keys.

print("Robot name:", robot["name"])
print("Robot ID:", robot["id"])
print("Battery level:", robot["battery"])
print("Robot status:", robot["status"])


# ============================================================
# SECTION 3: USING get()
# ============================================================

# get() returns the value associated with a key.
# If the key does not exist, it returns None by default.

print("Robot name:", robot.get("name"))
print("Robot speed:", robot.get("speed"))

# We can provide a default value.

print("Robot speed:", robot.get("speed", 0))


# ============================================================
# SECTION 4: ADDING NEW KEY-VALUE PAIRS
# ============================================================

# Assigning a value to a new key adds it to the dictionary.

robot["speed"] = 2.5
robot["location"] = "Warehouse A"

print("Updated robot information:", robot)


# ============================================================
# SECTION 5: MODIFYING EXISTING VALUES
# ============================================================

# Assigning a new value to an existing key updates it.

robot["battery"] = 75
robot["status"] = "Moving"

print("Updated battery:", robot["battery"])
print("Updated status:", robot["status"])


# ============================================================
# SECTION 6: REMOVING DICTIONARY ITEMS
# ============================================================

# pop() removes an item using its key
# and returns the value.

robot = {
    "name": "WarehouseBot",
    "battery": 80,
    "speed": 2.5
}

removed_speed = robot.pop("speed")

print("Removed speed:", removed_speed)
print("Remaining robot information:", robot)


# ============================================================
# SECTION 7: CHECKING WHETHER A KEY EXISTS
# ============================================================

# The 'in' operator checks whether a key exists.

robot = {
    "name": "WarehouseBot",
    "battery": 80,
    "status": "Ready"
}

print("Does name exist?", "name" in robot)
print("Does speed exist?", "speed" in robot)


# ============================================================
# SECTION 8: GETTING ALL KEYS
# ============================================================

# keys() returns all dictionary keys.

robot = {
    "name": "WarehouseBot",
    "battery": 80,
    "speed": 2.5
}

print("Robot keys:", robot.keys())


# ============================================================
# SECTION 9: GETTING ALL VALUES
# ============================================================

# values() returns all dictionary values.

print("Robot values:", robot.values())


# ============================================================
# SECTION 10: GETTING ALL KEY-VALUE PAIRS
# ============================================================

# items() returns all key-value pairs.

print("Robot items:", robot.items())


# ============================================================
# SECTION 11: LOOPING THROUGH A DICTIONARY
# ============================================================

# A for loop can process each key in a dictionary.

robot = {
    "name": "WarehouseBot",
    "battery": 80,
    "speed": 2.5,
    "status": "Ready"
}

for key in robot:
    print("Key:", key)


# ============================================================
# SECTION 12: LOOPING THROUGH VALUES
# ============================================================

for value in robot.values():
    print("Value:", value)


# ============================================================
# SECTION 13: LOOPING THROUGH KEY-VALUE PAIRS
# ============================================================

# items() allows us to access both the key and value.

for key, value in robot.items():
    print(key, ":", value)


# ============================================================
# SECTION 14: DICTIONARY OF SENSOR READINGS
# ============================================================

# Store sensor readings using meaningful names.

sensor_readings = {
    "lidar": 3.5,
    "ultrasonic": 1.2,
    "infrared": 0.8
}

print("Sensor readings:", sensor_readings)

print("Lidar distance:", sensor_readings["lidar"])
print("Ultrasonic distance:", sensor_readings["ultrasonic"])
print("Infrared distance:", sensor_readings["infrared"])


# ============================================================
# SECTION 15: UPDATING SENSOR READINGS
# ============================================================

# A robot may receive new readings continuously.

sensor_readings["lidar"] = 2.8
sensor_readings["ultrasonic"] = 0.9

print("Updated sensor readings:", sensor_readings)


# ============================================================
# SECTION 16: DICTIONARY LENGTH
# ============================================================

# len() returns the number of key-value pairs.

print("Number of sensors:", len(sensor_readings))


# ============================================================
# SECTION 17: CLEARING A DICTIONARY
# ============================================================

# clear() removes all key-value pairs.

temporary_data = {
    "battery": 80,
    "speed": 2.5
}

print("Before clearing:", temporary_data)

temporary_data.clear()

print("After clearing:", temporary_data)


# ============================================================
# SECTION 18: NESTED DICTIONARIES
# ============================================================

# A dictionary can contain another dictionary.

robot = {
    "name": "WarehouseBot",
    "sensors": {
        "lidar": 3.5,
        "camera": "Active",
        "ultrasonic": 1.2
    }
}

print("Robot name:", robot["name"])
print("Lidar reading:", robot["sensors"]["lidar"])
print("Camera status:", robot["sensors"]["camera"])


# ============================================================
# SECTION 19: DICTIONARY WITH A LIST
# ============================================================

# A dictionary value can be a list.

robot = {
    "name": "WarehouseBot",
    "tasks": ["Move", "Scan", "Pick", "Place"]
}

print("Robot name:", robot["name"])
print("Robot tasks:", robot["tasks"])
print("First task:", robot["tasks"][0])


# ============================================================
# SECTION 20: LIST OF DICTIONARIES
# ============================================================

# A list can store multiple dictionaries.
# This is useful when multiple robots are present.

robots = [
    {"name": "Robot A", "battery": 90},
    {"name": "Robot B", "battery": 75},
    {"name": "Robot C", "battery": 60}
]

for robot in robots:
    print("Robot name:", robot["name"])
    print("Battery:", robot["battery"])


# ============================================================
# SECTION 21: WHAT IS A SET?
# ============================================================

# A set stores unique values.
# Sets use curly braces {}.
#
# Duplicate values are automatically removed.

sensor_types = {"Lidar", "Camera", "GPS", "Lidar"}

print("Sensor types:", sensor_types)


# ============================================================
# SECTION 22: CREATING A SET
# ============================================================

robot_sensors = {"Lidar", "Camera", "Ultrasonic"}

print("Robot sensors:", robot_sensors)


# ============================================================
# SECTION 23: ADDING ITEMS TO A SET
# ============================================================

# add() adds one item to a set.

robot_sensors.add("GPS")

print("Updated sensors:", robot_sensors)


# ============================================================
# SECTION 24: REMOVING ITEMS FROM A SET
# ============================================================

# remove() deletes an item.
# It raises an error if the item does not exist.

robot_sensors.remove("Camera")

print("After removing Camera:", robot_sensors)


# discard() removes an item if it exists.
# It does not raise an error if the item is missing.

robot_sensors.discard("Radar")

print("After discarding Radar:", robot_sensors)


# ============================================================
# SECTION 25: CHECKING ITEMS IN A SET
# ============================================================

print("Is Lidar available?", "Lidar" in robot_sensors)
print("Is Radar available?", "Radar" in robot_sensors)


# ============================================================
# SECTION 26: LOOPING THROUGH A SET
# ============================================================

# Sets do not guarantee a particular order.

for sensor in robot_sensors:
    print("Sensor:", sensor)


# ============================================================
# SECTION 27: SET LENGTH
# ============================================================

print("Number of unique sensors:", len(robot_sensors))


# ============================================================
# SECTION 28: SET UNION
# ============================================================

# Union combines elements from two sets.
# Duplicate elements appear only once.

navigation_sensors = {"Lidar", "GPS"}
vision_sensors = {"Camera", "Depth Camera"}

all_sensors = navigation_sensors.union(vision_sensors)

print("All sensors:", all_sensors)


# ============================================================
# SECTION 29: SET INTERSECTION
# ============================================================

# Intersection finds elements common to both sets.

robot_a_sensors = {"Lidar", "Camera", "GPS"}
robot_b_sensors = {"Camera", "GPS", "Radar"}

common_sensors = robot_a_sensors.intersection(robot_b_sensors)

print("Common sensors:", common_sensors)


# ============================================================
# SECTION 30: SET DIFFERENCE
# ============================================================

# Difference finds elements present in one set
# but not in the other.

robot_a_sensors = {"Lidar", "Camera", "GPS"}
robot_b_sensors = {"Camera", "GPS", "Radar"}

unique_to_robot_a = robot_a_sensors.difference(robot_b_sensors)

print("Sensors unique to Robot A:", unique_to_robot_a)


# ============================================================
# SECTION 31: CONVERTING A LIST TO A SET
# ============================================================

# Conversion to a set removes duplicates.

sensor_list = ["Lidar", "Camera", "Lidar", "GPS", "Camera"]

unique_sensors = set(sensor_list)

print("Original list:", sensor_list)
print("Unique sensors:", unique_sensors)


# ============================================================
# SECTION 32: DICTIONARY VS SET
# ============================================================

# Dictionary: key-value pairs.
robot_data = {
    "name": "WarehouseBot",
    "battery": 85
}

# Set: unique values.
robot_statuses = {"Ready", "Moving", "Charging"}

print("Robot data:", robot_data)
print("Robot statuses:", robot_statuses)


# ============================================================
# SECTION 33: WAREHOUSE ROBOT DATA
# ============================================================

robot = {
    "name": "WarehouseBot",
    "id": 101,
    "battery": 82,
    "speed": 2.5,
    "status": "Moving",
    "position": {
        "x": 10,
        "y": 20
    },
    "sensors": {
        "lidar": 3.2,
        "ultrasonic": 1.4
    }
}

print("Robot name:", robot["name"])
print("Robot battery:", robot["battery"])
print("Robot status:", robot["status"])

print("Robot X position:", robot["position"]["x"])
print("Robot Y position:", robot["position"]["y"])

print("Lidar reading:", robot["sensors"]["lidar"])
print("Ultrasonic reading:", robot["sensors"]["ultrasonic"])


# ============================================================
# SECTION 34: FINAL MINI PROJECT
# WAREHOUSE ROBOT STATUS MONITOR
# ============================================================

print("\n===== WAREHOUSE ROBOT STATUS MONITOR =====")

robot = {
    "name": "WarehouseBot",
    "battery": 75,
    "status": "Ready",
    "sensors": {
        "lidar": 2.5,
        "ultrasonic": 0.8,
        "infrared": 1.2
    },
    "tasks": ["Move", "Scan", "Pick", "Place"]
}

print("Robot:", robot["name"])
print("Battery:", robot["battery"], "%")
print("Status:", robot["status"])

print("\nSensor readings:")

for sensor, distance in robot["sensors"].items():
    print(sensor, ":", distance, "meters")

print("\nTask queue:")

for task in robot["tasks"]:
    print(task)

# Set of available sensors.
available_sensors = {"Lidar", "Camera", "GPS", "Ultrasonic"}

print("\nAvailable sensor types:", available_sensors)
print("Number of available sensor types:", len(available_sensors))

print("\n===== MONITORING COMPLETE =====")


# ============================================================
# END OF CHAPTER 11
# ============================================================
