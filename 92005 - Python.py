'''A program to conect to the Āhua_Gallery database and run difrent queries on 
it.
By: Matt Smith                                                      12/8/2024'''

#all the constences
DATABASE = "92005 - Database.SQlite"
LOWEST_PRICE = 25

#import staments
import sqlite3
import os
# run pip3 install tabulate to use this libry to print results in columns
from tabulate import tabulate

#funtions for the Querys
def all_pieces():
    '''Deplay all infomation of all pieces in the Āhua_Gallery'''
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        qrl = "SELECT * FROM pieces;"
        cursor.execute(qrl)
        results = cursor.fetchall()
        headings = ["piece_id","piece_name","price","purchase status",
                    "material","commission", "maker"]
        alignments = ("left","left","left","left","center","center","center")
        #print resalts of query
        print("All infomation of the peices in the Āhua_Gallery:\n")
        print(tabulate(results, headings,tablefmt="plain",colalign=alignments))

def all_sold():
    '''Deplay all usefull infomation of all pieces in the Āhua_Gallery that 
    have sold'''
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        qrl = '''SELECT pieces.piece_id, pieces.price, pieces.piece_name, 
        customers.first_name, customers.last_name, customers.postal_address, 
        customers.town, customers.postal_code FROM pieces JOIN customer_piece, 
        customers ON customer_piece.piece_id = pieces.piece_id AND 
        customer_piece.customer_id = customers.customer_id;'''
        cursor.execute(qrl)
        results = cursor.fetchall()
        headings = ["piece_id","price","piece_name","first_name",
                    "last_name","postal_address", "town", "postal_code"]
        alignments = ("left","left","left","left","left","left","left","center")
        #print resalts of query
        print("All usefull infomation of the peices in the Āhua_Gallery that "
              "have sold:\n")
        print(tabulate(results, headings,tablefmt="plain",colalign=alignments))

def all_under_price():
    '''Deplay all usefull infomation of all pieces in the Āhua_Gallery that 
    have sold'''
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        price = int(input("Sort by what price?"))
        os.system("cls")
        qrl = f'''SELECT piece_id, piece_name, price, material, maker FROM 
        pieces WHERE price <= {price} AND purchase_status = 'Avalbile';'''
        cursor.execute(qrl)
        results = cursor.fetchall()
        headings = ["piece_id","piece_name","price","material","maker",]
        alignments = ("left","left","center","left","left")
        #print resalts of query
        print("All usefull infomation of the peices in the Āhua_Gallery that "
              "are under a certain price:\n")
        print(tabulate(results, headings,tablefmt="plain",colalign=alignments))

if __name__ == "__main__":
    count = "i"
    option = "1"
    while option != "5":
        os.system("cls")
        print("---------MENU---------")
        print("1. ")
        print("2. ")
        print("3. ")
        print("4. Exit")
        while count != "Exit":
            option = input("Choose an option from the menu 1, 2, 3, and 4: ")
            os.system("cls")
            if option == "1":
                all_pieces()
                count = "Exit"
            elif option == "2":
                all_sold()
                count = "Exit"
            elif option == "3":
                all_under_price()
                count = "Exit"
            elif option == "4":
                print("Goodbye.........")
                exit()
            else:
                print("This is not one of the options try again")
        count = input("Enter to return to menu...")
