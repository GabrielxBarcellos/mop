
from controle import agente as agente_obj
from controle import mop
import csv
from datetime import datetime
import ado
import os
import datetime

# tratando importa RH
def backup_mop(pasta):
    mop_ = mop()
    cabecalho = []
    linha = []
    lista = []
    lista.append(list(mop_[0].keys()))
    for linha in mop_:
        aux = []
        for item in mop_[0].keys():
            aux.append(linha[item])
        lista.append(aux)

    filename = str(datetime.datetime.now())
    filename = filename.replace(":","-")+'.csv'

    arquivo = os.path.join(os.path.join(pasta, 'backup_importas'),filename)
    with open(arquivo, "w", newline="", encoding='utf-8') as f:
        writer = csv.writer(f, delimiter = ";")
        writer.writerows(lista)

    return True

def listToDict(lstA, lstB):
    zippedLst = zip(lstA, lstB)
    op = dict(zippedLst)
    print(op)
    return op

def dt_br_to_dt(data_str):
    b = datetime.datetime.strptime(data_str,'%d/%m/%Y')
    return datetime.datetime.strftime(b,'%Y-%m-%d')

def importar_v2(agente_obj):
        SQL = """
        BEGIN TRAN 

        IF EXISTS (SELECT * 
                FROM   nc_mop WITH (updlock, serializable) 
                WHERE  
                        CAD = '{CAD}'
                        AND
                        MES_ANO = '{MES_ANO}')
        BEGIN 
            UPDATE nc_mop 
            SET    
 
                        CAD = '{CAD}',
                        CC = '{CC}',
                        NOME = '{NOME}',
                        CARGO = '{CARGO}',
                        MES_ANO = '{MES_ANO}',
                        DATA_ADM ='{DATA_ADM}'
                    
            WHERE  MES_ANO  = '{MES_ANO}' AND CAD = '{CAD}' 
        END 
        ELSE 
        BEGIN 
            INSERT INTO nc_mop 
                        (
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
                        STATUS) 
            VALUES      (
                        '{CAD}',
                        '{NOME}',
                        '{RAMAL}',
                        '{PAUSAS}',
                        '{CELULAR}',
                        '{MONITORIA}',
                        '{CC}',
                        '{SETOR}',
                        '{CARGO}',
                        '{FUNCAO}',
                        '{NVL}',
                        '{GESTOR}',
                        '{JORNADA}',
                        '{SAB}',
                        '{MES_ANO}',
                        '{DATA_ADM}',
                        '{DATA_DESLIGAMENTO}',
                        '{STATUS}'
                        )
        END 

        COMMIT TRAN 
        """.format(
                        CAD= agente_obj.cad,
                        NOME= agente_obj.nome,
                        RAMAL= agente_obj.ramal               ,
                        PAUSAS= agente_obj.pausa,
                        CELULAR=agente_obj.celular,
                        MONITORIA= agente_obj.monitoria,
                        CC=agente_obj.cc,
                        SETOR= agente_obj.setor,
                        CARGO=agente_obj.cargo,
                        FUNCAO=agente_obj.funcao,
                        NVL=agente_obj.nvl,
                        GESTOR=agente_obj.gestor,
                        JORNADA=agente_obj.jornada,
                        SAB=agente_obj.sab,
                        MES_ANO=agente_obj.mes_ano,
                        DATA_ADM =agente_obj.data_adm,
                        DATA_DESLIGAMENTO =agente_obj.data_desligamento,
                        STATUS =agente_obj.status,
        )
        print(SQL)
        ado.executar(SQL)
        return True

def importar_agentes (arquivo):
    with open(arquivo,encoding='utf-8') as arquivo:
        linhas = csv.reader(arquivo, delimiter=";")

        aux = []
        for item in linhas:
            aux.append(item)
        

    #transformar em dict
    cabecalho = aux[0]
    corpo = aux[1:]

    for item in corpo :
        agente = listToDict(cabecalho,item)
        agent = agente_obj(
            cad = agente["Cadast."],
            nome = agente["Nome"],
            ramal= "i",
            pausa = "i",
            celular = "i",
            monitoria="i",
            cc= agente["CC"],
            setor = "i",
            cargo = agente["CARGO"],
            funcao = "i",
            nvl = "i",
            gestor = "i",
            jornada = 'i',
            sab = 'i',
            mes_ano = agente["MES_ANO"],
            data_adm =dt_br_to_dt( agente["ADM"] ),
            status = 'i',
            data_desligamento = 'i'
            )
        print(agent.data_desligamento)
        importar_v2(agent)
    return True

def csv_to_sql(arquivo_csv):

    with open(arquivo_csv,encoding='utf-8') as arquivo:

        linhas = csv.reader(arquivo, delimiter=";")

        contagem = 0
        SQL = 'INSERT INTO NC_MOP('
        for linha in linhas:            
            #CABEÇALHO

            if (contagem == 0) :
                
                ignora = 0 #ignora o id
                for item in linha:
                    if ignora != 0:
                        SQL += str(item).strip() + ","
                    ignora += 1



                SQL = SQL.strip()
                SQL = SQL[:-2] +') VALUES '
                contagem += 1

                continue

            #corpo
            SQL+="("
            ignora = 0 #ignora o id
            for item in linha:
                if ignora != 0 :
                    SQL += "'" +item + "',"
                ignora += 1
            SQL = SQL[:-4] + "),"
            contagem +=1
        SQL = SQL[:-1]
        print(SQL)
        return SQL

def importar(arquivo):

    ado.executar(csv_to_sql(arquivo))
    os.remove(arquivo)
# end importa RH


#copiar mes

    
def copiar_mes(mes_antigo, mes_novo,pasta_backup):
    def copiar_mes_sql(mes_antigo, mes_novo):
        CABECALHO =  list(ado.buscar(cmd_sql="SELECT TOP 1 * FROM NC_MOP")[0].keys())
        SQL = "SELECT "
        campos = ""
        for campo in CABECALHO:
            if campo != "ID" and campo != "MES_ANO":
                campos = campos + campo+","
        
        campos = campos[:len(campos)-1]

        SQL = SQL + campos +  ", '{}' MES_ANO  FROM NC_MOP WHERE MES_ANO = '{}'".format(mes_novo,mes_antigo)
        SQL_INSERT = "INSERT INTO NC_MOP ("+campos+", MES_ANO) " + SQL
        ado.executar(SQL_INSERT)
        return True

    try:
        backup_mop(pasta_backup)
    except:
        return print("nao foi possível fazer o backup")
        
    SQL = "DELETE FROM NC_MOP WHERE MES_ANO = '{}'".format(mes_novo)
    print(ado.executar(SQL))
    copiar_mes_sql(mes_antigo,mes_novo)
    return print("mes copiado")
