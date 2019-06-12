#====================================== BIBLIOTECAS ===============================================
from tkinter import *                                               #Biblioteca referente à interface grafica
from tkinter.filedialog import askopenfilename


import os
from CompressoresDescompressores.compactador import compactar
from CompressoresDescompressores.descompactador import descompactar

#==================================================================================================



#from tkinter import Tk
#from tkinter.filedialog import askopenfilename

#Tk().withdraw() # Isto torna oculto a janela principal
#filename = askopenfilename() # Isto te permite selecionar um arquivo
#print(filename) # printa o arquivo selecionado
"""
def SelecaodeArquivo():
    teladeselecao = Tk()
    teladeselecao.filename = filedialog.askopenfilename(initialdir="/", title="Selecione o arquivo",
                                               filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    print(teladeselecao.filename)

"""
#janela de selecao de arquivo
def SelecaodeArquivo_Compactar():
    teladeselecao = Tk()

    teladeselecao.filename = askopenfilename(initialdir="/", title="Selecione o arquivo",
                                                   filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    diretorio_arquivo = teladeselecao.filename
    if(diretorio_arquivo[-4:] == ".txt"):
        compactar()
    else:
        print("Erro. tente novamente")
    return


def SelecaodeArquivo_Descompactar():
    teladeselecao_descompactar = Tk()
    teladeselecao_descompactar.filename = askopenfilename(initialdir="/", title="Selecione o arquivo (.ale)",
                                                   filetypes=(("txt files", "*.txt"), ("all files", ".")))
    diretorio_arquivo = teladeselecao_descompactar.filename

    if(diretorio_arquivo[-4:] == ".ale"):
        descompactar()

    return


#Esta é a janela de compactacao
def JaneladeCompactacao():
    janela = Tk()
    janela.title("ALE- Tela de Compactacao")

    selecione = Label(janela, text="Selecione o diretório do arquivo: ")
    selecione.place(x=25,y=100)

    SelecionarDiretorio = Button(janela, width = 5,  text = "...", command=SelecaodeArquivo_Compactar)  #botao selecao diretorio
    SelecionarDiretorio.place(x=250, y=95)


    voltar = Button(janela, width=10, text="Voltar", command = janela.destroy)
    voltar.place(x = 125, y=175)

    janela.geometry("350x300+150+150")
    janela.mainloop()                                           #Laço de exebição infinito
    janela.destroy()                                            #Fecho a janela de compactacao
    return


#Esta é a janela de compactacao
def JaneladeDescompactacao():
    janela = Tk()
    janela.title("ALE- Tela de Descompactacao")

    selecione = Label(janela, text="Selecione o diretório do arquivo (.ale): ")
    selecione.place(x=25,y=100)

    SelecionarDiretorio = Button(janela, width = 5,  text = "...", command=SelecaodeArquivo_Descompactar)  #botao selecao diretorio
    SelecionarDiretorio.place(x=250, y=95)


    voltar = Button(janela, width=10, text="Voltar", command = janela.destroy)
    voltar.place(x = 125, y=175)

    janela.geometry("350x300+150+150")
    janela.mainloop()                                           #Laço de exebição infinito
    janela.destroy()                                            #Fecho a janela de compactacao
    return


def ProgramaPrincipal():
    janela = Tk()                                               #Janela principal com uma nova instancia de TK
    janela.title("ALE - Tela Principal (beta)")

    lb = Label(janela, text="Selecione a opção desejada:")
    lb["background"] = "white"
    lb.place(x=70, y = 25)

    Compactar = Button(janela, width = 20, text = "Compactar", command=JaneladeCompactacao)
    Compactar.place(x=70, y=60)

    Descompatar = Button(janela, width=20, text="Descompactar", command = JaneladeDescompactacao)
    Descompatar.place(x=70,y=110)

    Sair = Button(janela, width=20, text="Sair",command = exit)
    Sair.place(x=70,y=160)

    Mensagem = Label(janela, text="#DiganaoaoWinRAR", bg="white", fg = "red", font = ("Arial",14))
    Mensagem.place(x = 60, y = 260)

    janela["background"] = "white"          #Cor do fundo
    janela.geometry("300x300+100+100")      #larguraxaltura+distanciaEsquerda+Distancia top
    janela.mainloop()                       #Laço de exebição infinito
    return janela.destroy

ProgramaPrincipal()


