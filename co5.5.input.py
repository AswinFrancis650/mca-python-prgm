import re
word = input("Enter the word to search: ")
filename = "input.txt"
with open(filename, "r") as file:
    text = file.read()
pattern = r'\b' + re.escape(word) + r'\b'
matches = re.findall(pattern, text, flags=re.IGNORECASE)
count = len(matches)
print(f"The word '{word}' occurs {count} times in the file.")
