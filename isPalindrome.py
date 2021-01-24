
#function which return reverse of a string
def isPalindrome(string):

    # Checking if both string are
    # equal or not
    return string == string[::-1]

#Enter string
inputString = raw_input("Enter String: ")

#lowercase input string
answer = isPalindrome(inputString.lower())
print answer
# outcome
if answer:
    print("It's Palindrome")
else:
    print("It's not Palindrome")
