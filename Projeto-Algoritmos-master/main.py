#====================================== BIBLIOTECAS ===============================================
import os
from CompressoresDescompressores.compactador import compactar
from CompressoresDescompressores.descompactador import descompactar
from Ferramentas.ferramentasDiversas import exibirMenu,encerrar

#===================================================================================================
def main():
    continuar = True
    while continuar:
        opcao = exibirMenu()
        if(opcao == 0):
            encerrar()
            continuar = False

        elif(opcao == 1):
            compactar()

        elif(opcao == 2):
            descompactar()

        else:
            print("Opcao Invalids Tente novamente")

if __name__ == '__main__':
    main()
