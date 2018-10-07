import MySQLdb as mysql

def connect():
    global db
    info = {
        'host':     'localhost',
        'db':       'project',
        'user':     'root',
        'passwd':   'smalldragon487',
        'charset':  'utf8'
    }
    # db = mysql.connect(**info)
    try:
        db = mysql.connect(**info)
        print('Connect success!')
    except:
        print('Connect fail!')
