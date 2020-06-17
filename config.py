import pygame
pygame.init()

class options:
    def __init__(self):
        #window stuff
        self.width = 1000 #in pixels (best multiple by 16)
        self.height = 700 #in pixels (best multiple by 16)
        self.fps = 60 #frames per second
        self.screen_title = "a project I probably won`t finish" #the title of the window
        self.displayer_choser = "mainMenu" #choos what display (example: mainMenu, game, inv...) to start with
        
        #player settings
        self.character_bigness = 2.5 #how big your character is
        self.player_speed = 5 #how many pixels you move
        self.player_crouching_speed = 2 #how many pixels the player moves when crouching
        self.player_animation_speed = 15 #after how many frames the next idle animation comes
        self.jump_lenght = 20 #how many frames you jump
        
        #world settings
        self.gravity = 5 #how many pixels you go down
        

class colors:
    def __init__(self):
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (30, 30, 30)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)

class fonts:
    def __init__(self):
        self.font10 = pygame.font.SysFont('Arial', 10)
        self.font20 = pygame.font.SysFont('Arial', 20)
        self.font30 = pygame.font.SysFont('Arial', 30)
        self.font40 = pygame.font.SysFont('Arial', 40)

class rects_game:
    def __init__(self, width, height):
        #background
        self.wallpaper = pygame.image.load("background.png")
        self.wallpaper = pygame.transform.scale(self.wallpaper, (width, height))
        
        self.background_list_game = [self.wallpaper]

        #UI
        self.test_rect = pygame.Rect(0, 0, 100, 100)
        
        self.UI_rects_list_game = [self.test_rect]
        
        #solid
        self.grass_rect = pygame.Rect(0, height-50, width, 100)
        self.dirt_rect = pygame.Rect(-1000, height+50, width+1000, 300)
        self.wall_rect = pygame.Rect(width-50, height-100, 10, 50)
        
        self.solid_moverect_list = [self.grass_rect, self.wall_rect, self.dirt_rect]
        
        #unsolid
        self.tree_rect = pygame.Rect(80, height-90, 20, 60)
        self.tree2_rect = pygame.Rect(80+200, height-90, 20, 60)
        self.leafs_rect = pygame.Rect(70, height-130, 40, 40)
        self.leafs2_rect = pygame.Rect(70+200, height-130, 40, 40)
        
        self.unsolid_moverect_list = [self.tree_rect, self.leafs_rect, self.tree2_rect, self.leafs2_rect]
        
        #player
        self.player_rect = pygame.Rect(int(width/2+7), int(height/2-15), 42, 72)
        self.player_sprite = pygame.image.load("art-assets/player/sprites/adventurer-idle-00.png")

class rects_mainMenu:
    def __init__(self, width, height):
        #background
        
        #buttons
        self.start_button = pygame.Rect(int(width/2-125), int(height/2-50), 250, 100)
        
        self.start_button_image = pygame.image.load("art-assets/ui/play_button.png")
        self.start_button_image = pygame.transform.scale(self.start_button_image, (250, 100))
        
        self.UI_rects_list = [self.start_button, self.start_button_image]
        
class rects_gameMenu:
    def __init__(self, width, height):
        #background
        
        #buttons
        self.game_button = pygame.Rect(int(width/2-125), int(height/2-125), 250, 100)
        self.mainMenu_button = pygame.Rect(int(width/2-125), int(height/2+25), 250, 100)
        
        self.mainMenu_button_image = pygame.image.load("art-assets/ui/play_button.png")
        self.mainMenu_button_image = pygame.transform.scale(self.mainMenu_button_image, (250, 100))
        
        self.game_button_image = pygame.image.load("art-assets/ui/exit_button.png")
        self.game_button_image = pygame.transform.scale(self.game_button_image, (250, 100))
        
        self.UI_rects_list = [self.game_button, self.mainMenu_button, self.mainMenu_button_image, self.game_button_image]