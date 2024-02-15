# Given list
my_list = [1, 2, 3, 4, 3, 2, 1]

# Check if the list is a palindrome using slicing
is_palindrome = my_list == my_list[::-1]

# Print the result
if is_palindrome:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")
