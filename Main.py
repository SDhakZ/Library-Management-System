import lists
import Borrow
import Return
import read
import os
"""Method for Menu,
Used to allow user to input value to
Display,Borrow and Return the book"""
def Reloop():
    while(True):
        print("-------------------------Library Management System-----------------------")
        print("__________________________________MENU___________________________________")
        print("\n|\t\tInput 1: To View available books\t\t\t|")
        print("|\t\tInput 2: To Borrow a book\t\t\t\t|")
        print("|\t\tInput 3: To Return the borrowed books\t\t\t|")
        print("|\t\tInput 4: To Exit the System\t\t\t\t|")
        print("_________________________________________________________________________")
        try:#Checking if the number is actual number
            a = int(input("\nInput a number from 1 to 4 to choose:"))
            print("_________________________________________________________________")
            if(a == 1):#Gives choice to Display Information of Normal Books or Manga Books
                print("_____________Select to view available types of book______________\n")
                print("\t\t\t1) Normal Books\t\t\t\t| \n\t\t\t\t\t\t\t\t|\n\t\t\t2) Manga Books\t\t\t\t|\n_________________________________________________________________")
                print()
                choice=int(input("Input 1 or 2 to choose:"))
                print()
                if (choice==1):#Displays Information of Normal Books
                    print("_________________________________________________________________________________")
                    print("\t\t\t\tNormal Books")
                    print("_________________________________________________________________________________")
                    print("SN, Book Name, Book Author, Book Stock, Book Price")
                    print("---------------------------------------------------------------------------------")
                    read.readBook() #Calls read module and readBook Function
                    print("_________________________________________________________________________________\n")
                elif (choice == 2):#Displays Information of Manga Books
                    print("____________________________________________________________________")
                    print("\t\t\tManga Books")
                    print("____________________________________________________________________")
                    print("SN, Book Name, Book Author, Book Stock, Book Price")
                    print("--------------------------------------------------------------------")
                    read.readMangaBook() #Calls read module and readMangaBook Function
                    print("____________________________________________________________________\n")

            elif (a == 2):#Borrowing Books
                print("____________Select to Borrow available types of book_____________\n")
                print("\t\t\t1) Normal Books\t\t\t\t| \n\t\t\t\t\t\t\t\t|\n\t\t\t2) Manga Books\t\t\t\t|\n________________________________________________________________")         
                print()
                choice=int(input("Enter 1 or 2:"))
                print()
                if (choice == 1):#Calls borrow() method from Borrow module
                    lists.lists()
                    Borrow.borrowBook()
                elif (choice == 2):#Calls borrowMangaBook() method from Borrow module
                    lists.lists()
                    Borrow.borrowMangaBook()
                else:
                    print("Enter the number as suggested")
            elif (a == 3):#Returning Book
                print("_________Select to Return the type of Borrowed book book___________\n")
                print("\t\t\t1) Normal Books\t\t\t\t| \n\t\t\t\t\t\t\t\t|\n\t\t\t2) Manga Books\t\t\t\t|\n________________________________________________________________")
                print()
                choices=int(input("Enter 1 or 2:"))
                if(choices == 1):#Calls returnBook() method from Return module
                    lists.lists()
                    Return.returnBook()
                elif(choices == 2):#Calls returnMangaBook() method from Return module
                    lists.lists()
                    Return.returnMangaBook()
                else:
                    print("Enter the number as suggested")
            elif(a == 4):#Breaks the menu
                print("********Thank you for using the Library Management System********")
                break
            else:
                print("Please enter a valid choice from 1-4")
        except ValueError:#prints error message due to not keeping number
            print("Please input as suggested.")
Reloop()
