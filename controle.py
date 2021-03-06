import ado
import csv
import os

class agente():
    def __init__(self, cad, nome, ramal ,pausa ,celular, monitoria, cc, setor, cargo, funcao, nvl, gestor, jornada, sab, mes_ano, data_adm, data_desligamento,status,dt_piso):
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
        self.data_adm =data_adm
        self.data_desligamento = data_desligamento
        self.status = status
        self.dt_piso = dt_piso

    @staticmethod
    def buscar_por_id(ID):

        SQL = "SELECT * FROM NC_MOP WHERE ID = " + ID 

        print(SQL)
        return ado.buscar(cmd_sql= SQL)[0]


    def cadastrar(self):
        SQL = """INSERT INTO NC_MOP(
        CAD,
        NOME,
        RAMAL,
        PAUSAS,
        CELULAR,
        MONITORIA,
        CC,
        SETOR,
        CARGO,
        FUNCAO,
        NVL,
        GESTOR,
        JORNADA,
        SAB,
        MES_ANO,
        DATA_ADM,
        DATA_DESLIGAMENTO,
        STATUS,
        DT_PISO) 
                             VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}', '{}')""".format(
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
                                 self.mes_ano,
                                 self.data_adm,
                                 self.data_desligamento,
                                 self.status,
                                 self.dt_piso
                             )
        print(SQL)
        return ado.executar(SQL)


    @staticmethod
    def deletar(id):
        SQL = "DELETE FROM NC_MOP WHERE ID = {}".format(id)
        
        try:
            ado.executar(SQL)
        except:
            return False
        return True
    def atualizar(self,id):
        SQL = """UPDATE NC_MOP
                SET
                        CAD = '{CAD}',
                        NOME = '{NOME}',
                        RAMAL = '{RAMAL}',
                        PAUSAS = '{PAUSAS}',
                        CELULAR = '{CELULAR}',
                        MONITORIA = '{MONITORIA}',
                        SETOR = '{SETOR}',
                        CARGO = '{CARGO}',
                        FUNCAO = '{FUNCAO}',
                        CC = '{CC}',
                        NVL = '{NVL}',
                        GESTOR = '{GESTOR}',
                        JORNADA = '{JORNADA}',
                        SAB = '{SAB}',
                        MES_ANO = '{MES_ANO}',
                        DATA_ADM ='{DATA_ADM}',
                        DATA_DESLIGAMENTO = '{DATA_DESLIGAMENTO}',
                        STATUS = '{STATUS}',
                        DT_PISO = '{DT_PISO}'
                WHERE
                    ID = {id}""".format(
                        CAD= self.cad,
                        NOME= self.nome,
                        RAMAL= self.ramal               ,
                        PAUSAS= self.pausa,
                        CELULAR=self.celular,
                        MONITORIA= self.monitoria,
                        CC=self.cc,
                        SETOR= self.setor,
                        CARGO=self.cargo,
                        FUNCAO=self.funcao,
                        NVL=self.nvl,
                        GESTOR=self.gestor,
                        JORNADA=self.jornada,
                        SAB=self.sab,
                        MES_ANO=self.mes_ano,
                        DATA_ADM =self.data_adm,
                        DATA_DESLIGAMENTO =self.data_desligamento,
                        STATUS =self.status,
                        DT_PISO = self.dt_piso,
                        id= id
                    )

        ado.executar(SQL)


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
            ('JORNADA',self.jornada),
            ('SAB',self.sab),
            ('MES_ANO',self.mes_ano),
            ('DATA_DESLIGAMENTO',self.data_desligamento),
            ('STATUS',self.status)
            ]

        lista_somente_elemento_preenchido = []
        
        for e  in elementos:
            if e[1] != '':
                lista_somente_elemento_preenchido.append(e)
        
        filtro = ""

        for campo in lista_somente_elemento_preenchido:
            filtro = filtro  + campo[0] + " = '" + campo[1] + "' and " 
        
        filtro = filtro[ :len(filtro) -4] 

        SQL = 'SELECT * FROM NC_MOP WHERE ' + filtro
        if (len(lista_somente_elemento_preenchido)>0) :
            return ado.buscar(cmd_sql= SQL)
        else:
            return mop()

def mop():
    SQL = """
    SELECT 
            A.*,B.HRS,B.TURNO
            FROM NC_MOP AS A
        LEFT JOIN
            NC_JORNADA AS B
        ON
            A.JORNADA = B.JORNADA
         """
    retorno  = ado.buscar( cmd_sql=SQL)
    return retorno

def jornada():
    return ado.buscar( cmd_sql="SELECT DISTINCT JORNADA FROM NC_JORNADA")

def gestor():
    return ado.buscar( table="NC_GESTOR")

def cc():
    return ado.buscar( table="NC_CC")

def setor():
    SQL = 'SELECT DISTINCT SETOR FROM NC_SETOR'
    return ado.buscar( cmd_sql= SQL)

def funcao_():
    SQL = "SELECT DISTINCT FUNCAO FROM NC_SETOR"
    return ado.buscar(cmd_sql= SQL) 

