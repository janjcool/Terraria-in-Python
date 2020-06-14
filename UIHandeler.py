class UIController:
    def __init__(self, event_dict):
        
        self.exit = event_dict.get('exit')
        self.testPressed = event_dict.get('test')
        
        if self.exit:
            self.exit = True
        
        if self.testPressed:
            self.testPressed = True
            print("test button")