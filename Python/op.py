'''
a=int(input("enter no"))
b=int(input("enter no"))
print(a+b)

a=int(input("enter no"))
b=int(input("enter no"))
print(a-b)

a=int(input("enter no"))
b=int(input("enter no"))
print(a*b)

a=int(input("enter no"))
b=int(input("enter no"))
print(a/b)

a=int(input("enter no"))
b=int(input("enter no"))
print(a%b)

a=float(input("enter no"))
b=int(input("enter no"))
print(a**b)


a=float(input("enter length"))
b=int(input("enter width"))
print("area=",a*b)

a=int(input("enter length"))
b=int(input("enter width"))
print("perimeter=",2*(a+b))

a=int(input("enter no"))
b=int(input("enter no"))
print("a=",a,"b=",b)
temp=a
a=b
b=temp
print("a=",a,"b=",b)

a=int(input("enter no"))
b=int(input("enter no"))
c=int(input("enter no"))
print("avg=",(a+b+c)/3)

a=int(input("enter no"))
b=int(input("enter no"))
if a==b:
    print("equal")
else:
    print("not equall")
   
a=int(input("enter no"))
b=int(input("enter no"))
if a>b:
    print("a greater")
else:
    print("bgreater")

a=int(input("enter no"))
b=int(input("enter no"))
if a<=b:
    print("a less")
else:
    print("bless")
     

a=int(input("enter ageof p1"))
b=int(input("enter age of p2"))
if a>b:
    print("p1 older")
else:
    print("p2 older")
   
b=int(input("mark"))
if b>=40:
    print("passed")
else:
    print("failed")


a=100
a+=50
print(a)
   
a=500
a-=100
print(a)
 
a=int(input("no"))
a*=5
print(a)
 
a=int(input("no"))
a/=2
print(a)

a=int(input("no"))
a%=7
print(a)


a=int(input("enter no"))
if a>18 and a<60:
    print("hmm")

a=int(input("enter no"))
if a%3==0 or a%5==0:
    print("divi")    
else:
    print("not")
  
log=True
if not log:
    print("log in")
else:
    print("Welcome")

     
m=int(input("enter mark"))
a=int(input("enter attendance"))
if m>80 and a>75:
    print("sc")
else:
    print("not eli")

    m=int(input("enter mark"))
a=int(input("enter attendance"))
if m>80 and a>75:
    print("sc")
else:
    print("not eli")

   
m=int(input("enter age"))
a=input("have id proof(y/n)")
if m>=18 and a=='y':
    print("can apply")
else:
    print("not eli")
     

l=['apple','orange','mango','kiwi']
if 'apple' in l:
    print("exist")
     
y='python'
if 'o' in y:
    print("exist")
else:
    print("not")
   
s=['ra','abd','ju']
print('ra' in s)

l=(10,20,30,40,50)
print(10 in l)

s="my python easy"
print("my" not in s)
 

l=['ds','df','gfg']
k=l
print(k is l)

l=['ds','df','gfg']
k=['ds','df','gfg']
print(k is l)

k=['ds','df','gfg']
l=['ds','df','gfg']
print(k==l)
print(k is l)

k='pyht'
l='pyht'
print(k is l)

d1={
    'a':1,'b':2
}
d2={
    'a':1,'b':2
}
print(d1 is not d2)

a=int(input("no"))
if a>0:
    print("+ve")
else:
    print("-ve")
  

a=int(input("no"))
if a%2==0:
    print("even")
else:
    print("odd")
     
a=int(input("no"))
if a>18:
    print("eligible")
else:
     print(" noteligible")

    
a=input("chara")
if a in "aeiouAEIOU":
    print("vowel")
else:
    print("conso")
     
y=int(input("enter year"))
if y % 4==0:
    print("leap")
else:
    print("not leap")
     
a=int(input("enter age"))
if a<12:
    print("child")
elif a>12 and a<=19:
    print("teena")
elif a>=20 and a<=59:
    print("adult")
else:
    print("senior")
 
   '''



#hangman

import random

# List of words
words = ["python", "computer", "network", "program", "keyboard"]

# Hangman stages
hangman = [
"""
 -----
 |   |
     |
     |
     |
     |
=========
""",
"""
 -----
 |   |
 O   |
     |
     |
     |
=========
""",
"""
 -----
 |   |
 O   |
 |   |
     |
     |
=========
""",
"""
 -----
 |   |
 O   |
/|   |
     |
     |
=========
""",
"""
 -----
 |   |
 O   |
/|\\  |
     |
     |
=========
""",
"""
 -----
 |   |
 O   |
/|\\  |
/    |
     |
=========
""",
"""
 -----
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========
"""
]

# Select a random word
word = random.choice(words)

guessed_letters = set()
wrong_guesses = 0
max_attempts = 6

print("Welcome to Hangman!")

while True:

    # Display current word status
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check win condition
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.add(guess)

    # Check guess
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1

        print(hangman[wrong_guesses])
        print("Wrong guess!")
        print("Attempts left:", max_attempts - wrong_guesses)

    # Check lose condition
    if wrong_guesses == max_attempts:
        print("\nGame Over!")
        print("The word was:", word)
        break