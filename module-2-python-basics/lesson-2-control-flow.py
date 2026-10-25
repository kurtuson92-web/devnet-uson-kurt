"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Uson, Kurt Angel D.
Date: September 27, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
This is like a chess moves for example if opponent made a move you can eighter attack or defend
if opponent do the move you can choose what to move then if that move is or will be countered by
the opponent you can move other piece.
============================================
KEY VOCABULARY
============================================
- condition:
condition is where your block of code will fall to if other condition is not met

- if / elif / else:
if statment is where it checks if the statement in if is true it will proceed,
if false it will go to elif statement which then will check if true, then if false
it will fall to else which will execute if all conditions is not met.

- comparison operator:
comparison operators is comparing two values or checks if two values have met the condition.

- boolean expression:
this checks if the two condition if true or false to execute the block of code.

============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

grade = int(input("Enter your Grade: "))
passing = 85
if grade >= passing:
    print("Passed")
elif grade <= 84:
    print("passed away")
else:
    print("Enter valid number")

yearlvl = int(input("Enter your Year lvl: "))
year = 3

if yearlvl == year:
    print("Hello batchmate")
elif yearlvl < year:
    print("Hello junior")
elif yearlvl > year:
    print("Hello senior")
else:
    print("please enter valid number")


if yearlvl > year and grade >= passing:
    print("wow you can graduate")
elif yearlvl <= year and grade >= passing:
    print("wow keep up")
elif yearlvl <= year or grade >= passing:
    print("keep it up you still have few years")
else:
    print("please enter valid number")
"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
Maybe i can make mistake if this is a nested conditions it like an elif and comparing if none
of it match you can make a condition for it

"i dont want to avoid but its ok to have a nested conditions"

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
