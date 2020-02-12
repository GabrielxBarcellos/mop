import csv

arquivo = 'uploads\\TESTE_IMPORTA.csv'
def importa(arquivo_csv):
    with open(arquivo_csv, encoding='utf-8') as arquivo:

        linhas = csv.reader(arquivo)

        contagem = 0
        SQL = 'INSERT INTO NC_MOP('
        for linha in linhas:
            #CABEÇALHO
            if (contagem == 0) :
                print('teste ' + str(contagem))
                ignora = 0 #ignora o id
                for item in linha:
                    if ignora != 0:
                        SQL += item + ","
                    ignora += 1
                SQL = SQL[:-1] +') VALUES '
                contagem += 1
                continue
            #corpo
            SQL+="("
            ignora = 0 #ignora o id
            for item in linha:
                if ignora != 0 :
                    SQL += "'" +item + "',"
                ignora += 1
            SQL = SQL[:-1] + "),"
            contagem +=1
        SQL = SQL[:-1]
        return SQL

print(importa(arquivo))