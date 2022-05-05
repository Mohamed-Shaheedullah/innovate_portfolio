
# create alphabet list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# loop through list
for i in alphabet:
    print(i)

# ask user for a number between 1 and 26
a_char =  int(input("Please type in a number between 1 and 26  "))

# print the letter
print(alphabet[a_char-1])

