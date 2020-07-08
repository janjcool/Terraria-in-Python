import pygame

class MainMenu:
    def __init__(self, gameDisplay, config_rects_mainMenu, config_dict):
        self.gameDisplay = gameDisplay
        self.config_dict, self.config_rects_mainMenu = config_dict, config_rects_mainMenu
        
        if config_dict["variables"]["main"]["temp_first_frame_of_new_menu"] == True:
            self.drawer()
            
            pygame.display.update()
    
    def drawer(self):
        
        #background
        self.gameDisplay.blit(self.config_rects_mainMenu.wallpaper, (0, 0))
        
        #debugging
        #pygame.draw.rect(self.gameDisplay, self.config_dict["colors"]["green"], self.config_rects_mainMenu.start_button) 
        #pygame.draw.rect(self.gameDisplay, self.config_dict["colors"]["green"], self.config_rects_mainMenu.exit_button) 
        #pygame.draw.rect(self.gameDisplay, self.config_dict["colors"]["green"], self.config_rects_mainMenu.settings_button) 
        
        #UI
        self.gameDisplay.blit(self.config_rects_mainMenu.start_button_text, (int(100), int(self.config_dict["window"]["window_height"]/2-300)))
        self.gameDisplay.blit(self.config_rects_mainMenu.settings_button_text, (int(100), int(self.config_dict["window"]["window_height"]/2-87)))
        self.gameDisplay.blit(self.config_rects_mainMenu.exit_button_text, (int(100), int(self.config_dict["window"]["window_height"]/2+125)))

class GameMenu:
    def __init__(self, gameDisplay, config_rects_gameMenu, config_dict):
        self.gameDisplay = gameDisplay
        self.config_dict, self.config_rects_gameMenu = config_dict, config_rects_gameMenu
        
        if config_dict["variables"]["main"]["temp_first_frame_of_new_menu"] == True:
            self.drawer()
            
            pygame.display.update()
    
    def drawer(self):
        
        #background
        self.gameDisplay.blit(self.config_rects_gameMenu.wallpaper, (0, 0))
        
        #debugging
        #pygame.draw.rect(self.gameDisplay, self.config_dict["colors"]["green"], self.config_rects_gameMenu.game_button)
        #pygame.draw.rect(self.gameDisplay, self.config_dict["colors"]["green"], self.config_rects_gameMenu.mainMenu_button)
        #pygame.draw.rect(self.gameDisplay, self.config_dict["colors"]["green"], self.config_rects_gameMenu.settings_button)
        
        #UI
        self.gameDisplay.blit(self.config_rects_gameMenu.play_button_text, (int(self.config_dict["window"]["window_width"]/2-125), int(self.config_dict["window"]["window_height"]/2-300)))
        self.gameDisplay.blit(self.config_rects_gameMenu.settings_button_text, (int(self.config_dict["window"]["window_width"]/2-225), int(self.config_dict["window"]["window_height"]/2-125)))
        self.gameDisplay.blit(self.config_rects_gameMenu.mainMenu_button_text, (int(self.config_dict["window"]["window_width"]/2-125), int(self.config_dict["window"]["window_height"]/2+25)))

class game:
    def __init__(self, gameDisplay, config_rects_game, config_dict):
        self.gameDisplay = gameDisplay
        self.config_dict, self.config_rects_game = config_dict, config_rects_game
        
        self.drawer()
        
        pygame.display.update()
    
    def drawer(self):
         
        #background
        self.gameDisplay.blit(self.config_rects_game.wallpaper, (0, 0))

        #floor
        pygame.draw.rect(self.gameDisplay, (16, 89, 15), self.config_rects_game.grass_rect)
        pygame.draw.rect(self.gameDisplay, (150, 85, 6), self.config_rects_game.dirt_rect)

        #for ground
        pygame.draw.rect(self.gameDisplay, self.config_dict["colors"]["green"], self.config_rects_game.leafs_rect)
        pygame.draw.rect(self.gameDisplay, (122, 84, 38), self.config_rects_game.tree2_rect)
        pygame.draw.rect(self.gameDisplay, self.config_dict["colors"]["green"], self.config_rects_game.leafs2_rect)
        pygame.draw.rect(self.gameDisplay, (122, 84, 38), self.config_rects_game.tree_rect)
        pygame.draw.rect(self.gameDisplay, (107, 58, 22), self.config_rects_game.wall_rect)
        
        #debugging 
        #pygame.draw.rect(self.gameDisplay, self.config_dict["colors"]["green"], self.config_rects_game.player_rect)      #enable for player collider
        
        #player
        self.gameDisplay.blit(self.config_rects_game.player_sprite, (int(self.config_dict["window"]["window_width"]/2-32), int(self.config_dict["window"]["window_height"]/2-32)))

        #UI
        pygame.draw.rect(self.gameDisplay, (33, 33, 33), self.config_rects_game.test_rect)
        
class FullScreen:
    def __init__(self, config_dict):

        if 0 == config_dict["window"]["display_mode"]:
            print("window")
            
        elif 1 == config_dict["window"]["display_mode"]:
            print("FullScreen does not work yet")
            
        elif 2 == config_dict["window"]["display_mode"]:
            config_dict["window"]["window_height"], config_dict["window"]["window_width"] = config_dict["window"]["display_height"], config_dict["window"]["display_width"]
            print("borderless FullScreen")