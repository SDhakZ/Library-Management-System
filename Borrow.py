import lists
import os
import datetime
"""-----------------------------Method for Borrowing Normal Books Allows user to borrow multiple books writes a receipt note for borrower----------------------------------"""
def borrowBook():
    success = False
    print("________________________________________________________________")
    print("_______________________Borrowers Info___________________________")
    
    while(True): #Input First name
        firstName = input("Enter the first name of the borrower: ")
        if firstName.isalpha(): #checks whether the First name has valid letters
            break
        print("Please enter the first name with valid letters")
        
    while(True): #Input Last name
        lastName=input("Enter the last name of the borrower: ")
        if lastName.isalpha():  #checks whether the last name has valid letters
            break
        print("Please enter the first name with valid letters")
    print("___________________________________________________________________")
    
    ID_abs_path=os.path.abspath( "TransactionID/ID.txt")
    g=ID_abs_path
    with open(g, "r") as f:
        line=f.read()
        transaction=line
        
    current_abs_path = os.path.abspath("Borrowers/""Borrower-" + transaction + "_" + firstName + ".txt")#Creating absolute path to create text file
    t = current_abs_path
    date=datetime.datetime.now()
    with open(t, "w+") as f: #Writing Borrower receipt
        f.write("\n--------------------------------Receipt--------------------------------\n")
        f.write("Borrowers Name: " + firstName+" " + lastName+"\n")
        f.write("Transaction ID:" + transaction+"\n")
        f.write("Date Borrowed: " +  date.strftime("%x") + "    Time:" + date.strftime("%X") +"\n\n")
    
    while success == False:
        print("\n_________________________________________________________________")
        print("________________Please select an option below:___________________\n")
        for i in range(len(lists.bookName)):
            print("\tInput", i, "to borrow book", lists.bookName[i])
        print("_________________________________________________________________")
    
        try:   
            a=int(input("Enter the number:"))
            try:
                if(int(lists.stocks[a])>0): #checks if the stock is available
                    
                    total = 0
                    with open(t,"a") as f:
                        total += int(lists.price[a])
                        f.write("S.N 1. "+"\nBookName:"+lists.bookName[a]+"\nAuthor:"+lists.author[a]+"\nPrice: NRs"+lists.price[a]+"\n")
                        
                    lists.stocks[a] = int(lists.stocks[a])-1 #decreases stock by 1 when borrowed
                    current_abs_path = os.path.abspath("Books/""Books.txt")
                    b = current_abs_path
                    with open(b,"w+") as f:
                        for i in range(5):
                            f.write(lists.bookName[i] + "," + lists.author[i] + "," + str(lists.stocks[i]) + ","+"NRs" + lists.price[i] + "\n")
                            
#----------------------------------------------If Borrowing Multiple Books------------------------------------------------#
                    loop = True
                    count = 1
                    while loop == True:
                        choice = str(input("Please press Y to borrow more books and N to not:"))
                        if(choice.upper() == "Y"):#to uppercase the letter y if input in small letter
                            count = count+1
                            print("\n_________________________________________________________________")
                            print("_________________Please select an option below:__________________\n")
                            for i in range(len(lists.bookName)):
                                print("\tInput", i, "to borrow book", lists.bookName[i])
                            print("_________________________________________________________________")
                            a = int(input("Enter the Number:"))
                            if(int(lists.stocks[a]) > 0):# checks if stock is available
                                print(">>>>>Book has been borrowed successfully<<<<<")
                                with open(t, "a") as f: # adding books if borrowed multiple times in receipt 
                                    total += int(lists.price[a])
                                    f.write("\nS.N:" + str(count) + "\nBook Name:" + lists.bookName[a] + "\nAuthor Name:" + lists.author[a] + "\nPrice: NRs" + lists.price[a]+"\n")
                                        
                                lists.stocks[a] = int(lists.stocks[a])-1 #Decreasing stock when borrowed
                                current_abs_path = os.path.abspath("Books/""Books.txt")
                                b = current_abs_path
                                
                                with open(b, "w+") as f: # ReWriting updated information in Books
                                    for i in range(5):
                                        f.write(lists.bookName[i] + "," + lists.author[i] + "," + str(lists.stocks[i]) + "," + "NRs"+lists.price[i] + "\n")
                                        success = False
                            else:
                                loop = False
                                break
                        elif (choice.upper() == "N"): #to uppercase the letter n if input in small letter
                            with open(t,"a") as f:
                                f.write("\n\t\t\t\tTotal: NRs" + str(total)+"\n----------------------------------------------------------------------")
                            with open(t,"r") as f:
                                data = f.read()
                                print(data)
                            print(">>>>>Book has been borrowed successfully<<<<<")
                            print ("Thank you for borrowing the books, Hope you have a wonderful day")
                            print("----------------------------------------------------------------------\n")
                            loop = False
                            success = True

                        else:
                            print("Please Input y or n for yes or no respectively")
                else:
                    print("Sorry, The Book is out of stock")
                    borrowBook()
                    success = False
            except IndexError:
                print("")
                print("Please Input the numbers according to the mentioned above")
        except ValueError:
            print("")
            print("Please choose as suggested.")
    with open(g,"w+") as f:
        tran=int(transaction)+1
        f.write(str(tran))
            
