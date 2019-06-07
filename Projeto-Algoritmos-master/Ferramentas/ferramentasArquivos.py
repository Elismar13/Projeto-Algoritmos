'''
Funcoes relacionas a manipulacao de arquivos
'''
#=================================Imports=================================
import os
from Ferramentas.ferramentasDiversas import *
from Ferramentas.binarios import *

#===============================Fim Imports===============================

'''
# Le o arquivo e retorna uma lista de bytes correspondendo a cada caracter do arquivo
# Parametros(arquivo:file)
# Return(lista:list(bytes))
'''
def lerArquivo(arquivo):
    lista = []
    arquivo.seek(0) #Posiciona o cursor no inicio do arquivo
    tamanho = os.path.getsize(arquivo.name)
    contador = 1
    for linha in arquivo:
        aux = linha
        for n in aux:
            lista.append(n)
        contador += 1
    return lista


'''
# Ler o conteuno do texto e converte cada caracter para o binario
# Parametros(caminho:string, posicao:int)
# Return(binarioCompleto:string)
'''
def transformarTextoBin(caminho,posicao):
    binarioCompleto = ""

    arq = open(caminho,"rb")
    tamanho = os.path.getsize(caminho)
    for i in range(posicao,tamanho):
        arq.seek(i)
        caracter = arq.read(1)
        cod = str(converterDecimalBinarioMin(ord(caracter.decode())))
        aux = len(cod) - 7
        if aux >= 1:
            cod = ajustaString(cod,aux)
        binarioCompleto += cod

    arq.close()
    return binarioCompleto
