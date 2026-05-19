# cloud-cost-calculator.py
# A CLI tool to estimate AWS EC2 and S3 costs
# Demonstrates: data types, if/elif/else, loops, functions
# Author: Saurav
# Day 3 of 30-day cloud engineeering program

#==============================================================
# FUNCTIONS - define first so they can be used below
#==============================================================

def calculate_ec2_cost(hours, instance_type="t2.micro"):
    """
    Calculate EC2 cost based on hours and instance type.
    Default is t2.micro (free tier eligible).
    """     
    rates = {
        "t2.micro": 0.0116,
        "t2.small": 0.023,
        "t2.medium": 0.0464,
        "t3.micro": 0.0104,
    }
    
    if instance_type not in rates:
        return "Unknown instance type"
    
    rate = rates[instance_type]
    cost = hours * rate
    return round(cost, 4)

def calculate_s3_cost(storage_gb):
    """
    Calculate S3 monthly storage cost.
    First 5GB is free tier.
    """
    if storage_gb <= 5:
        return 0.0
    billable_gb = storage_gb - 5
    cost = billable_gb * 0.023
    return round(cost, 4)

def print_divider():
    """Prints a visual separator line."""
    print("-" * 40)

def display_report(service, details, cost):
    """Formats and prints the cost report."""
    print(f"\nService: {service}")
    print(f"Details: {details}")
    if cost == 0:
        print("Cost:    FREE (within free tier)")
    else:
        print(f"Cost:    ${cost} per month")

#==============================================================
# MAIN PROGRAM - rums when you execute the script
#==============================================================

print("=" * 40)
print("   AWS COST Estimator")
print("   Day 3 - Cloud Engineering")
print("=" * 40)

#List of avvailable services
services = ["EC2", "S3", "Exit"]

while True:
    print("\nWhat would you like to estimate?")

    for i, service in enumerate(services, 1):
        print(f"  {i}. {service}")

    choice = input("\nEnter number:")

    # ---- EC2 CALCULATION ----
    if choice == "1":
        print_divider()
        print("EC2 Cost Estimator")
        print_divider()
        
        hours = float(input("Hours per month (max 744):"))
        print("\nInstance types:")
        print(" 1. t2.micro ($0.0116/hr) - free tier eligible")
        print(" 2. t2.small ($0.023/hr)")
        print(" 3. t2.medium ($0.0464/hr)")
        print(" 4. t3.micro ($0.0104/hr)")
        instance_choice = input("nChoose instance (1-4): ")

        instance_map = {
            "1": "t2.micro",
            "2": "t2.small",
            "3": "t2.medium",
            "4": "t3.micro"
        }
        instance_type = instance_map.get(instance_choice, "t2.micro")
        cost = calculate_ec2_cost(hours, instance_type)

        if hours <= 750 and instance_type == "t2.micro":
            display_report("EC2", f"{instance_type} for {hours} hrs", 0)
            print("(t2.micro is free tier for first 750 hrs/month)")
        else:
            display_report("EC2", f"{instance_type} for {hours} hrs", cost)

    # ---- S3 CALCULATION ----
    elif choice == "2":
        print_divider()
        print("S3 Cost Estimator")
        print_divider()
        
        storage = float(input("Storage in GB: "))
        cost = calculate_s3_cost(storage)
        display_report("S3", f"{storage} GB storage", cost)

    # ---- EXIT ----
    elif choice == "3":
        print("\nExiting Cost Estimator . Good luck with AWS!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")