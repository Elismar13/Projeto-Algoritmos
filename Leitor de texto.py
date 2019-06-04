#====================================== BIBLIOTECAS ===============================================
import os
import json
#==================================================================================================

#======================================= ARQUIVOS =================================================

#==================================================================================================



#=====================================Estrutura dos nós============================================

#Função para juntar nós do dicionário
def juntarNo(dic1,dic2):

    quantidade1 = dic1["quantidade"]
    quantidade2 = dic2["quantidade"]
    caracter1 = dic1["caracter"]
    caracter2 = dic2["caracter"]


    #print(caracter1 + caracter2)
    novoNO = {
        "quantidade": quantidade1 + quantidade2,
        "caracter": caracter1 + caracter2,
        "direita": dic1,
        "esquerda": dic2
    }
    return novoNO

#Ordena a lista em um formato crescente
def ordenarNo(listaNos):
    for i in range(len(listaNos)):
        aux = listaNos[i]
        #print(aux)
        for j in range(i,-1,-1):
            if(j == 0):
                listaNos[0] = aux
                break
            if(aux["quantidade"] > listaNos[j - 1]["quantidade"]):
                listaNos[j] = aux
                break

            listaNos[j] = listaNos[j - 1]
    # print("Lista nos: ", listaNos)
    return listaNos

#Crio o nó a partir dos dados do dicionário
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
#==================================================================================================



#===================================Criar e ordenar lista==========================================

#Converter de String para Binário
def str_to_bin(string):
    binario = ''
    for i in string:
        binario += bin(ord(i))[2::] + ' '
    return binario

#Função para criar o dicionario e contar as letras
def Contar_Caracteres(palavra):
    letras = {}

    for percorrer in palavra:                   #Criar o dicionario
        letras[percorrer] = 0

    for percorrer_2 in palavra:                 #Adicionar elementos no dicionario
        letras[percorrer_2] += 1

    return letras

#Crio a lista com os dicionários
def Criar_Lista(dicionario):

    lista = []
    caracters = list(dicionario.keys())
    qtd = list(dicionario.values())
    for i in range(len(dicionario)):
        lista.append({caracters[i]:qtd[i]})

    print("Dicionario criado: ", lista, "\n\n")

    return lista


def OrdenarDicionario_SemFuncao(listaOrdenada):
    for i in range(len(listaOrdenada)):
        aux = listaOrdenada[i]
        for j in range(i,-1,-1):
            if(j == 0):
                listaOrdenada[0] = aux
                break
            if(list(aux.values())[0] > list(listaOrdenada[j - 1].values())[0]):
                listaOrdenada[j] = aux
                break

            listaOrdenada[j] = listaOrdenada[j - 1]
    print("Dicionario ordenado:" ,listaOrdenada, "\n\n")
    return listaOrdenada
#==================================================================================================


#======================================= Gerenciar Árvore =========================================

def CondicionalArvore(no_raiz, codigo = "",lista = []):

    if(no_raiz["esquerda"] != None):
        CondicionalArvore(no_raiz["esquerda"], codigo + "0",lista)

    if(no_raiz["direita"] != None):
        CondicionalArvore(no_raiz["direita"], codigo + "1",lista)

    if(no_raiz["esquerda"] == None and no_raiz["direita"] == None):

        dicionario = {no_raiz["caracter"] : codigo}
        lista.append(dicionario)
    return lista

#==================================================================================================


#====================================== Gerenciar Arquivo =========================================

def LerArquivo(arquivo):
    texto = ""
    arquivo.seek(0)
    for linha in arquivo:
        texto += linha.decode("utf-8")
    print(texto)
    return texto


def GerenciarCodigo(texto, ListaOrdenada):
    aux = ''
    nome = input("Digite o nome do novo arquivo: ")
    print(texto)
    ArquivoComprimido = open(nome+".ale", "w")
    for i in range(len(texto)):
        for elemento in ListaOrdenada:
            #if texto[i] == elemento["caracter"]:
            print(elemento)


    return


#====================================== PROGRAMA PRINCIPAL ===============================================

def main():
    arquivo = open("arq.txt", "rb")
    dicionario = Contar_Caracteres(LerArquivo(arquivo))
    lista = Criar_Lista(dicionario)
    listaOrdenada = OrdenarDicionario_SemFuncao(lista)
    conteudo_arquivo = LerArquivo(arquivo)
    GerenciarCodigo(conteudo_arquivo, listaOrdenada)

    listaNos = []

    for item in listaOrdenada:
        listaNos.append(inicializarNo(item))



    #Inicio do loop
    for n in range(0,len(listaNos)):
        if(len(listaNos) > 1):
            newNo = juntarNo(listaNos[0],listaNos[1])
            del listaNos[0]
            del listaNos[0]
            listaNos.append(newNo)

            listaNos = ordenarNo(listaNos)

    arq2 = open("arq2.txt","w")
    arq2.write(json.dumps(listaNos, indent=4, sort_keys=False))
    print(CondicionalArvore(listaNos[0]))




if __name__ == '__main__':
    main()
