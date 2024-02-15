# Create a dictionary named student
student = {
    'name': 'John',
    'age': 18,
    'grade': 'B'
}

# Accessing dictionary values
print("The name of the student is:", student['name'])
print("The age of the student is:", student['age'])
print("The grade of the student is:", student['grade'])

# Modify dictionary values
student['grade'] = 'A'

# Updated student grade
print("The updated grade of the student is:", student['grade'])

# Checking if 'gender' key is present
if 'gender' in student:
    print("The 'gender' key is present in the student dictionary.")
else:
    print("The 'gender' key is not present in the student dictionary.")
