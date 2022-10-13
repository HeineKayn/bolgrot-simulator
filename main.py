import pygame
from constantes import SCREEN_SIZE

from menu import Menu
from game import Game

def main():

    pygame.init()
    # pygame.display.set_icon(pygame.image.load("ressources/textures/nexus.png"))
    pygame.display.set_caption("Bolgrot Simulator")

    ecran = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()

    # menu = Menu(ecran,clock)
    # menu.start()

    jeu = Game(ecran,clock)
    jeu.start()

    pygame.quit()

if __name__ == '__main__':
    main()