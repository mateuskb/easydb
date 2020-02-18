import psycopg2
import sys, os

BASE_PATH = os.path.abspath(__file__+ '../../../')
sys.path.append(BASE_PATH)

from inc.consts.consts import Consts as consts
from inc.classes.Exceptions import ConnectError

class Pgsql:

    def __init__ (self, **kwargs):
        self.user = kwargs.get('user')
        self.password = kwargs.get('password')
        self.host = kwargs.get('host')
        self.port = kwargs.get('port')
        self.database = kwargs.get('database')
    


    def connect(self):
        try:
            connection = psycopg2.connect(user = self.user,
                                        password = self.password,
                                        host = self.host,
                                        port = self.port,
                                        database = self.database,
                                        connect_timeout=consts.CONNECT_TIMEOUT)
                                    

            cursor = connection.cursor()
            # Print PostgreSQL Connection properties
            # print ( connection.get_dsn_parameters(),"\n")

            # Print PostgreSQL version
            cursor.execute("SELECT version();")
            record = cursor.fetchone()
            print("You are connected to - ", record,"\n")
            # self.connection = connection
            return connection

        except (Exception, psycopg2.Error) as error :
            raise ConnectError("Error while connecting to PostgreSQL", error)

    def read_tables(self, conn):
        tables = []
        cursor = conn.cursor()
        cursor.execute("select * from information_schema.tables where table_schema='public';")
        resp = cursor.fetchall()
    
        for table in resp[0]:
            if table:
                tables.append(table)
    
        return tables