words = input("Enter words separated by space: ").split() 
longest = 0 
for w in words: 
  if len(w) > longest: 
   longest = len(w) 
print("Length of the longest word:", longest) 
