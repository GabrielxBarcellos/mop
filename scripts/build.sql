CREATE TABLE NC_JORNADA (
    JORNADA VARCHAR(255),
    HRS VARCHAR(2),
    TURNO VARCHAR(255)
) 
INSERT INTO NC_JORNADA(JORNADA, HRS, TURNO) VALUES ('07:20 às 17:00','8','GERAL'),
('08:00 às 17:40','8','GERAL'),
('07:40 às 14:00','6','MATUTINO'),
('09:00 às 15:20','6','VESPERTINO'),
('07:40 às 17:20','8','GERAL'),
('08:00 às 14:20','6','MATUTINO'),
('08:00 às 12:00','4','MATUTINO'),
('09:00 às 18:40','8','VESPERTINO'),
('08:20 às 18:00','8','GERAL'),
('12:20 às 22:00','8','VESPERTINO'),
('09:00 às 13:00','4','MATUTINO'),
('10:00 às 16:20','6','VESPERTINO'),
('13:00 às 17:00','4','VESPERTINO'),
('12:00 às 18:20','6','VESPERTINO'),
('11:00 às 17:20','6','VESPERTINO'),
('12:00 às 16:00','4','VESPERTINO'),
('12:20 às 18:40','6','VESPERTINO'),
('10:00 às 19:40','8','VESPERTINO'),
('13:00 às 19:20','6','VESPERTINO'),
('14:00 às 18:00','4','VESPERTINO'),
('13:30 às 17:30','4','VESPERTINO'),
('14:00 às 20:20','6','VESPERTINO'),
('14:20 às 18:20','4','VESPERTINO'),
('14:20 às 20:40','6','VESPERTINO'),
('15:00 às 19:00','4','VESPERTINO'),
('15:40 às 22:00','6','NOTURNO'),
('18:00 às 22:00','4','NOTURNO'),
('14:40 às 21:00','6','VESPERTINO')

CREATE TABLE NC_SETOR (
    NC_SETOR VARCHAR(255),
    CARGO VARCHAR(255),
    FUNCAO VARCHAR(255)
) 

