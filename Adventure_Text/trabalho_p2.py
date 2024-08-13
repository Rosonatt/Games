import random
import time
import pygame

# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega os sons
som_ataque = pygame.mixer.Sound("sons/ataque.mp3")
som_dano = pygame.mixer.Sound("sons/dano.mp3")
som_derrota = pygame.mixer.Sound("sons/derrota.mp3")
som_vitoria = pygame.mixer.Sound("sons/vitoria.mp3")
som_dragao = pygame.mixer.Sound("sons/dragao.mp3")
som_queda = pygame.mixer.Sound("sons/queda.mp3")
som_bem_vindo = pygame.mixer.Sound("sons/bem-vindo.mp3")

# Diminui o volume da música de boas-vindas
som_bem_vindo.set_volume(0.2)  # Define o volume para 20%

class Jogador:
    def __init__(self, nome, vida=80, ataque=15):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
    
    def esta_vivo(self):
        return self.vida > 0  # Verifica se o jogador está vivo
    
    def sofrer_dano(self, dano):
        self.vida -= dano  # Reduz a vida do jogador com base no dano recebido
        pygame.mixer.Sound.play(som_dano)
        time.sleep(1)  # Adiciona um delay para dar tempo de tocar o som

    def atacar_inimigo(self, inimigo):
        dano_causado = self.gerar_dano()  # Gera um valor de dano aleatório
        inimigo.sofrer_dano(dano_causado)  # Faz o inimigo sofrer dano
        pygame.mixer.Sound.play(som_ataque)
        time.sleep(1)  # Adiciona um delay para dar tempo de tocar o som
        print(f"{self.nome} ataca {inimigo.nome} causando {dano_causado} de dano!")  # Exibe mensagem de ataque
    
    def gerar_dano(self):
        return random.randint(0, self.ataque)  # Gera um valor de dano aleatório com base no ataque do jogador

class Dragao:
    def __init__(self, nome, vida=40, ataque=20):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
    
    def esta_vivo(self):
        return self.vida > 0  # Verifica se o dragão está vivo
    
    def sofrer_dano(self, dano):
        self.vida -= dano  # Reduz a vida do dragão com base no dano recebido
        pygame.mixer.Sound.play(som_dano)
        time.sleep(1)  # Adiciona um delay para dar tempo de tocar o som
    
    def atacar_jogador(self, jogador):
        dano_causado = self.gerar_dano()  # Gera um valor de dano aleatório
        jogador.sofrer_dano(dano_causado)  # Faz o jogador sofrer dano
        pygame.mixer.Sound.play(som_ataque)
        time.sleep(1)  # Adiciona um delay para dar tempo de tocar o som
        print(f"{self.nome} ataca {jogador.nome} causando {dano_causado} de dano!")  # Exibe mensagem de ataque
    
    def gerar_dano(self):
        return random.randint(0, self.ataque)  # Gera um valor de dano aleatório com base no ataque do dragão

def lutar_com_dragao(jogador, dragao):
    while jogador.esta_vivo() and dragao.esta_vivo():
        print("Você se depara com um dragão enorme! O que você quer fazer?")
        print("1. Atacar o dragão")
        print("2. Tentar se esquivar do ataque do dragão")

        escolha = input("Digite sua escolha: ")

        if escolha == "1":
            jogador.atacar_inimigo(dragao)
            if dragao.esta_vivo():
                dragao.atacar_jogador(jogador)
        elif escolha == "2":
            rolagem_sorte = random.randint(1, 10)
            if rolagem_sorte > 7:
                print("Você consegue se esquivar do ataque do dragão!")
                print("Você aproveita a oportunidade para atacar o dragão!")
                jogador.atacar_inimigo(dragao)
            else:
                print("Você tenta se esquivar do ataque do dragão, mas falha!")
                dragao.atacar_jogador(jogador)
        else:
            print("Escolha inválida!")

    if jogador.esta_vivo():
        pygame.mixer.Sound.play(som_vitoria)
        time.sleep(2)  # Adiciona um delay para dar tempo de tocar o som
        print("Parabéns! Você derrotou o dragão!")
    else:
        pygame.mixer.Sound.play(som_derrota)
        time.sleep(2)  # Adiciona um delay para dar tempo de tocar o som
        print("Você foi derrotado pelo dragão. Tente novamente!")

