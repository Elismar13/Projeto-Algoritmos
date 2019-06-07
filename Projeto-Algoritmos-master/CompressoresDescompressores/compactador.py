'''
Este arquivopossui funcoes relacionadas a compressao de arquivos
'''

#===============================Imports=========================================
from Ferramentas import binarios
from Ferramentas.ferramentasArquivos import *
from Ferramentas.ferramentasDiversas import *
from Ferramentas.binarios import *
from model.no import *

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

'''
# Funcao responsavel por efetuar a compactacao dos arquivos chamando as funcoes necessarias
# Parametros()
# Return()
'''
def compactar():
    caminho = input(":Digite o nome do arquivo: ")
    arquivo = open(caminho, "rb")

    texto = lerArquivo(arquivo)
    print(texto)
    dados = Contar_Caracteres(texto)
    lista = Criar_Lista(dados)
    listaOrdenada = OrdenarDicionario_SemFuncao(lista)
    listaNos = gerarNos(listaOrdenada)
    noRaiz = gerarArvore(listaNos)
    tabela = gerarTabela(noRaiz,gerar=True)
    bits = substituirCaracterBin(texto,tabela)
    listaBytes = substituirBits(bits)
    criarNovoArquivoComprimido(caminho,listaBytes,tabela,dados)



'''
# Gera um novo arquivo compactado com os dados informados
# Parametros(caminho:string, listaBytes:list(bytes))
# Return()
'''
def criarNovoArquivoComprimido(caminho,listsBytes,tabela,frequencia):
    nomeDividido = caminho.split(".")
    nomeSemExtensao = nomeDividido[0]
    extensao = nomeDividido[1]
    novoArquivo = open(nomeSemExtensao + ".ale","wb")
    padronizar(novoArquivo,tabela,extensao,frequencia)

    for byte in listsBytes:
        caracter = bytes(converterByte(byte),encoding="utf-8")
        novoArquivo.write(caracter)
    novoArquivo.close()




#====================================== Padrao ==================================================
# - quantidade de bytes com informacoes
# - byte(caracter) -
# - caracter Representado os bits
#Configura os primeiros bits para informacoes do arquivos compactado
def padronizar(arq,lista,extensao,frequencia):
    qtd = len(lista)
    arq.write(bytes(extensao,encoding="utf-8"))
    arq.write(bytes(" ",encoding="utf-8"))
    arq.write(bytes(chr(qtd),encoding="utf-8"))
    for item in lista:
        caracter = list(item.keys())[0]
        arq.write(bytes(chr(caracter),encoding="utf-8"))
        arq.write(bytes(chr(binarios.converterBinarioDecimal(item[caracter])), encoding="utf-8"))
        arq.write(bytes(chr(frequencia[caracter]),encoding="utf-8"))
