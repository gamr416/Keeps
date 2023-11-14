import sqlite3
import os

class Storage:
    def __init__(self):
        self.note_add_callback = None
        absolute_path = os.path.dirname(__file__)
        relative_path = 'current_user.txt'
        full_path = os.path.join(absolute_path, relative_path)
        file = open(full_path)
        lines = file.read().split('\n')
        self.id = lines[0]
        self.name = lines[1]
        self.email = lines[2]
        self.password = lines[3]
        file.close()
        
    def set_note_add_callback(self, function):
        self.note_add_callback = function
    
    def add_note(self, date, text):
        absolute_path = os.path.dirname(__file__)
        relative_path = 'databases/users_db'
        full_path = os.path.join(absolute_path, relative_path)
        self.con = sqlite3.connect(full_path)
        self.cur = self.con.cursor()
        command = self.cur.execute(
                    f"""INSERT INTO {'s' + str(self.id)}(note, date)
                        VALUES('{text}', '{date}')"""
                )
        self.con.commit()
        self.con.close()
        if bool(self.note_add_callback):
            self.note_add_callback()

global_storage = Storage()
            