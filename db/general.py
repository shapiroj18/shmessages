import os
import re
import sqlite3

class DB:
    def __init__(self):
        self.chat_db_path = os.environ['CHATDB_PATH']
        self.contacts_db_path = os.environ['CONTACTSDB_PATH']
        self.connection = sqlite3.connect(self.chat_db_path)
        self.cursor = self.connection.cursor()
        
    def substr_phone(self, phone_number):
        try:
            formatted_num = re.sub('\D', '', phone_number)
            return formatted_num
        except TypeError:
            return None

        
    def setup_attached_databases(self):
        self.connection.create_function("substr_phone", 1, self.substr_phone)
        self.cursor.execute(f"""ATTACH DATABASE '{self.contacts_db_path}' AS contacts;""")
    
    
    def query_db(self, query):
        self.cursor.execute(query)
        response_data = []
        for row in self.cursor.fetchall():
            response_data.append(row)
            
        return response_data