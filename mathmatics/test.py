# Given list of numbers
a = [23, 17, 13, 42, 91, 83, 156, 248, 78]

# Empty list to store multiples of 13
b = []

# Iterate through each number in the list 'a'
for i in a:
    # Check if the number is a multiple of 13
    if i % 13 == 0:
        # Append the number to list 'b'
        b.append(i)

# Print the list containing multiples of 13
print(b)