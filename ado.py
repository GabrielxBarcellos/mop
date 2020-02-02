import pyodbc
import json

def json_config():
    with open("dados.json", "r") as read_file:
        data = json.load(read_file)
    return data


def conn():
    credenciais = json_config()["conn"]
    server = credenciais["server"]
    database = credenciais["database"]
    username = credenciais["username"]
    password = credenciais["password"]
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