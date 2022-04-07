import cv2
import numpy
from matplotlib import pyplot

def exibirImagem(imagem):
    pyplot.imshow(imagem)
    pyplot.show()

def converterCanais(imagem):
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
    exibirImagem(imagem)

def dimensaoImagem(imagem):
    altura, largura, canais = imagem.shape
    print("Altura:",altura,"Largura:",largura,"Canais:",canais)

def conteudoPixel(imagem):
    altura, largura, canais = imagem.shape
    for x in range(0, altura):
        print(x)
        print("\n")
        for y in range(0, largura):
            print(imagem[x][y], end=" ")

def imagemAzul(imagem):
    altura, largura, canais = imagem.shape
    for x in range(0, altura):
        for y in range(0, largura):
            imagem.itemset((x, y, 0), 0)
            imagem.itemset((x, y, 1), 0)
    exibirImagem(imagem)
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
    cv2.imwrite("imagens/imagemAzul.jpg", imagem)

def imagemVermelho(imagem):
    altura, largura, canais = imagem.shape
    for x in range(0, altura):
        for y in range(0, largura):
            imagem.itemset((x, y, 1), 0)
            imagem.itemset((x, y, 2), 0)
    exibirImagem(imagem)
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
    cv2.imwrite("imagens/imagemVermelho.jpg", imagem)

def imagemVerde(imagem):
    altura, largura, canais = imagem.shape
    for x in range(0, altura):
        for y in range(0, largura):
            imagem.itemset((x, y, 0), 0)
            imagem.itemset((x, y, 2), 0)
    exibirImagem(imagem)
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
    cv2.imwrite("imagens/imagemVerde.jpg", imagem)

def recortarImagemSave(imagem):
    imagem = imagem[28:60,20:90]
    converterCanais(imagem)
    cv2.imwrite("imagens/modificado.jpg", imagem)
