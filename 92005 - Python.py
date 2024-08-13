'''A program to conect to the Āhua_Gallery database and run difrent queries on 
it.
By: Matt Smith                                                      12/8/2024'''

#all the constences
DATABASE = "92005 - Database.SQlite"

#import staments
import sqlite3
import os
# run pip3 install tabulate to use this libry to print results in columns
from tabulate import tabulate

#funtions for the Querys
def all_pieces():
    '''Deplay all infomation of all pieces'''
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        qrl = "SELECT * FROM pieces;"
        cursor.execute(qrl)
        results = cursor.fetchall()
        headings = ["player_id","piece_name","price","purchase status","material",
                    "commission", "maker"]
        alignments = ("left","left","left","left","center","center","center")
        #print resalts of query
        print("All infomation of All Black players:\n")
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
        print("4. ")
        print("5. Exit")
        while count != "Exit":
            option = input("choose an option from the menu 1, 2, 3, 4, and 5: ")
            os.system("cls")
            if option == "1":
                all_pieces()
                count = "Exit"
            elif option == "2":
                fly_half()
                count = "Exit"
            elif option == "3":
                most_points()
                count = "Exit"
            elif option == "4":
                started_after_2010_50_tests()
                count = "Exit"
            elif option == "5":
                print("Goodbye.........")
                exit()
            else:
                print("This is not one of the options try again")
        count = input("Enter to return to menu...")
