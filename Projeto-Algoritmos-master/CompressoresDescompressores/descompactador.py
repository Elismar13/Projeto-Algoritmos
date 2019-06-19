''''
Arquivo contendo funcoes responsaveis pela descompressao de arquivos
'''
#==========================Imports==================================
from Ferramentas.ferramentasArquivos import *
from Ferramentas.ferramentasDiversas import *
from Ferramentas.binarios import *
from model.no import *
#========================Fim imports================================
'''
# Recuperar a extensao do arquivo 
# Parametros(dados:list)
# Return(extensao:string, posicao:int)
'''
def recuperarExtensao(dados):
    cursor = 0
    extensao = ""
    for c in dados:
        if(c == " "):
            break
    
        extensao += c
        cursor += 1
    
    return [extensao,cursor]


'''
# Verifica o prefixo do codigo a ser adicionado, ajustando quando necessario
# Parametros(codigoBin:string, tabela:dict)
# Return(codigoBin:string)
'''
def verficarPrefixo(codigoBin,tabela):    
    #Verificacao de prefixo em codigos
    for codigo in list(tabela.values()):
        if(codigoBin == codigo):
            codigoBin = "0" + codigoBin
            continue

        if(codigoBin == codigo[:len(codigo) - 1]):
            codigoBin = "0" + codigoBin
            continue

    return codigoBin

'''
# Recria a frequencia dos caracter
# Parametros(texto:list, posicao:int)
# Return([frequencia:dict,cursor:int,tabela:dict)
'''
def recuperarCaracterFrequencia(texto,posicao):
    contadorCaracter = 0
    frequencia = {}
    tabela = {}
    cursor = posicao
    n = ord(texto[cursor])
    cursor += 1
    while(contadorCaracter < n ):
        caracter = texto[cursor]
        while(caracter in tabela):
            cursor += 1
            caracter = texto[cursor]
        codigoBin = str(int(converterDecimalBinario(ord(texto[cursor + 1]))))
        codigoBin = verficarPrefixo(codigoBin,tabela)
        frequencia[caracter] = ord(texto[cursor + 2])
        tabela[caracter] = codigoBin
        contadorCaracter += 1
        cursor += 3
    return [frequencia,cursor,tabela]

'''
# Recria a Arvore a partir da frequencia
# Parametros(frequencia:dict)
# Return(noRaiz:dict)
'''
def regenerarArvore(frequencia):
    listFrequencia = []
    for item in frequencia:
        listFrequencia.append({item:frequencia[item]})
    frequenciaAux = ordenarFrequencia(listFrequencia)
    noRaiz = gerarArvore(frequenciaAux)
    return noRaiz


'''
# Calcula a quantidade de bits que precisara
# Parametros(frequencia:dict, tabela:dict)
# Return(qtd:int)
'''
def calcularQuantidadeBits(frequencia, tabela):
    qtd = 0
    for chave in list(frequencia.keys()):
        qtd += frequencia[chave] * len(tabela[chave])
    return qtd

'''
# Recupera o padra(tabela) de codigos gerados pela compressao e o codigo binario do codigo do texto
# Parametros(caminho:string)
# Return([tabela:dict,binarioCompleto:
'''
def recuperarDados(caminho):
    arquivo = open(caminho,"rb")
    texto = lerArquivo(arquivo)
    print("Recuperando extensao do arquivo...")
    primeirosDados = recuperarExtensao(texto)
    extensao = primeirosDados[0]
    cursor = primeirosDados[1] + 1 # Para nao ficar no espaco
    # Parte 2
    print("Recuperando a Frequencia de Cada Caracter...")
    segundosDados = recuperarCaracterFrequencia(texto,cursor)
    frequencia = segundosDados[0]
    cursor = segundosDados[1]
    tabela = segundosDados[2]
    print("Regenerando a Arvore...")
    noRaiz = regenerarArvore(frequencia)
    print("Calculando Quantidade de Bits")
    quantidadeBits = calcularQuantidadeBits(frequencia,tabela)
    tamanho = len(texto)
    print("Resgatando Conteudo em Binario...")
    binarioCompleto = transformarTextoBin(cursor,quantidadeBits,tamanho,texto)
    return [noRaiz,binarioCompleto,extensao]

'''
# Regenera o arquivo apartir do codigo binario do conteudo e do noRaiz do padrao
# parametros(codigoCompleto:string, noRaiz:dict)
# return(lista:list(bytes))
'''
def regenerar(codigoCompleto,noRaiz):
    lista = []
    no = noRaiz
    for bit in codigoCompleto:

        if(bit == "1"):
            no = no["direita"]
            if(no["esquerda"] == None and no["direita"] == None):
                lista += [no["caracter"]]
                no = noRaiz

        elif(bit == "0"):
            no = no["esquerda"]
            if(no["esquerda"] == None and no["direita"] == None):
                lista += [no["caracter"]]
                no = noRaiz

    return lista

'''
# Substitue o tamanho do codigo a uma frequencia para facilitar a recriacao da arvore e a descompactacao
# Parametros(tabela:dict)
# Return(novaTabela:dict)
'''
def recriarTabela(tabela):
    chaves = list(tabela.keys())
    novaTabela = {}
    for i in range(0,len(chaves)):
        novaTabela[chaves[i]] = (len(tabela[chaves[i]]) ** 2) + converterBinarioDecimal(tabela[chaves[i]])
    return novaTabela


'''
# Funcao responsavel por efetuar a descompactacao dos arquivos chamando as funcoes necessarias
# Parametros()
# Return()
'''
def descompactar(caminhoArquivo):
    caminho = caminhoArquivo
    print("Iniciando a Descompactacao...")
    dados = recuperarDados(caminho)
    tamanho = os.path.getsize(caminho)
    noRaiz = dados[0]
    binarioCompleto = dados[1]
    extensao = dados[2]
    caminhoNovo = caminho.split(".")[0]
    CaminhoDescompactado = caminhoNovo + "." + extensao
    print("Regenerando Novo Arquivo...")
    listaBytes  = regenerar(binarioCompleto,noRaiz)
    novoTamanho = recriarArquivoDescompactado(caminhoNovo,listaBytes)
    print("Descompressao Concluida")
    print("Tamanho Compactado -", tamanho)
    print("Tamanho Descompactado -", novoTamanho)
    print("Percentual Descomprimido - %0.2f" %(100 - ((novoTamanho * 100) / tamanho)), "%", sep="")
    print("=============================================")


'''
# Gera um novo arquivo descompactado com os dados informados
# Parametros(caminho:string, listaBytes:list(bytes))
# Return(tamanho do arquivo criado)
'''
def recriarArquivoDescompactado(caminho, listaBytes):
    arquivoRegenerado = open(caminho, "wb")
    tamanho = len(listaBytes)
    contadorBytes = 1
    for item in listaBytes:
        percentual = (contadorBytes * 100) / tamanho
        exibirPercentual(percentual)
        arquivoRegenerado.write(bytes(item,encoding="utf-8"))
        contadorBytes += 1

    arquivoRegenerado.close()
    return os.path.getsize(caminho)
