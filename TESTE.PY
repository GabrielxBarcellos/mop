import ado
import controle

def copiar_mes(mes_antigo, mes_novo):
    CABECALHO =  list(ado.buscar(cmd_sql="SELECT TOP 1 * FROM NC_MOP")[0].keys())
    SQL = "SELECT "
    campos = ""
    for campo in CABECALHO:
        if campo != "ID" and campo != "MES_ANO":
            campos = campos + campo+","
    
    campos = campos[:len(campos)-1]

    SQL = SQL + campos +  ", '{}' MES_ANO  FROM NC_MOP WHERE MES_ANO = '{}'".format(mes_novo,mes_antigo)
    SQL_INSERT = "INSERT INTO NC_MOP ("+campos+", MES_ANO) " + SQL
    print(SQL_INSERT)

    return True
copiar_mes('2','2')