import pygame

class renderer:
    def __init__(self, gameDisplay, config_dict, UI_config_dict):
        self.gameDisplay = gameDisplay
        self.config_dict = config_dict
        self.UI_config_dict = UI_config_dict
    
    def MainMenu(self):
        
        if self.config_dict["variables"]["main"]["temp_first_frame_of_new_menu"] == True:
            self.MainMenu_drawer()
            
            pygame.display.update()
    
    def MainMenu_drawer(self):
        
        #background
        self.gameDisplay.blit(self.UI_config_dict["MainMenu"]["images"]["wallpaper"][0], (0, 0))
        
        #debugging
        #pygame.draw.rect(self.gameDisplay, self.config_dict["colors"]["green"], self.UI_config_dict["MainMenu"]["rects"]["start_button"][0]) 
        #pygame.draw.rect(self.gameDisplay, self.config_dict["colors"]["green"], self.UI_config_dict["MainMenu"]["rects"]["exit_button"][0]) 
        #pygame.draw.rect(self.gameDisplay, self.config_dict["colors"]["green"], self.UI_config_dict["MainMenu"]["rects"]["settings_button"][0]) 
        
        #UI
        self.gameDisplay.blit(self.UI_config_dict["MainMenu"]["text"]["start_button"][0], (int(100), int(self.config_dict["window"]["window_height"]/2-300)))
        self.gameDisplay.blit(self.UI_config_dict["MainMenu"]["text"]["settings_button"][0], (int(100), int(self.config_dict["window"]["window_height"]/2-87)))
        self.gameDisplay.blit(self.UI_config_dict["MainMenu"]["text"]["exit_button"][0], (int(100), int(self.config_dict["window"]["window_height"]/2+125)))
    
    def GameMenu(self):
        
        if self.config_dict["variables"]["main"]["temp_first_frame_of_new_menu"] == True:
            self.GameMenu_drawer()
            
            pygame.display.update()
    
    def GameMenu_drawer(self):
        
        #background
        self.gameDisplay.blit(self.UI_config_dict["GameMenu"]["images"]["wallpaper"][0], (0, 0))
        
        #debugging
        #pygame.draw.rect(self.gameDisplay, self.config_dict["colors"]["green"], self.UI_config_dict["GameMenu"]["rects"]["play_button"][0])
        #pygame.draw.rect(self.gameDisplay, self.config_dict["colors"]["green"], self.UI_config_dict["GameMenu"]["rects"]["exit_button"][0])
        #pygame.draw.rect(self.gameDisplay, self.config_dict["colors"]["green"], self.UI_config_dict["GameMenu"]["rects"]["settings_button"][0])
        
        #UI
        self.gameDisplay.blit(self.UI_config_dict["GameMenu"]["text"]["play_button"][0], (int(self.config_dict["window"]["window_width"]/2-125), int(self.config_dict["window"]["window_height"]/2-300)))
        self.gameDisplay.blit(self.UI_config_dict["GameMenu"]["text"]["settings_button"][0], (int(self.config_dict["window"]["window_width"]/2-225), int(self.config_dict["window"]["window_height"]/2-125)))
        self.gameDisplay.blit(self.UI_config_dict["GameMenu"]["text"]["exit_button"][0], (int(self.config_dict["window"]["window_width"]/2-125), int(self.config_dict["window"]["window_height"]/2+25)))
        
    def game(self):
        
        self.game_drawer()
        
        pygame.display.update()

    def game_drawer(self):
         
        #background
        self.gameDisplay.blit(self.UI_config_dict["Game"]["images"]["wallpaper"][0], (0, 0))

        #floor
        pygame.draw.rect(self.gameDisplay, (16, 89, 15), self.UI_config_dict["Game"]["rects"]["grass"][0])
        pygame.draw.rect(self.gameDisplay, (150, 85, 6), self.UI_config_dict["Game"]["rects"]["dirt"][0])

        #for ground
        pygame.draw.rect(self.gameDisplay, self.config_dict["colors"]["green"], self.UI_config_dict["Game"]["rects"]["leafs"][0])
        pygame.draw.rect(self.gameDisplay, (122, 84, 38), self.UI_config_dict["Game"]["rects"]["tree2"][0])
        pygame.draw.rect(self.gameDisplay, self.config_dict["colors"]["green"], self.UI_config_dict["Game"]["rects"]["leafs2"][0])
        pygame.draw.rect(self.gameDisplay, (122, 84, 38), self.UI_config_dict["Game"]["rects"]["tree"][0])
        pygame.draw.rect(self.gameDisplay, (107, 58, 22), self.UI_config_dict["Game"]["rects"]["wall"][0])
        
        #debugging 
        #pygame.draw.rect(self.gameDisplay, self.config_dict["colors"]["green"], self.UI_config_dict["Game"]["rects"]["player"][0])      #enable for player collider
        
        #player
        self.gameDisplay.blit(self.UI_config_dict["Game"]["images"]["player"][0], (int(self.config_dict["window"]["window_width"]/2-32), int(self.config_dict["window"]["window_height"]/2-32)))

        #UI
        pygame.draw.rect(self.gameDisplay, (33, 33, 33), self.UI_config_dict["Game"]["rects"]["test"][0])
        
class FullScreen:
    def __init__(self, config_dict):

        if 0 == config_dict["window"]["display_mode"]:
            print("window")
            
        elif 1 == config_dict["window"]["display_mode"]:
            print("FullScreen does not work yet")
            
        elif 2 == config_dict["window"]["display_mode"]:
            config_dict["window"]["window_height"], config_dict["window"]["window_width"] = config_dict["window"]["display_height"], config_dict["window"]["display_width"]
            print("borderless FullScreen")