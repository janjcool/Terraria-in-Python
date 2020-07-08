from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

import sprintLoader
import eventHandler
import config
import playerController
import UIHandler
import worldGenerator
import renderer
import entity
import miscellaneous as misc

pygame.init()

def main():
    config_dict = misc.config()
    display_info = pygame.display.Info()
    entity_variables = entity.Variables(display_info)
    renderer.FullScreen(config_dict, entity_variables)
    config_rects_game = config.rects_game(config_dict)
    config_rects_mainMenu = config.rects_mainMenu(config_dict)
    config_rects_gameMenu = config.rects_gameMenu(config_dict)
    config_rects_worldGen_menu = config.rects_worldGen_menu(config_dict)
    UIcontrollor_class = UIHandler.UIController()

    gameDisplay = pygame.display.set_mode((config_dict["window"]["window_width"], config_dict["window"]["window_height"]), flags=pygame.NOFRAME, depth=0, display=config_dict["window"]["display"]) #(size), flags, depth, display
    pygame.display.set_caption(config_dict["window"]["screen_title"])
    clock = pygame.time.Clock()

    while entity_variables.mainloop:
        #get event input from pygame
        entity_variables.events = pygame.event.get()

        #=======================================================================================================================================================================================#
        if config_dict["window"]["display_choser"] == "MainMenu":

            #get if this is the first frame in temp_first_frame_of_new_menu
            entity_variables.temp_first_frame_of_new_menu = entity_variables.first_frame_of_new_menu
            entity_variables.first_frame_of_new_menu = False

            #event class
            eventHandler.events_dict(entity_variables, config_rects_mainMenu, config_dict)

            #UI
            UIcontrollor_class.mainMenu(config_dict, entity_variables)

            #render
            renderer.MainMenu(gameDisplay, config_rects_mainMenu, config_dict, entity_variables)

        #=======================================================================================================================================================================================#
        elif config_dict["window"]["display_choser"] == "game":

            #get if this is the first frame in temp_first_frame_of_new_menu
            entity_variables.temp_first_frame_of_new_menu = entity_variables.first_frame_of_new_menu
            entity_variables.first_frame_of_new_menu = False

            #event class
            eventHandler.events_dict(entity_variables, config_rects_game, config_dict)

            #UI
            UIcontrollor_class.game(config_dict, entity_variables)

            if UIcontrollor_class.testPressed:
                print("start test button")

                #worldGenerator.World(config_dict, entity_variables)
                print("does nothing right now")

                print("end test button")

            #playerController class
            playerController_class = playerController.movement(entity_variables, config_rects_game, config_dict)

            #player animation class
            player_animation_chooser_class = sprintLoader.player_animation_chooser(playerController_class, entity_variables, config_dict)
            config_rects_game.player_sprite = player_animation_chooser_class.player_sprite

            #render
            renderer.game(gameDisplay, config_rects_game, config_dict, entity_variables)

        #=======================================================================================================================================================================================#
        elif config_dict["window"]["display_choser"] == "GameMenu":

            #get if this is the first frame in temp_first_frame_of_new_menu
            entity_variables.temp_first_frame_of_new_menu = entity_variables.first_frame_of_new_menu
            entity_variables.first_frame_of_new_menu = False

            #event class
            eventHandler.events_dict(entity_variables, config_rects_gameMenu, config_dict)

            #UI
            UIcontrollor_class.gameMenu(config_dict, entity_variables)

            #render
            renderer.GameMenu(gameDisplay, config_rects_gameMenu, config_dict, entity_variables)

        #=======================================================================================================================================================================================#
        else:
            print('config_dict["window"]["display_choser"] type not supported -->' + str(config_dict["window"]["display_choser"]) + '<-- types that are supported: game, MainMenu')


        entity_variables.deltatime = clock.tick(config_dict["window"]["fps"]) #delta time is x milliseconds since the previous call

if __name__ == '__main__':
    main()