INSERT INTO  NC_SETOR (NC_SETOR, CARGO,FUNCAO) VALUES('ATACADO','ASSISTENTE COMERCIAL','ASSISTENCIA'),
('ATACADO','GER.COMERCIAL','GERENCIA'),
('ATACADO','ANALISTA COMERCIAL','ANALISE COMERCIAL'),
('ATACADO','OPER. DE TELEMARKETING','VENDAS'),
('CALL CENTER','SUPERVISOR COMERCIAL','SUPERVISAO'),
('CALL CENTER','OPER. DE TELEMARKETING','CONVERSAO'),
('CALL CENTER','COORD. COMERCIAL','COORDENACAO'),
('CALL CENTER','OPER. DE TELEMARKETING','REPESCAGEM'),
('CALL CENTER','OPER. DE TELEMARKETING','VENDAS'),
('CALL CENTER','ASSISTENTE COMERCIAL','CONVERSAO'),
('CALL CENTER','ASSISTENTE SUPERVISAO','ASSISTENCIA'),
('CALL CENTER','GERENTE ADM DE VENDAS','GERENCIA'),
('CALL CENTER','OPER. DE TELEMARKETING','TREINAMENTO'),
('NUCLEO CONTROLE','ASSISTENTE SUPERVISAO','ASSISTENCIA'),
('NUCLEO CONTROLE','ANALISTA COMERCIAL','ANALISE DADOS'),
('NUCLEO CONTROLE','ANALISTA COMERCIAL','ANALISE COMERCIAL'),
('NUCLEO CONTROLE','ANALISTA BUSINESS INTELIGENCE','ANALISE DADOS'),
('NUCLEO CONTROLE','ANALISTA MIS','ANALISE DADOS'),
('NUCLEO CONTROLE','ASSISTENTE ADMINISTRATIVO','ASSISTENCIA'),
('POS-VENDAS','OPER. DE TELEMARKETING','FALTA/FURO'),
('POS-VENDAS','OPER. DE TELEMARKETING','MATERIAIS DESACORDO'),
('POS-VENDAS','OPER. DE TELEMARKETING','TRANSPORTE'),
('POS-VENDAS','OPER. DE TELEMARKETING','SAC'),
('POS-VENDAS','OPER. DE TELEMARKETING','RETIFICACAO'),
('POS-VENDAS','OPER. DE TELEMARKETING','EMAIL'),
('POS-VENDAS','OPER. DE TELEMARKETING','WHATS APP'),
('POS-VENDAS','OPER. DE TELEMARKETING','ATA'),
('POS-VENDAS','ASSISTENTE POS VENDAS','MIGRACAO'),
('POS-VENDAS','OPER. DE TELEMARKETING','SOLICITACOES FINANCEIRAS'),
('POS-VENDAS','ASSISTENTE SUPERVISAO','ASSISTENCIA'),
('POS-VENDAS','OPER. DE TELEMARKETING','CHAT'),
('POS-VENDAS','OPER. DE TELEMARKETING','PAPELARIA'),
('POS-VENDAS','ASSISTENTE POS VENDAS','MATERIAIS DESACORDO'),
('POS-VENDAS','ANALISTA POS VENDAS','MIGRACAO'),
('POS-VENDAS','ASSISTENTE POS VENDAS','TRANSPORTE'),
('POS-VENDAS','SUPERVISOR POS VENDAS','SUPERVISAO'),
('POS-VENDAS','ASSISTENTE POS VENDAS','SOLICITACOES FINANCEIRAS'),
('POS-VENDAS','ASSISTENTE ATENDIMENTO','REDES SOCIAIS'),
('POS-VENDAS','ASSISTENTE POS VENDAS','RETIFICACAO'),
('POS-VENDAS','ASSISTENTE ADMINISTRATIVO','JURIDICO'),
('POS-VENDAS','OPER. DE TELEMARKETING','TREINAMENTO'),
('PRE-FATURAMENTO','OPER. DE TELEMARKETING','CADASTRO'),
('PRE-FATURAMENTO','OPER. DE TELEMARKETING','RETIDO CREDITO'),
('PRE-FATURAMENTO','OPER. DE TELEMARKETING','RETIDO'),
('PRE-FATURAMENTO','SUPERVISOR COMERCIAL','SUPERVISAO'),
('PRE-FATURAMENTO','ASSISTENTE SUPERVISAO','ASSISTENCIA'),
('PRE-FATURAMENTO','OPER. DE TELEMARKETING','BOLETO'),
('PRE-FATURAMENTO','ANALISTA COMERCIAL','ASSISTENCIA'),
('PRE-FATURAMENTO','OPER. DE TELEMARKETING','TREINAMENTO'),
('PROGRAMA ESTUDANTES','OPER. DE TELEMARKETING','ADMINISTRATIVO PE'),
('PROGRAMA ESTUDANTES','OPER. DE TELEMARKETING','VENDAS ESTUDANTES'),
('PROGRAMA ESTUDANTES','SUPERVISOR COMERCIAL','SUPERVISAO'),
('PROGRAMA ESTUDANTES','ASSISTENTE SUPERVISAO','ASSISTENCIA'),
('QUALIDADE','MONITOR QUALIDADE','MONITORIA'),
('QUALIDADE','COORD. COMERCIAL','COORDENACAO'),
('QUALIDADE','ASSISTENTE POS VENDAS','AUDITORIA'),
('QUALIDADE','MONITOR QUALIDADE','ASSISTENCIA'),
('QUALIDADE','ANALISTA E-COMMERCE JR.','AUDITORIA'),
('QUALIDADE','MONITOR QUALIDADE','AUDITORIA'),
('QUALIDADE','ANALISTA TREINAMENTO','TREINAMENTO POS'),
('QUALIDADE','ANALISTA TREINAMENTO','TREINAMENTO VENDAS'),
('SUPPLIER SERVICE','OPER. DE TELEMARKETING','VENDAS'),
('SUPPLIER SERVICE','SUPERVISOR COMERCIAL','SUPERVISAO'),
('SUPPLIER SERVICE','ASSISTENTE COMERCIAL','ASSISTENCIA'),
('SUPPLIER SERVICE','OPER. DE TELEMARKETING','VISITA VIRTUAL'),
('SUPPLIER SERVICE','COORD. COMERCIAL','COORDENACAO'),
('SUPPLIER SERVICE','OPER. DE TELEMARKETING','TREINAMENTO')

