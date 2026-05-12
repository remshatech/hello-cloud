# hello_cloud.py
# My first cloud engineering script
# Author: Remsha Shrestha
# Date: May 12, 2026

# Line 1: print()displays text on the screen
print("Hello,Cloud World!")

# Line 2: Variables store information
my_name = "Remsha Shrestha"
cloud_goal = "AWS Cloud Engineer"

# Line 3: f-strings let you put variables inside text
print(f"My name is {my_name}")
print (f"My goal is to become an {cloud_goal}")

# Line 4: A list stores multiple items
aws_services = ["S3", "EC2", "Lambda", "IAM", "CloudWatch"]

# Line 5: A for loop goes through each item in the list
# print("\nAWS Services I will learn:")
# for service in aws_services:
#     print(f" - {services}")

# Line 6: Simple function - a reusable block of code
def greet_cloud(name) :
    return f"Welcome to cloud engineering, {name}!"

# Line 7: Call the function
message = greet_cloud(my_name)
print("\n" + message)