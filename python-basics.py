# ================================================
# PART 1: DATA TYPES
# ================================================

# STRING — any text, always inside quotes
from unittest import result


service_name = "Amazon EC2"
region = "us-east-1"
status = 'running'          # single quotes work too

# INTEGER — whole numbers, no decimal
max_instances = 10
free_tier_hours = 750
port_number = 22

# FLOAT — numbers with decimals
cost_per_hour = 0.0116
storage_per_gb = 0.023

# BOOLEAN — only two values: True or False
is_free_tier = True
is_stopped = False

# Now let's see what TYPE each variable is
print(type(service_name))
print(type(max_instances))
print(type(cost_per_hour))
print(type(is_free_tier))

# Converting between types
hours_as_string = "750"          # this is text, not a number
hours_as_integer = int(hours_as_string)   # now it's a number
print(hours_as_integer + 100)    # 850 — math works now

cost_as_string = str(cost_per_hour)      # turn float into text
print("The cost is: " + cost_as_string)  # can now join with text

# ================================================
# PART 2: IF / ELIF / ELSE
# ================================================

hours_used = 2000

if hours_used <= 750:
    print("FREE TIER — no charge")
elif hours_used <= 1500:
    billed_hours = hours_used - 750
    print(f"PAID TIER — {billed_hours} hours billed")
else:
    print("HIGH USAGE — consider a Reserved Instance")

    cpu_percent = 85
instance_running = True

# AND — both must be True
if cpu_percent > 80 and instance_running:
    print("WARNING: High CPU on running instance")

# OR — at least one must be True
if cpu_percent > 90 or instance_running == False:
    print("ACTION REQUIRED")

# ================================================
# PART 3: FOR LOOPS
# ================================================

aws_regions = ["us-east-1", "us-west-2", "eu-west-1", "ap-south-1"]

# Basic loop — go through every item
for region in aws_regions:
    print(region)

    # enumerate() gives you the index (position) + the item
for index, region in enumerate(aws_regions, 1):
    print(f"  {index}. {region}")

    # Only print US regions
for region in aws_regions:
    if region.startswith("us-"):
        print(f"US region found: {region}")

        # ================================================
# PART 4: WHILE LOOPS
# ================================================

# while loops keep running as long as the condition is True
countdown = 5

while countdown > 0:
    print(f"Shutting down instance in {countdown}...")
    countdown -= 1       # countdown = countdown - 1

print("Instance stopped.")

attempts = 0

while True:                    # this would run forever without break
    attempts += 1
    print(f"Connection attempt {attempts}...")

    if attempts == 3:
        print("Connected!")
        break                  # exit the loop immediately

    instances = ["i-001", "stopped", "i-002", "stopped", "i-003"]

for instance in instances:
    if instance == "stopped":
        continue               # skip this item, go to next
    print(f"Processing instance: {instance}")

    # ================================================
# PART 5: FUNCTIONS
# ================================================

# Basic structure
def function_name(parameter1, parameter2):
    # code goes here
    return result

# Function with one parameter
def check_free_tier(hours_used):
    if hours_used <= 750:
        return "Within free tier"
    else:
        billed = hours_used - 750
        return f"{billed} hours will be charged"

# Call the function with different inputs
print(check_free_tier(400))
print(check_free_tier(900))

def calculate_ec2_cost(hours, rate=0.0116):
    # rate has a default value — optional to pass in
    cost = hours * rate
    return round(cost, 4)        # round() limits decimal places

print(calculate_ec2_cost(100))          # uses default rate

def get_instance_info(hours_used, storage_gb):
    compute_cost = round(hours_used * 0.0116, 4)
    storage_cost = round(storage_gb * 0.023, 4)
    total = round(compute_cost + storage_cost, 4)
    return compute_cost, storage_cost, total

# Unpack all three return values
compute, storage, total = get_instance_info(100, 50)
print(f"Compute: ${compute}")
print(f"Storage: ${storage}")
print(f"Total:   ${total}")