import main
import miscellaneous as misc

class UIController:
    def __init__(self):
        self.testPressed = None
    
    def game(self, config_options, entity_variables):
        self.testPressed = entity_variables.event_dict.get('test')
        
        if entity_variables.event_dict.get('exit') == True:
                misc.exit()
        
        if entity_variables.event_dict.get('escape_down') == True:
                misc.menuManager(config_options, entity_variables, "gameMenu")
    
    def mainMenu(self, config_options, entity_variables):

        if entity_variables.event_dict.get('start button') == True:
                misc.menuManager(config_options, entity_variables, "game")
        if entity_variables.event_dict.get('exit') == True:
                misc.exit()
        if entity_variables.event_dict.get('settings') == True:
                print("doet niks")
        
    def gameMenu(self, config_options, entity_variables):
            
        if entity_variables.event_dict.get('exit') == True:
            misc.exit()
            
        if entity_variables.event_dict.get('mainMenu button') == True:
            misc.menuManager(config_options, entity_variables, "mainMenu")
        
        if entity_variables.event_dict.get('game button') == True:
            misc.menuManager(config_options, entity_variables, "game")
        
        if entity_variables.event_dict.get('escape_down') == True:
            misc.menuManager(config_options, entity_variables, "game")