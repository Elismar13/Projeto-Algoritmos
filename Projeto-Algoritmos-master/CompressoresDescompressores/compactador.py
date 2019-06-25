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
    bits = ""
    dicionario = {} #Inicializando Dicionario vazio
    for item in tabela:     #Gerando Dicionario a partir da tabela de codigos
        chave = list(item.keys())[0]
        valor = list(item.values())[0]
        dicionario[chave] = valor

    for i in range(0,len(palavra)):     #Convertendo caracter em binarios(String)
        bits += dicionario[palavra[i]]

    return bits

'''
# Funcao responsavel por efetuar a compactacao dos arquivos chamando as funcoes necessarias
# Parametros(CaminhoAquivo: string)
# Return()
'''
def compactar(caminhoArquivo):
    caminho = caminhoArquivo
    arquivo = open(caminho, "rb")
    tamanho = os.path.getsize(caminho)
    print("Lendo Arquivo...")
    texto = lerArquivo(arquivo)
    print("Verificando Frequencia...")
    dados = Contar_Caracteres(texto)
    noRaiz = gerarArvore(dados)
    print("Gerando Nova Tabela de Codigos...")
    tabela = gerarTabela(noRaiz,gerar=True)
    print("Substituindo bits")
    bits = substituirCaracterBin(texto,tabela)
    listaBytes = substituirBits(bits)
    print("Gerando novo Arquivo - Caminho --", caminho)
    novoTamanho = criarNovoArquivoComprimido(caminho,listaBytes,tabela,dados,tamanho)
    print("Compressao Concluida")
    print("Tamanho Original -", tamanho)
    print("Novo Tamanho -", novoTamanho)
    print("Percentual Comprimido - %0.2f" %(100 - ((novoTamanho * 100) / tamanho)), "%", sep="")
    print("bits", bits)
    print("=============================================  ")
    print("0011100110001010010000011000100000100000011101101011001111111011011100101110101001100001001010000101001011")
    print("0011100110001010010000011000100000100000011101101011001111111011011100101110101001100001001010000101001010000001")
    print("00111001100010100100000110001000001000000111011010110011111110110111001011101010011000010011000011001011")
    print("0011100011000100100100000110000100000100000010110110101100110111110101011100010111010100110001001100001100101000001")




'''
# Gera um novo arquivo compactado com os dados informados
# Parametros(caminho:string, listaBytes:list(bytes))
# Return(tamanho do arquivo criado)
'''
def criarNovoArquivoComprimido(caminho,listsBytes,tabela,frequencia,tamanho):
    nomeDividido = pegarCaminhoExtensao(caminho)
    nomeSemExtensao = nomeDividido[0]
    extensao = nomeDividido[1]
    novoArquivo = open(nomeSemExtensao + ".ale","wb")
    padronizar(novoArquivo,tabela,extensao,frequencia)
    quantidadeBytes = len(listsBytes)
    cont = 1
    for byte in listsBytes:
        percentual = (cont * 100) / quantidadeBytes # Calcula o percentual
        exibirPercentual(percentual) # Exibe o percentual
        caracter = bytes(converterByte(byte),encoding="utf-8")
        novoArquivo.write(caracter)
        cont += 1

    novoArquivo.close()
    novoTamanho = os.path.getsize(nomeSemExtensao + ".ale")
    return novoTamanho


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
        arq.write(bytes(caracter,encoding="utf-8"))
        arq.write(bytes(chr(buscarFrequencia(caracter,frequencia)),encoding="utf-8"))


'''
# Busca a Frequencia de um caracter na lista de frequencia 
# Parametros(caracter:string, frequencia:list(dict))
# Return(item[chave:int)
'''
def buscarFrequencia(caracter,frequencia):
    for item in frequencia:
        chave = list(item.keys())[0]
        if(caracter == chave):
            return item[chave]
