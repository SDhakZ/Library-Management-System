import lists
import os
import datetime
def returnBook():
    name = input("Enter name of borrower: ")
    transaction = input("Enter transaction ID: ")
    current_abs_path = os.path.abspath("Borrowers/""Borrower-"+transaction+"_"+name+".txt")
    a = current_abs_path
    try:
        with open(a,"r") as f:
            lines = f.readlines()
            lines = [a.strip("NRs") for a in lines]
    
        with open(a, "r") as f:
            data = f.read()
            print(data)
    except:
        print("The borrower name does not exist or is incorrectly typed")
        returnBook()
    current_abs_path2 = os.path.abspath("Returns/""Return-"+transaction+"_"+name+".txt")
    r = current_abs_path2
    date = datetime.datetime.now()
    with open(r, "w+")as f:
        f.write("\n----------------------------Return receipt----------------------------\n")
        f.write("Returned By: " + name + "\n")
        f.write("Transaction ID: " + transaction + "\n")
        f.write("Date: " + date.strftime("%x") + "    Time:" + date.strftime("%X") + "\n\n")
    total = 0.0
    for i in range(5):
        if lists.bookName[i] in data:
            with open(r, "a") as f:
                f.write("\nS.N:" + str(i + 1) + "\nBook Name:" + lists.bookName[i] + "\nPrice: NRs" + lists.price[i] + "\n\n")
                lists.stocks[i] = int(lists.stocks[i]) + 1
            total += float(lists.price[i])
    print("____________________________________________________________________________")
    print("_____________________________Due Submission_________________________________")
    print("Is the book return date expired?")
    print("Press number of days the books are borrowed")
    stat = int(input())
    print("____________________________________________________________________________")
    if(stat > 10):
        days = 0
        print("____________________________________________________________________________")
        days = stat-10
        fine = 20*days
        with open(r, "a")as f:
            f.write("\t\t\tSub-Total:" + str(total))
            f.write("\n\t\t\tFine:NRs" + str(fine))
        total = total + fine
        with open(r, "r") as f:
            data = f.read()
            print(data)
            print("\t\t\tTotal After Fine:" + "Nrs"+str(total))
        with open(r, "a")as f:
            f.write("\n\t\t\tTotal After Fine: Nrs" + str(total) + "\n----------------------------------------------------------------------")
    else:
        with open(r, "a")as f:
            f.write("\t\t\tTotal:NRs" + str(total)+ "\n----------------------------------------------------------------------")
        with open(r, "r") as f:
            data = f.read()
        print(data)
        print("----------------------------------------------------------------------\n")
    
    
    current_abs_path = os.path.abspath("Books/""Books.txt")
    b = current_abs_path
    with open(b, "w+") as f:
            for i in range(5):
                f.write(lists.bookName[i] + ","+lists.author[i] + ","+str(lists.stocks[i]) + "," + "NRs" + lists.price[i] + "\n")
"""---------------Manga Book Return Function------------------"""
def returnMangaBook():
    name = input("Enter name of borrower: ")
    transaction = input("Enter transaction ID: ")
    current_abs_path = os.path.abspath("Borrowers/""BorrowerMB-" + transaction + "_" + name + ".txt")
    a = current_abs_path
    try:
        with open(a, "r") as f:
            lines = f.readlines()
            lines = [a.strip("NRs") for a in lines]
    
        with open(a, "r") as f:
            data = f.read()
            print(data)
    except:
        print("The borrower name does not exist or is incorrectly typed")
        returnMangaBook()
    current_abs_path2 = os.path.abspath("Returns/""ReturnMB-" + transaction + "_" + name + ".txt")
    r = current_abs_path2
    date = datetime.datetime.now()
    with open(r, "w+")as f:
        f.write("\n----------------------------Return receipt----------------------------\n")
        f.write("Returned By: " + name + "\n")
        f.write("Transaction ID: " + transaction + "\n")
        f.write("Date: " + date.strftime("%x") + "    Time:" + date.strftime("%X") + "\n\n")
    total = 0.0
    for i in range(5):
        if lists.bookName2[i] in data:
            with open(r, "a") as f:
                f.write("\nS.N:" + str(i+1) + "\nBook Name:" + lists.bookName2[i] + "\nPrice: NRs" + lists.price2[i] + "\n\n")
                lists.stocks2[i] = int(lists.stocks2[i])+1
            total += float(lists.price2[i])
    print("____________________________________________________________________________")
    print("_____________________________Due Submission_________________________________")
    print("Press number of days the books are borrowed")
    stat = int(input())
    print("____________________________________________________________________________")
    if(stat > 10):
        days = 0
        print("____________________________________________________________________________")
        days = stat-10
        fine = 20*days
        with open(r, "a")as f:
            f.write("\t\t\tSub-Total:" + str(total))
            f.write("\n\t\t\tFine:NRs" + str(fine))
        total = total + fine
        with open(r, "r") as f:
            data = f.read()
            print(data)
            print("\t\t\tTotal After Fine:" + "Nrs"+str(total))
        with open(r, "a")as f:
            f.write("\n\t\t\tTotal After Fine:Nrs" + str(total) + "\n----------------------------------------------------------------------")
    else:
        with open(r, "a")as f:
            f.write("\t\t\tTotal:NRs" + str(total)+ "\n----------------------------------------------------------------------")
        with open(r, "r") as f:
            data = f.read()
        print(data)
        print("----------------------------------------------------------------------\n")
            
        
    print("-----------------------------------------------------------------------------------------\n")
    
    current_abs_path = os.path.abspath("Books/""MangaBooks.txt")
    b = current_abs_path
    with open(b, "w+") as f:
            for i in range(5):
                f.write(lists.bookName2[i] + ","+lists.author2[i] + "," + str(lists.stocks2[i]) + "," + "NRs" + lists.price2[i] + "\n")
