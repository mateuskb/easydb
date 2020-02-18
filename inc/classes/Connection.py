import sys, os

BASE_PATH = os.path.abspath(__file__+ '../../')
sys.path.append(BASE_PATH)

from inc.consts.consts import Consts as consts
from inc.classes.Exceptions import *

from inc.classes.sgdb.Pgsql import Pgsql
from inc.classes.sgdb.Mysql import Mysql

class Connection:

    def __init__ (self, sgdb, **kwargs):
        self.conn = None;

        self.sgdb = sgdb

        self.host = kwargs.get('host')
        self.user = kwargs.get('user')
        self.password = kwargs.get('password')
        self.database = kwargs.get('database')
        self.port = kwargs.get('port') if kwargs.get('port')  else ''

        self.connect()

    def connect(self):
        try:
            if self.sgdb == 'pgsql':
                self.obj = Pgsql(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database,
                    port=self.port
                    )

            elif self.sgdb == 'mysql':
                self.obj = Mysql(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database,
                    port=self.port
                    )

            self.conn = self.obj.connect()

        except Exception as e:
            raise InputError(self.sgdb, f'Error: {e}')

    def read_tables(self):
        return self.obj.read_tables(self.conn)


    def create(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def insert(self):
        pass