def funcao(setor):
    SQL = "SELECT DISTINCT FUNCAO FROM NC_SETOR WHERE SETOR = '{}'".format(setor)
    print(SQL)
    return ado.buscar( cmd_sql= SQL)
    
def cargo(setor,funcao):
    SQL = "SELECT DISTINCT CARGO FROM NC_SETOR WHERE SETOR = '{}' and FUNCAO = '{}'".format(setor,funcao)
    return ado.buscar( cmd_sql= SQL)

def cargo_():
    SQL = """SELECT DISTINCT CARGO FROM(
                SELECT DISTINCT CARGO FROM NC_SETOR
                UNION
                SELECT DISTINCT CARGO FROM NC_MOP) AS A """
    return ado.buscar( cmd_sql= SQL)

def mes():
    SQL = "SELECT * FROM NC_MES ORDER BY ORDEM DESC"
    return ado.buscar( cmd_sql= SQL)

def status():
    SQL = "SELECT * FROM NC_STATUS"
    return ado.buscar(cmd_sql=SQL)

def logar(usuario,senha):

    SQL = "SELECT * FROM NC_USER WHERE MATRICULA = {} AND SENHA = '{}'".format(usuario,senha)
    return ado.buscar(cmd_sql=SQL)[0]
def buscar_importados():
    SQL = "SELECT * FROM NC_USER WHERE STATUS = 'i'"
    return ado.buscar(cmd_sql=SQL)

def movimentacao(matricula,mes_ano,nome,setor_antigo,cargo_antigo,funcao_antigo,status_antigo, cc_antigo, jornada_antigo,setor_novo,cargo_novo,funcao_novo,jornada_novo,cc_novo,movimentacao,data):
    SQL = """INSERT INTO NC_MOVIMENTACOES_DESLIGAMENTO
    (MATRICULA,
    MES_ANO,
    NOME,
    SETOR_ANTIGO,
    CARGO_ANTIGO,
    FUNCAO_ANTIGO,
    CC_ANTIGO,
    JORNADA_ANTIGO,
    STATUS_ANTIGO,
    SETOR_NOVO,
    CARGO_NOVO,
    FUNCAO_NOVO,
    CC_NOVO,
    JORNADA_NOVO,
    MOVIMENTACAO,
    DATA_MOVIMENTACAO)
    VALUES(
        {MATRICULA},
        '{MES_ANO}',
        '{NOME}',
        '{SETOR_ANTIGO}',
        '{CARGO_ANTIGO}',
        '{FUNCAO_ANTIGO}',
        '{CC_ANTIGO}',
        '{JORNADA_ANTIGO}',
        '{STATUS_ANTIGO}',
        '{SETOR_NOVO}',
        '{CARGO_NOVO}',
        '{FUNCAO_NOVO}',
        '{CC_NOVO}',
        '{JORNADA_NOVO}',
        '{MOVIMENTACAO}',
        '{DATA}'      
        )""".format(MATRICULA = matricula, 
        MES_ANO = mes_ano,
        NOME = nome, 
        SETOR_ANTIGO = setor_antigo, 
        CARGO_ANTIGO = cargo_antigo, 
        FUNCAO_ANTIGO = funcao_antigo,
        CC_ANTIGO = cc_antigo,
        JORNADA_ANTIGO = jornada_antigo  ,
        STATUS_ANTIGO = status_antigo,
        SETOR_NOVO = setor_novo,
        CARGO_NOVO = cargo_novo,
        FUNCAO_NOVO = funcao_novo,
        CC_NOVO = cc_novo,
        JORNADA_NOVO = jornada_novo,
        MOVIMENTACAO = movimentacao,
        DATA = data
         )
    try:
        print(SQL)
        return ado.executar(SQL)
    except:
        print('erro ao fazer a operacao')
        return False


def dict_to_agente(dicionario):
    return agente(
    dicionario['CAD'],
    dicionario['NOME'],
    dicionario['RAMAL'],
    dicionario['PAUSAS'],
    dicionario['CELULAR'],
    dicionario['MONITORIA'],
    dicionario['CC'],
    dicionario['SETOR'],
    dicionario['CARGO'],
    dicionario['FUNCAO'],
    dicionario['NVL'],
    dicionario['GESTOR'],
    dicionario['JORNADA'],
    dicionario['SAB'],
    dicionario['MES_ANO'],
    dicionario['DATA_ADM'],
    dicionario['DATA_DESLIGAMENTO'],
    dicionario['STATUS'],
    None)

def movimentacoes():
    movimentacoes = ado.buscar(table="NC_MOVIMENTACOES_DESLIGAMENTO")
    if len(movimentacoes) == 0  : 
        movimentacoes = [{"SEM RESULTADO":"SEM RESULTADO"}]
    return movimentacoes

def atualizar_movimentacao(feito, id_movimentacao):
    SQL = """
    UPDATE NC_MOVIMENTACOES_DESLIGAMENTO
    SET 
        FEITO = {}
    WHERE
        ID = {}""".format(feito, id_movimentacao)
    print(SQL)
    return ado.executar(SQL)

def jornadas():
    jornadas =ado.buscar(table='NC_JORNADA') 
    if len(jornadas) == 0  : 
        jornadas = [{"SEM RESULTADO":"SEM RESULTADO"}]
    return jornadas