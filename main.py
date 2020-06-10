from opensimplex import OpenSimplex
import pygame
import random
import sprint-loader
pygame.init()

def handle_events(events, quit_rect, test_rect):
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
                    # `event.pos` is the mouse position.
                    if quit_rect.collidepoint(event.pos):
                        handle_events_dict['exit'] = True
                    if test_rect.collidepoint(event.pos):
                        handle_events_dict['test'] = True
                        
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
                handle_events_dict['exit'] = True
            
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
    
    return handle_events_dict

def player_animation(animation_list, animation_repeat):
    if temp_timer:
        do_next_animation == False
        
        if temp_timer == animation_repeat:
            do_next_animation = True
        else:
            temp_timer += 1

    else:
        print("begin timer for player_animation function")
        temp_timer = 0
    
    if do_next_animation == True:
        items_in_list = len(animation_list)
        if temp_animation_counter:
            if temp_animation_counter == items_in_list+1:
                temp_animation_counter == 0
            else:
                temp_animation_counter += 1
        else:
            print("begin animation image counter")
            temp_animation_counter = 0
        
        return animation_list[temp_animation_counter]
        

def main():
    width = 1000 #16*50
    height = 700 #16*30
    fps = 60
    character_bigness = 2
    player_speed = 5
    gravity = 5
    jump_lenght = 20 #how many frames you jump
    jump_speed = 30 #pixel you jump per second

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (30, 30, 30)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    gameDisplay = pygame.display.set_mode((width,height), 0, 32)
    pygame.display.set_caption('a project I probably won`t finish')
    font20 = pygame.font.SysFont('Arial', 20)
    font30 = pygame.font.SysFont('Arial', 30)
    font40 = pygame.font.SysFont('Arial', 40)

    #seed of opensimplex noise (like perlin noise)
    tmp = OpenSimplex(seed=1)
    clock = pygame.time.Clock()

    player_sprite_idle_00 = pygame.image.load("art-assets/player/sprites/adventurer-idle-00.png")
    
    wallpaper = pygame.image.load("background.png")
    wallpaper = pygame.transform.scale(wallpaper, (width, height))

    quit_rect = pygame.Rect(width-80, 0, 80, 60)
    test_rect = pygame.Rect(0, 0, 100, 100)
    grass_rect = pygame.Rect(0, height-50, width, 100)
    tree_rect = pygame.Rect(80, height-90, 20, 60)
    leafs_rect = pygame.Rect(70, height-130, 40, 40)
    player_rect = pygame.Rect(int(width/2-4), int(height/2-18), 38, 58)
    wall_rect = pygame.Rect(width-50, height-100, 10, 50)
    tree2_rect = pygame.Rect(80+200, height-90, 20, 60)
    leafs2_rect = pygame.Rect(70+200, height-130, 40, 40)
    cloud1_rect = pygame.Rect(0, 80, 60, 40)
    cloud2_rect = pygame.Rect(80, 100, 60, 40)
    cloud3_rect = pygame.Rect(width-80, 90, 70, 35)
    dirt_rect = pygame.Rect(0, height+50, width, 300)

    unsolid_moverect_list = [tree_rect, leafs_rect, tree2_rect, leafs2_rect, cloud1_rect, cloud2_rect, cloud3_rect]
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
    
    while mainloop:
        events = pygame.event.get()
        mouse = pygame.mouse.get_pos()
        action = handle_events(events, quit_rect, test_rect)
        player_x = 0
        player_y = 0
        temp_jump = 0
        player_movement_allow = True
        gravity_movement_allow = True
        jump_movement_allow = True
        one_pixel_movement_allow = True
        in_block = False
        player_on_the_ground = False
        jumping = False

        exit = action.get('exit')
        movement_event_happened = action.get('movement_event_happened')
        ctrl_event_happened = action.get('ctrl_event_happened')
        space_event_happened = action.get('space_event_happened')
        testPressed = action.get('test')
        
        if movement_event_happened != False:
            w_down, s_down, a_down, d_down = action.get('w_down'), action.get('s_down'), action.get('a_down'), action.get('d_down')
        if ctrl_event_happened != False:
            ctrl_down = action.get('ctrl_down')
        if space_event_happened != False:
            space_down = action.get('space_down')

        if exit:
            return True
        
        if testPressed:
            print("test button")

        if w_down:
            player_y -= 0 * player_speed # w is disabeld
        elif s_down:
            player_y += 0 * player_speed # s is disabeld
        elif a_down:
            player_x -= 1 * player_speed
        elif d_down:
            player_x += 1 * player_speed
            
        if ctrl_down:
            player_rect.height -= 32
            player_rect.top += 32
        
        #kijk of de speler op de grond is
        for rects in solid_moverect_list:
            rects.top -= 1
            if player_rect.colliderect(rects) == True:
                player_on_the_ground = True
            rects.top += 1
        
        #calculate jump
        if player_on_the_ground == True and temp_jump_lenght != 0:
            temp_jump_lenght = 0
            can_jump = True
        if space_down:
            if temp_jump_lenght == jump_lenght:
                can_jump = False
            if can_jump == True:
                temp_jump_lenght += 1
                jumping = True
        if jumping == True:
            player_y -= 5
        
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
        pygame.draw.rect(gameDisplay, BLUE, unsolid_moverect_list[4])
        pygame.draw.rect(gameDisplay, BLUE, unsolid_moverect_list[5])
        pygame.draw.rect(gameDisplay, BLUE, unsolid_moverect_list[6])
        pygame.draw.rect(gameDisplay, (122, 84, 38), unsolid_moverect_list[0])
        pygame.draw.rect(gameDisplay, (107, 58, 22), solid_moverect_list[1])
        
        #debugging level
        pygame.draw.rect(gameDisplay, GREEN, player_rect)      #enable for player collider
        
        #player
        gameDisplay.blit(player_sprite, (int(width/2-32), int(height/2-32)))

        #ui level
        pygame.draw.rect(gameDisplay, (33, 33, 33), UI_rects[1])
        pygame.draw.rect(gameDisplay, (23, 23, 23), UI_rects[0])
        gameDisplay.blit(font30.render('quit', True, WHITE), (width-60, 10))

        if ctrl_down:
            player_rect.height += 32
            player_rect.top -= 32

        pygame.display.update()
        first_frame = False
        #delta time is milliseconds since the previous call
        deltatime = clock.tick(fps)


main()
pygame.quit()
quit()