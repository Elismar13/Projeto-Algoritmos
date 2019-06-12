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
        print(linha)
        for n in linha:
            print(n)
            lista.append(n)
        contador += 1

    return lista


'''
# Ler o conteuno do texto e converte cada caracter para o binario
# Parametros(caminho:string, posicao:int)
# Return(binarioCompleto:string)
'''
def transformarTextoBin(caminho,posicao,quantidadeBits,tamanho,texto):
    binarioCompleto = ""

    arq = open(caminho,"rb")

    for i in range(posicao,tamanho):

        caracter = texto[i]

        cod = ""
        if(quantidadeBits >= 7):
            cod = str(converterDecimalBinarioMin(ord(caracter)))

        else:
            cod = str(int(converterDecimalBinarioMin(ord(caracter),quantidadeBits - 2)))

        aux = len(cod) - 7
        if aux >= 1:
            cod = ajustaString(cod,aux)

        binarioCompleto += cod
        quantidadeBits -= len(cod)

    arq.close()
    return binarioCompleto
