import sys
def array_of_name(dictionary):
    full_name= []
    for first_name, last_name in dictionary.items():
        full_name.append(f"{first_name.capitalize()}{last_name.capitalize()}")
    return full_name
dictionary = {
    "mitree":"kumsu"
}
result = array_of_name(dictionary)
print(result)