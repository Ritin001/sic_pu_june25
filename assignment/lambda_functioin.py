import re #regular expressions
#extract the numbers in the string returns list of 2D;
data1 = ["Hello123", "Hi1100m82111", "No143numbers"]
cleaned1 = list(map(lambda s: re.findall(r'\d+', s), data1))
print(cleaned1)

# Remove all non-alphabetic characters
data2 = ["Hello123", "A@B#C", "Clean_text", "X Y Z"]
cleaned2 = list(map(lambda s: re.sub(r'[^a-zA-Z]', '', s), data2))#r- recturn the value inside the simngle quotes
print(cleaned2) 

# Extract domain using regex
emails = ["alice@gmail.com", "bob@yahoo.com", "user@outlook.com"]
domains = list(map(lambda s: re.search(r'@(\w+)\.com', s).group(1), emails))
print(domains)  # ['gmail', 'yahoo', 'outlook']


# Capitalize all the 

words = ["apple", "banana", "orange", "grape", "umbrella"]

vowel_caps = list(map(lambda w: re.sub(r'^[aeiou](\w+)', lambda m: m.group().upper(), w), words))
print(vowel_caps)  # ['Apple', 'banana', 'Orange', 'grape', 'Umbrella']