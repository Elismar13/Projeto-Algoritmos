''''
Arquivo contendo funcoes responsaveis pela descompressao de arquivos
'''
#==========================Imports==================================
from Ferramentas.ferramentasArquivos import *
from Ferramentas.ferramentasDiversas import *
from Ferramentas.binarios import *
from model.no import *

'''
# Recupera o padra(tabela) de codigos gerados pela compressao e o codigo binario do codigo do texto
# Parametros(caminho:string)
# Return([tabela:dict,binarioCompleto:
'''
def recuperarDados(caminho):
    tabela = {}
    arquivo = open(caminho,"r", encoding="utf-8")
    cont = 0
    cursor = 0
    texto = lerArquivo(arquivo)

    extensao = ""
    frequencia = {}

    for c in texto:
        if(c == " "):
            break

        extensao += c
        cursor += 1

    cursor += 1

    n = ord(texto[cursor])

    cursor += 1


    while(cont < n ):
        arquivo.seek(cursor)
        caracter = texto[cursor]
        while(caracter in tabela):
            cursor += 1
            caracter = texto[cursor]

        codigoBin = str(int(converterDecimalBinario(ord(texto[cursor + 1]))))
        frequencia[caracter] = ord(texto[cursor + 2])
        #Verificacao de prefixo em codigos
        for codigo in list(tabela.values()):
            if(codigoBin == codigo):
                codigoBin = "0" + codigoBin
                continue

            if(codigoBin == codigo[:len(codigo) - 1]):
                codigoBin = "0" + codigoBin
                continue

        tabela[caracter] = codigoBin
        cont += 1
        cursor += 3

    #Determinando numero de bits necessarios a produzir
    qtd = 0
    listFrequencia = []
    for item in frequencia:
        listFrequencia.append({item:frequencia[item]})

    frequenciaAux = ordenarFrequencia(listFrequencia)
    listaOrdenada = OrdenarDicionario_SemFuncao(frequenciaAux)
    listaNos = gerarNos(listaOrdenada)
    print("Lista ordenada decompactar: ", listaOrdenada)
    noRaiz = gerarArvore(listaNos)

    tabelaAux = gerarTabela(noRaiz)
    for item in tabelaAux:
        chave = list(item.keys())[0]
        tabela[chave] = item[chave]

    tamanho = len(texto)
    for chave in list(frequencia.keys()):
        qtd += frequencia[chave] * len(tabela[chave])

    print(texto[cursor])
    binarioCompleto = transformarTextoBin(caminho, cursor,qtd,tamanho,texto)
    print(binarioCompleto)
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
        print("---",chaves[i],"<><><>",len(tabela[chaves[i]]) + converterBinarioDecimal(tabela[chaves[i]]))
    return novaTabela


'''
# Funcao responsavel por efetuar a descompactacao dos arquivos chamando as funcoes necessarias
# Parametros()
# Return()
'''
def descompactar():
    caminho = input("Digite o nome do arquivo: ")
    dados = recuperarDados(caminho)
    noRaiz = dados[0]
    print("Raiz-", noRaiz)
    binarioCompleto = dados[1]
    extensao = dados[2]
    caminhoNovo = caminho.split(".")[0]
    arquivoRegenerado = open(caminhoNovo + "." + extensao, "wb")
    listaFinal  = regenerar(binarioCompleto,noRaiz)
    for item in listaFinal:
        arquivoRegenerado.write(bytes(item,encoding="utf-8"))

    arquivoRegenerado.close()
