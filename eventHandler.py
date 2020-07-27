import pygame

class events_dict:
    def __init__(self, UI_config_dict, config_dict):
        self.UI_config_dict = UI_config_dict
        self.config_dict = config_dict
        self.config_dict["variables"]["general"]["event_dict"] = {}
        
        self.main()
        
    def main(self):
        no_movement = False
        no_ctrl = False
        no_space = False
        
        for event in self.config_dict["variables"]["general"]["events"]:
            if event.type == pygame.QUIT:
                self.config_dict["variables"]["general"]["event_dict"]['exit'] = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 1 is left, 2 is middle, 3 is right mouse button.
                    if event.button == 1:
                        if self.config_dict["window"]["display_choser"] == "Game":
                            # `event.pos` is the mouse position.
                            if self.UI_config_dict["Game"]["rects"]["test_rect"]["pygame object"].collidepoint(event.pos):
                                self.config_dict["variables"]["general"]["event_dict"]['test'] = True
                                
                        if self.config_dict["window"]["display_choser"] == "MainMenu":
                            if self.UI_config_dict["MainMenu"]["rects"]["start_button"]["pygame object"].collidepoint(event.pos):
                                self.config_dict["variables"]["general"]["event_dict"]['start button'] = True
                            elif self.UI_config_dict["MainMenu"]["rects"]["exit_button"]["pygame object"].collidepoint(event.pos):
                                self.config_dict["variables"]["general"]["event_dict"]['exit'] = True
                            elif self.UI_config_dict["MainMenu"]["rects"]["settings_button"]["pygame object"].collidepoint(event.pos):
                                self.config_dict["variables"]["general"]["event_dict"]['settings'] = True
                                
                        if self.config_dict["window"]["display_choser"] == "GameMenu":
                            if self.UI_config_dict["GameMenu"]["rects"]["play_button"]["pygame object"].collidepoint(event.pos):
                                self.config_dict["variables"]["general"]["event_dict"]['game button'] = True
                            elif self.UI_config_dict["GameMenu"]["rects"]["exit_button"]["pygame object"].collidepoint(event.pos):
                                self.config_dict["variables"]["general"]["event_dict"]['MainMenu button'] = True
                            
            elif event.type == pygame.KEYDOWN:
                if event.key == self.config_dict["buttons"]["forward_key"]:
                    self.config_dict["variables"]["general"]["event_dict"]['w_down'] = True
                    no_movement = True
                elif event.key == self.config_dict["buttons"]["back_key"]:
                    self.config_dict["variables"]["general"]["event_dict"]['s_down'] = True
                    no_movement = True
                elif event.key == self.config_dict["buttons"]["left_key"]:
                    self.config_dict["variables"]["general"]["event_dict"]['a_down'] = True
                    no_movement = True
                elif event.key == self.config_dict["buttons"]["right_key"]:
                    self.config_dict["variables"]["general"]["event_dict"]['d_down'] = True
                    no_movement = True

                elif event.key == self.config_dict["buttons"]["esc_key"]:
                    self.config_dict["variables"]["general"]["event_dict"]['escape_down'] = True
                
                elif event.key == self.config_dict["buttons"]["crouch_key"]:
                    self.config_dict["variables"]["general"]["event_dict"]['ctrl_down'] = True
                    no_ctrl = True     
                elif event.key == self.config_dict["buttons"]["space_key"]:
                    self.config_dict["variables"]["general"]["event_dict"]['space_down'] = True
                    no_space = True
                elif event.key == self.config_dict["buttons"]["backspace_key"]:
                    self.config_dict["variables"]["general"]["event_dict"]['exit'] = True
        
            elif event.type == pygame.KEYUP:
                if event.key == self.config_dict["buttons"]["forward_key"]:
                    self.config_dict["variables"]["general"]["event_dict"]['w_down'] = False
                    no_movement = True
                elif event.key == self.config_dict["buttons"]["back_key"]:
                    self.config_dict["variables"]["general"]["event_dict"]['s_down'] = False
                    no_movement = True
                elif event.key == self.config_dict["buttons"]["left_key"]:
                    self.config_dict["variables"]["general"]["event_dict"]['a_down'] = False
                    no_movement = True
                elif event.key == self.config_dict["buttons"]["right_key"]:
                    self.config_dict["variables"]["general"]["event_dict"]['d_down'] = False
                    no_movement = True
                elif event.key == self.config_dict["buttons"]["crouch_key"]:
                    self.config_dict["variables"]["general"]["event_dict"]['ctrl_down'] = False
                    no_ctrl = True
                elif event.key == self.config_dict["buttons"]["space_key"]:
                    self.config_dict["variables"]["general"]["event_dict"]['space_down'] = False
                    no_space = True
            
        if no_movement != True:
            self.config_dict["variables"]["general"]["event_dict"]['movement_event_happened'] = False
        if no_ctrl != True:
            self.config_dict["variables"]["general"]["event_dict"]['ctrl_event_happened'] = False
        if no_space != True:
            self.config_dict["variables"]["general"]["event_dict"]['space_event_happened'] = False