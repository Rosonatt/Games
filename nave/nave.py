import pygame
import random
from pygame.locals import *
from scripts.player import Player, Shot
from scripts.enemy import Enemy

class Jogo:
    def __init__(self):
        pygame.init()  # Inicializa o pygame

        self.largura_janela = 1200
        self.altura_janela = 600
        self.janela = pygame.display.set_mode((self.largura_janela, self.altura_janela))  # Cria a janela do jogo

        self.fundo = pygame.image.load("img/background2_day.jpg")  # Carrega a imagem de fundo
        self.fundo = pygame.transform.scale(self.fundo, (self.largura_janela, self.altura_janela))  # Redimensiona a imagem de fundo

        # Jogador
        self.grupo_jogador = pygame.sprite.Group()
        self.jogador = Player()
        self.grupo_jogador.add(self.jogador)
        self.movendo_direita = False
        self.movendo_esquerda = False

        # Tiro
        self.grupo_tiros = pygame.sprite.Group()

        # Inimigos
        self.grupo_inimigos = pygame.sprite.Group()

        # Pontuação e Nível
        self.pontos_jogador = 0
        self.fonte = pygame.font.Font("font/8bit.ttf", 30)
        self.atualizar_pontuacao()
        self.nivel = 0
        self.atualizar_nivel()

        # Música de fundo
        pygame.mixer.init()
        pygame.mixer.set_reserved(0)
        self.musica_jogo = pygame.mixer.Sound("sounds/game_music.wav")
        pygame.mixer.Channel(0).play(self.musica_jogo, -1)  # Toca a música de fundo em loop

        # FPS
        self.fps = pygame.time.Clock()

        # Loop principal do jogo
        self.jogo_rodando = True
        self.loop_principal()

    def lidar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()

            if evento.type == KEYDOWN:
                if evento.key == K_RIGHT:
                    self.movendo_direita = True
                if evento.key == K_LEFT:
                    self.movendo_esquerda = True
                if evento.key == K_SPACE:
                    tiro_jogador = Shot()
                    tiro_jogador.rect[0] = self.jogador.rect[0] + 23
                    tiro_jogador.rect[1] = self.jogador.rect[1]
                    self.grupo_tiros.add(tiro_jogador)
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("sounds/shot.wav"))

            if evento.type == KEYUP:
                if evento.key == K_RIGHT:
                    self.movendo_direita = False
                if evento.key == K_LEFT:
                    self.movendo_esquerda = False

    def atualizar_estado_jogo(self):
        if self.movendo_direita:
            self.jogador.rect.x += self.jogador.velocidade
        if self.movendo_esquerda:
            self.jogador.rect.x -= self.jogador.velocidade

        self.grupo_tiros.update()
        self.grupo_jogador.update()
        self.grupo_inimigos.update()

        self.spawn_inimigos()

        for inimigo in self.grupo_inimigos:
            if inimigo.rect.y > self.altura_janela:
                self.grupo_inimigos.remove(inimigo)

        self.verificar_colisoes()

    def desenhar_elementos(self):
        self.janela.blit(self.fundo, (0, 0))
        self.janela.blit(self.texto_pontos, (850, 10))
        self.janela.blit(self.texto_nivel, (650, 10))
        self.grupo_tiros.draw(self.janela)
        self.grupo_jogador.draw(self.janela)
        self.grupo_inimigos.draw(self.janela)

    def spawn_inimigos(self):
        if len(self.grupo_inimigos) < 5:
            for _ in range(5):
                inimigo = Enemy()
                self.grupo_inimigos.add(inimigo)

    def verificar_colisoes(self):
        if pygame.sprite.groupcollide(self.grupo_tiros, self.grupo_inimigos, True, True):
            self.pontos_jogador += random.randint(1, 10)
            self.atualizar_pontuacao()
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("sounds/enemy_death.wav"))

        if pygame.sprite.groupcollide(self.grupo_jogador, self.grupo_inimigos, True, False):
            self.reiniciar_jogo()

    def atualizar_pontuacao(self):
        self.texto_pontos = self.fonte.render("PONTOS: " + str(self.pontos_jogador), 1, (255, 255, 255))

    def atualizar_nivel(self):
        niveis = [500, 2000, 4000, 8000, 10000, 20000, 50000]
        velocidades = [2, 3, 4, 6, 8, 9, 12]
        for i, limite in enumerate(niveis):
            if self.pontos_jogador > limite:
                self.nivel = i + 1
                for inimigo in self.grupo_inimigos:
                    inimigo.velocidade = velocidades[i]
        if self.pontos_jogador > 50000:
            self.nivel = "FINAL"
            for inimigo in self.grupo_inimigos:
                inimigo.velocidade = 12
        self.texto_nivel = self.fonte.render("NÍVEL: " + str(self.nivel), 1, (255, 255, 255))

    def reiniciar_jogo(self):
        self.__init__()

    def loop_principal(self):
        while self.jogo_rodando:
            self.fps.tick(30)
            self.lidar_eventos()
            self.atualizar_estado_jogo()
            self.desenhar_elementos()
            pygame.display.update()

# Inicializa o jogo fora da função main
jogo = Jogo()
