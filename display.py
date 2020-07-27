import pygame

class renderer:
    def __init__(self, gameDisplay, config_dict, UI_config_dict):
        self.gameDisplay = gameDisplay
        self.config_dict = config_dict
        self.UI_config_dict = UI_config_dict
        
    
    def UI_drawer(self):
        for x in self.UI_config_dict[self.config_dict["window"]["display_choser"]]:
            if x == "images":
                for y in self.UI_config_dict[self.config_dict["window"]["display_choser"]][x]:
                    if self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y]["type of render"] == 1:
                        self.gameDisplay.blit(self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y]["pygame object"],
                                              (self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y]["x"], 
                                               self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y]["y"]))
                        self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y]["type of render"] = 0
            elif x == "rects":
                for y in self.UI_config_dict[self.config_dict["window"]["display_choser"]][x]:
                    if self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y]["type of render"] == 1:
                        pygame.draw.rect(self.gameDisplay,
                                         self.config_dict["colors"][self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y]["color"]],
                                         self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y]["pygame object"])
                        self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y]["type of render"] = 0
            elif x == "text":
                for y in self.UI_config_dict[self.config_dict["window"]["display_choser"]][x]:
                    if self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y]["type of render"] == 1:
                        self.gameDisplay.blit(self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y]["pygame object"],
                                              (self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y]["x"], 
                                               self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y]["y"]))
                        self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y]["type of render"] = 0
            
            if self.config_dict["variables"]["main"]["firstframe"] == True:
                for y in self.UI_config_dict[self.config_dict["window"]["display_choser"]][x]:
                    self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y]["type of render"] = 0
                self.config_dict["variables"]["main"]["firstframe"] = False
    
    def reset_render_type(self, window_type = None):
        if window_type is None:
            window_type = self.config_dict["window"]["display_choser"]
        
        for x in self.UI_config_dict[window_type]:
            for y in self.UI_config_dict[window_type][x]:
                self.UI_config_dict[window_type][x][y]["type of render"] = self.UI_config_dict[window_type][x][y]["type of render original"]
    
    def MainMenu(self):
        
        self.UI_drawer()
        
        pygame.display.update()
    
    def Game(self):
        
        self.UI_drawer()
        
        pygame.display.update()
    
    def GameMenu(self):
        
        self.UI_drawer()
        
        pygame.display.update()
        
class FullScreen:
    def __init__(self, config_dict):

        if 0 == config_dict["window"]["display_mode"]:
            print("window")
            
        elif 1 == config_dict["window"]["display_mode"]:
            print("FullScreen does not work yet")
            
        elif 2 == config_dict["window"]["display_mode"]:
            config_dict["window"]["window_height"], config_dict["window"]["window_width"] = config_dict["window"]["display_height"], config_dict["window"]["display_width"]
            print("borderless FullScreen")