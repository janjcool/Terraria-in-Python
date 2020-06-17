class UIController:
    def __init__(self, config_options, event_dict):
        self.event_dict = event_dict
        self.config_options = config_options
        
        if self.config_options.displayer_choser == "game":
            self.game()
        elif self.config_options.displayer_choser == "mainMenu":
            self.mainMenu()
        elif self.config_options.displayer_choser == "gameMenu":
            self.gameMenu()
    
    def game(self):
        self.exit = self.event_dict.get('exit')
        self.testPressed = self.event_dict.get('test')
        self.gameMenu_button_pressed = self.event_dict.get('escape_down')
    
    def mainMenu(self):
        self.exit = self.event_dict.get('exit')
        self.testPressed = self.event_dict.get('test')
        self.start_button_pressed = self.event_dict.get('start button')
        
    def gameMenu(self):
        self.exit = self.event_dict.get('exit')
        self.mainMenu_button_pressed = self.event_dict.get('mainMenu button')
        if self.event_dict.get('game button') == True or self.event_dict.get('escape_down') == True:
            self.game_button_pressed = True
        else:
            self.game_button_pressed = False