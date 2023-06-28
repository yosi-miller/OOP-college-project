import sqlite3 as s

class DataManagement:

    def __init__(self, name_file):
        self.connect = s.connect(name_file)  # This is creating a database and connect to the data
        self.pointer = self.connect.cursor()  # this is the pointer of the tada connect

    def create_tabel(self, tabel_name):  #הנתון יתקבל כטאפל או שנפתח לכל טבלה מחלקה חדשה?
        pass

    def insert_data(self, tabel_name, data):   #הנתון יתקבל כטאפל או שנפתח לכל טבלה מחלקה חדשה?
        pass

    def select_data(self, column_name, tabel_name):
        pass