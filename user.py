import ado

def users():
    return ado.buscar(cmd_sql="SELECT * FROM NC_USER")
def user_novo_update(user):
    SQL ="""
    IF NOT EXISTS (SELECT * FROM NC_USER WHERE MATRICULA = {MATRICULA})
    INSERT INTO NC_USER
    (MATRICULA,
     SENHA,
      NV)
    VALUES(
        {MATRICULA},
        '{SENHA}',
        '{NV}'
    )
    ELSE
    UPDATE NC_USER
                SET
                    SENHA = '{SENHA}',
                    NV = '{NV}'
                WHERE
                    MATRICULA = {MATRICULA}
    """.format(
                MATRICULA = user[0],
                SENHA = user[1],
                NV = user[2])
    print(SQL)
    return ado.executar(SQL)
def delete_user(id):
    SQL = "DELETE FROM NC_USER WHERE MATRICULA ={}".format(id)
    return ado.executar(SQL)

def trocar_senha(usuario , senha):
    SQL = """UPDATE NC_USER
            SET
                MATRICULA = {MATRICULA},
                SENHA = '{SENHA}'
            WHERE MATRICULA = {MATRICULA}""".format(MATRICULA = usuario, SENHA = senha)
    print(SQL)
    return ado.executar(SQL)