def jogo():
    nome_jogador = input("Qual é o seu nome herói? ")
    jogador = Jogador(nome_jogador)
    dragao = Dragao("Dragão Quetzalcóatl")

    

    pygame.mixer.Sound.play(som_bem_vindo, loops=-1) # Toca o som de boas-vindas em loop infinito
    print(f"Bem-vindo à Kukulkan's Riches: Echoes of the Serpent's Lair, {jogador.nome}!")
    print("Você está em uma aventura perigosa em busca de um tesouro lendário.")
    print("Você chega a uma encruzilhada. À sua esquerda, há um castelo. À sua direita, uma ponte estreita.")

    escolha = input("Você deseja entrar no castelo (1) ou atravessar a ponte (2)? Escolha sabiamente: ")

    if escolha.lower() == "1":
        
        castelo = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡄⠀⠀⠀⠀⠰⠿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⡀⠈⡇⠀⠀⠀⡄⣴⣶⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠛⠷⢸⡇⣦⣦⡖⡏⠈⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⢸⣷⣿⣿⣧⡇⠠⣿⡇⣰⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⢻⣼⣿⡿⣻⢿⣇⣴⣿⡇⡟⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⢸⢻⣿⡇⡏⢸⣿⢹⣿⣟⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⠀⢸⠿⣿⡇⡇⢸⣿⠿⣿⡿⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣠⣠⣠⠀⠀⠀⢺⠀⢸⠀⣿⣷⣷⣾⣿⠀⣿⡇⡗⡇⠀⠀⣤⣠⣠⢠⠀⠀⠀⠀
