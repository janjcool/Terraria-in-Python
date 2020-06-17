import pygame
pygame.init()

class events_dict:
    def __init__(self, events, config_options, UI_rects_list = []):
        handle_events_dict = {}
        no_movement = False
        no_ctrl = False
        no_space = False
        
        for event in events:
            if event.type == pygame.QUIT:
                handle_events_dict['exit'] = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 1 is the left mouse button, 2 is middle, 3 is right.
                    if event.button == 1:
                        if len(UI_rects_list) != 0:
                            if config_options.displayer_choser == "game":
                                # `event.pos` is the mouse position.
                                if UI_rects_list[0].collidepoint(event.pos):
                                    handle_events_dict['test'] = True
                                    
                            if config_options.displayer_choser == "mainMenu":
                                if UI_rects_list[0].collidepoint(event.pos):
                                    handle_events_dict['start button'] = True
                                    
                            if config_options.displayer_choser == "gameMenu":
                                if UI_rects_list[0].collidepoint(event.pos):
                                    handle_events_dict['game button'] = True
                                if UI_rects_list[1].collidepoint(event.pos):
                                    handle_events_dict['mainMenu button'] = True
                            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    handle_events_dict['w_down'] = True
                    no_movement = True
                elif event.key == pygame.K_s:
                    handle_events_dict['s_down'] = True
                    no_movement = True
                elif event.key == pygame.K_a:
                    handle_events_dict['a_down'] = True
                    no_movement = True
                elif event.key == pygame.K_d:
                    handle_events_dict['d_down'] = True
                    no_movement = True

                elif event.key == pygame.K_ESCAPE:
                    handle_events_dict['escape_down'] = True
                
                elif event.key == 1073742048:
                    handle_events_dict['ctrl_down'] = True
                    no_ctrl = True     
                elif event.key == 32:
                    handle_events_dict['space_down'] = True
                    no_space = True
        
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    handle_events_dict['w_down'] = False
                    no_movement = True
                elif event.key == pygame.K_s:
                    handle_events_dict['s_down'] = False
                    no_movement = True
                elif event.key == pygame.K_a:
                    handle_events_dict['a_down'] = False
                    no_movement = True
                elif event.key == pygame.K_d:
                    handle_events_dict['d_down'] = False
                    no_movement = True
                elif event.key == 1073742048:
                    handle_events_dict['ctrl_down'] = False
                    no_ctrl = True
                elif event.key == 32:
                    handle_events_dict['space_down'] = False
                    no_space = True
            
        if no_movement != True:
            handle_events_dict['movement_event_happened'] = False
        if no_ctrl != True:
            handle_events_dict['ctrl_event_happened'] = False
        if no_space != True:
            handle_events_dict['space_event_happened'] = False
        
        self.handle_events_dict = handle_events_dict