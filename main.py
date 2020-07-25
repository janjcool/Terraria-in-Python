from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

import sprintLoader
import eventHandler
import config
import playerController
import UIHandler
import worldGenerator
import display
import miscellaneous as misc
import fileReader

pygame.init()

def main():
    display_info = pygame.display.Info()
    config_dict = fileReader.config(display_info)
    display.FullScreen(config_dict)
    UI_config_dict = fileReader.UI_config_file(config_dict)
    #config_rects_game = config.rects_game(config_dict)
    #config_rects_mainMenu = config.rects_mainMenu(config_dict)
    #config_rects_gameMenu = config.rects_gameMenu(config_dict)
    #config_rects_worldGen_menu = config.rects_worldGen_menu(config_dict)
    ButtonController_class = UIHandler.ButtonController()
    world = {}

    gameDisplay = pygame.display.set_mode((config_dict["window"]["window_width"], config_dict["window"]["window_height"]), flags=pygame.NOFRAME, depth=0, display=config_dict["window"]["display"]) #(size), flags, depth, display
    pygame.display.set_caption(config_dict["window"]["screen_title"])
    renderer_class = display.renderer(gameDisplay, config_dict, UI_config_dict)
    clock = pygame.time.Clock()

    while config_dict["variables"]["main"]["mainloop"]:
        #get event input from pygame
        config_dict["variables"]["general"]["events"] = pygame.event.get()

        #=======================================================================================================================================================================================#
        if config_dict["window"]["display_choser"] == "MainMenu":

            #get if this is the first frame in temp_first_frame_of_new_menu
            config_dict["variables"]["main"]["temp_first_frame_of_new_menu"] = config_dict["variables"]["main"]["first_frame_of_new_menu"]
            config_dict["variables"]["main"]["first_frame_of_new_menu"] = False
                

            #event class
            eventHandler.events_dict(UI_config_dict, config_dict)

            #UI
            ButtonController_class.mainMenu(config_dict)

            #render
            renderer_class.MainMenu()

        #=======================================================================================================================================================================================#
        elif config_dict["window"]["display_choser"] == "Game":

            #get if this is the first frame in temp_first_frame_of_new_menu
            config_dict["variables"]["main"]["temp_first_frame_of_new_menu"] = config_dict["variables"]["main"]["first_frame_of_new_menu"]
            config_dict["variables"]["main"]["first_frame_of_new_menu"] = False

            #event class
            eventHandler.events_dict(UI_config_dict, config_dict)

            #UI
            ButtonController_class.game(config_dict)

            if ButtonController_class.testPressed:
                print("start test button")

                worldGenerator.World(config_dict, world)
                #print("does nothing right now")

                print("end test button")

            #playerController class
            playerController_class = playerController.movement(UI_config_dict, config_dict)

            #player animation class
            player_animation_chooser_class = sprintLoader.player_animation_chooser(playerController_class, config_dict)
            UI_config_dict["Game"]["images"]["player"][0] = player_animation_chooser_class.player_sprite

            #render
            renderer_class.Game()

        #=======================================================================================================================================================================================#
        elif config_dict["window"]["display_choser"] == "GameMenu":

            #get if this is the first frame in temp_first_frame_of_new_menu
            config_dict["variables"]["main"]["temp_first_frame_of_new_menu"] = config_dict["variables"]["main"]["first_frame_of_new_menu"]
            config_dict["variables"]["main"]["first_frame_of_new_menu"] = False

            #event class
            eventHandler.events_dict(UI_config_dict, config_dict)

            #UI
            ButtonController_class.gameMenu(config_dict)

            #render
            renderer_class.GameMenu()

        #=======================================================================================================================================================================================#
        else:
            print('config_dict["window"]["display_choser"] string not supported: ' + str(config_dict["window"]["display_choser"]) + ' (types that are supported: Game, MainMenu, GameMenu)')
            eventHandler.events_dict(UI_config_dict, config_dict)


        config_dict["variables"]["main"]["deltatime"] = clock.tick(config_dict["window"]["fps"]) #delta time is x milliseconds since the previous call

if __name__ == '__main__':
    main()
