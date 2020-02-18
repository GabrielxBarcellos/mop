
from controle import agente as agente_obj
from controle import mop
import csv
from datetime import datetime
import ado
import os


def backup_mop():
    mop = controle.mop()
    cabecalho = []
    linha = []
    lista = []

    for chave in dict (mop).keys():
        cabecalho.a(chave)

    for linha in mop:
        print(linha)

backup_mop()