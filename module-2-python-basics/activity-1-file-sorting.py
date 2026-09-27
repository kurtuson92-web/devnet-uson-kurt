"""
Module 2 — Activity: File Sorting with os and shutil
Student: Uson, Kurt Angel D.
Date: September 27, 2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
I used the old sorting activity if its the needed but i didnt finish it
this file ask for a folder path and checks if the folder path exist i
also make count for files like image, vid, docs and others but not used.

============================================
KEY VOCABULARY
============================================
- os module:
this help python on handling files and folders

- shutil module:
helps the program to move or copy files from one to anotehr

- file path:
the local location of the folder or file in the local storage

- directory:
this is the folder itself its like the one who contains the files

============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

dire = input("Enter folder Path ")

if os.path.exists(dire):
    files = os.listdir(dire)
    img = 0
    vid = 0
    doc = 0
    oth = 0

else:
    print("unknown directory")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
i first used files = os.listdir() without putting the folderpath inside
so ilearned that i need to tell the python program which directory i want to check

heres teh previous link of this activity
https://github.com/kurtuson92-web/Test-Uson-Kurt/blob/main/Test-Project.py


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
