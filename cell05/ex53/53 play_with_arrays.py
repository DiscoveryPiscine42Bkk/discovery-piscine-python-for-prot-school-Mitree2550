original_array = [2, 8, 9, 48, 8, 22, -12, 2]

new_array_set = set()

for number in original_array:
    if number > 5 :
      new_array_set.add(number + 2)

new_array = list(new_array_set)

print("Original array:", original_array)
print("New array (only values > 5 , each +2):", new_array)