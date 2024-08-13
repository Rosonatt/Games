import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/enemy.png")  # Substitua pelo caminho correto da imagem
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1200 - self.rect.width)
        self.rect.y = -self.rect.height
        self.velocidade = 2  # Adiciona o atributo velocidade

    def update(self):
        self.rect.y += self.velocidade  # Move o inimigo para baixo
        if self.rect.y > 600:
            self.kill()  # Remove o inimigo se sair da tela
