
#function which return reverse of a string
import re

def isPalindrome(string):

    # Removing punctuations, white spaces and lowercase string
    res = re.sub(r'[^\w\s]', '', string.replace(' ','').lower())

    # Checking if both string are equal or not
    return res == res[::-1]

#Enter string
inputString = raw_input("Enter String: ")

#lowercase and remove  input string
answer = isPalindrome(inputString)

# print outcome
if answer:
    print("It's Palindrome")
else:
    print("It's not Palindrome")

