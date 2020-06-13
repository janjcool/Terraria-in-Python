import pygame
pygame.init()

class options:
    def __init__(self):
        self.width = 1000 #in pixels (best mulipley by 16)
        self.height = 700 #in pixels (best mulipley by 16)
        self.fps = 60 #frames per second
        self.character_bigness = 2.5 #how big your character is
        self.player_speed = 5 #how many pixels you move
        self.player_crouching_speed = 2 #how many pixels the player moves when crouching
        self.gravity = 5 #how many pixels you go down
        self.player_animation_speed = 15 #after how many frames the next idle animation comes
        self.jump_lenght = 20 #how many frames you jump
        self.jump_speed = 30 #pixel you jump per second

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

class rects:
    def __init__(self, width, height):
        #background
        wallpaper = pygame.image.load("background.png")
        self.wallpaper = pygame.transform.scale(wallpaper, (width, height))
        
        self.background_list = [wallpaper]

        #UI
        self.quit_rect = pygame.Rect(width-80, 0, 80, 60)
        self.test_rect = pygame.Rect(0, 0, 100, 100)
        
        self.UI_rects = [self.quit_rect, self.test_rect]
        
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