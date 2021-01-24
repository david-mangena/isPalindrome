
# import regex
import re

# function that returns a boolean indicating
# whether or not a string is a palindrome.
def isPalindrome(input_string):

    # use replace built-in function to remove white spaces
    string = re.sub(r'[^\w\s]', '', input_string.replace(' ',''))
    # string = input_string.replace(' ','')

    # reverse a string using slicing by providing the step value as -1
    # checking if input string is equal or not to revised input string
    return string == string[::-1]

# enter string
input_string = raw_input("Enter String: ")

# lowercase input string
answer = isPalindrome(input_string.lower())

# print outcome
if answer:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
