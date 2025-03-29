# Raising custom exceptions

def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above.")
    print("Access granted.")

try:
    age = int(input("Enter your age: "))
    check_age(age)
except ValueError as e:
    print("Error:", e)
