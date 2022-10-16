import pygame

SCREEN_SIZE = (WIDTH,HEIGHT) = 1000, 800

TILEHEIGHT = TILEWIDTH = 70
TILEWIDTH_HALF = TILEWIDTH / 2
TILEHEIGHT_UPPER = TILEHEIGHT / 4 * 3

# --- SPRITES ---

FOLDER = 'ressources/textures/'
BG_TEXTURE = FOLDER + 'bg.png'
TILE_TEXTURE = FOLDER + 'ground.png'
PLAYER_TEXTURE = FOLDER + 'iop.png'
ENNEMY_TEXTURE = FOLDER + 'tofu.png'

# --- COULEURS ---

RED 	= (255, 0, 0)
GREEN 	= (0, 255, 0)
BLUE 	= (0, 0, 255)
YELLOW 	= (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN 	= (0, 255, 255)
BLACK 	= (0, 0, 0)
GRAY 	= (150, 150, 150)
WHITE 	= (255, 255, 255)


# --- MENU --- 

FONT_LIST = {"h1" : (None, 48, 10),
             "h2" : (None, 30, 5)}

TEXT_MENU = [{"content" : "Bolgrot Simulator", "color" : WHITE, "style" : "h1"},
			 {"content" : "Appuyez sur une touche","color" : WHITE, "style" : "h2"}]

CLIGNE_PERIODE = 30

# --- MAP --- 

MAP_SIZE = 9