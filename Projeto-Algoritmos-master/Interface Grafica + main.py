#====================================== BIBLIOTECAS ===============================================
from tkinter import *                                               #Biblioteca referente à interface grafica
import os
from CompressoresDescompressores.compactador import compactar
from CompressoresDescompressores.descompactador import descompactar

#==================================================================================================



def ProgramaPrincipal():
    janela = Tk()                           #Janela principal com uma nova instancia de TK
    janela.title("ALE - Tela Principal")

    lb = Label(janela, text="Selecione a opção desejada:")
    lb["background"] = "white"
    lb.place(x=60, y = 25)

    Compactar = Button(janela, width = 20, text = "Compactar", command=compactar)
    Compactar.place(x=60, y=60)

    Descompatar = Button(janela, width=20, text="Descompactar", command = descompactar)
    Descompatar.place(x=60,y=110)

    Sair = Button(janela, width=20, text="Sair",command = exit)
    Sair.place(x=60,y=160)

    janela["background"] = "white"          #Cor do fundo
    janela.geometry("300x300+100+200")      #larguraxaltura+distanciaEsquerda+Distancia top
    janela.mainloop()                       #Laço de exebição infinito
    return

ProgramaPrincipal()
