import pygame

SCREEN_SIZE = (WIDTH,HEIGHT) = 1000, 800

# --- SPRITES ---

FOLDER = 'ressources/textures/'
BG_TEXTURE = FOLDER + 'bg.png'
NEXUS_TEXTURES = [FOLDER + 'nexus_anim/nexus' + str(x) + '.png' for x in range(1,8)]
FIREBALL_TEXTURES = [FOLDER + 'fireball_anim/fireball' + str(x) + '.png' for x in range(1,13)]

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

# --- NEXUS --- 

NEXUS_HP = 20
NEXUS_ANIM_FRAMES = 100

# --- PROJECTILE --- 

FIREBALL_SPAWNAREA = {"xMin" : WIDTH + 5,
					  "xMax" : WIDTH + 30,
					  "yMin" : -100,
					  "yMax" : HEIGHT + 100}

# FIREBALL_SPAWNAREA = {"xMin" : WIDTH - 200,
# 					  "xMax" : WIDTH - 173,
# 					  "yMin" : 30,
# 					  "yMax" : HEIGHT - 30}

FIREBALL_SIZE = (50, 50)
FIREBALL_ANIM_FRAMES = 15

FIREBALL_SPAWN_DELAY = 60
FIREBALL_MAX_SPAWN = 10
FIREBALL_MAX_TIME = 4500
FIREBALL_MAX_AMP = 0.02

FIREBALL_GAUSS_MU_INIT = 0
FIREBALL_GAUSS_MU_MAX = 1
FIREBALL_GAUSS_SIG_INIT = 0.2

# --- HP BAR ---

HP_BAR_SIZE = (160,15)
HP_BAR_OFFSET = 30
HP_BAR_THICK = 3

HP_BAR_INNER_COLOR = GREEN
HP_BAR_EDGE_COLOR = WHITE

# --- MANA BAR ---

MANA_BAR_SIZE = (250,30)
MANA_BAR_THICK = 5

# --- BARRIER ---

BARRIER_SIZE 	= 3
BARRIER_COLOR 	= WHITE
BARRIER_HP 		= 1
BARRIER_TIME 	= 2000
BARRIER_LIMIT 	= 500
BARRIER_CREATE_DELAY = 20