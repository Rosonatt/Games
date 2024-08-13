import pygame
from sys import exit
import random

pygame.init()
relogio = pygame.time.Clock()

# Sons
som_morte = pygame.mixer.Sound("assets/sfx/dead.wav")
som_bater_asas = pygame.mixer.Sound("assets/sfx/flap.wav")
som_pontuacao = pygame.mixer.Sound("assets/sfx/score.wav")

# Janela
altura_janela = 720
largura_janela = 551
janela = pygame.display.set_mode((largura_janela, altura_janela))

# Imagens
imagens_passaro = [pygame.image.load("assets/bird_down.png"),
                   pygame.image.load("assets/bird_mid.png"),
                   pygame.image.load("assets/bird_up.png")]
imagem_fundo = pygame.image.load("assets/background.png")
imagem_chao = pygame.image.load("assets/ground.png")
imagem_cano_topo = pygame.image.load("assets/pipe_top.png")
imagem_cano_fundo = pygame.image.load("assets/pipe_bottom.png")
imagem_game_over = pygame.image.load("assets/game_over.png")
imagem_inicio = pygame.image.load("assets/start.png")

# Jogo
velocidade_scroll = 1.1  # Aumento de 10% na velocidade
posicao_inicial_passaro = (100, 250)
pontuacao = 0
fonte = pygame.font.SysFont('Segoe', 26)
jogo_parado = True

class Passaro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagens_passaro[0]
        self.rect = self.image.get_rect()
        self.rect.center = posicao_inicial_passaro
        self.indice_imagem = 0
        self.vel = 0
        self.bateu_asas = False
        self.vivo = True

    def update(self, entrada_usuario):
        # Animar Pássaro
        if self.vivo:
            self.indice_imagem += 1
        if self.indice_imagem >= 30:
            self.indice_imagem = 0
        self.image = imagens_passaro[self.indice_imagem // 10]

        # Gravidade e Bater Asas
        self.vel += 0.5
        if self.vel > 7:
            self.vel = 7
        if self.rect.y < 500:
            self.rect.y += int(self.vel)
        if self.vel == 0:
            self.bateu_asas = False

        # Rotacionar Pássaro
        self.image = pygame.transform.rotate(self.image, self.vel * -7)

        # Entrada do Usuário
        if entrada_usuario[pygame.K_SPACE] and not self.bateu_asas and self.rect.y > 0 and self.vivo:
            self.bateu_asas = True
            self.vel = -7
            som_bater_asas.play()

class Cano(pygame.sprite.Sprite):
    def __init__(self, x, y, imagem, tipo_cano):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.entrada, self.saida, self.passou = False, False, False
        self.tipo_cano = tipo_cano

    def update(self):
        # Mover Cano
        self.rect.x -= velocidade_scroll
        if self.rect.x <= -self.rect.width:
            self.kill()

        # Pontuação
        global pontuacao
        if self.tipo_cano == 'fundo':
            if posicao_inicial_passaro[0] > self.rect.topleft[0] and not self.passou:
                self.entrada = True
            if posicao_inicial_passaro[0] > self.rect.topright[0] and not self.passou:
                self.saida = True
            if self.entrada and self.saida and not self.passou:
                self.passou = True
                pontuacao += 1
                som_pontuacao.play()

class Chao(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem_chao
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self):
        # Mover Chão
        self.rect.x -= velocidade_scroll
        if self.rect.x <= -self.rect.width:
            self.rect.x = self.rect.width

def sair_jogo():
    # Sair do Jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

# Método Principal do Jogo
def principal():
    global pontuacao, jogo_parado

    # Instanciar Pássaro
    passaro = pygame.sprite.GroupSingle()
    passaro.add(Passaro())

    # Configurar Canos
    temporizador_cano = 0
    canos = pygame.sprite.Group()

    # Instanciar Chão Inicial
    chao = pygame.sprite.Group()
    chao.add(Chao(0, 520))
    chao.add(Chao(imagem_chao.get_width(), 520))

    rodando = True
    morte_timer = 0
    while rodando:
        # Sair
        sair_jogo()

        # Resetar Frame
        janela.fill((0, 0, 0))

        # Entrada do Usuário
        entrada_usuario = pygame.key.get_pressed()

        # Desenhar Fundo
        janela.blit(imagem_fundo, (0, 0))

        # Desenhar - Canos, Chão e Pássaro
        canos.draw(janela)
        chao.draw(janela)
        passaro.draw(janela)

        # Mostrar Pontuação
        texto_pontuacao = fonte.render('Pontuação: ' + str(pontuacao), True, pygame.Color(255, 255, 255))
        janela.blit(texto_pontuacao, (20, 20))

        # Atualizar - Canos, Chão e Pássaro
        if passaro.sprite.vivo:
            canos.update()
            chao.update()
            passaro.update(entrada_usuario)

            # Detecção de Colisão
            colisoes_canos = pygame.sprite.spritecollide(passaro.sprite, canos, False)
            colisoes_chao = pygame.sprite.spritecollide(passaro.sprite, chao, False)
            if colisoes_canos or colisoes_chao:
                passaro.sprite.vivo = False
                som_morte.play()
                morte_timer = 180  # 3 segundos

            # Gerar Canos
            if temporizador_cano <= 0 and passaro.sprite.vivo:
                x_topo, x_fundo = 550, 550
                y_topo = random.randint(-600, -480)
                y_fundo = y_topo + random.randint(90, 130) + imagem_cano_fundo.get_height()
                canos.add(Cano(x_topo, y_topo, imagem_cano_topo, 'topo'))
                canos.add(Cano(x_fundo, y_fundo, imagem_cano_fundo, 'fundo'))
                temporizador_cano = random.randint(180, 250)
            temporizador_cano -= 1

        else:  # Se o pássaro morreu
            morte_timer -= 1
            if morte_timer <= 0:
                jogo_parado = True
                break

        relogio.tick(60)
        pygame.display.update()

    # Depois que o jogo termina
    while jogo_parado:
        sair_jogo()

        # Desenhar Game Over
        janela.blit(imagem_game_over, (largura_janela // 2 - imagem_game_over.get_width() // 2,
                                       altura_janela // 2 - imagem_game_over.get_height() // 2))

        # Mostrar pontuação final
        texto_pontuacao_final = fonte.render('Pontuação final: ' + str(pontuacao), True, pygame.Color(255, 255, 255))
        janela.blit(texto_pontuacao_final, (largura_janela // 2 - texto_pontuacao_final.get_width() // 2,
                                            altura_janela // 2 + imagem_game_over.get_height()))

        # Eventos do usuário
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    jogo_parado = False
                    pontuacao = 0
                    principal()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        pygame.display.update()

# Menu
def menu():
    global jogo_parado

    while jogo_parado:
        sair_jogo()

        # Desenhar Menu
        janela.fill((0, 0, 0))
        janela.blit(imagem_fundo, (0, 0))
        janela.blit(imagem_chao, (0, 520))
        janela.blit(imagens_passaro[0], (100, 250))
        janela.blit(imagem_inicio, (largura_janela // 2 - imagem_inicio.get_width() // 2,
                                    altura_janela // 2 - imagem_inicio.get_height() // 2))

        # Entrada do Usuário
        entrada_usuario = pygame.key.get_pressed()
        if entrada_usuario[pygame.K_SPACE]:
            jogo_parado = False
            principal()

        pygame.display.update()

menu()



##############creator#######ROSONATT#########

           
