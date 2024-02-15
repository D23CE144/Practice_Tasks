original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_indices_list = []
odd_indices_list = []

for index, element in enumerate(original_list):
    if index % 2 == 0:
        even_indices_list.append(element)
    else:
        odd_indices_list.append(element)

print("Elements at even indices:", even_indices_list)
print("Elements at odd indices:", odd_indices_list)
