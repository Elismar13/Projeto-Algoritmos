'''
Este arquivopossui funcoes relacionadas a compressao de arquivos
'''

#===============================Imports=========================================
import binarios


#=============================Fim Import========================================

#=============================Funcoes===========================================
#substitue os caracters pelas suas respectivas codificacoes geradas
#Parametros(palavra:bytes, tabela:diconario[])
#return lista de bits
def substituirCaracterBin(palavra,tabela):
    bits = []
    dicionario = {} #Inicializando Dicionario vazio
    for item in tabela:     #Gerando Dicionario a partir da tabela de codigos
        chave = list(item.keys())[0]
        valor = list(item.values())[0]
        dicionario[chave] = valor

    for i in range(0,len(palavra)):     #Convertendo caracter em binarios(String)
        bits.append(dicionario[palavra[i]])

    return bits




#====================================== Padrao ==================================================
# - quantidade de bytes com informacoes
# - byte(caracter) -
# - caracter Representado os bits
#Configura os primeiros bits para informacoes do arquivos compactado
def padronizar(arq,lista):
    qtd = len(lista)
    arq.write(bytes(chr(qtd),encoding="utf-8"))
    for item in lista:
        caracter = list(item.keys())[0]
        arq.write(caracter)
        arq.write(bytes(chr(binarios.converterBinarioDecimal(item[caracter])),encoding="utf-8"))

