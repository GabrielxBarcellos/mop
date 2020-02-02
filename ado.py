import pyodbc


def conn():
    server = 'gbarcellossilva.database.windows.net'
    database = 'SANDBOX'
    username = 'gbarcellossilva'
    password = 'Red-Hot1996'
    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    return cnxn


def buscar(table="", cmd_sql="SELECT * FROM "):
    cnxn = conn()
    cursor = cnxn.cursor()
    if cmd_sql == "SELECT * FROM ":
        cursor.execute("SELECT * FROM " + table)
    else:
        cursor.execute(cmd_sql)
    columns = [column[0] for column in cursor.description]
    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    cnxn.close()
    return results
def executar(SQL):
        numero_linhas = 0
        try: 
            cnxn = conn()
            cursor = cnxn.cursor()
            cursor.execute(SQL)
            numero_linhas = cursor.rowcount
            cnxn.commit()
            cnxn.close()
        except:
            return numero_linhas

        return numero_linhas