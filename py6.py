list1=list(map(int,input("Enter the list Elements: ").split()))
list2=list(map(int,input("Enter the list Elements: ").split()))
print(f"LIST1:{list1}\n LIST2:{list2}")
if len(list1)>len(list2):
  print(f"List 1 has more Element,{len(list1)} elements")
elif len(list1)<len(list2):
  print(f"List 2 has more Element,{len(list2)} elements")
else:
  print(f"List1 and 2 both are of same length, {len(list1)} elements")
 
if sum(list1)==sum(list2):
  print(f"Sum of both lists are same,{sum(list1)}")
else:
  print(f"Sum is different, sum of list1={sum(list1)}, sum of list2={sum(list2)}")

for i in range(0,len(list1)):  
  for j in range(0,len(list2)):
    if list1[i]==list2[j]:
       print(f"{list1[i]} occurs in both")
