import cv2
import numpy

def GerarImagemFinal(ImagememString, PixelsX, PixelsY):

     imagemOrdenada = [[0 for a in range(PixelsY)] for b in range(PixelsX)]     #Crio uma matriz 2D que será a imagem FINAL


     for i in range (len(ImagememString)):
          for j in range(len(ImagememString[i])):
               if ImagememString[i][j] != " ":
                    imagemOrdenada[i][j] = int(ImagememString[i][j])
               else:
                    imagemOrdenada[i][j] = ImagememString[i][j]

     #Crio a imagem final transformando em um array numpy
     ImagemFinal = numpy.array(imagemOrdenada)
     print("Ordenada: ", ImagemFinal)
     cv2.imwrite("16x16 (1).jpg", ImagemFinal)

#Transformo a imagem em STRING para uma MATRIZ NUMPY 2-dimensões
def GerarImagemString(LinhaEmString, PixelsX, PixelsY):
     linha = ''
     imagemString = []
     for elemento in range(len(LinhaEmString)):
          if LinhaEmString[elemento] == "\n":
               imagemString.append(linha.split())
               linha = ''
          else:
               linha += LinhaEmString[elemento]
     GerarImagemFinal(imagemString, PixelsX, PixelsY)

def AbrirImagem(caminho):
     img = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)
     print(type(img))
     shape = img.shape
     pixelsX, pixelsY = shape
     print(pixelsX, pixelsY)
     linhaImagem = ''

     for x in range(pixelsX):
          for y in range(pixelsY):
               linhaImagem += str(img[x][y]) + " "
          linhaImagem += "\n"

     print("Linha imagem: ", len(linhaImagem))
     GerarImagemString(linhaImagem, pixelsX, pixelsY)






"""
for i in range(a):
     for j in range(b):
          countArray[img[i][j]] += 1
"""



