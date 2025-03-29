# Using finally to execute code regardless of exceptions

try:
    file = open("sample.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found!")
finally:
    print("Closing file...")
    file.close()
