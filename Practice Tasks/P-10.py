# Create a dictionary where keys are subjects and values are sets of students
subjects_students = {
    'math': {'Raj', 'Rohit', 'Mohit'},
    'science': {'Mohit', 'Jayesh', 'Vishal'}
}

# Add a new student to the 'math' subject
subjects_students['math'].add('Mukesh')

# Remove a student from the 'science' subject
subjects_students['science'].remove('Vishal')

# Find and print the students who take both 'math' and 'science'
common_students = subjects_students['math'].intersection(subjects_students['science'])
print("Students who take both 'math' and 'science':", common_students)

# Create a nested dictionary for countries, cities, and populations
countries = {
    'USA': {'New York': 8_623_000, 'Los Angeles': 3_898_000, 'Chicago': 2_705_000},
    'China': {'Shanghai': 24_281_000, 'Beijing': 21_516_000, 'Guangzhou': 14_904_000},
    'India': {'Mumbai': 18_394_000, 'Delhi': 16_787_000, 'Bangalore': 11_431_000}
}

print("\nNested Dictionary - Countries, Cities, and Populations:")
for country, cities in countries.items():
    print(f"\n{country}:")
    for city, population in cities.items():
        print(f"{city}: {population}")
