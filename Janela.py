import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("RETORNO DO REI")

fonte = pygame.font.SysFont("arial", 28)
branco = (255, 255, 255)
preto = (0, 0, 0)

def desenhar_texto(lista_texto):
    tela.fill(preto)
    for i, texto in enumerate(lista_texto):
        linha = fonte.render(texto, True, branco)
        tela.blit(linha, (40, 40 + i * 40))
    pygame.display.update()

def esperar_enter():
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == KEYDOWN:
                if evento.key == K_RETURN:
                    return
                
mensagens = [
    "----- RETORNO DO REI -----",
    "Pressione Enter para continuar..."
]

desenhar_texto(mensagens)
esperar_enter()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()