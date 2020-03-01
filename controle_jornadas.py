import ado

def jornada_novo_update(jornadaList):
    if jornadaList[0] == '':
        SQL = "INSERT INTO NC_JORNADA(JORNADA,HRS,TURNO) VALUES('{}','{}','{}')".format(jornadaList[1],jornadaList[2],jornadaList[3])
    else:
        SQL = """UPDATE NC_JORNADA
                SET
                    JORNADA = '{}',
                    HRS = '{}',
                    TURNO = '{}'
                WHERE
                    ID = {}
            """.format(jornadaList[1],jornadaList[2],jornadaList[3],jornadaList[0])
    print(SQL)
    return ado.executar(SQL)

def deletar_jornada(id):
    SQL = """
    DELETE FROM NC_JORNADA 
    WHERE ID = {}
    """.format(id)
    print(SQL)
    return ado.executar(SQL)

