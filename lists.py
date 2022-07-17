import os
"""Storing the data in lists"""
def lists():
    #declaring global varfiables show that these variables are acessed throughout the program
    global bookName,author,stocks,price
    global stocks2,bookName2,author2,price2
    #Normal books Lists
    bookName=[]
    author=[]
    stocks=[]
    price=[]
    #Manga Book Lists
    bookName2=[]
    author2=[]
    stocks2=[]
    price2=[]
    #Normal Books storing
    current_abs_path=os.path.abspath("Books/""Books.txt")
    b=current_abs_path
    with open(b,"r") as f:
        lines=f.readlines()
        lines=[x.strip('\n') for x in lines]#removing escape sequence to store in list
        for i in range(len(lines)):
            c=0
            for a in lines[i].split(','):#splitting the data and putting counter to store in respective list
                if(c==0):
                    bookName.append(a)
                elif(c==1):
                    author.append(a)
                elif(c==2):
                    stocks.append(a)
                elif(c==3):
                    price.append(a.strip("NRs"))
                c+=1
    #MangaBooks storing         
    current_abs_path=os.path.abspath("Books/""MangaBooks.txt")
    m=current_abs_path
    with open(m,"r") as f:
        lines=f.readlines()
        lines=[x.strip('\n') for x in lines] #removing escape sequence to store in list
        for i in range(len(lines)):
            c=0
            for a in lines[i].split(','): #splitting the data and putting counter to store in respective list
                if(c==0):
                    bookName2.append(a)
                elif(c==1):
                    author2.append(a)
                elif(c==2):
                    stocks2.append(a)
                elif(c==3):
                    price2.append(a.strip("NRs")) #removes NRs so that oly number is stored wich becomes easier to add 
                c+=1
