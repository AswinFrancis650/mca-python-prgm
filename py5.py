list1=list(input("Enter the colours:").split())
print("List1:",list1)
print(f"First colour:{list1[0]}\nlast colour:{list1[-1]}")
list2=list(input("Enter the colours(list2):").split())
new=[x for x in list1 if x not in list2]
print("List2:",list2)
print("Colours in list1 that are not in list 2:",new)
