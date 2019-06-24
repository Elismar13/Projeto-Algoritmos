#====================================== BIBLIOTECAS ===============================================
from tkinter import *                                               #Biblioteca referente à interface grafica
from tkinter.filedialog import askopenfilename


import os
from CompressoresDescompressores.compactador import compactar
from CompressoresDescompressores.descompactador import descompactar

#==================================================================================================



"""
def SelecaodeArquivo():
    teladeselecao = Tk()
    teladeselecao.filename = filedialog.askopenfilename(initialdir="/", title="Selecione o arquivo",
                                               filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    print(teladeselecao.filename)

"""


#================================JANELAS REFERENTE A COMPACTACAO ====================================
#Esta é a janela de compactacao
def JaneladeCompactacao():
    janela = Toplevel()
    janela.title("ALE- Tela de Compactacao")


    selecione = Label(janela, text="Selecione o diretório do arquivo: ", font=("Arial", 11))
    selecione.place(x=30,y=100)

    SelecionarDiretorio = Button(janela, width = 5,  text = "...",cursor="hand2", command=SelecaodeArquivo_Compactar)  #botao selecao diretorio
    SelecionarDiretorio.place(x=260, y=100)


    voltar = Button(janela, width=10, text="Voltar", cursor="hand2", command = janela.destroy)
    voltar.place(x = 135, y=175)

    janela.geometry("350x300+150+150")
    janela.mainloop()                                           #Laço de exebição infinito
    janela.destroy()                                            #Fecho a janela de compactacao
    return


#janela de selecao de arquivo
def SelecaodeArquivo_Compactar():
    diretorio_arquivo = ""

    try:
        filename = askopenfilename(initialdir="/", title="Selecione o arquivo",
                                                       filetypes=(("Arquivos de Texto", "*.txt"),("Arquivos de Imagem", "*.jpg *.png"), ("Todos Arquivos", "*.*")))
        diretorio_arquivo = filename
    except:
        erroCompactar()

    if len(diretorio_arquivo) > 0:
        if(diretorio_arquivo[-4:] == ".txt") or (diretorio_arquivo[-4:] == ".png") or (diretorio_arquivo[-4:] == ".jpg"):
            compactar(diretorio_arquivo)
        else:
            erroCompactar(diretorio_arquivo)

#Mensagem de erro
def erroCompactar(diretorio=""):
    erro = Tk()
    erro.title("ERRO")
    erro.geometry("300x100+250+250")
    mensagem = Label(erro, text="Arquivo inválido ou não suportado.\n Tente novamente.", fg="red",
                     font=("Arial", 12))
    mensagem.place(x=25, y=10)
    voltar = Button(erro, width=5, text="Ok", cursor="hand2", command=erro.destroy)
    voltar.place(x=120, y=60)
    erro.mainloop()

    return

#==================================================================================================



#===============================JANELAS REFERENTE A DESCOMPACTACAO ================================
#Esta é a janela de compactacao
def JaneladeDescompactacao():
    janela = Tk()
    janela.title("ALE- Tela de Descompactacao")

    selecione = Label(janela, text="Selecione o diretório do arquivo (.ale): ", font=("Arial",11))
    selecione.place(x=20,y=100)

    SelecionarDiretorio = Button(janela, width = 5,  text = "...",cursor="hand2",command=SelecaodeArquivo_Descompactar)  #botao selecao diretorio
    SelecionarDiretorio.place(x=280, y=95)


    voltar = Button(janela, width=6, text="Voltar", command = janela.destroy)
    voltar.place(x = 125, y=175)

    janela.geometry("350x300+150+150")
    janela.mainloop()                                           #Laço de exebição infinito
    janela.destroy()                                            #Fecho a janela de compactacao
    return


def SelecaodeArquivo_Descompactar():
    try:
        filename = askopenfilename(initialdir="/", title="Selecione o arquivo",
                                                       filetypes=(("Arquivos de Texto", "*.txt"),("Arquivos de Imagem", "*.jpg *.png"), ("Todos Arquivos", "*.*")))
        diretorio_arquivo = filename
    except:
        erroCompactar()

    if(diretorio_arquivo[-4:] == ".ale"):
        descompactar()
    else:
        erroDescompactar()
    return


def erroDescompactar():
    return

#==================================================================================================



#============================JANELAS REFERENTE AO PROGRAMA PRINCIPAL ==============================

def ProgramaPrincipal():
    principal = Tk()                                               #Janela principal com uma nova instancia de TK
    principal.title("ALE - Tela Principal (beta)")
    #icone_compactar = PhotoImage(file = "compactar.png")


    lb = Label(principal, text="Selecione a opção desejada:", font="Arial 14")
    lb["background"] = "white"
    lb.place(x=30, y = 25)

    Compactar = Button(principal, width = 20, text = "Compactar", cursor="hand2", command=JaneladeCompactacao)
    Compactar.place(x=70, y=80)
    #Compactar_figura = Label(principal, image = icone_compactar, width=10)
    #Compactar_figura.place(x = 30, y = 80)


    Descompatar = Button(principal, width=20, text="Descompactar" ,cursor="hand2", command = JaneladeDescompactacao)
    Descompatar.place(x=70,y=130)

    Sair = Button(principal, width=20, text="Sair do Programa", cursor="hand2", command = exit)
    Sair.place(x=70,y=180)

    Mensagem = Label(principal, text="Desenvolvido por Elismar Silva e Lucas Dantas \nAlgoritmos e Lógica de Programação\nProfessora: Ianna Sodré", bg="white", fg = "red",font = ("Arial",9,"bold italic"))
    Mensagem.place(x = 12, y = 250)

    principal["background"] = "white"          #Cor do fundo
    principal.geometry("300x300+100+100")      #larguraxaltura+distanciaEsquerda+Distancia top
    principal.resizable(0,0)
    principal.mainloop()                       #Laço de exebição infinito
    return

ProgramaPrincipal()