⠀⠀⠀⠈⣿⣿⡏⠀⠀⠀⢼⣰⣸⣿⡏⠛⢻⠛⡟⣿⣿⡇⣿⡇⠀⠀⠈⣿⣿⡏⠀⠀⠀⠀
⠀⠀⠀⠀⣿⡏⡇⠀⠀⠀⣼⣿⣿⣿⣷⣶⣾⣶⣶⣿⣿⡇⣿⡇⠀⠀⠀⡏⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣇⡇⠀⠀⠀⢿⣿⣿⣿⡿⠟⠲⠻⢿⣿⣿⡇⣿⡇⠀⠀⠀⣅⣿⡇⠀⠀⠀⠀
⠀⠀⠀⢹⣿⣿⣷⢰⡆⢰⣿⡿⢿⠀⠀⠀⠀⠀⠀⠀⠀⡿⢿⣷⡀⣰⣆⣿⡇⣿⡟⠁⠀⠀
⠀⠀⠀⢸⣿⣿⣿⡟⠛⣿⣿⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⡇⢸⣿⣿⠛⢻⣿⣿⣿⡏⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⡇⠀⣿⣿⣿⣏⠀⢀⠀⠀⢀⠀⠀⠀⣿⣿⣿⣯⠀⢸⣿⣿⣿⡇⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⣷⣷⣿⣿⣿⣧⢼⣈⠃⠀⢸⢋⣠⠄⣿⣿⣿⣿⣾⣿⣿⣿⣿⡇⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⢥⢇⡃⠀⢸⡺⡪⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣜⣟⠂⠀⢸⢲⢏⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠺⣌⡇⠀⢸⣧⡝⢲⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀
⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣃⣀⣸⣾⣶⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀
⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⡀⠀
⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠸⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
"""    
        print("Você entra no castelo e se depara com um dragão enorme e amedrontador chamado Quetzalcóatl, e percebe que ele está protegendo um baú cheio de tesouros!")
        ascii_lines = castelo.split("\n") # Divide a string castelo em uma lista de linhas, usando "\n" como delimitador
        for line in ascii_lines: # Itera sobre cada linha da lista ascii_lines
              print(line) # Imprime a linha atual no console
              time.sleep(0.2) # Pausa a execução por 0,2 segundos antes de continuar para a próxima linha
              Dragão = """"
                   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠄⠀⠀⠀⢠⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠋⠀⠀⠀⢠⡟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⢹⡄⠀⠀⠀⢸⢣⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡿⠀⢻⡻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⡜⢿⣇⠀⠀⡏⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⢸⡇⠀⠈⣷⡹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⡀⠉⠓⢶⡇⢠⣧⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣴⣶⣶⣤⣄⣀⠀⠀⠀⠀⢸⡇⢸⣇⠀⠀⠸⡇⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣷⣄⢸⡇⠈⣿⡟⠳⢦⣄⡀⠀⠀⠀⠀⠉⠻⢯⡉⠙⠶⣄⠉⠳⣤⠀⠀⠸⣇⠀⢻⡀⠀⠀⢱⠀⠸⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡇⠀⢯⢷⠀⠀⠀⠉⠛⠶⣦⣄⡀⠀⠀⢳⡀⠀⠀⠳⡄⠀⠳⡄⠀⠻⣆⠀⠻⣆⠀⢸⡆⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡇⠀⢸⡌⣧⡀⠒⢦⣀⠀⠀⠀⠙⠻⢦⣀⢷⡀⠀⠀⢹⡄⠀⠹⣦⡠⢿⣿⡷⣮⣻⣾⡇⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠘⣷⠙⣿⣶⣄⡉⠳⣄⡀⠀⠀⠀⠈⠻⢷⣄⠀⠀⣿⠀⠀⠙⣶⣏⣡⣶⠿⠿⠏⢻⣄⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠶⢿⠀⠀⠸⣆⠘⢷⡙⠿⣦⡈⠳⣦⣀⠀⠀⠀⠀⠙⢧⣀⣿⠆⠀⢸⠟⢻⣿⠻⣆⠀⠀⠀⠙⢧⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠛⠛⠛⢳⣾⡆⠀⠀⠻⡄⠈⠳⣄⠙⢿⣦⡈⠻⣧⡄⠀⠀⠀⠀⠙⢿⡆⠀⠃⠀⠉⣿⣆⢹⡄⠀⠀⠀⠈⣧⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣴⣞⣉⣷⠀⠀⠀⠹⣄⠀⠙⢧⡀⠙⢷⣄⠘⢿⣤⡀⠀⠀⠀⠀⠻⣦⣄⠀⢸⠋⠙⣦⣿⡀⠀⠀⠀⠹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⡛⠛⠛⠻⢿⣧⡀⠀⠀⠙⢧⡀⠈⠻⣦⢤⣹⣦⠀⢻⣿⠀⠀⠀⠀⣀⣹⣏⣴⣇⠀⠀⠈⣿⡇⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠈⢹⣷⠀⠀⠈⢷⠳⡀⠀⠀⠈⠻⣄⠀⠉⢷⣭⡙⣧⠀⣹⣷⣶⢖⣫⣭⣽⣿⣅⠀⠀⣰⠟⠙⡿⣦⣤⣤⣄⣸⣷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠘⣧⠙⢦⣀⡀⠀⠙⢦⡀⠀⠙⢿⣿⣿⣏⣽⣿⣿⠟⠛⢋⣻⣿⣷⣶⡋⠀⠀⣠⠾⢿⣗⠿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣾⡿⠿⠶⠶⢶⣶⣶⣶⣿⣧⡀⠻⣿⣶⡀⠈⢳⣄⠠⣄⠀⠙⠿⣿⡟⠁⠀⡴⠋⠉⠉⠙⣧⡉⠀⠊⠀⠀⠀⢙⣷⣌⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠿⢦⡀⠀⠀⠀⠀⠀⠀⠈⠉⠙⢿⣿⣦⡀⠻⣿⣶⣤⠹⣦⠈⢷⡀⢠⡟⢿⣄⠀⠀⠀⡴⠒⠂⠉⠻⢦⡀⠀⢀⠞⠉⠙⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠞⠉⠀⠀⠀⢠⡟⠀⣀⣀⣀⣀⣀⣀⣠⡶⠛⠛⣿⣿⣷⡀⠉⠻⣿⣌⣧⠀⣿⡟⠀⠀⠙⢷⣄⣸⠁⠀⠀⠀⠠⠤⢽⣏⠛⠀⠀⣀⣼⣿⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⠿⠿⠛⠻⢿⣿⡿⠋⠀⠀⠈⠉⢿⣿⣿⣄⠀⠹⣿⣿⣿⣿⠁⠀⠀⠀⠀⠙⣿⣦⡀⣸⠀⠀⠀⠀⡬⢷⣤⣴⠁⠀⠻⣿⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣾⡿⠟⠉⠀⠀⠀⠀⠀⠀⣠⠏⠀⠀⢀⣀⣠⠾⣿⣿⣿⣿⣄⠀⠉⠉⢻⣿⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣷⣄⣰⡄⠀⠀⠀⠹⠀⠀⠀⠛⢿⣿⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⣿⠥⢤⡀⠀⠀⠀⠀⣀⣠⡾⠃⠀⠀⠈⠉⠁⠀⠀⠀⠈⠻⣿⣿⣧⣀⣀⣘⣿⡄⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠰⡄⠀⡀⠀⢸⣷⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣼⠟⠁⠀⢀⣇⣀⣴⣶⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡿⠿⢿⣿⡿⠉⠻⣦⡀⠀⠀⠀⠀⠀⠻⣇⠉⠛⢿⣿⣆⠀⠀⠀⠀⣳⣠⡇⣰⣼⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠁⠀⣠⣴⠿⠛⠉⠁⠀⣰⠟⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣶⣾⣿⡟⢿⠃⠀⠀⠙⢿⣦⡀⠀⠀⠀⠀⠙⢷⣤⣤⣿⣿⢿⡶⠤⠶⠛⣿⠛⠛⡿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⡿⠋⠁⠀⠀⠀⠀⣰⠇⠀⠀⠀⠀⠀⢀⡤⠖⠛⣫⣴⣾⣿⠛⠋⠀⠸⣧⣸⠀⠀⠀⠀⠀⠙⢷⡀⠀⠀⠀⠀⠀⠉⠻⣿⣿⠀⢷⡀⠀⠀⢻⡆⠘⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⡟⠀⠀⠀⠀⠀⣠⣾⠋⠀⠀⠀⠀⣠⠾⠋⢀⣤⣾⣿⠛⠉⠻⣆⠀⠀⠀⠙⢿⡄⠀⠀⠀⠀⠀⠈⠃⠀⠀⠀⠀⠀⠀⠀⠘⣿⣧⠘⠇⠀⠀⠘⡇⠀⡇⠀⠀⠀⠀⠀
