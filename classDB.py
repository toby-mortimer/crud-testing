from fileinput import filename
import sqlite3
from sqlite3 import Error

class People:
    """ Initialise a database and creates a connection string"""

    @property
    def Conn(self):
        return self.conn

    def __init__(self, filename) -> None:
        """ Creates a database during instance construction
        :param db name: database filename
        :param conn: Connection to the database
        """
        self.db_name = filename
        self.conn = None
        self.create_connection(self,db_name)

    
    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        self.conn = conn
    
    if __name__ == '__main__':
        print("Must be loaded as a module")