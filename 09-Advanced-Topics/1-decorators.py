# Using decorators to modify function behavior

def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before", original_function.__name__)
        return original_function()
    return wrapper_function

@decorator_function
def say_hello():
    print("Hello, World!")

say_hello()
