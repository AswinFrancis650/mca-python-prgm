students = {
    "Anu": 85,
    "Ravi": 90, 
    "Minu": 75, 
    "Sara": 88, 
    "Tom": 94
}

print("Student Dictionary:", students)
print("The Value of Sara:", students["Sara"])

students["Kiran"] = 80
students.update({"Minu": 82})
print("New student Kiran is added and Minu's mark updated:", students)

students.pop("Tom")
print("Deleted Tom from the dictionary:", students)
key = students.keys()
print("The Keys are:", key)

values = students.values()
print("The Values are:", values)

keyvalue = students.items()
print("Key-Value pairs:", keyvalue)

print("Sorted Keys:", sorted(key))
print("Dictionary sorted by values (ascending):", dict(sorted(students.items(), key=lambda x: x[1])))

x = max(students, key=students.get)
print("The Top Scorer is:", x)

stud = {
    "Anusha": 85, 
    "Navin": 70, 
    "Libin": 75
}

print("Second Dictionary:", stud)

students.update(stud)
print("Merged Dictionaries:", students) 
