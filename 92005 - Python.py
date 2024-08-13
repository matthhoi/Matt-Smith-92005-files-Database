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


