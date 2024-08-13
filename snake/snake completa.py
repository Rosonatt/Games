 # iniciando projeto
import pygame, random
from pygame.locals import *

# Funções de auxilio
def on_grid_random():
    x = random.randint(0,59)
    y = random.randint(0,59)
    return (x * 10, y * 10)

def BATER(r1, r2):
    return (r1[0] == r2[0]) and (r1[1] == r2[1])

# Definindo Macro Para o Movimento 
EMCIMA = 0
DIREITA = 1
EMBAIXO = 2
ESQUERDA = 3

pygame.init()
Tela = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Sn8k-G')

SN8K_G = [(200, 200), (210, 200), (220,200)]
SN8K_skin = pygame.Surface((10,10))
SN8K_skin.fill((255,255,255)) #White

maçã_pos = on_grid_random()
maçã = pygame.Surface((10,10))
maçã.fill((255,0,0))

direção = ESQUERDA

Tempo = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 18)
Pontos = 0

fim_do_jogo = False
while not fim_do_jogo:
    Tempo.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP and direção != EMBAIXO:
                direção = EMCIMA
            if event.key == K_DOWN and direção != EMCIMA:
                direção = EMBAIXO
            if event.key == K_LEFT and direção != DIREITA:
                direção = ESQUERDA
            if event.key == K_RIGHT and direção != ESQUERDA:
                direção = DIREITA

    if BATER(SN8K_G[0], maçã_pos):
        maçã_pos = on_grid_random()
        SN8K_G.append((0,0))
        Pontos = Pontos + 1
        
    # Verifique se a cobra colidiu com os limites
    if SN8K_G[0][0] == 600 or SN8K_G[0][1] == 600 or SN8K_G[0][0] < 0 or SN8K_G[0][1] < 0:
        fim_do_jogo = True
        break
    
   # Verifique se a cobra bateu em si mesma
    for i in range(1, len(SN8K_G) - 1):
        if SN8K_G[0][0] == SN8K_G[i][0] and SN8K_G[0][1] == SN8K_G[i][1]:
            fim_do_jogo = True
            break

    if fim_do_jogo:
        break
    
    for i in range(len(SN8K_G) - 1, 0, -1):
        SN8K_G[i] = (SN8K_G[i-1][0], SN8K_G[i-1][1])
        
    # Na verdade, faça a cobra se mover.
    if direção == EMCIMA:
        SN8K_G[0] = (SN8K_G[0][0], SN8K_G[0][1] - 10)
    if direção == EMBAIXO:
        SN8K_G[0] = (SN8K_G[0][0], SN8K_G[0][1] + 10)
    if direção == DIREITA:
        SN8K_G[0] = (SN8K_G[0][0] + 10, SN8K_G[0][1])
    if direção == ESQUERDA:
        SN8K_G[0] = (SN8K_G[0][0] - 10, SN8K_G[0][1])
    
    Tela.fill((0,0,0))
    Tela.blit(maçã, maçã_pos)
    
    for x in range(0, 600, 10): # Desenhar linhas verticais
        pygame.draw.line(Tela, (40, 40, 40), (x, 0), (x, 600))
    for y in range(0, 600, 10): # Desenhar linhas horizontais
        pygame.draw.line(Tela, (40, 40, 40), (0, y), (600, y))
    
    fonte_dos_pontos = font.render('Score: %s' % (Pontos), True, (255, 255, 255))
    gravando_pontos = fonte_dos_pontos.get_rect()
    gravando_pontos.topleft = (600 - 120, 10)
    Tela.blit(fonte_dos_pontos, gravando_pontos)
    
    for pos in SN8K_G:
        Tela.blit(SN8K_skin,pos)

    pygame.display.update()

while True:
    fim_de_jogo_font = pygame.font.Font('freesansbold.ttf', 75)
    tela_de_fim_de_jogo = fim_de_jogo_font.render('perdeu! kk', True, (255, 255, 255))
    gravando_fim_de_jogo = tela_de_fim_de_jogo.get_rect()
    gravando_fim_de_jogo.midtop = (600 / 2, 10)
    Tela.blit(tela_de_fim_de_jogo, gravando_fim_de_jogo)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()