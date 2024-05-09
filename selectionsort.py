# Define a list of integers
numbers = [64, 25, 12, 22, 11]

# Iterate through each index in the range of the length of the list
for current_index in range(len(numbers)):
    # Initialize min_index to the current index
    min_index = current_index
    # Iterate through the sublist starting from current_index+1 to the end of the list
    for j in range(current_index+1, len(numbers)):
        # Check if the element at the current minimum index is greater than the element at index j
        if numbers[min_index] > numbers[j]:
            # If so, update min_index to j
            min_index = j
    # Swap the elements at indices current_index and min_index
    numbers[current_index], numbers[min_index] = numbers[min_index], numbers[current_index]

# Print the sorted array
print("Sorted array : ")
# Iterate through each element in the sorted list
for num in numbers:
    # Print the element followed by a space
    print("%d" % num, end=" ")



'''
# Define a list of integers
numbers = [64, 25, 12, 22, 11]  # This initializes a list named 'numbers' with unsorted integers.

# Iterate through each index in the range of the length of the list
for current_index in range(len(numbers)):  # Start a loop over the indices of 'numbers'.
    # Initialize min_index to the current index
    min_index = current_index  # Set 'min_index' to the current position in the loop.

    # Iterate through the sublist starting from current_index+1 to the end of the list
    for j in range(current_index+1, len(numbers)):  # Loop over the sublist after 'current_index'.
        # Check if the element at the current minimum index is greater than the element at index j
        if numbers[min_index] > numbers[j]:  # Compare the current min element with the next element in the sublist.
            # If so, update min_index to j
            min_index = j  # Update 'min_index' if a new minimum is found.

    # Swap the elements at indices current_index and min_index
    numbers[current_index], numbers[min_index] = numbers[min_index], numbers[current_index]  # Swap the found minimum element with the first element of the unsorted part.

# Print the sorted array
print("Sorted array : ")  # Print a message indicating the next output will be the sorted array.

# Iterate through each element in the sorted list
for num in numbers:  # Loop over each number in the sorted 'numbers' list.
    # Print the element followed by a space
    print("%d" % num, end=" ")  # Print each number followed by a space instead of a newline.
'''