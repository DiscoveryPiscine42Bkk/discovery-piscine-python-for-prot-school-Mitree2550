import sys
def greetings(name="noble stranger"):
    if isinstance(name, str):
        print(f"Welcome, {name}!")
    else:
        print("Error: The name must be a string.")
greetings()