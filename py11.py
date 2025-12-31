a = input("Enter a list of integers separated by spaces: ") integers = [int(num) for num in a.split()] 
for i in range(len(integers)):     
     if integers[i] > 100:         
        integers[i] = 'over'  
print("Modified list:", integers) 
