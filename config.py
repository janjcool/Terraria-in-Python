import pygame

class rects_game:
    def __init__(self, config_dict):
        #background
        self.wallpaper = pygame.image.load("art-assets/background/finalDay-edit.PNG")
        self.wallpaper = pygame.transform.scale(self.wallpaper, (config_dict["window"]["window_width"], config_dict["window"]["window_height"]))

        #UI
        self.test_rect = pygame.Rect(0, 0, 100, 100)
        
        #solid
        self.grass_rect = pygame.Rect(-400, config_dict["window"]["window_height"]-50, config_dict["window"]["window_width"]+800, 100)
        self.dirt_rect = pygame.Rect(-400, config_dict["window"]["window_height"]+50, config_dict["window"]["window_width"]+800, 400)
        self.wall_rect = pygame.Rect(config_dict["window"]["window_width"]-50, config_dict["window"]["window_height"]-100, 10, 50)
        
        self.solid_moverect_list = [self.grass_rect, self.wall_rect, self.dirt_rect]
        
        #unsolid
        self.tree_rect = pygame.Rect(80, config_dict["window"]["window_height"]-90, 20, 60)
        self.tree2_rect = pygame.Rect(80+200, config_dict["window"]["window_height"]-90, 20, 60)
        self.leafs_rect = pygame.Rect(70, config_dict["window"]["window_height"]-130, 40, 40)
        self.leafs2_rect = pygame.Rect(70+200, config_dict["window"]["window_height"]-130, 40, 40)
        
        self.unsolid_moverect_list = [self.tree_rect, self.leafs_rect, self.tree2_rect, self.leafs2_rect]
        
        #player
        self.player_rect = pygame.Rect(int(config_dict["window"]["window_width"]/2+7), int(config_dict["window"]["window_height"]/2+15), 42, 42)
        self.player_sprite = pygame.image.load("art-assets/player/sprites/adventurer-idle-00.png")

class rects_mainMenu:
    def __init__(self, config_dict):
        #background
        self.wallpaper = pygame.image.load("art-assets/background/finalNight.PNG")
        self.wallpaper = pygame.transform.scale(self.wallpaper, (config_dict["window"]["window_width"], config_dict["window"]["window_height"]))
        
        #buttons
        self.start_button = pygame.Rect(int(100), int(config_dict["window"]["window_height"]/2-275), 300, 150)
        self.settings_button = pygame.Rect(int(100), int(config_dict["window"]["window_height"]/2-87), 520, 175)
        self.exit_button = pygame.Rect(int(100), int(config_dict["window"]["window_height"]/2+125), 300, 150)
        
        self.start_button_text = pygame.font.Font('art-assets/fonts/Arial.TTF', int(150)).render('play', True, config_dict["colors"]["white"])
        self.exit_button_text = pygame.font.Font('art-assets/fonts/Arial.TTF', int(150)).render('exit', True, config_dict["colors"]["white"])
        self.settings_button_text = pygame.font.Font('art-assets/fonts/Arial.TTF', int(150)).render('settings', True, config_dict["colors"]["white"])
        
        
class rects_gameMenu:
    def __init__(self, config_dict):
        #background
        self.wallpaper = pygame.image.load("art-assets/background/transparant.png")
        self.wallpaper = pygame.transform.scale(self.wallpaper, (config_dict["window"]["window_width"], config_dict["window"]["window_height"]))
        
        #buttons
        self.game_button = pygame.Rect(int(config_dict["window"]["window_width"]/2-125), int(config_dict["window"]["window_height"]/2-125), 250, 100)
        self.mainMenu_button = pygame.Rect(int(config_dict["window"]["window_width"]/2-125), int(config_dict["window"]["window_height"]/2+25), 250, 100)
        self.settings_button = pygame.Rect(int(config_dict["window"]["window_width"]/2-125), int(config_dict["window"]["window_height"]/2+25), 250, 100)
        
        self.mainMenu_button_text = pygame.font.Font('art-assets/fonts/Arial.TTF', int(150)).render('exit', True, (150, 150, 150))
        self.settings_button_text = pygame.font.Font('art-assets/fonts/Arial.TTF', int(150)).render('settings', True, config_dict["colors"]["white"])
        self.play_button_text = pygame.font.Font('art-assets/fonts/Arial.TTF', int(150)).render('play', True, config_dict["colors"]["white"])

class rects_worldGen_menu:
    def __init__(self, config_dict):
        #background
        
        #buttons
        self.start_button = pygame.Rect(int(config_dict["window"]["window_width"]-300), int(config_dict["window"]["window_height"]/150), 250, 100)
        self.exit_button = pygame.Rect(int(config_dict["window"]["window_width"]/2-125), int(config_dict["window"]["window_height"]/2+25), 250, 100)
        
        self.start_button_image = pygame.image.load("art-assets/ui/play_button.png")
        self.start_button_image = pygame.transform.scale(self.start_button_image, (250, 100))
        
        self.exit_button_image = pygame.image.load("art-assets/ui/exit_button.png")
        self.exit_button_image = pygame.transform.scale(self.exit_button_image, (250, 100))
        
        self.UI_rects_list = [self.start_button, self.start_button_image, self.exit_button_image, self.exit_button]