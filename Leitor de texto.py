#====================================== BIBLIOTECAS ===============================================
# import os
#
# #======================================= ARQUIVOS =================================================
# import Interface


#========================================Estrutura==================================================

def juntarNo(dic1,dic2):

    quantidade1 = dic1["quantidade"]
    quantidade2 = dic2["quantidade"]
    caracter1 = dic1["caracter"]
    caracter2 = dic2["caracter"]


    print(caracter1 + caracter2)
    no = {
        "quantidade":quantidade1 + quantidade2,
        "caracter": caracter1 + caracter2,
        "direita": dic1,
        "esquerda": dic2
    }

    return no

def ordenarNo(listaNos):
    for i in range(len(listaNos)):
        aux = listaNos[i]
        print(aux)
        for j in range(i,-1,-1):
            if(j == 0):
                listaNos[0] = aux
                break
            if(aux["quantidade"] > listaNos[j - 1]["quantidade"]):
                listaNos[j] = aux
                break

            listaNos[j] = listaNos[j - 1]
    print(listaNos)
    return listaNos

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

def str_to_bin(string):
    binario = ''
    for i in string:
        binario += bin(ord(i))[2::] + ' '
    return binario

def Criar_Dicionario(palavra):                  #Função para criar o dicionario e contar as letras
    letras = {}


    for percorrer in palavra:                   #Criar o dicionario
        letras[percorrer] = 0

    for percorrer_2 in palavra:                 #Adicionar elementos no dicionario
        letras[percorrer_2] += 1

    return letras

def Ordenar_Lista(dicionario):

    listaOrdenada = []
    caracters = list(dicionario.keys())
    qtd = list(dicionario.values())
    for i in range(len(dicionario)):
        listaOrdenada.append({caracters[i]:qtd[i]})

    print(listaOrdenada)

    return listaOrdenada

def OrdenarDicionario_SemFuncao(listaOrdenada):
    for i in range(len(listaOrdenada)):
        aux = listaOrdenada[i]
        print(aux)
        for j in range(i,-1,-1):
            if(j == 0):
                listaOrdenada[0] = aux
                break
            if(list(aux.values())[0] > list(listaOrdenada[j - 1].values())[0]):
                listaOrdenada[j] = aux
                break

            listaOrdenada[j] = listaOrdenada[j - 1]
    print(listaOrdenada)
    return listaOrdenada



def main():
    dicionario = Criar_Dicionario("aaabbccccccccc")
    listaQuase = Ordenar_Lista(dicionario)
    listaOrdenada = OrdenarDicionario_SemFuncao(listaQuase)


    listaNos = []

    for item in listaOrdenada:
        listaNos.append(inicializarNo(item))

    print("ANTES")
    for item in listaNos:
        print(item)

    newNo = juntarNo(listaNos[0],listaNos[1])
    listaNos.append(newNo)
    del listaNos[0]
    del listaNos[0]

    print("Depois")
    for item in listaNos:
        print(item)





if __name__ == '__main__':
    main()
