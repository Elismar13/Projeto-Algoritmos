'''
Funcoes relacionas a manipulacao de arquivos
'''
#=================================Imports=================================
import os
from Ferramentas.ferramentasDiversas import *
from Ferramentas.binarios import *

#===============================Fim Imports===============================

'''
!!!Restrito ao txt
# Le o arquivo e retorna uma lista de bytes correspondendo a cada caracter do arquivo
# Parametros(arquivo:file)
# Return(lista:list(bytes))
'''
def lerArquivo(arquivo):
    lista = []
    arquivo.seek(0) #Posiciona o cursor no inicio do arquivo
    contador = 1
    for linha in arquivo:
        for n in linha.decode():
            lista.append(n)
        contador += 1

    return lista


'''
# Ler o conteuno do texto e converte cada caracter para o binario
# Parametros(caminho:string, posicao:int)
# Return(binarioCompleto:string)
'''
def transformarTextoBin(posicao,quantidadeBits,tamanho,texto):
    binarioCompleto = ""
    for i in range(posicao,tamanho):
        caracter = texto[i]
        cod = ""
        if(quantidadeBits >= 7):
            cod = str(converterDecimalBinarioMin(ord(caracter)))
            print("QUANTIDQADED", quantidadeBits)
        else:
            cod = str(int(converterDecimalBinarioMin(ord(caracter),quantidadeBits - 2)))

        aux = len(cod) - 7
        if aux >= 1:
            cod = ajustaString(cod,aux)
        binarioCompleto += cod

        quantidadeBits -= len(cod)
    return binarioCompleto


def pegarCaminhoExtensao(caminho):
    extensao = ""
    caminhoSemExtensao = ""
    for i in range(len(caminho) -1,-1,-1):
        if(caminho[i] == "."):
            caminhoSemExtensao = caminho[:i]
            break
        extensao = caminho[i] + extensao

    return [caminhoSemExtensao,extensao]
