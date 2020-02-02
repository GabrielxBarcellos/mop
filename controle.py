import ado
class agente():
    def __init__(self, cad, nome, ramal ,pausa ,celular, monitoria, cc, setor, cargo, funcao, nvl, gestor, jornada, sab, mes_ano ):
        self.cad = cad
        self.nome = nome
        self.ramal = ramal
        self.pausa  = pausa
        self.celular = celular
        self.monitoria = monitoria
        self.cc = cc
        self.setor = setor
        self.cargo = cargo
        self.funcao = funcao
        self.nvl = nvl
        self.gestor = gestor
        self.jornada = jornada
        self.sab = sab
        self.mes_ano = mes_ano

    def cadastrar(this):
        SQL = """INSERT INTO NC_MOP(CAD,NOME,RAMAL,PAUSAS,CELULAR,MONITORIA,CC,SETOR,CARGO,FUNCAO,NVL,GESTOR,JORNADA,SAB,MES_ANO) 
                             VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(
                                 this.cad,
                                 this.nome,
                                 this.ramal,
                                 this.pausa,
                                 this.celular,
                                 this.monitoria,
                                 this.cc,
                                 this.setor,
                                 this.cargo,
                                 this.funcao,
                                 this.nvl,
                                 this.gestor,
                                 this.jornada,
                                 this.sab,
                                 this.mes_ano
                             )
        return ado.executar(SQL)

def mop():
    return ado.buscar( table="NC_MOP")

def jornada():
    return ado.buscar( cmd_sql="SELECT DISTINCT JORNADA FROM NC_JORNADA")

def gestor():
    return ado.buscar( table="NC_GESTOR")

def cc():
    return ado.buscar( table="NC_CC")

def setor():
    SQL = 'SELECT DISTINCT SETOR FROM NC_SETOR'
    return ado.buscar( cmd_sql= SQL)

def funcao(setor):
    SQL = "SELECT DISTINCT FUNCAO FROM NC_SETOR WHERE SETOR = '{}'".format(setor)
    return ado.buscar( cmd_sql= SQL)
    
def cargo(setor,funcao):
    SQL = "SELECT DISTINCT CARGO FROM NC_SETOR WHERE SETOR = '{}' and FUNCAO = '{}'".format(setor,funcao)
    return ado.buscar( cmd_sql= SQL)

def mes():
    SQL = "SELECT * FROM NC_MES ORDER BY ORDEM DESC"
    return ado.buscar( cmd_sql= SQL)