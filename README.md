# Project Title

Python program to check if a string is palindrome or not

A palindrome is a word, phrase, number or sequence of words that reads the same backward as forward. 
Punctuation and spaces between the words or lettering is allowed.

## Project Setup
You can run this program using any OS: Windows, macOS, Linux, etc.

This program requires Python 2.7 or higher. 

You will need Git to copy this project code.

Clone this repository ```https://github.com/david-mangena/isPalindrome.git```

Run cd ```isPalindrome``` to enter the project.

## Running the program

On your terminal run the program with the follow command ```python isPalindrome.py```



# Test Cases
```
* Null String Test
Input: null
Expected Output: NullPointerException
```
```
* Empty String Test
Input: ""
Expected Output: true (Is a Palindrome)
```
```
* Multiple White Space Test
Input: "A   Santa         at Nasa"
Expected Output: true (Is a Palindrome)
```
```
* Single Character Test
Input: "H"
Expected Output: true (Is a Palindrome)
```
```
* Punctuation Test
Input: "Eva, can I see bees in a cave?"
Expected Output: false (Not a Palindrome)
```
```
* Unicode Test
Input: "\u20A9 My gym \u20A9"
Expected Output: false (Not a Palindrome)
```
```
* Alpha Numeric Test
Input: "Air 2 an a2ria"
Expected Output: true (Is a Palindrome)
```
```
* Valid Palindrome Test
Input: "No lemon no melon"
Expected Output: true (Is a Palindrome)
```
```
* Invalid Palindrome Test
Input: "I am a tester"
Expected Output: false (Not a Palindrome)
```




















## Positive testing
The program will prompt you to enter string, enter ``palindrome`` see below given valid dataset (example 1) 

## Negative testing
 Enter ``semordnilap`` words that can be read backwards. but the backwards spelling forms an entirely different word, see below given invalid dataset (example 2)

## valid Dataset (example 1)
```
Madam
Noon
Racecar
Radar
Redder
Refer
Repaper
Rotator
Rotor
Sagas
Solos
Stats
Tenet

Malayalam 
saippuakivikauppias


Never odd or even.
We panic in a pew.
Won’t lovers revolt now?
Don't nod.
I did, did I?
My gym.
Red rum, sir, is murder.
Step on no pets.
Top spot.
Was it a cat I saw?
Eva, can I see bees in a cave?
No lemon, no melon.

Ed, I saw Harpo Marx ram Oprah W. aside.

313
5A5
5FF5
16FLF61

0 
121
676
10,201
69,696
698,896
1,002,001
6,948,496
100,020,001
522,808,225

12/12/2121
12/1/21 
1/20/21
1/29/21

Are we not pure? "No, sir!" Panama's moody Noriega brags. "It is garbage!" Irony dooms a man—a prisoner up to new era.
```
## invalid Dataset (example 2)
```
12
224
10,110
123,001
5502,229

stressed - desserts
rewarder - redrawer

deliver - reviled
stinker - reknits
redroot - to-order

redraw - warder
reward - drawer
repaid - diaper
sinned - Dennis
Kramer -remark

soccer - reccos
denier - reined

spider - redips
tenner - rennet

depot - toped
denim - mined
dinar - ranid

regal - lager
trams - smart
devil - lived
warts - straw
sleep - peels
revel - lever
