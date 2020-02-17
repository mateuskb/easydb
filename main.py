import pandas as pd
import sys, os

BASE_PATH = os.path.abspath(__file__+ './')
sys.path.append(BASE_PATH)

from inc.consts.consts import Consts as consts
from inc.classes.Exceptions import InputError

from inc.classes.sgdb.Pgsql import Pgsql
from inc.classes.sgdb.Mysql import Mysql


class Easydb:

    def __init__ (self, sgdb):
        if sgdb in consts.SGDB:
            self.sgdb = sgdb
        else:
            raise InputError(sgdb, f'SGDB {sgdb} is not supported! Check documentation!')

    def connect(self, **kwargs):
        if self.sgdb == 'pgsql':
            return(Pgsql(**kwargs))
        elif self.sgdb == 'mysql':
            return(Mysql(**kwargs))

obj = Easydb('mysql')
#obj = Easydb('pgsql')

conn = obj.connect(host="localhost", user="mateuskb", password='Qwerty123@', database='pibiti') # MYSQL
#conn = obj.connect(host="192.168.100.59", user="mateuskb", password='djrtdg33', database='GestMe') # PGSQL

print(conn.read_tables())

'''{
    'hostname': "192.168.100.59",
    'username': "mateuskb",
    'password': "djrtdg33",
    'database': "GestMe"
}''' 
'''{
    'hostname': "localhost",
    'username': "mateuskb",
    'password': "Qwerty123@",
    'database': "pibiti"
}''' 
