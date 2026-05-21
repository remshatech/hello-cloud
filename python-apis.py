# ================================================
# PART 1: LISTS
# ================================================

# A list holds multiple items in order
aws_services = ["S3", "EC2", "Lambda", "IAM", "CloudWatch"]

# --- Indexing ---
# Each item has a position number starting at 0
print(aws_services[0])    # S3    ← first item
print(aws_services[1])    # EC2   ← second item
print(aws_services[-1])   # CloudWatch ← last item (negative counts from end)
print(aws_services[-2])   # IAM   ← second to 

# --- Slicing ---
# Get a portion of the list: [start:end]
# end is NOT included
print(aws_services[0:2])   # ['S3', 'EC2'] — items at index 0 and 1
print(aws_services[1:4])   # ['EC2', 'Lambda', 'IAM']
print(aws_services[:3])    # ['S3', 'EC2', 'Lambda'] — from start to index 2
print(aws_services[2:])    # ['Lambda', 'IAM', 'CloudWatch'] — from index 2 to end

# --- List Methods ---
regions = ["us-east-1", "us-west-2", "eu-west-1"]

regions.append("ap-south-1")       # add to end
print(regions)

regions.insert(0, "us-east-2")     # insert at position 0 (beginning)
print(regions)

regions.remove("eu-west-1")        # remove by value
print(regions)

regions.sort()                     # sort alphabetically
print(regions)

print(len(regions))                # count how many items

# Check if something exists in a list
if "us-east-1" in regions:
    print("us-east-1 is in our region list")

if "ap-southeast-1" not in regions:
    print("ap-southeast-1 is NOT in our region list")

# ================================================
# PART 2: DICTIONARIES
# ================================================

# Create a dictionary — curly braces, key: value pairs
ec2_instance = {
    "instance_id":   "i-1234567890abc",
    "instance_type": "t2.micro",
    "state":         "running",
    "region":        "us-east-1",
    "cpu_usage":     45
}

# --- Access values ---
print(ec2_instance["instance_type"])   # t2.micro
print(ec2_instance["state"])           # running

# --- Add and update ---
ec2_instance["public_ip"] = "54.23.101.5"    # add a new key
ec2_instance["state"] = "stopped"             # update existing key
ec2_instance["cpu_usage"] = 0                 # update to new value

print(ec2_instance)

# --- Loop through a dictionary ---
print("\nInstance Details:")
for key, value in ec2_instance.items():
    print(f"  {key}: {value}")

# --- Get just keys or just values ---
print("\nKeys:")
for key in ec2_instance.keys():
    print(f"  {key}")

print("\nValues:")
for value in ec2_instance.values():
    print(f"  {value}")

# --- Check if a key exists ---
if "public_ip" in ec2_instance:
    print(f"Public IP: {ec2_instance['public_ip']}")

if "private_ip" not in ec2_instance:
    print("No private IP stored")

# ================================================
# PART 3: FILE HANDLING
# ================================================

# --- Write to a file ---
# "w" mode — write (creates file if not exists, OVERWRITES if it does)
with open("cloud-report.txt", "w") as f:
    f.write("AWS Resource Report\n")
    f.write("=" * 30 + "\n")
    f.write("Date: May 2026\n")
    f.write("\n")

# --- Append to a file ---
# "a" mode — append (adds to end, does NOT overwrite)
instances = [
    {"id": "i-001", "type": "t2.micro",  "state": "running"},
    {"id": "i-002", "type": "t2.small",  "state": "stopped"},
    {"id": "i-003", "type": "t2.medium", "state": "running"},
]
with open("cloud-report.txt", "a") as f:
    for instance in instances:
        f.write(f"Instance: {instance['id']} | {instance['type']} | {instance['state']}\n")

# --- Read a file ---
# "r" mode — read
with open("cloud-report.txt", "r") as f:
    content = f.read()       # reads entire file as one string
    print(content)

# --- Read line by line ---
with open("cloud-report.txt", "r") as f:
    for line in f:
        print(line.strip())   # .strip() removes the \n at end of each 
        
#===============================================
# PART 4: APIs
#===============================================

import requests

# requests.get() sends a GET request to a URL
# It's like your browser visiting a webpage - but returns data (JSON) not html

response = requests.get("https://wttr.in/Orlando?format=j1")
print(response.status_code)  # 200 means success, 404 means not found
print(type(response))         # <class 'requests.models.Response'>

# .json() converts the response text into a Python 
data = response.json()
print(type(data))             # <class 'dict'>

# The weather data is nested — drill down to find it
current = data["current_condition"][0]   # first item in the list

# Print everything to see what's available
print("\nAll current weather fields:")
for key, value in current.items():
    print(f"  {key}: {value}")

# Extract only what we need
temp_f       = current["temp_F"]
temp_c       = current["temp_C"]
feels_like_f = current["FeelsLikeF"]
humidity     = current["humidity"]
wind_mph     = current["windspeedMiles"]
description  = current["weatherDesc"][0]["value"]   # nested one more level

print(f"\nCity: Orlando")
print(f"Temperature: {temp_f}°F / {temp_c}°C")
print(f"Feels like:  {feels_like_f}°F")
print(f"Humidity:    {humidity}%")
print(f"Wind:        {wind_mph} mph")
print(f"Condition:   {description}")    