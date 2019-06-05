#====================================== BIBLIOTECAS ===============================================
import os


#==================================================================================================

#======================================= ARQUIVOS =================================================

#==================================================================================================


#========================================Estrutura==================================================
#Função para juntar nós do dicionário

#==================================================================================================


def Contar_Caracteres(palavra):
    letras = {}

    for percorrer in palavra:                    # Criar o dicionario
        # print(percorrer)
        letras[percorrer] =  0

    for percorrer_2 in palavra:                  # Adicionar elementos no dicionario
        # print(percorrer_2, letras[percorrer_2])

        letras[percorrer_2] +=  1


    return letras

#Crio a lista com os dicionários
def Criar_Lista(dicionario):

    listaOrdenada = []
    caracters = list(dicionario.keys())
    qtd = list(dicionario.values())
    for i in range(len(dicionario)):
        listaOrdenada.append({caracters[i]:qtd[i]})

    # print(listaOrdenada)

    return listaOrdenada

def OrdenarDicionario_SemFuncao(listaOrdenada):
    for i in range(len(listaOrdenada)):
        aux = listaOrdenada[i]
        # print(aux)
        for j in range(i,-1,-1):
            if(j == 0):
                listaOrdenada[0] = aux
                break
            if(list(aux.values())[0] > list(listaOrdenada[j - 1].values())[0]):
                listaOrdenada[j] = aux
                break

            listaOrdenada[j] = listaOrdenada[j - 1]
    # print(listaOrdenada)
    return listaOrdenada


def gerarTabela(no,num = ""):
    tabela = []
    if(no["direita"] != None):
        tabela += gerarTabela(no["direita"],num + "1")

    if(no["esquerda"] != None):
        tabela += gerarTabela(no["esquerda"],num + "0")

    if(no["esquerda"] == None and no["direita"] == None):
        tabela.append({no["caracter"]: num})

    # novaTabela = open("tabela.txt","wb")
    # novaTabela.write(json.dumps(tabela))
    # novaTabela .close()
    return tabela









#====================================== Gerenciar Arquivo =========================================

def LerArquivo(arquivo):
    lista = []
    texto = ""
    arquivo.seek(0)
    tamanho = os.path.getsize(arquivo.name)
    contador = 1
    for linha in arquivo:
        if(contador == tamanho - 2):
            break
        aux = linha
        for n in aux:
            lista.append(bytes(chr(n),encoding="utf-8"))
        contador += 1
    return lista


def GerenciarCodigo(texto, ListaOrdenada):
    aux = ''
    nome = input("Digite o nome do novo arquivo: ")
    ArquivoComprimido = open(nome+".ale", "w")
    for i in range(len(texto)):
        for elemento in ListaOrdenada:
            #if texto[i] == elemento["caracter"]:
            print(elemento)


    return

#=============================================================================================

def ajustaString(string,n):
    novaString = ""
    for n in range(n,len(string)):
        novaString += string[n]

    return novaString

def lerArquivoPosicao(caminho,posicao):
    binarioCompleto = ""

    # novoArquivo = open("arquivoRestaurado.txt","w")
    arq = open(caminho,"r")
    tamanho = os.path.getsize(caminho)
    for i in range(posicao,tamanho):
        arq.seek(i)
        caracter = arq.read(1)
        cod = str(converterDecimalBinario2(ord(caracter)))
        aux = len(cod) - 7
        if aux >= 1:
            cod = ajustaString(cod,aux)
        binarioCompleto += cod

    print(binarioCompleto)
    arq.close()
    return binarioCompleto

def recuperarPadrao(caminho):
    print("=======Recuper Padrao==========")
    tabela = {}
    arquivo = open(caminho,"rb")
    cont = 0
    texto = LerArquivo(arquivo)
    n = ord(texto[0].decode("utf-8"))
    cursor = 1
    print(n)
    while(cont < n):

        arquivo.seek(cursor)
        caracter = texto[cursor]
        while(caracter in tabela):
            cursor += 1
            caracter = texto[cursor]


        valor = texto[cursor + 1]
        print(valor)
        tabela[caracter] = converterDecimalBinario1(ord(valor.decode()))
        cont += 1
        cursor += 2

    print(tabela)


    binarioCompleto = lerArquivoPosicao(caminho, cursor)
    return [tabela,binarioCompleto]


def regenerar(tabela,codigoCompleto,noRaiz):
    texto = []
    no = noRaiz
    for bit in codigoCompleto:
        # print("======")
        # print(no)
        # print(texto)
        if(bit == "1"):
            no = no["direita"]
            if(no["esquerda"] == None and no["direita"] == None):
                texto += [no["caracter"]]
                no = noRaiz

        elif(bit == "0"):
            no = no["esquerda"]
            if(no["esquerda"] == None and no["direita"] == None):
                texto += [no["caracter"]]
                no = noRaiz

    print("-->",texto)
    return texto


#====================================== PROGRAMA PRINCIPAL ===============================================

def main():
    print("============Concorreten do WInrar============")
    nome = input((":Digite o nome do arquivo: "))
    arquivo = open(nome+".txt", "rb")

    texto = LerArquivo(arquivo)
    dados = Contar_Caracteres(texto)
    lista = Criar_Lista(dados)
    listaOrdenada = OrdenarDicionario_SemFuncao(lista)
    print(texto[0])
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


    arq = open("arq.txt","w")
    #arq.write(var)
    arq.close()
    noRaiz = listaNos[0]
    tabela = gerarTabela(noRaiz)
    print("--",len(tabela))
    bits = trocarCaracter(texto,tabela)
    listaBytes = substituirBits(bits)


    novoNome = arquivo.name.split(".")[0]
    print(novoNome)
    novoArquivo = open(novoNome + ".ale","wb")
    padronizar(novoArquivo,tabela)

    print("Bytes",listaBytes)
    for byte in listaBytes:

        caracter = bytes(converterByte(byte),encoding="utf-8")
        novoArquivo.write(caracter)
    novoArquivo.close()


    op = 1
    if(op == 1):
        teste = recuperarPadrao(novoNome + ".ale")
        tabelaRegenarada = teste[0]
        binarioCompleto = teste[1]
        print("BITS",bits)
        if(binarioCompleto == bits):
            print("SHOW DE BOLA")

        else:
            print("ALGO A SER SANADO")
        # print("-->>",tabelaRegenarada)
        # print("<<<>>>",LerArquivo(novoArquivo2))
        # print()
        # print()
        arquivoRegenerado = open("ArquivoRegenerado.txt", "wb")
        listaFinal  = regenerar(tabelaRegenarada,binarioCompleto,listaNos[0])
        for item in listaFinal:
            arquivoRegenerado.write(item)

        arquivoRegenerado.close()


    print("===========Obrigado por nos utilizar========")
    print("===========Avalie em 5 estrelas========")
    print("===========#NaoAoWINRAR========")
if __name__ == '__main__':
    main()
