# Create a variable and set it as an List
my_numbers=[12,13,2,45,67,3]
my_words=["apple","google","facebook"]
vowels = ['e', 'a', 'u', 'o', 'i']
print(my_words)
#accessing list elements
print(my_words[0])
print(my_words[1])
print(my_words[2])
#negative indexing
print(my_words[-1])
print(my_words[-2])
print(my_words[-3])
# Adds an element onto the end of a List
my_words.append("Amazon")
print(my_words)
my_words.remove("facebook")
print(my_words)
# print vowels
print('Sorted list:', vowels)
print('Sorted list:', my_numbers)
print("pop======"+my_words.pop(1))
print("after pop======",my_words)
#my_words.append(vowels)
my_words.extend(vowels)
print(my_words)
#Returns the index of the first object with a matching value
print(my_words.index('apple'))
#adding elements at particuar index
my_words.insert(0, "microsoft")
print(my_words)
#length method 
print(len(my_words))
#sort method
vowels.sort()
my_numbers.sort()
print('Sorted list:', vowels)
print('Sorted list:', my_numbers)
#pop method
print("pop======"+my_words.pop(1))
print("after pop======",my_words)
#slicing operation on lists
print(my_words[1:3])
l = [0, 10, 20, 30, 40, 50, 60]
print(l[1:4])
print(l)
print(l[-4:-1])


