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

    def cadastrar(self):
        SQL = """INSERT INTO NC_MOP(CAD,NOME,RAMAL,PAUSAS,CELULAR,MONITORIA,CC,SETOR,CARGO,FUNCAO,NVL,GESTOR,JORNADA,SAB,MES_ANO) 
                             VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(
                                 self.cad,
                                 self.nome,
                                 self.ramal,
                                 self.pausa,
                                 self.celular,
                                 self.monitoria,
                                 self.cc,
                                 self.setor,
                                 self.cargo,
                                 self.funcao,
                                 self.nvl,
                                 self.gestor,
                                 self.jornada,
                                 self.sab,
                                 self.mes_ano
                             )
        return ado.executar(SQL)

    def filtrar(self):
        elementos = [
            ('CAD',self.cad), 
            ('NOME',self.nome),
            ('RAMAL',self.ramal),
            ('PAUSAS',self.pausa),
            ('CELULAR',self.celular),
            ('MONITORIA',self.monitoria),
            ('CC',self.cc),
            ('SETOR',self.setor),
            ('CARGO',self.cargo),
            ('FUNCAO',self.funcao),
            ('NVL',self.nvl),
            ('GESTOR',self.gestor),
            ('JORNADA',self.jornada)]

        lista_somente_elemento_preenchido = []
        
        for e  in elementos:
            if e[1] != None:
                lista_somente_elemento_preenchido.append(e)
        
        filtro = ""

        for campo in lista_somente_elemento_preenchido:
            filtro = campo[0] + " = '" + campo[1] + "'," 
        
        filtro = filtro.sus[ :len(filtro) -1] 

        return filtro
        


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