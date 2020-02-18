from mysql import connector as mys
import sys, os

BASE_PATH = os.path.abspath(__file__+ '../../../')
sys.path.append(BASE_PATH)

from inc.consts.consts import Consts as consts
from inc.classes.Exceptions import ConnectError

class Mysql:

    def __init__ (self, **kwargs):
        self.user = kwargs.get('user')
        self.password = kwargs.get('password')
        self.host = kwargs.get('host')
        self.port = kwargs.get('port') if kwargs.get('port')  else '3306'
        self.database = kwargs.get('database')

    def connect(self):
        try:
            connection = mys.connect(user = self.user,
                                        password = self.password,
                                        host = self.host,
                                        port = self.port,
                                        database = self.database)

            cursor = connection.cursor()
            cursor.execute("SELECT version();")
            record = cursor.fetchone()
            print("You are connected to - ", record,"\n")
            # self.conn = connection
            return connection

        except (Exception, mys.Error) as error :
            raise ConnectError("Error while connecting to MySQL", error)
    
    def read_tables(self, conn):
        tables = []
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES;")
        resp = cursor.fetchall()
    
        for table in resp:
            if table:
                tables.append(table[0])
    
        return tables
 