⠀⠀⠀⣴⡏⣠⡀⠀⣠⣴⣾⣿⠇⠀⠀⠀⠀⠞⠋⠀⣴⣿⣿⣿⠁⠀⠀⠀⠙⢧⡀⠀⠀⠈⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣧⡀⠀⠀⠐⢷⡀⣷⠀⠀⠀⠀⠀
⠀⠀⢠⣿⠟⠉⣡⣾⡿⠋⠁⡟⠀⠀⠀⠀⠀⠀⢀⣾⣿⠟⠁⢿⡆⠀⠀⠀⠀⢀⡟⠻⣍⠉⠉⠻⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣬⡇⠀⠀⠀⠈⠳⢻⡆⠀⠀⠀⠀
⠀⠀⠸⠁⢀⣾⡟⠋⠀⠀⣼⠀⠀⠀⠀⠀⠀⣠⣿⣿⠁⠀⠀⠀⠙⣦⡀⠀⠀⢸⡀⠀⢈⡷⢦⣤⣬⡿⢶⣄⡀⠀⠀⢰⣤⡀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠈⢷⠀⠀⠀⠀
⠀⠀⠀⢀⣾⠏⠀⠀⠀⣰⠇⠀⠀⠀⠀⠀⣴⣿⣿⣹⣧⠀⠀⠀⠀⠀⠉⠉⠉⠉⠻⣏⠁⠀⣠⡟⠁⠀⠀⠈⠙⠶⣄⠘⠿⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀
⠀⠀⠀⣿⠃⠀⠀⢀⣼⡟⠀⠀⠀⠀⠀⢰⣿⡿⠁⠀⠘⢧⡀⠀⠀⠀⠘⢷⣀⣀⣤⠾⢿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠈⠹⣦⡀⠉⠳⣦⡀⠀⠀⠀⠀⠀⢴⡏⠉⠙⠶⠄⠘⡗⠶⡄
⠀⠀⢸⣇⡴⢶⣠⣾⣿⡇⠀⠀⠀⠀⢰⣿⣿⠃⠀⠀⠀⠀⠉⠛⢶⠶⠶⠞⢷⠀⠀⣰⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠙⢳⣄⠀⠀⠀⠈⣿⣄⠀⠀⠀⠀⠀⠀⣿
⠀⠀⣼⠟⢀⣾⡿⠋⣸⡇⠀⠀⠀⠀⣼⣿⠹⣇⠀⠀⠀⠀⠀⠀⠈⣆⠀⣀⣨⠟⠋⣽⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣀⠠⡀⠙⣧⡀⠀⢰⣿⣿⣆⠀⠀⠀⠀⠀⢻
⠀⢀⡏⢀⣾⡟⠀⠀⣿⠃⠀⠀⠀⢸⣿⡿⠶⠛⠷⣤⣀⣀⣀⣀⣠⢿⡟⠉⠁⠀⣼⡿⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠷⣽⡄⠸⣇⠀⠘⠞⢿⣿⠤⠶⠂⡔⢠⠟
⠀⠀⠀⣾⡟⠀⠀⢰⡿⠀⠀⠀⠀⣿⡟⠀⠀⠀⠀⠀⠉⢹⡏⠁⠀⠈⢷⡤⠤⢴⣿⡇⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠀⠻⣄⡀⠀⠶⠏⠀⠀⠀⡇⣸⠀
⠀⠀⢸⣿⠁⠀⠀⢸⡇⠀⠀⠀⢰⣿⠻⣄⠀⠀⠀⠀⠀⠈⢷⣀⣤⠔⠋⠀⠀⢰⣿⠃⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣄⠈⠛⠲⣤⡀⠀⣀⡼⣿⠏⠀
⠀⠀⣼⡇⠀⠀⠀⢸⡇⠀⠀⠀⣼⣿⠴⠚⠓⢤⣄⣀⣀⣤⠴⣯⡀⠀⠀⠀⠀⣼⣿⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠓⠦⣤⠬⢿⣦⣅⡿⠋⠀⠀
⠀⠀⣿⣴⠞⠛⢳⣼⡇⠀⠀⢠⣿⠏⠀⠀⠀⠀⠈⢹⡍⠀⠀⠈⢳⣤⣤⣴⠞⢻⡏⠀⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠀⠀⠀⠀
⠀⢐⡿⠁⠀⠀⣾⣿⡇⠀⠀⣸⣿⡀⠀⠀⠀⠀⠀⠀⠙⣆⣀⡤⠞⠁⠀⠀⠙⢿⡇⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⡇⠀⠀⣼⣿⢻⣇⠀⠀⣿⣿⠓⢤⣀⠀⠀⠀⢀⣤⠿⣯⠀⠀⠀⠀⠀⢀⣾⡇⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠁⠀⢸⣿⠃⢘⣿⠀⠀⣿⣿⠶⠋⠉⠛⠛⣿⠉⠁⠀⠙⢷⣤⣀⣠⣴⠊⣻⡇⠀⠀⠸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⡟⠀⠈⣿⠀⢸⣿⡟⠀⠀⠀⠀⠀⠘⠦⣀⢀⣠⠟⠁⠀⠀⠈⠻⣿⡇⠀⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢰⣿⢡⠞⢧⣿⠀⢸⣿⣧⡀⠀⠀⠀⠀⠀⠀⣰⣏⠀⠀⠀⠀⠀⠀⠀⢸⣷⠀⠀⠀⠀⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⠇⠀⣸⣿⠀⣾⣿⣍⣳⠦⢤⣀⡤⠴⠞⠁⠸⢧⡀⠀⠀⠀⠀⣠⣾⣿⡀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡿⠀⢠⣿⣿⠀⣿⡿⠉⠁⠀⠀⠹⣇⠀⠀⠀⠀⠀⣿⠷⠶⠶⠟⠻⣅⣿⡇⠀⠀⠀⠀⠈⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠃⣿⠀⣿⣇⠀⠀⠀⠀⠀⠈⠳⢤⣀⡴⠞⠁⠀⠀⠀⠀⠀⠀⣿⣇⠀⠀⠀⠀⠀⠘⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡿⢰⡟⢠⣿⣿⡄⠀⠀⠀⠀⠀⣀⣴⢿⡅⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡀⠀⠀⠀⠀⠀⠈⠻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⣸⡇⢸⣿⣿⡿⠓⠦⢤⣶⡛⠋⠁⠀⠙⠲⣤⣄⣀⣀⣀⣀⣴⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⢻⡇⢸⣿⠁⠀⠀⠀⠀⠈⢷⠀⠀⠀⠀⢀⣼⠟⠉⠉⠋⠉⠀⠉⠹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠈⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢁⣿⠇⢸⣿⠀⠀⠀⠀⠀⠀⠈⠳⢤⣤⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⡏⠀⣸⣿⡀⠀⠀⠀⠀⠀⠀⣠⣼⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⢹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠃⠀⣿⣿⣷⣶⣶⣶⣶⣶⡿⠋⠀⠉⠈⠙⢦⣄⣀⣀⣀⣠⣤⠶⠚⠓⠛⠛⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠷⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⡟⠀⢰⣿⣿⠿⢛⡏⠉⢻⡇⠀⠀⠀⠀⠀⠀⢀⡽⠋⠉⠉⠉⠀⠀⠀⠀⠀⠀⠘⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠷⣤⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣿⠃⠀⣸⣿⠉⠓⠊⠀⠀⠀⢳⡄⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣼⡿⠀⢠⣿⣿⠀⠀⠀⠀⠀⠀⠀⠙⢦⣀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠟⠈⠻⣿⣷⣄⡀⠀⠀⠀⠀⠀⣀⣠⣤⠶⠶⠶⠛⠛⠛⠲⠿⠀⠀⠀⠀⠀⠀
⠀⢀⣴⣿⡇⠀⠀⣸⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⣠⡿⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⠿⠦⠤⠴⠾⠋⠁⠉⠙⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣠⠟⠁⣿⣀⣀⣾⡿⠿⠛⠿⢷⣶⣤⣠⣤⠴⠞⠋⠀⠀⠙⢦⣄⣀⠀⠀⠀⠀⠀⣀⣠⠶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠉⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⢉⡟⠛⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣆⠀⠀⠀⠀⠀⢀⡴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⢦⣥⠤⠞⠋⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""        
        pygame.mixer.Sound.play(som_dragao)
        time.sleep(2)
        ascii_lines = Dragão.split("\n")
        for line in ascii_lines:
           print(line)
           time.sleep(0.2)
        lutar_com_dragao(jogador, dragao)  # Inicia a luta com o dragão
    elif escolha.lower() == "2":
        print("Você decide atravessar a ponte. Ela parece instável...")
        ponte = """                                              
                             ___....___                             
   ^^                __..-:'':__:..:__:'':-..__                                   
            _ :.':  :  :  :  :  :  :  :  :  :  :  :'.: _           
           [ ]:  :  :  :  :  :  :  :  :  :  :  :  :  :[ ]          
           [ ]:  :  :  :  :  :  :  :  :  :  :  :  :  :[ ]          
  :::::::::[ ]:__:__:__:__:__:__:__:__:__:__:__:__:__:[ ]:::::::::::
 !!!!!!!!![ ]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!![ ]!!!!!!!!!!!
  ^^^^^^^^^[ ]^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^[ ]^^^^^^^^^^^
           [ ]                                        [ ]          
           [ ]                                        [ ]          
           [ ]                                        [ ] 

    """
        pygame.mixer.Sound.play(som_queda)
        time.sleep(0.2)
        ascii_lines = ponte.split("\n")
        for line in ascii_lines:
            print(line)
            time.sleep(0.2)

            perdeu = """
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠒⠊⠉⠉⠉⠒⠲⢤⣀⠀⠀⠀⠀⠀⣀⣤⠤⠶⠒⠶⠤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠦⡤⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠙⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⢀⣀⣠⠤⢤⣀⣀⡀⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀⠀⠀⣠⠴⠚⠉⠀⠀⠀⠀⠀⠀⠉⠙⠲⢤⣹⣀⣀⡤⠤⠤⠤⠤⠤⠤⢄⣀⣈⣇⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣙⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠓⢦⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠒⣊⡭⠥⠔⠒⠲⠦⠤⢭⣉⣳⣄⣤⣴⣒⣊⡭⠭⠭⠭⠭⠭⣿⣶⣻⣦⣀⠀
⠀⠀⠀⢀⡴⠚⢹⠃⠀⠀⠀⠀⠀⠀⢀⡤⠖⢚⣡⠖⠋⠁⠀⠀⠀⠀⠀⢀⣀⣀⣀⣙⣿⡛⠉⠁⠀⢀⣀⣀⣠⣤⣤⣤⠤⣭⣝⣿⣄
⠀⠀⢠⡞⠁⠀⣾⠀⠀⠀⠀⠀⠀⣾⣛⣛⠋⠉⢀⣀⣀⡠⠤⢶⣶⢿⣿⣿⣤⡀⠀⠀⠈⡷⠒⠚⠉⠉⢠⣿⡿⢿⣿⣿⣦⡀⠀⠉⢻
⠀⢀⡏⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠯⣉⠀⠀⠀⢠⣿⣿⣶⣿⠛⢻⣿⡆⠀⣰⠁⠀⠀⠀⠀⣿⣿⠿⣿⣏⣹⣿⣧⢀⣠⡞
⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠦⢬⣙⠒⠤⢼⠿⢿⡿⠿⠿⠿⠛⠛⢉⡼⠛⠓⠒⠒⠶⠟⠛⠛⠛⠛⠛⠋⢩⡿⠛⠀
⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠒⠒⠒⠒⠒⠒⣲⡾⠉⠉⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠋⠀⠀⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠶⠋⠁⠀⠀⠀⠀⠈⠛⠢⢤⣤⠤⠤⠴⠒⢿⡁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠙⢦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠁⡀⠀⣀⡀⠀⠉⠉⠙⠓⠒⠲⠦⠤⠤⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣤⠤⠶⠚⠉⢉⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡅⠀⠀⠉⠉⠉⠉⠉⠓⠒⠶⠤⢤⣤⣀⣀⣀⣀⡀⠀⠀⠉⠉⠉⠉⠁⣀⣀⣀⣀⣠⣴⠟⠁⠀⠀
⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠙⠒⠒⠒⠒⠒⠲⠦⠤⠤⣀⣀⣀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⢀⣿⠀⠀⠀⠀
⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠦⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠙⠛⠛⠒⠒⠒⠒⠶⠶⠶⠶⢶⡦⠶⠒⠋⠁⠀⠀⠀⠀
⠟⠿⢿⡶⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠔⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠓⠦⣭⣉⠓⠒⠶⠦⠤⢤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡤⠖⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠓⠲⠦⢤⣤⣤⣀⣀⣀⣉⣉⣉⣉⣉⡉⢉⣉⣉⣉⣉⣩⣭⠟⠛⠷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠈⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                    
"""
        ascii_lines = perdeu.split("\n")
        for line in ascii_lines:
            print(line)
            time.sleep(0.2)
        print("Você escorrega e cai em um abismo profundo e sem saída. Você escolheu a MORTE!")
    else:
        print("Escolha inválida! Você fica parado sem fazer nada.")

jogo()
