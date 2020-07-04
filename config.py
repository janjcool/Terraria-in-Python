import pygame

class options:
    def __init__(self):
        
        #window stuff
        self.width = 1000 #in pixels (best multiple by 16)
        self.height = 700 #in pixels (best multiple by 16)
        self.fps = 60 #frames per second
        self.screen_title = "a project I probably won`t finish" #the title of the window
        self.displayer_choser = "MainMenu" #choos what display (example: MainMenu, game, inv...) to start with
        self.UI_scale = 1.5
        self.display = 0
        self.display_mode = 2 #(0, 1, 2) = (window, FullScreen, borderless_fullscreen)
        
        #player settings
        self.character_bigness = 2.5 #how big your character is
        self.player_speed = 5 #how many pixels you move
        self.player_crouching_speed = 2 #how many pixels the player moves when crouching
        self.player_animation_speed = 15 #after how many frames the next idle animation comes
        self.jump_lenght = 20 #how many frames you jump
        
        #World settings
        self.gravity = 5 #how many pixels you go down
        
        #map settings
        self.mountain_steepness = 60 #more meens the heights and the lowest point of mountens are further apart
        self.amount_of_sky = 5 #them amount of blocks before any land comes
        self.distance_between_raw = 10 #amount of blocks between each opensimplex noise number !!!  this must be divisible by world_width  !!!
        self.chunk_size = 32 #how many Block by how many Block a Chunk is
        self.map_width_small = 32 * 150 #width of a small map
        self.map_height_small = 32 * 10 #height of a small map
        self.map_width_medium = 32 * 200 #width of a medium map
        self.map_height_medium = 32 * 12 #height of a medium map
        self.map_width_large = 32 * 250 #width of a big map
        self.map_height_large = 32 * 14 #height of a big map
        
        #sprites
        self.dirt = ["dirt", "art-assets/dirt.png"]
        self.sky = ["sky", 0]

class buttons:
    def __init__(self):
        self.forward_key = 119
        self.left_key = 97
        self.back_key = 115
        self.right_key = 100
        self.crouch_key = 1073742048
        self.esc_key = 27
        self.backspace_key = 8
        self.space_key = 32

class colors:
    def __init__(self):
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (30, 30, 30)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)

class fonts:
    def __init__(self, config_options):
        self.Arial_font40 = pygame.font.Font('art-assets/fonts/Arial.TTF', int(40 * config_options.UI_scale))
        self.Arial_font60 = pygame.font.Font('art-assets/fonts/Arial.TTF', int(60 * config_options.UI_scale))
        self.Arial_font80 = pygame.font.Font('art-assets/fonts/Arial.TTF', int(80 * config_options.UI_scale))
        self.Arial_font100 = pygame.font.Font('art-assets/fonts/Arial.TTF', int(100 * config_options.UI_scale))
        self.Arial_font120 = pygame.font.Font('art-assets/fonts/Arial.TTF', int(120 * config_options.UI_scale))
        self.Arial_font140 = pygame.font.Font('art-assets/fonts/Arial.TTF', int(140 * config_options.UI_scale))
        
        self.Arial_Bold_font40 = pygame.font.Font('art-assets/fonts/Arial_bold.TTF', int(40 * config_options.UI_scale))
        self.Arial_Bold_font60 = pygame.font.Font('art-assets/fonts/Arial_bold.TTF', int(60 * config_options.UI_scale))
        self.Arial_Bold_font80 = pygame.font.Font('art-assets/fonts/Arial_bold.TTF', int(80 * config_options.UI_scale))
        self.Arial_Bold_font100 = pygame.font.Font('art-assets/fonts/Arial_bold.TTF', int(100 * config_options.UI_scale))

