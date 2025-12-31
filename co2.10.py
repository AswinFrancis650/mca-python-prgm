'''Generate positive list of numbers from a given list of integers '''
numbers = input("Enter integers: ").split(",") 
numbers = [int(num) for num in numbers] 
positive_list = []                              
for x in numbers: 
    if x > 0:                                   
       positive_list.append(x)       
print("Positive numbers:", positive_list) 

''' Square of N numbers'''
n = int(input("Enter N: ")) 
squares = [] 
for i in range(1, n+1): 
squares.append(i * i)   
print("Squares:", squares) 

'''Form a list of vowels selected from a given word '''
word = input("Enter a word: ") 
vowels = ['a', 'e', 'i', 'o', 'u'] 
vowel_list = [] 
for ch in word: 
   if ch.lower() in vowels:   
        vowel_list.append(ch 
print("Vowels in the word:", vowel_list) 
