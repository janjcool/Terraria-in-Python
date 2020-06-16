from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import sprintLoader, eventHandeler, config, playerController, UIHandeler, worldGenerator
import pygame
import random
pygame.init()
      
def main():
    config_options = config.options()
    config_colors = config.colors()
    config_fonts = config.fonts()
    config_rects = config.rects(config_options.width, config_options.height)

    gameDisplay = pygame.display.set_mode((config_options.width,config_options.height), 0, 32)
    pygame.display.set_caption(config_options.screen_title)
    clock = pygame.time.Clock()

    #don't chance the following variables
    w_down, s_down, a_down, d_down, ctrl_down, space_down = False, False, False, False, False, False
    playerController_variables = [w_down, s_down, a_down, d_down, ctrl_down, space_down]
    deltatime, temp_jump_lenght, player_animation_timer, player_sprite_number = 0, 0, 0, 0
    mainloop, can_jump, temp_player_crouching = True, True, False
    
    while mainloop:
        #get event input from pygame
        events = pygame.event.get()
        mouse = pygame.mouse.get_pos()
        
        #event class
        event_class = eventHandeler.events_dict(events, config_rects.UI_rects_list)
        event_dict = event_class.handle_events_dict
        
        #UI
        UIController = UIHandeler.UIController(event_dict)
        if UIController.exit == True:
            return
        
        testPressed = event_dict.get('test')
        if testPressed:
            testPressed = True
            print("start test button")
            worldGenerator_class = worldGenerator.world("medium", config_options)
            print("end test button")
        
        #playerController class
        playerController_class = playerController.movement(event_dict, playerController_variables, config_rects, config_options, temp_jump_lenght, can_jump, temp_player_crouching)
        temp_jump_lenght, can_jump = playerController_class.temp_jump_lenght, playerController_class.can_jump
        playerController_variables = playerController_class.playerController_variables
        temp_player_crouching = playerController_class.temp_player_crouching
        
        #player animation class    
        if player_animation_timer == config_options.player_animation_speed:
            player_animation_timer = 0
        else:
            player_animation_timer += 1
            
        player_animation_chooser_class = sprintLoader.player_animation_chooser(player_animation_timer, config_options.character_bigness, playerController_class.player_crouching, playerController_class.player_running_to_left, playerController_class.jumping, playerController_class.gravity_movement_allow, playerController_class.player_running_to_right, player_sprite_number)
        player_sprite = player_animation_chooser_class.player_sprite
        player_sprite_number = player_animation_chooser_class.player_sprite_number
        
        #--------------------------------------#
        
        #background
        gameDisplay.fill(config_colors.GRAY)
        gameDisplay.blit(config_rects.background_list[0], (0, 0))

        #floor
        pygame.draw.rect(gameDisplay, (16, 89, 15), config_rects.solid_moverect_list[0])
        pygame.draw.rect(gameDisplay, (150, 85, 6), config_rects.solid_moverect_list[2])

        #for ground
        pygame.draw.rect(gameDisplay, config_colors.GREEN, config_rects.unsolid_moverect_list[1])
        pygame.draw.rect(gameDisplay, (122, 84, 38), config_rects.unsolid_moverect_list[2])
        pygame.draw.rect(gameDisplay, config_colors.GREEN, config_rects.unsolid_moverect_list[3])
        pygame.draw.rect(gameDisplay, (122, 84, 38), config_rects.unsolid_moverect_list[0])
        pygame.draw.rect(gameDisplay, (107, 58, 22), config_rects.solid_moverect_list[1])
        
        #debugging level
        pygame.draw.rect(gameDisplay, config_colors.GREEN, config_rects.player_rect)      #enable for player collider
        
        #player
        gameDisplay.blit(player_sprite, (int(config_options.width/2-32), int(config_options.height/2-32)))

        #UI level
        pygame.draw.rect(gameDisplay, (33, 33, 33), config_rects.UI_rects_list[1])
        pygame.draw.rect(gameDisplay, (23, 23, 23), config_rects.UI_rects_list[0])
        gameDisplay.blit(config_fonts.font30.render('quit', True, config_colors.WHITE), (config_options.width-60, 10))

        pygame.display.update()
        deltatime = clock.tick(config_options.fps) #delta time is milliseconds since the previous call

if __name__ == '__main__':
    main()
    
pygame.quit()
quit()
