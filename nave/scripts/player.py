import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/player1.gif")  # Substitua pelo caminho correto da imagem
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 500
        self.velocidade = 20  # Adiciona o atributo velocidade
        self.pontos = 0  # Adiciona um atributo para armazenar os pontos do jogador

    def update(self):
        # Atualizações do jogador, se necessário
        pass

class Shot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/shot.png")  # Substitua pelo caminho correto da imagem
        self.rect = self.image.get_rect()
        self.rect.x = 0  # Inicializa com uma posição padrão
        self.rect.y = 0  # Inicializa com uma posição padrão
        self.velocidade = -10  # Velocidade do tiro, negativo para ir para cima

    def update(self):
        self.rect.y += self.velocidade  # Move o tiro para cima
        if self.rect.y < 0:
            self.kill()  # Remove o tiro se sair da tela

