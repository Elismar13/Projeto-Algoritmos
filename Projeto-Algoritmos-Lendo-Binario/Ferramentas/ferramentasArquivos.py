'''
Funcoes relacionas a manipulacao de arquivos
'''
#=================================Imports=================================
import os
from Ferramentas.ferramentasDiversas import *
from Ferramentas.binarios import *
import binascii

#===============================Fim Imports===============================
def abre_arquivo_binDescomapctador(arquivo): #transforma o arquivo desejado em hexadecimal
    with open(arquivo, 'rb') as f:
        content = f.read()

    hexadecimal = binascii.hexlify(content).decode('ascii')
    binlist = []
    for i in range(0,len(hexadecimal), 2):
        codigoBin = converterDecimalBinario(int(hexadecimal[i] + hexadecimal[i + 1],16))
        while(len(codigoBin) < 8):
            codigoBin = "0" + codigoBin
        binlist += [codigoBin]
    listaCaracter = []
    for byte in binlist:
        listaCaracter.append(bytes([converterBinarioDecimal(byte)]))
    return listaCaracter


def abre_arquivo_bin(arquivo): #transforma o arquivo desejado em hexadecimal
    with open(arquivo, 'rb') as f:
        content = f.read()

    hexadecimal = binascii.hexlify(content).decode('ascii')
    binlist = ""
    for i in range(0,len(hexadecimal), 2):
        codigoBin = converterDecimalBinario(int(hexadecimal[i] + hexadecimal[i + 1],16))
        while(len(codigoBin) < 8):
            codigoBin = "0" + codigoBin
        binlist += codigoBin
    listaBytes = substituirBits(binlist)
    listaCaracter = []
    for byte in listaBytes:
        listaCaracter.append(converterByte(byte))
    arquivBin = open("compac.txt", "w")
    arquivBin.write(str(binlist))
    arquivBin.close()

    return listaCaracter


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
