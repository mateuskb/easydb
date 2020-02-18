from main import Easydb

obj = Easydb('mysql')
#obj = Easydb('pgsql')

conn = obj.connect(host="localhost", user="mateuskb", password='Qwerty123@', database='easyDB') # MYSQL
#conn = obj.connect(host="192.168.100.59", user="mateuskb", password='djrtdg33', database='easydb') # PGSQL

print(conn.read_tables())


'''{
    'hostname': "192.168.100.59",
    'username': "mateuskb",
    'password': "djrtdg33",
    'database': "easydb"
}''' 
'''{
    'hostname': "localhost",
    'username': "mateuskb",
    'password': "Qwerty123@",
    'database': "easyDB"
}''' 
