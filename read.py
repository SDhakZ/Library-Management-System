import os
def readBook():
    snum = 1
    current_abs_path = os.path.abspath("Books/""Books.txt")
    b = current_abs_path
    with open(b, "r") as f:
        for line in f:
            print(snum,")",line)
            snum+=1
def readMangaBook():
    sn = 1
    current_abs_path = os.path.abspath("Books/""MangaBooks.txt")
    b = current_abs_path
    with open(b, "r") as f:
        for line in f:
            print(sn, ")", line)
            sn += 1
