names = input("Enter first names separated by spaces: ").split()
print("\nList of names:", names)
count_names = len(names)
print("Number of elements in the list:", count_names)
count_a = 0
for name in names:
    count_a += name.lower().count('a')

print("Total occurrences of 'a' in the list:", count_a) 
