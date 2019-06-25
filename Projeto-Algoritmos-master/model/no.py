'''
Arquivo contendo as funções que envolvem os nós da arvore
'''
#==============================Imports====================
import json
from Ferramentas.ferramentasDiversas import *
#=========================================================
'''
#unta dois nos
#Parametros(no1:dict, no2:dict)
#Reutn(novoNo:dict)
'''
def juntarNo(no1,no2):

    novoNO = {}
    quantidade1 = no1["quantidade"]
    quantidade2 = no2["quantidade"]
    caracter1 = no1["caracter"]
    caracter2 = no2["caracter"]

    if(quantidade1 < quantidade2):
        novoNO = {
            "quantidade":quantidade1 + quantidade2,
            "caracter": caracter1 + caracter2,
            "direita": no1,
            "esquerda": no2
        }
    elif(quantidade2 < quantidade1):
        novoNO = {
            "quantidade":quantidade1 + quantidade2,
            "caracter": caracter1 + caracter2,
            "direita": no2,
            "esquerda": no1
        }

    else:
        if(ord(caracter1[0]) < ord(caracter2[0])):
            novoNO = {
            "quantidade":quantidade1 + quantidade2,
            "caracter": caracter1 + caracter2,
            "direita": no1,
            "esquerda": no2
            }

        else:
            novoNO = {
            "quantidade":quantidade1 + quantidade2,
            "caracter": caracter1 + caracter2,
            "direita": no2,
            "esquerda": no1
         }


    return novoNO

'''
# Soma o ord de cada caracter
# Parametros(string: string)
# Return(valor:int)
'''
def somarOrd(string):
    valor = 0
    for c in string:
        valor += ord(c)

    return valor




'''
#Ordena a lista em um formato crescente
#Parametros(listaNos:list)
#Return(listaNos:list)
'''
def ordenarNo(listaNos):
    for i in range(len(listaNos)):
        aux = listaNos[i]
        for j in range(i,-1,-1):
            if(j == 0):
                listaNos[0] = aux
                break
            if(aux["quantidade"] > listaNos[j - 1]["quantidade"]):
                listaNos[j] = aux
                break

            listaNos[j] = listaNos[j - 1]

    return listaNos

'''
#Crio o nó a partir dos dados do dicionário
#Parametros(item:dicit) 
#Return(no:dict)
'''
def inicializarNo(item):

    quantidade = list(item.values())[0]
    caracter = list(item.keys())[0]
    no = {
        "quantidade":quantidade,
        "caracter": caracter,
        "direita": None,
        "esquerda": None
    }

    return no



'''
#Gera a tabela de codigos a apartir de uma arvore
#Parametros(no:Dicionario, cod:string)
#Return (tabela:LIST[DICT])
'''
def gerarTabela(no,cod = "",gerar = False):
    tabela = []
    if(no["direita"] != None):
        tabela += gerarTabela(no["direita"],cod + "1")
    if(no["esquerda"] != None):
        tabela += gerarTabela(no["esquerda"],cod + "0")

    if(no["esquerda"] == None and no["direita"] == None):
        tabela.append({no["caracter"]: cod})

    if(gerar == True):
        novaTabela = open("tabelades.txt","w")
        novaTabela.write(json.dumps(tabela,indent=4))
        novaTabela .close()

    return tabela



'''
# Gera a arvore de Huffman a apartir da lista de Nos ordenada pela frequencia dos seus caracters
# Parametros(listaNos:list(dict)
# return(No raiz:dict)
'''
def gerarArvore(frequencia):
    print("Ordenando a Frequencia...")
    listaOrdenada = OrdenarDicionario_SemFuncao(frequencia)
    print("Gerando Nos e Arvore...")
    listaNos = gerarNos(listaOrdenada)
    for n in range(0,len(listaNos)):    #Percorre a lista de nos
        if(len(listaNos) > 1):     #Verifica se ha mais de um item na lista
            novoNo = juntarNo(listaNos[0],listaNos[1])   #Junta os nos que possuem caracter com menor frequencia
            del listaNos[0]     #Apaga os nos unificados da lista
            del listaNos[0]
            listaNos.append(novoNo)     #adiciona o novo no na lista de nos
            listaNos = ordenarNo(listaNos)  #Reordena a lista de nos

    return listaNos[0]  #Retorna o no raiz


'''
# Para cada item na lista gera um no com o mesmo conteudo
# Parametros(lista:list)
# Return(listaNos:list(dict))
'''
def gerarNos(lista):
    listaNos = []
    for item in lista:
        listaNos.append(inicializarNo(item))

    return listaNos

