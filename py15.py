numbers = list(map(int,input("Enter the list elements:").split()))
result = [num for num in numbers if num % 2 != 0]
print("Original list:", numbers)
print("List after removing even numbers:", result)