CREATE TABLE NC_CC(
    CC VARCHAR(4),
    DESC_CC VARCHAR(255)
)

INSERT INTO NC_CC(CC,DESC_CC) VALUES ('5310','VENDAS'),
('5367','PRE-FATURAMENTO'),
('5325','ESTUDANTES'),
('5324','SUPPLIER'),
('5314','POS-VENDAS'),
('5323','ATACADO')


CREATE TABLE NC_MOP(
ID INT PRIMARY KEY IDENTITY,
CAD	VARCHAR (10)	,
NOME	VARCHAR (255)	,
RAMAL	VARCHAR (255)	,
PAUSAS	VARCHAR (255)	,
CELULAR	VARCHAR (255)	,
MONITORIA	VARCHAR (255)	,
CC	VARCHAR (10)	,
SETOR	VARCHAR (255)	,
CARGO	VARCHAR (255)	,
FUNCAO	VARCHAR (255)	,
NVL	VARCHAR (10)	,
GESTOR	VARCHAR (255)	,
JORNADA	VARCHAR (255)	,
HRS	VARCHAR (255)	,
TURNO	VARCHAR (255)	,
SAB	VARCHAR (255)	,
MES_ANO	VARCHAR (10),
DATA_ADM VARCHAR(10),
DATA_DESLIGAMENTO VARCHAR(10),
STATUS VARCHAR(100),
DATA_IMPORTACAO VARCHAR(100)
)


CREATE TABLE NC_GESTOR(
CAD	VARCHAR (10),
NOME VARCHAR(255)
)

INSERT INTO NC_GESTOR (CAD, NOME) VALUES('724581','ADRIANO LUCAS PEREIRA'),
('701025','ANDERSON BEHRING'),
('721824','CARLOS ALEXANDRE COELHO'),
('701211','CRISTIANE DE ALENCAR FRAGA'),
('701220','DAIANE CRISTINA DA SILVA'),
('705268','DJESSICA PEREIRA'),
('728012','FABIO VALERIO VON HELD'),
('720305','FLAVIA MAIRA ROSA'),
('701599','JACIRA BUBLITZ DA SILVA'),
('705357','JAICYELE BAUER SANTANNA'),
('','JONATAS DE SENA'),
('701750','JOSEANE JAROSZ NOVAK'),
('714690','KAYNANA IONA MULLER DA COSTA'),
('709840','LUANA ANDRESSA DE SOUZA'),
('717770','LUCIANA DOS SANTOS CASTANHA DE MORAIS'),
('710008','MARCELO NATHAN ROZA'),
('715166','MATHEUS CESAR BRUCH'),
('707899','PAULO HENRIQUE NOVAES PEREIRA DA SILVA'),
('705470','TALITA SAMARA LUDWIG')


DROP TABLE  NC_MES
CREATE TABLE NC_MES(
    MES_ANO datetime
)

INSERT INTO MES_ANO (MES_ANO) VALUES ('2020-01-01')

INSERT INTO MES_ANO (MES_ANO) VALUES ('2020-02-01')

INSERT INTO MES_ANO (MES_ANO) VALUES ('2020-03-01')

INSERT INTO MES_ANO (MES_ANO) VALUES ('2020-04-01')

INSERT INTO MES_ANO (MES_ANO) VALUES ('2020-05-01')

INSERT INTO MES_ANO (MES_ANO) VALUES ('2020-06-01')

INSERT INTO MES_ANO (MES_ANO) VALUES ('2020-07-01')

INSERT INTO MES_ANO (MES_ANO) VALUES ('2020-08-01')

INSERT INTO MES_ANO (MES_ANO) VALUES ('2020-09-01')

INSERT INTO MES_ANO (MES_ANO) VALUES ('2020-10-01')

INSERT INTO MES_ANO (MES_ANO) VALUES ('2020-11-01')