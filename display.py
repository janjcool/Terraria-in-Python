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
                    if self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y][1] == 1:
                        self.gameDisplay.blit(self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y][0],
                                              (self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y][4], 
                                               self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y][5]))
                        self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y][1] = 0
            elif x == "rects":
                for y in self.UI_config_dict[self.config_dict["window"]["display_choser"]][x]:
                    if self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y][1] == 1:
                        print(self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y][3])
                        pygame.draw.rect(self.gameDisplay,
                                         self.config_dict["colors"][self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y][3]],
                                         self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y][0])
                        self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y][1] = 0
            elif x == "text":
                for y in self.UI_config_dict[self.config_dict["window"]["display_choser"]][x]:
                    if self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y][1] == 1:
                        self.gameDisplay.blit(self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y][0],
                                              (self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y][7], 
                                               self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y][8]))
                        self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y][1] = 0
            
            if not x == "options":
                if self.UI_config_dict[self.config_dict["window"]["display_choser"]]["options"]["firstframe"] == True:
                    for y in self.UI_config_dict[self.config_dict["window"]["display_choser"]][x]:
                        self.UI_config_dict[self.config_dict["window"]["display_choser"]][x][y][1] = 0
    
    def UI_redraw(self, window_type = None):
        if window_type is None:
            window_type = self.config_dict["window"]["display_choser"]
        
        for x in self.UI_config_dict[window_type]:
            for y in self.UI_config_dict[window_type][x]:
                self.UI_config_dict[window_type][x][y][1] = 1
    
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