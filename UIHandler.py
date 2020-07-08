import main
import miscellaneous as misc

class UIController:
    def __init__(self):
        self.testPressed = None
    
    def game(self, config_dict):
        self.testPressed = config_dict["variables"]["general"]["event_dict"].get('test')
        
        if config_dict["variables"]["general"]["event_dict"].get('exit') == True:
                misc.exit()
        
        if config_dict["variables"]["general"]["event_dict"].get('escape_down') == True:
                misc.menuManager(config_dict, "GameMenu")
    
    def mainMenu(self, config_dict):

        if config_dict["variables"]["general"]["event_dict"].get('start button') == True:
                misc.menuManager(config_dict, "game")
        if config_dict["variables"]["general"]["event_dict"].get('exit') == True:
                misc.exit()
        if config_dict["variables"]["general"]["event_dict"].get('settings') == True:
                print("does nothing")
        
    def gameMenu(self, config_dict):
            
        if config_dict["variables"]["general"]["event_dict"].get('exit') == True:
            misc.exit()
            
        if config_dict["variables"]["general"]["event_dict"].get('MainMenu button') == True:
            misc.menuManager(config_dict, "MainMenu")
        
        if config_dict["variables"]["general"]["event_dict"].get('game button') == True:
            misc.menuManager(config_dict, "game")
        
        if config_dict["variables"]["general"]["event_dict"].get('escape_down') == True:
            misc.menuManager(config_dict, "game")