"""A program to conect to the Āhua_Gallery database and run difrent queries on 
it.
By: Matt Smith                                                      17/9/2024"""

# all the constences
DATABASE = "92005 - Database.SQlite"
LOWEST_PRICE = 25

# import staments
import sqlite3
import os
# run pip3 install tabulate to use this libry to print results in columns
from tabulate import tabulate
# run pip3 install easygui to use this libry to use the gui
import easygui

# funtions for the Querys


def all_pieces():
    """Deplay all infomation of all pieces in the Āhua_Gallery"""
    with sqlite3.connect(DATABASE) as d_b:
        cursor = d_b.cursor()
        qrl = "SELECT piece_id, piece_name, price, material, maker FROM pieces;"
        cursor.execute(qrl)
        results = cursor.fetchall()
        headings = ["piece_id","piece_name","price","material", "maker"]
        alignments = ("left","left","left","center","center")
        # print resalts of query
        easygui.msgbox("All infomation of the peices in the Āhua_Gallery:\n" + 
                       tabulate(results, headings,tablefmt="plain",
                                colalign=alignments), "MENU")


def all_sold():
    """Deplay all usefull infomation of all pieces in the Āhua_Gallery that 
    have sold"""
    with sqlite3.connect(DATABASE) as d_b:
        cursor = d_b.cursor()
        qrl = """SELECT pieces.piece_id, pieces.price, pieces.piece_name, 
        customers.first_name, customers.postal_address 
        FROM pieces JOIN customer_piece, customers ON customer_piece.piece_id
        = pieces.piece_id AND customer_piece.customer_id = 
        customers.customer_id;"""
        cursor.execute(qrl)
        results = cursor.fetchall()
        headings = ["piece_id","price","piece_name","first_name",
                    "postal_address"]
        alignments = ("left","left","left","left","left")
        # print resalts of query
        easygui.msgbox("All usefull infomation of the peices in the "
                       "Āhua_Gallery that have sold:\n" + 
                       tabulate(results, headings,tablefmt="plain",
                                colalign=alignments), "MENU")


def all_under_price():
    """Deplay all usefull infomation of the peices in the Āhua_Gallery that are 
    under a certain price"""
    with sqlite3.connect(DATABASE) as d_b:
        cursor = d_b.cursor()
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
        # print resalts of query
        easygui.msgbox("All usefull infomation of the peices in the "
                       "Āhua_Gallery that are under a certain price:\n" + 
                       tabulate(results, headings,tablefmt="plain",
                                colalign=alignments), "MENU")


def specific_customers():
    """Deplay infomation on specific customers in the Āhua_Gallery"""
    with sqlite3.connect(DATABASE) as d_b:
        cursor = d_b.cursor()
        qrl = """SELECT first_name FROM customers;"""
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
                qrl = f"""SELECT first_name, last_name, postal_address, town, 
                postal_code FROM customers WHERE first_name = '{option}';"""
                cursor.execute(qrl)
                results = cursor.fetchall()
                headings = ["first_name","last_name","postal_address","town",
                            "postal_code"]
                alignments = ("left","left","center","left","left")
                # print resalts of query
                easygui.msgbox("infomation on specific customers in the "
                               "Āhua_Gallery:\n" + 
                               tabulate(results, headings, tablefmt="plain", 
                                        colalign=alignments), "MENU")
                break
            except:
                easygui.msgbox("Please choose one", "MENU")


def change_data():
    """Being able to DELETE/INSERT data"""
    with sqlite3.connect(DATABASE) as d_b:
        cursor = d_b.cursor()
        choce = easygui.choicebox("Do you whant to DELETE or INSERT data", 
                                  "MENU", ["DELETE", "INSERT"])
        if choce == "DELETE":
            try:
                piece = int(easygui.enterbox("Plese enter the piece id of the "
                                            "piece you want to delete", "MENU"))
            except:
                piece = int(easygui.enterbox("Plese enter a number", "MENU"))
            qrl = f"""DELETE FROM pieces WHERE piece_id = {piece};"""
            cursor.execute(qrl)
        elif choce == "INSERT":
            piece_name = easygui.enterbox("What is the name of the piece?", 
                                              "MENU")
            try:
                piece_price = int(easygui.enterbox("How much dose the piece "
                                                   "cost?", "MENU"))
            except:
                piece_price = int(easygui.enterbox("Pleace enter a number", 
                                                   "MENU"))
            piece_material = easygui.enterbox("What is the piece made out of?", 
                                              "MENU")
            piece_commission = easygui.ynbox("Is this piece a commission", 
                                             "MENU")
            if piece_commission == "True":
                piece_commission = "Yes"
            else:
                piece_commission = "No"
            piece_maker = easygui.enterbox("Who is the maker?", "MENU")
            qrl = f"""INSERT INTO pieces (piece_name, price, purchase_status, 
            material, commission, maker) VALUES ('{piece_name}', '{piece_price}'
            , 'Avalvbile', '{piece_material}', '{piece_commission}', 
            '{piece_maker}');"""
            cursor.execute(qrl)


