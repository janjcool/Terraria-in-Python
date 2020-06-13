from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from opensimplex import OpenSimplex
import pygame
import random
import sprintLoader
import events_handeler
import config
pygame.init()
      
def main():
    config_options = config.options()
    config_colors = config.colors()
    config_fonts = config.fonts()
    config_rects = config.rects(config_options.width, config_options.height)

    gravity = 5 #how many pixels you go down
    player_animation_speed = 15 #after how many frames the next idle animation comes
    jump_lenght = 20 #how many frames you jump
    jump_speed = 30 #pixel you jump per second

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (30, 30, 30)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    gameDisplay = pygame.display.set_mode((config_options.width,config_options.height), 0, 32)
    pygame.display.set_caption('a project I probably won`t finish')
    font20 = pygame.font.SysFont('Arial', 20)
    font30 = pygame.font.SysFont('Arial', 30)
    font40 = pygame.font.SysFont('Arial', 40)

    #seed of opensimplex noise (like perlin noise)
    tmp = OpenSimplex(seed=1)
    clock = pygame.time.Clock()
    
    wallpaper = pygame.image.load("background.png")
    wallpaper = pygame.transform.scale(wallpaper, (config_options.width, config_options.height))

    quit_rect = pygame.Rect(config_options.width-80, 0, 80, 60)
    test_rect = pygame.Rect(0, 0, 100, 100)
    grass_rect = pygame.Rect(0, config_options.height-50, config_options.width, 100)
    tree_rect = pygame.Rect(80, config_options.height-90, 20, 60)
    leafs_rect = pygame.Rect(70, config_options.height-130, 40, 40)
    player_rect = pygame.Rect(int(config_options.width/2+7), int(config_options.height/2-15), 42, 72)
    wall_rect = pygame.Rect(config_options.width-50, config_options.height-100, 10, 50)
    tree2_rect = pygame.Rect(80+200, config_options.height-90, 20, 60)
    leafs2_rect = pygame.Rect(70+200, config_options.height-130, 40, 40)
    dirt_rect = pygame.Rect(-1000, config_options.height+50, config_options.width+1000, 300)

    unsolid_moverect_list = [tree_rect, leafs_rect, tree2_rect, leafs2_rect]
    solid_moverect_list = [grass_rect, wall_rect, dirt_rect]
    UI_rects = [quit_rect, test_rect]
    background_list = [wallpaper]

    w_down, s_down, a_down, d_down, ctrl_down, space_down = False, False, False, False, False, False
    deltatime = 0 #don't chanche this
    mainloop = True
    player_on_the_ground = False
    world_seed = random.randint(1, 9999999999)
    player_x = 0
    player_y = 0
    first_frame = True
    temp_jump_lenght = 0
    can_jump = True
    player_animation_timer = 0
    player_sprite_number = 0
    
    while mainloop:
        events = pygame.event.get()
        mouse = pygame.mouse.get_pos()
        event_class = events_handeler.events_dict(events, UI_rects)
        event_dict = event_class.handle_events_dict
        player_x = 0
        player_y = 0
        temp_jump = 0
        one_pixel_movement_allow, jump_movement_allow, gravity_movement_allow = True, True, True
        player_on_the_ground, jumping, in_block, player_movement_allow = False, False, False, True
        player_running_to_right, player_running_to_left, player_crouching = False, False, False
        middle_player_jump = False

        exit = event_dict.get('exit')
        movement_event_happened = event_dict.get('movement_event_happened')
        ctrl_event_happened = event_dict.get('ctrl_event_happened')
        space_event_happened = event_dict.get('space_event_happened')
        testPressed = event_dict.get('test')
        
        if movement_event_happened != False:
            w_down, s_down, a_down, d_down = event_dict.get('w_down'), event_dict.get('s_down'), event_dict.get('a_down'), event_dict.get('d_down')
        if ctrl_event_happened != False:
            ctrl_down = event_dict.get('ctrl_down')
        if space_event_happened != False:
            space_down = event_dict.get('space_down')

        if exit:
            return True
        
        if testPressed:
            print("test button")

        if w_down:
            player_y -= 0 * config_options.player_speed # w is disabeld
        elif s_down:
            player_y += 0 * config_options.player_speed # s is disabeld
        elif a_down:
            if ctrl_down:
                player_x -= 1 * config_options.player_crouching_speed
            else:
                player_x -= 1 * config_options.player_speed
        elif d_down:
            if ctrl_down:
                player_x += 1 * config_options.player_crouching_speed
            else:
                player_x += 1 * config_options.player_speed
            
        if ctrl_down:
            player_rect.height -= 32
            player_rect.top += 32
            player_crouching = True
        
        #look if player is on the ground
        for rects in solid_moverect_list:
            rects.top -= 1
            if player_rect.colliderect(rects) == True:
                player_on_the_ground = True
            rects.top += 1
        
        #calculate jump
        if space_down:
            if player_on_the_ground == True and temp_jump_lenght != 0:
                temp_jump_lenght = 0
                can_jump = True
            if space_down:
                if temp_jump_lenght == jump_lenght:
                    can_jump = False
                    middle_player_jump = True
                if can_jump == True:
                    temp_jump_lenght += 1
                    player_y -= 5
                    jumping = True
        
        #look if you can jump
        for rects in solid_moverect_list:
            rects.top += temp_jump
            if player_rect.colliderect(rects) == True:
                jump_movement_allow = False
            rects.top -= temp_jump

        #add jump
        if jump_movement_allow == True:
            for rects in solid_moverect_list:
                rects.top += temp_jump
            for rects in unsolid_moverect_list:
                rects.top += temp_jump
        
        if jumping != True:  
            #look if you can add gravity
            for rects in solid_moverect_list:
                rects.top -= gravity
                if player_rect.colliderect(rects) == True:
                    gravity_movement_allow = False
                rects.top += gravity

            #add gravity
            if gravity_movement_allow == True:
                for rects in solid_moverect_list:
                    rects.top -= gravity
                for rects in unsolid_moverect_list:
                    rects.top -= gravity
        
        #look if you can add button movement
        for rect in solid_moverect_list:
            rect.top -= player_y
            rect.left -= player_x
            if player_rect.colliderect(rect) == True:
                player_movement_allow = False
            rect.top += player_y
            rect.left += player_x

        #add button movement
        if player_x != 0 or player_y != 0:
            if player_movement_allow == True:
                for rect in solid_moverect_list:
                    rect.top -= player_y
                    rect.left -= player_x
                for rect in unsolid_moverect_list:
                    rect.top -= player_y
                    rect.left -= player_x
                
            if player_x > 0:
                player_running_to_right = True
            if player_x < 0:
                player_running_to_left = True
        
        #look if you can add 1 pixel down
        for rects in solid_moverect_list:
            rects.top -= 1
            if player_rect.colliderect(rects) == True:
                one_pixel_movement_allow = False
            rects.top += 1

        #add 1 pixel down
        if gravity_movement_allow != True:
            if one_pixel_movement_allow == True:
                for rects in solid_moverect_list:
                    rects.top -= 1
                for rects in unsolid_moverect_list:
                    rects.top -= 1
        
        #look if your in a block
        for rect in solid_moverect_list:
            if player_rect.colliderect(rect) == True:
                in_block = True
        
        #push you up if your stuck in a block
        if in_block == True:
            print("stuck")
            for rect in solid_moverect_list:
                rect.top += gravity
            for rect in unsolid_moverect_list:
                rect.top += gravity

        #calculate what player sprite needs to be displayed
        if player_animation_timer == player_animation_speed:
            player_animation_timer = 0
        else:
            player_animation_timer += 1
        
        player_animation_chooser_class = sprintLoader.player_animation_chooser(player_animation_timer, config_options.character_bigness, player_crouching, player_running_to_left, jumping, gravity_movement_allow, player_running_to_right, player_sprite_number)
        player_sprite = player_animation_chooser_class.player_sprite
        player_sprite_number = player_animation_chooser_class.player_sprite_number
        
        #background
        gameDisplay.fill(GRAY)
        gameDisplay.blit(background_list[0], (0, 0))

        #floor
        pygame.draw.rect(gameDisplay, (16, 89, 15), solid_moverect_list[0])
        pygame.draw.rect(gameDisplay, (150, 85, 6), solid_moverect_list[2])

        #for ground
        pygame.draw.rect(gameDisplay, GREEN, unsolid_moverect_list[1])
        pygame.draw.rect(gameDisplay, (122, 84, 38), unsolid_moverect_list[2])
        pygame.draw.rect(gameDisplay, GREEN, unsolid_moverect_list[3])
        pygame.draw.rect(gameDisplay, (122, 84, 38), unsolid_moverect_list[0])
        pygame.draw.rect(gameDisplay, (107, 58, 22), solid_moverect_list[1])
        
        #debugging level
        pygame.draw.rect(gameDisplay, GREEN, player_rect)      #enable for player collider
        
        #player
        gameDisplay.blit(player_sprite, (int(config_options.width/2-32), int(config_options.height/2-32)))

        #ui level
        pygame.draw.rect(gameDisplay, (33, 33, 33), UI_rects[1])
        pygame.draw.rect(gameDisplay, (23, 23, 23), UI_rects[0])
        gameDisplay.blit(font30.render('quit', True, WHITE), (config_options.width-60, 10))

        if ctrl_down:
            player_rect.height += 32
            player_rect.top -= 32

        pygame.display.update()
        first_frame = False
        #delta time is milliseconds since the previous call
        deltatime = clock.tick(config_options.fps)


main()
pygame.quit()
quit()