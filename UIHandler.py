import main
import miscellaneous as misc

class UIController:
    def __init__(self):
        self.testPressed = None
    
    def game(self, config_dict, entity_variables):
        self.testPressed = entity_variables.event_dict.get('test')
        
        if entity_variables.event_dict.get('exit') == True:
                misc.exit()
        
        if entity_variables.event_dict.get('escape_down') == True:
                misc.menuManager(config_dict, entity_variables, "GameMenu")
    
    def mainMenu(self, config_dict, entity_variables):

        if entity_variables.event_dict.get('start button') == True:
                misc.menuManager(config_dict, entity_variables, "game")
        if entity_variables.event_dict.get('exit') == True:
                misc.exit()
        if entity_variables.event_dict.get('settings') == True:
                print("does nothing")
        
    def gameMenu(self, config_dict, entity_variables):
            
        if entity_variables.event_dict.get('exit') == True:
            misc.exit()
            
        if entity_variables.event_dict.get('MainMenu button') == True:
            misc.menuManager(config_dict, entity_variables, "MainMenu")
        
        if entity_variables.event_dict.get('game button') == True:
            misc.menuManager(config_dict, entity_variables, "game")
        
        if entity_variables.event_dict.get('escape_down') == True:
            misc.menuManager(config_dict, entity_variables, "game")