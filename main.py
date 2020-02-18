import pandas as pd
import sys, os

BASE_PATH = os.path.abspath(__file__+ './')
sys.path.append(BASE_PATH)

from inc.consts.consts import Consts as consts
from inc.classes.Exceptions import InputError

from inc.classes.Connection import Connection


class Easydb:
    '''
        EasyDB is a API to help you connect to your favourite SGDB's
        Args:
            sgdb : e.g 'mysql'
        Return EasyDB object.

        def connect 
        args:
            host: e.g. 'localhost'
            user: e.g. 'Username'        
            password: e.g. 'password'        
            database: e.g. 'database'     
            port: e.g. 0000   
    '''
    def __init__ (self, sgdb):
        
        if sgdb in consts.SGDB:
            self.sgdb = sgdb
        else:
            raise InputError(sgdb, f'SGDB {sgdb} is not supported! Check documentation!')

    def connect(self, **kwargs):
        return Connection(self.sgdb, **kwargs)

