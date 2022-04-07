from funcoesPDI import *
import cv2
import numpy
from matplotlib import pyplot

def main():
    # Implementação de variáveis diferentes para não sobrescrever as cores.

    imageR = cv2.imread("imagens/python.jpg")
    imageG = cv2.imread("imagens/python.jpg")
    imageB = cv2.imread("imagens/python.jpg")

    # Todos os pontos pedidos estão comentados e implementados a seguir:

    # 1.1
    exibirImagem(imageR)

    # 1.2
    converterCanais(imageR)

    # 1.7 e 1.8 Recortando a imagem e salvando como "modificado.jpg" na pasta "imagens"
    recortarImagemSave(imageR)

    # 1.3
    dimensaoImagem(imageR)

    # 1.4
    conteudoPixel(imageR)

    # 1.5.1
    imagemAzul(imageB)

    # 1.5.2
    imagemVerde(imageG)

    # 1.5.3
    imagemVermelho(imageR)

    # 1.6 está implementado em todas as funções das cores salvando as versões na pasta "imagens".

main()
