import ado

def setor():
    return ado.buscar(cmd_sql="SELECT * FROM NC_SETOR")
def setor_novo_update(setorList):
    if setorList[0] == '':
        SQL = "INSERT INTO NC_SETOR(SETOR,CARGO,FUNCAO) VALUES('{}','{}','{}')".format(setorList[1],setorList[2],setorList[3])
    else:
        SQL = """UPDATE NC_SETOR
                SET
                    SETOR = '{}',
                    CARGO = '{}',
                    FUNCAO = '{}'
                WHERE
                    ID = {}
            """.format(setorList[1],setorList[2],setorList[3],setorList[0])
    print(SQL)
    return ado.executar(SQL)
def deletar_setor(id):
    SQL = "DELETE FROM NC_SETOR WHERE ID ={}".format(id)
    return ado.executar(SQL)