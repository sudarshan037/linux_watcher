import os
import sqlite3
from datetime import datetime

class ChromeHistory:
    def __init__(self):
        username = os.getlogin( )
        self.connection_string = f'/home/{username}/.config/google-chrome/Default/History'
        self.query = "select url, title, visit_count, last_visit_time from urls"
        self.cursor = None

    def __connect(self):
        connection = sqlite3.connect(self.connection_string)
        self.cursor = connection.cursor()

    def execute(self):
        self.__connect()
        self.cursor.execute(self.query)
        results = self.cursor.fetchall()
        return results