class rects_game:
    def __init__(self, config_options):
        #background
        self.wallpaper = pygame.image.load("art-assets/background/finalDay-edit.PNG")
        self.wallpaper = pygame.transform.scale(self.wallpaper, (config_options.width, config_options.height))

        #UI
        self.test_rect = pygame.Rect(0, 0, 100, 100)
        
        #solid
        self.grass_rect = pygame.Rect(-400, config_options.height-50, config_options.width+800, 100)
        self.dirt_rect = pygame.Rect(-400, config_options.height+50, config_options.width+800, 400)
        self.wall_rect = pygame.Rect(config_options.width-50, config_options.height-100, 10, 50)
        
        self.solid_moverect_list = [self.grass_rect, self.wall_rect, self.dirt_rect]
        
        #unsolid
        self.tree_rect = pygame.Rect(80, config_options.height-90, 20, 60)
        self.tree2_rect = pygame.Rect(80+200, config_options.height-90, 20, 60)
        self.leafs_rect = pygame.Rect(70, config_options.height-130, 40, 40)
        self.leafs2_rect = pygame.Rect(70+200, config_options.height-130, 40, 40)
        
        self.unsolid_moverect_list = [self.tree_rect, self.leafs_rect, self.tree2_rect, self.leafs2_rect]
        
        #player
        self.player_rect = pygame.Rect(int(config_options.width/2+7), int(config_options.height/2+15), 42, 42)
        self.player_sprite = pygame.image.load("art-assets/player/sprites/adventurer-idle-00.png")

class rects_mainMenu:
    def __init__(self, config_options, config_colors, config_fonts):
        #background
        self.wallpaper = pygame.image.load("art-assets/background/finalNight.PNG")
        self.wallpaper = pygame.transform.scale(self.wallpaper, (config_options.width, config_options.height))
        
        #buttons
        self.start_button = pygame.Rect(int(100), int(config_options.height/2-275), 300, 150)
        self.settings_button = pygame.Rect(int(100), int(config_options.height/2-87), 520, 175)
        self.exit_button = pygame.Rect(int(100), int(config_options.height/2+125), 300, 150)
        
        self.start_button_text = config_fonts.Arial_font100.render('play', True, config_colors.WHITE)
        self.exit_button_text = config_fonts.Arial_font100.render('exit', True, config_colors.WHITE)
        self.settings_button_text = config_fonts.Arial_font100.render('settings', True, config_colors.WHITE)
        
        
class rects_gameMenu:
    def __init__(self, config_options, config_colors, config_fonts):
        #background
        self.wallpaper = pygame.image.load("art-assets/background/transparant.png")
        self.wallpaper = pygame.transform.scale(self.wallpaper, (config_options.width, config_options.height))
        
        #buttons
        self.game_button = pygame.Rect(int(config_options.width/2-125), int(config_options.height/2-125), 250, 100)
        self.mainMenu_button = pygame.Rect(int(config_options.width/2-125), int(config_options.height/2+25), 250, 100)
        self.settings_button = pygame.Rect(int(config_options.width/2-125), int(config_options.height/2+25), 250, 100)
        
        self.mainMenu_button_text = config_fonts.Arial_Bold_font100.render('exit', True, (150, 150, 150))
        self.settings_button_text = config_fonts.Arial_Bold_font100.render('settings', True, config_colors.WHITE)
        self.play_button_text = config_fonts.Arial_Bold_font100.render('play', True, config_colors.WHITE)

class rects_worldGen_menu:
    def __init__(self, config_options):
        #background
        
        #buttons
        self.start_button = pygame.Rect(int(config_options.width-300), int(config_options.height/150), 250, 100)
        self.exit_button = pygame.Rect(int(config_options.width/2-125), int(config_options.height/2+25), 250, 100)
        
        self.start_button_image = pygame.image.load("art-assets/ui/play_button.png")
        self.start_button_image = pygame.transform.scale(self.start_button_image, (250, 100))
        
        self.exit_button_image = pygame.image.load("art-assets/ui/exit_button.png")
        self.exit_button_image = pygame.transform.scale(self.exit_button_image, (250, 100))
        
        self.UI_rects_list = [self.start_button, self.start_button_image, self.exit_button_image, self.exit_button]