def update_data():
    """Being able to UPDATE data"""
    with sqlite3.connect(DATABASE) as d_b:
        cursor = d_b.cursor()
        try:
            piece = int(easygui.enterbox("Plese enter the piece id of the "
                                        "piece you want to update", "MENU"))
        except:
            piece = int(easygui.enterbox("Plese enter a number", "MENU"))
        change = easygui.choicebox("What do you want to UPDATE", "MENU", 
                                   ["piece_name", "price", "purchase_status"])
        if change == "piece_name":
            change_value = easygui.enterbox("What is the new name?", "MENU")
            qrl = f"""UPDATE pieces SET {change} = "{change_value}" WHERE 
            piece_id = {piece};"""
        elif change == "price":
            try:
                change_value = int(easygui.enterbox("What is the new price?", 
                                                    "MENU"))
            except:
                change_value = int(easygui.enterbox("Enter a number", "MENU"))
            qrl = f"""UPDATE pieces SET {change} = {change_value} WHERE 
            piece_id = {piece};"""
        elif change == "purchase_status":
            change_value = easygui.choicebox("What do you what to update to", 
                                             "MENU", ["Avalbile", "Sold"])
            buyer = easygui.choicebox("Who boght it?", "MENU", 
                                      ["New buyer", "Previous buyer"])
            if buyer == "Previous buyer":
                costomer_id = easygui.enterbox("What is the costomer id?", 
                                               "MENU")
                qrl = f"""INSERT INTO pieces (piece_id, customer_id) VALUES 
                ('{piece}', '{costomer_id}');"""
                cursor.execute(qrl)
            else:
                cust_first = easygui.enterbox("What is the first name of the "
                                             "customer?", "MENU")
                cust_last = easygui.enterbox("What is the last name of the "
                                               "customer?", "MENU")
                cust_address = easygui.enterbox("What is the address of the "
                                               "customer?", "MENU")
                cust_town = easygui.enterbox("What is the town of the "
                                               "customer?", "MENU")
                try:
                    cust_postal_code = int(easygui.enterbox("What is the postal"
                                                            " code?", "MENU"))
                except:
                    cust_postal_code = int(easygui.enterbox("Enter a number", 
                                                        "MENU"))
                qrl = f"""INSERT INTO customers (first_name, last_name, 
                postal_address, town, postal_code) VALUES ('{cust_first}', 
                '{cust_last}', '{cust_address}', '{cust_town}', 
                {cust_postal_code})"""
                cursor.execute(qrl)
                costomer_id = easygui.enterbox("What is the costomer id?", 
                                               "MENU")
                qrl = f"""INSERT INTO pieces (piece_id, customer_id) VALUES 
                ('{piece}', '{costomer_id}');"""
                cursor.execute(qrl)
            qrl = f"""UPDATE pieces SET {change} = "{change_value}" WHERE 
            piece_id = {piece};"""
        cursor.execute(qrl)

# gui interface
if __name__ == "__main__":
    count = "i"
    option = "1"
    while option != "5":
        possible_querys = ["1. Deplaying all infomation of pieces", "2. "
                           "Deplaying all pieces that have sold", "3. Deplaying"
                           " all peices that are under a certain price", "4. "
                           "Deplay infomation on specific customers", "5. "
                           "DELETE/INSERT data", "6. UPDATE data", "7. Exit"]
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
            elif option == "5. DELETE/INSERT data":
                change_data()
            elif option == "6. UPDATE data":
                update_data()
            else:
                easygui.msgbox("Goodbye", "MENU")
                exit()
