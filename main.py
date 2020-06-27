from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import sprintLoader, eventHandeler, config, playerController, UIHandeler, worldGenerator, renderer, entity
import pygame
pygame.init()

def exit():    
    pygame.quit()
    quit()

def main():
    config_options = config.options()
    config_colors = config.colors()
    config_fonts = config.fonts()
    config_rects_game = config.rects_game(config_options.width, config_options.height)
    config_rects_mainMenu = config.rects_mainMenu(config_options.width, config_options.height)
    config_rects_gameMenu = config.rects_gameMenu(config_options.width, config_options.height)
    variables_class = entity.variables()

    gameDisplay = pygame.display.set_mode((config_options.width,config_options.height), 0, 32)
    pygame.display.set_caption(config_options.screen_title)
    clock = pygame.time.Clock()

    #don't chance the following variables
    playerController_class_variables = [0, True, [False, False, False, False, False, False], True]
    deltatime, player_animation_timer, player_sprite_number = 0, 0, 0
    mainloop = True
    
    while mainloop:
        #get event input from pygame
        events = pygame.event.get()
        mouse = pygame.mouse.get_pos()
        
        #=======================================================================================================================================================================================#
        if config_options.displayer_choser == "mainMenu": 
            
            #event class
            event_class_mainMenu = eventHandeler.events_dict(events, config_options, config_rects_mainMenu.UI_rects_list)
            event_dict_mainMenu = event_class_mainMenu.handle_events_dict
            
            #UI
            UIController = UIHandeler.UIController(config_options, event_dict_mainMenu)
            
            if UIController.exit == True:
                exit()
            
            if UIController.testPressed:
                print("doet niks")
            
            if UIController.start_button_pressed == True:
                print("go to game")
                config_options.displayer_choser = "game"
                
            #render
            renderer.mainMenu(gameDisplay, config_rects_mainMenu, config_colors, config_options, config_fonts)
            
        #=======================================================================================================================================================================================#
        elif config_options.displayer_choser == "game":
            
            #event class
            event_class_game = eventHandeler.events_dict(events, config_options, config_rects_game.UI_rects_list)
            event_dict_game = event_class_game.handle_events_dict
            
            #UI
            UIController = UIHandeler.UIController(config_options, event_dict_game)
            if UIController.exit == True:
                exit()
                
            if UIController.testPressed:
                print("start test button")
                worldGenerator_class = worldGenerator.world(config_options, variables_class)
                print("end test button")
            
            if UIController.gameMenu_button_pressed == True:
                print("go to gameMenu")
                config_options.displayer_choser = "gameMenu"
            
            #playerController class
            playerController_class = playerController.movement(event_dict_game, playerController_class_variables[2], config_rects_game, config_options, playerController_class_variables[0], playerController_class_variables[1], playerController_class_variables[3])
            playerController_class_variables = [playerController_class.temp_jump_lenght, playerController_class.can_jump, playerController_class.playerController_variables, playerController_class.temp_player_crouching] #get info from when je call the class to the next
            
            temp_jump_lenght = playerController_class.temp_jump_lenght
            can_jump = playerController_class.can_jump
            playerController_variables = playerController_class.playerController_variables
            temp_player_crouching = playerController_class.temp_player_crouching
            
            #player animation class    
            if player_animation_timer == config_options.player_animation_speed:
                player_animation_timer = 0
            else:
                player_animation_timer += 1
                
            player_animation_chooser_class = sprintLoader.player_animation_chooser(player_animation_timer, config_options.character_bigness, playerController_class.player_crouching, playerController_class.player_running_to_left, playerController_class.jumping, playerController_class.gravity_movement_allow, playerController_class.player_running_to_right, player_sprite_number)
            config_rects_game.player_sprite = player_animation_chooser_class.player_sprite
            player_sprite_number = player_animation_chooser_class.player_sprite_number
            
            #render
            renderer.game(gameDisplay, config_rects_game, config_colors, config_options, config_fonts)
        
        #=======================================================================================================================================================================================#
        elif config_options.displayer_choser == "gameMenu": 
            
            #event class
            event_class_gameMenu = eventHandeler.events_dict(events, config_options, config_rects_gameMenu.UI_rects_list)
            event_dict_gameMenu = event_class_gameMenu.handle_events_dict
            
            #UI
            UIController = UIHandeler.UIController(config_options, event_dict_gameMenu)
            
            if UIController.exit == True:
                exit()
            
            if UIController.mainMenu_button_pressed == True:
                print("go to mainMenu")
                config_options.displayer_choser = "mainMenu"
            
            if UIController.game_button_pressed == True:
                print("go to game")
                config_options.displayer_choser = "game"
                
            #render
            renderer.gameMenu(gameDisplay, config_rects_gameMenu, config_colors, config_options, config_fonts)
            
        #=======================================================================================================================================================================================#
        else:
            print("config_options.displayer_choser type not supported -->" + str(config_options.displayer_choser) + "<-- types that are suported: game, mainMenu")

        pygame.display.update()
        deltatime = clock.tick(config_options.fps) #delta time is x milliseconds since the previous call

if __name__ == '__main__':
    main()
