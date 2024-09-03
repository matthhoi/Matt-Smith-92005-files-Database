'''A program to conect to the Āhua_Gallery database and run difrent queries on 
it.
By: Matt Smith                                                      6/9/2024'''

#all the constences
DATABASE = "92005 - Database.SQlite"
LOWEST_PRICE = 25

#import staments
import sqlite3
import os
#run pip3 install tabulate to use this libry to print results in columns
from tabulate import tabulate
#run pip3 install easygui to use this libry to use the gui
import easygui

#funtions for the Querys
def all_pieces():
    '''Deplay all infomation of all pieces in the Āhua_Gallery'''
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        qrl = "SELECT piece_id, piece_name, price, material, maker FROM pieces;"
        cursor.execute(qrl)
        results = cursor.fetchall()
        headings = ["piece_id","piece_name","price","material", "maker"]
        alignments = ("left","left","left","center","center")
        #print resalts of query
        easygui.msgbox("All infomation of the peices in the Āhua_Gallery:\n" + 
                       tabulate(results, headings,tablefmt="plain",
                                colalign=alignments), "MENU")

def all_sold():
    '''Deplay all usefull infomation of all pieces in the Āhua_Gallery that 
    have sold'''
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        qrl = '''SELECT pieces.piece_id, pieces.price, pieces.piece_name, 
        customers.first_name, customers.postal_address 
        FROM pieces JOIN customer_piece, customers ON customer_piece.piece_id
        = pieces.piece_id AND customer_piece.customer_id = 
        customers.customer_id;'''
        cursor.execute(qrl)
        results = cursor.fetchall()
        headings = ["piece_id","price","piece_name","first_name",
                    "last_name","postal_address"]
        alignments = ("left","left","left","left","left")
        #print resalts of query
        easygui.msgbox("All usefull infomation of the peices in the Āhua_Gallery"
                       " that have sold:\n" + 
                       tabulate(results, headings,tablefmt="plain",
                                colalign=alignments), "MENU")

def all_under_price():
    '''Deplay all usefull infomation of the peices in the Āhua_Gallery that are 
    under a certain price'''
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        while True:
            try:
                price = int(easygui.enterbox("Sort by what price?", "MENU"))
                if price > LOWEST_PRICE:
                    break
                else:
                    easygui.msgbox("Please enter a number more than 25", "MENU")
            except:
                easygui.msgbox("Please enter a number", "MENU")
        os.system("cls")
        qrl = f'''SELECT piece_id, piece_name, price, material, maker FROM 
        pieces WHERE price <= {price} AND purchase_status = 'Avalbile';'''
        cursor.execute(qrl)
        results = cursor.fetchall()
        headings = ["piece_id","piece_name","price","material","maker",]
        alignments = ("left","left","center","left","left")
        #print resalts of query
        easygui.msgbox("All usefull infomation of the peices in the Āhua_Gallery"
                       " that are under a certain price:\n" + 
                       tabulate(results, headings,tablefmt="plain",
                                colalign=alignments), "MENU")

def specific_customers():
    '''Deplay infomation on specific customers in the Āhua_Gallery'''
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        qrl = f'''SELECT first_name FROM customers;'''
        cursor.execute(qrl)
        customers = cursor.fetchall()
        while True:
            try:
                option = easygui.choicebox("---------MENU---------", "MENU", 
                                           customers)
                option = str(option)
                option = option.replace("(", "")
                option = option.replace("'", "")
                option = option.replace(")", "")
                option = option.replace(",", "")
                os.system("cls")
                qrl = f'''SELECT first_name, last_name, postal_address, town, 
                postal_code FROM customers WHERE first_name = '{option}';'''
                cursor.execute(qrl)
                results = cursor.fetchall()
                headings = ["first_name","last_name","postal_address","town",
                            "postal_code"]
                alignments = ("left","left","center","left","left")
                #print resalts of query
                easygui.msgbox("infomation on specific customers in the "
                            "Āhua_Gallery:\n" + 
                            tabulate(results, headings, tablefmt="plain", 
                                        colalign=alignments), "MENU")
                break
            except:
                easygui.msgbox("Please choose one", "MENU")

#gui interface
if __name__ == "__main__":
    count = "i"
    option = "1"
    while option != "5":
        possible_querys = ["1. Deplaying all infomation of pieces", "2. "
                           "Deplaying all pieces that have sold", "3. Deplaying"
                           " all peices that are under a certain price", "4. "
                           "Deplay infomation on specific customers", "5. Exit"]
        while count != "Exit":
            option = easygui.choicebox("---------MENU---------", "MENU", 
                                       possible_querys)
            if option == "1. Deplaying all infomation of pieces":
                all_pieces()
            elif option == "2. Deplaying all pieces that have sold":
                all_sold()
            elif option == "3. Deplaying all peices that are under a certain price":
                all_under_price()
            elif option == "4. Deplay infomation on specific customers":
                specific_customers()
            else:
                easygui.msgbox("Goodbye", "MENU")
                exit()
