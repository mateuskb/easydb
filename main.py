import psycopg2
import pandas as pd
import sys, os

BASE_PATH = os.path.abspath(__file__+ './')
sys.path.append(BASE_PATH)

from inc.consts.consts import Consts as consts
from inc.classes.Exceptions import InputError

class Easydb:

    def __init__ (self, sgdb):
        if sgdb in consts.SGDB:
            self.sgdb = sgdb
        else:
            raise InputError(sgdb, f'SGDB {sgdb} is not supported! Check documentation!')


obj = Easydb('mongodb')
print(obj)