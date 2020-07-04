from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import sprintLoader, eventHandeler, config, playerController, UIHandeler, worldGenerator, renderer, entity
import pygame
pygame.init()

def main():
    display_info = pygame.display.Info()
    config_options = config.options()
    entity_variables = entity.variables(display_info)
    fullscreen_class = renderer.fullscreen(config_options, entity_variables)
    config_colors = config.colors()
    config_fonts = config.fonts(config_options)
    config_rects_game = config.rects_game(config_options)
    config_rects_mainMenu = config.rects_mainMenu(config_options, config_colors, config_fonts)
    config_rects_gameMenu = config.rects_gameMenu(config_options, config_colors, config_fonts)
    config_rects_worldGen_menu = config.rects_worldGen_menu(config_options)
    UIcontrolor_class = UIHandeler.UIController()
    
    button_class = config.buttons()

    gameDisplay = pygame.display.set_mode((config_options.width, config_options.height), flags=pygame.NOFRAME, depth=0, display=config_options.display) #(size), flags, depth, display
    pygame.display.set_caption(config_options.screen_title)
    clock = pygame.time.Clock()
    
    while entity_variables.mainloop:
        #get event input from pygame
        entity_variables.events = pygame.event.get()
        
        #=======================================================================================================================================================================================#
        if config_options.displayer_choser == "mainMenu": 
            
            #get if this is the first frame in temp_first_frame_of_new_menu
            entity_variables.temp_first_frame_of_new_menu = entity_variables.first_frame_of_new_menu
            entity_variables.first_frame_of_new_menu = False
            
            #event class
            event_class_mainMenu = eventHandeler.events_dict(entity_variables, config_options, config_rects_mainMenu, button_class)
            
            #UI
            UIcontrolor_class.mainMenu(config_options, entity_variables)
                
            #render
            renderer.mainMenu(gameDisplay, config_rects_mainMenu, config_colors, config_options, config_fonts, entity_variables)
            
        #=======================================================================================================================================================================================#
        elif config_options.displayer_choser == "game":
            
            #get if this is the first frame in temp_first_frame_of_new_menu
            entity_variables.temp_first_frame_of_new_menu = entity_variables.first_frame_of_new_menu
            entity_variables.first_frame_of_new_menu = False
            
            #event class
            event_class_game = eventHandeler.events_dict(entity_variables, config_options, config_rects_game, button_class)
            
            #UI
            UIcontrolor_class.game(config_options, entity_variables)
                
            if UIcontrolor_class.testPressed:
                print("start test button")
                
                #worldGenerator_class = worldGenerator.world(config_options, entity_variables)
                print("does nothing right now")
                
                print("end test button")
            
            #playerController class
            playerController_class = playerController.movement(entity_variables, config_rects_game, config_options)
            
            #player animation class    
            player_animation_chooser_class = sprintLoader.player_animation_chooser(playerController_class, entity_variables, config_options)
            config_rects_game.player_sprite = player_animation_chooser_class.player_sprite
            
            #render
            renderer.game(gameDisplay, config_rects_game, config_colors, config_options, config_fonts, entity_variables)
            
        #=======================================================================================================================================================================================#
        elif config_options.displayer_choser == "gameMenu": 
            
            #get if this is the first frame in temp_first_frame_of_new_menu
            entity_variables.temp_first_frame_of_new_menu = entity_variables.first_frame_of_new_menu
            entity_variables.first_frame_of_new_menu = False
            
            #event class
            event_class_gameMenu = eventHandeler.events_dict(entity_variables, config_options, config_rects_gameMenu, button_class)
            
            #UI
            UIcontrolor_class.gameMenu(config_options, entity_variables)
                
            #render
            renderer.gameMenu(gameDisplay, config_rects_gameMenu, config_colors, config_options, config_fonts, entity_variables)
            
        #=======================================================================================================================================================================================#
        else:
            print("config_options.displayer_choser type not supported -->" + str(config_options.displayer_choser) + "<-- types that are suported: game, mainMenu")


        entity_variables.deltatime = clock.tick(config_options.fps) #delta time is x milliseconds since the previous call

if __name__ == '__main__':
    main()
