import mariadb
import dbcreds

def Userlogin():
    conn = None
    cursor = None

    try:
        print('Welcome to CliSocialMedia')
        alias = input('alias: ')
        password = input('password: ')

        conn = mariadb.connect(
            user=dbcreds.user,
            host=dbcreds.host,
            password=dbcreds.password,
            port=dbcreds.port,
            database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM hackers WHERE alias = ? AND password = ?' , [alias, password])
        result = cursor.fetchall()
        user_id = result[0][0]
        if len(result) == 1:
            print('you have logged in')
        
        else:
           raise Exception('not logged in')
    except mariadb.ProgrammingError:
        print('Bad sql code written')

    except mariadb.OperationalError:
        print('connection failed')

    except:
        print('check username/password')
    finally:
        if(cursor != None):
            cursor.close()
        if(conn != None):
            conn.rollback()
            conn.close
        return user_id
def CreateExploit():
    conn = None
    cursor = None

    try:
        conn = mariadb.connect(
            ser=dbcreds.user,
            host=dbcreds.host,
            password=dbcreds.password,
            port=dbcreds.port,
            database=dbcreds.database)
        cursor = conn.cursor()
        exploit = input('Enter exploit: ')
        cursor.execute('INSERT INTO exploits(content) VALUES(?)', [exploit, ])
        cursor.commit()
        if(cursor.rowcount == 1):
            print('Exploit posted')
        else:
            raise Exception('exploit not created')
    except mariadb.ProgrammingError:
            print('Sorry bad SQL written')
    except mariadb.OperationalError:
            print('connection failed')
    finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close

def SeeAllExploits():
    conn = None
    cursor = None

    try:
        conn = mariadb.connect(
                ser=dbcreds.user,
                host=dbcreds.host,
                password=dbcreds.password,
                port=dbcreds.port,
                database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM exploits')
        allExploits = cursor.fetchall()
        print(allExploits)
    except mariadb.OperationalError:
            print('connection failed')
    except mariadb.ProgrammingError:
            print("SQL lessons needed")
    finally:
            if(cursor != None):
                cursor.close
            if(conn != None):
                conn.rollback
                conn.close

def otherExploits():
    conn = None
    cursor = None

    try:
        conn = mariadb.connect(
                ser=dbcreds.user,
                host=dbcreds.host,
                password=dbcreds.password,
                port=dbcreds.port,
                database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute(' SELECT * FROM exploits WHERE user_id!=?', [user_id,])
        otherExploits = cursor.fetchall()
    except mariadb.ProgrammingError:
        print('Bad SQL code written')
    except mariadb.OperationalError:
        print('Connection failed')
    finally:
        if(cursor != None):
            cursor.close
        if(conn != None):
            conn.rollback
            conn.close

def exitApp():
    conn = None
    cursor = None

    try:
        if(cursor != None):
            cursor.close
        if(conn != None):
            conn.rollback
            conn.close
       
while true:
    #cant solve this error :(
    print('Chose one of the options: ')
    print('1. Create exploits')
    print('2. See your exploits')
    print('3. See all exploits')
    print('4. Exit')

    options = '1', '2,', '3', '4'
    if options == 1:
        CreateExploit()
    elif options == 2:
        SeeAllExploits()
    elif options == 3:
        otherExploits()
    else options == 4:
        exitApp()