"""------------------------Method for Borrowing Manga Books Allows user to borrow multiple books writes a receipt note for borrower-----------------------"""

def borrowMangaBook():
    success = False
    print("________________________________________________________________")
    print("_______________________Borrowers Info___________________________")
    while(True):
        firstName = input("Enter the first name of the borrower: ")
        if firstName.isalpha(): #checks whether the First name has valid letters 
            break
        print("Please enter the first name with valid letters")
    while(True):
        lastName = input("Enter the last name of the borrower: ")
        if lastName.isalpha():  #checks whether the last name has valid letters
            break
        print("Please enter the first name with valid letters")
    print("___________________________________________________________________")
    ID_abs_path=os.path.abspath( "TransactionID/ID.txt")
    g=ID_abs_path
    with open(g, "r") as f:
        line=f.read()
        transaction=line
    current_abs_path = os.path.abspath("Borrowers/""BorrowerMB-" + transaction + "_" + firstName+".txt")
    t = current_abs_path
    date = datetime.datetime.now()
    with open(t,"w+") as f:# Writing Borrower receipt
        f.write("\n-------------------------------Receipt--------------------------------\n")
        f.write("Borrowers Name: " + firstName + " " + lastName+"\n")
        f.write("Transaction ID:" + transaction+"\n")
        f.write("Date Borrowed: " + date.strftime("%x") + "    Time:" + date.strftime("%X") + "\n\n")
    
    while success == False:
        print("\n_________________________________________________________________")
        print("________________Please select an option below:___________________\n")
        for i in range(len(lists.bookName2)):
            print("\tInput", i, "to borrow Manga book", lists.bookName2[i])
        try:   
            a = int(input("Enter the number:"))
            try:
                if(int(lists.stocks2[a])>0):
                    print(">>>>>Book has been borrowed successfully<<<<<")
                    total = 0
                    with open(t,"a") as f: 
                        total += int(lists.price2[a])
                        f.write("S.N:1." + "\nBook Name:" + lists.bookName2[a] + "\nAuthor Name:" + lists.author2[a] + "\nPrice:" + lists.price2[a] + "\n")

                    lists.stocks2[a] = int(lists.stocks2[a])-1
                    current_abs_path = os.path.abspath("Books/""MangaBooks.txt")
                    b = current_abs_path
                    with open(b,"w+") as f:
                        for i in range(5):
                            f.write(lists.bookName2[i] + "," + lists.author2[i] + "," + str(lists.stocks2[i]) + "," + "NRs" + lists.price2[i] + "\n")
                        print("_________________________________________________________________")


                    #-----------------------------------if borrowiing multiple books-------------------------------------#
                        
                    loop = True
                    count = 1
                    while loop == True:
                        choice = str(input("Please press Y to borrow more books and N to not:"))
                        if(choice.upper() == "Y"):#to uppercase the letter y if input in small letter
                            count = count+1
                            print("\n________________________________________________________________")
                            print("_________________Please select an option below:__________________\n")
                            for i in range(len(lists.bookName2)):
                                print("\tInput", i, "to borrow Manga book", lists.bookName2[i])
                            print("_________________________________________________________________")
                            a = int(input("Enter the Number:"))
                            if(int(lists.stocks2[a])>0):
                                print(">>>>>Book has been borrowed successfully<<<<<")
                                with open(t, "a") as f: # adding books if borrowed multiple times in receipt 
                                    total += int(lists.price2[a])
                                    f.write("\nS.N:" + str(count) + "\nBook Name:" + lists.bookName2[a] + "\nAuthor Name:" + lists.author2[a] + "\nPrice:" + lists.price2[a]+"\n" )

                                lists.stocks2[a] = int(lists.stocks2[a])-1 #decreases stock by 1 when borrowed
                                current_abs_path = os.path.abspath("Books/""MangaBooks.txt")
                                b = current_abs_path
                                with open(b, "w+") as f:
                                    for i in range(5):
                                        f.write(lists.bookName2[i] + "," + lists.author2[i] + ","+str(lists.stocks2[i]) + "," + "NRs"+lists.price2[i] + "\n")
                                        success = False
                            else:
                                loop = False
                                break
                        elif (choice.upper() == "N"): #to uppercase the letter n if input in small letter
                            with open(t,"a") as f:
                                f.write("\n\t\t\t\tTotal: NRs"+str(total)+"\n----------------------------------------------------------------------")
                            with open(t,"r") as f:
                                data = f.read()
                                print(data)
                            print ("Thank you for borrowing the books, Hope you have a wonderful day")
                            print("----------------------------------------------------------------------\n")
                            loop = False
                            success = True
                            
                        else: 
                            print("Please Input y or n for yes or no respectively")
                else:
                    print("Sorry, The Book is out of stock")
                    borrowMangaBook()
                    success = False
            except IndexError:
                print("")
                print("Please Input the numbers according to the mentioned above")
        except ValueError:
            print("")
            print("Please choose as suggested.")
    with open(g,"w+") as f:
        tran=int(transaction)+1
        f.write(str(tran))
