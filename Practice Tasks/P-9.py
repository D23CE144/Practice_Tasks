# Create sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Displaying f sets
print("Elements in set1: ",set1)
print("Elements in set2: ",set2)

# Union of Sets
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

# Intersection of Sets
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

# Difference of Sets
difference_set = set1.difference(set2)
print("Elements in set1 but not in set2:", difference_set)

# Check Subset
if set1.issubset(set2):
    print("set1 is a subset of set2")
else:
    print("set1 is not a subset of set2")
