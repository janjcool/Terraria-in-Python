from opensimplex import OpenSimplex
import pygame
import random
pygame.init()

def handle_events(events, quit_rect, test_rect):
    for event in events:
        if event.type == pygame.QUIT:
            return {'exit': True}
        elif event.type == pygame.MOUSEBUTTONDOWN:
                # 1 is the left mouse button, 2 is middle, 3 is right.
                if event.button == 1:
                    # `event.pos` is the mouse position.
                    if quit_rect.collidepoint(event.pos):
                        print("exit")
                        return {'exit': True}
                    if test_rect.collidepoint(event.pos):
                        print("test")
                        print("mouse pos:" + str(event.pos))
                        return {'test': True}
                        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                return {'w_down': True}
            elif event.key == pygame.K_s:
                return {'s_down': True}
            elif event.key == pygame.K_a:
                return {'a_down': True}
            elif event.key == pygame.K_d:
                return {'d_down': True}

            elif event.key == pygame.K_ESCAPE:
                # Exit the game
                print("exit")
                return {'exit': True}
    
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                return {'w_down': False}
            elif event.key == pygame.K_s:
                return {'s_down': False}
            elif event.key == pygame.K_a:
                return {'a_down': False}
            elif event.key == pygame.K_d:
                return {'d_down': False}
        return {'event_happened': False}    
    return {'event_happened': False}

def rects_render(gameDisplay, w_down, s_down, a_down, d_down, player_x, player_y, player_speed, deltatime, unsolid_moverect_list, solid_moverect_list, player_rect, UI_rects, gravity):
    player_x = 0
    player_y = 0
    player_movement_allow = True
    gravity_movement_allow = True
    in_block = False

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (30, 30, 30)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    if w_down:
        player_y -= 1 * player_speed
    elif s_down:
        player_y += 1 * player_speed
    elif a_down:
        player_x -= 1 * player_speed
    elif d_down:
        player_x += 1 * player_speed

    #look if you can add gravity
    for y in solid_moverect_list:
        y.top -= gravity +1
        if player_rect.colliderect(y) == True:
            gravity_movement_allow = False
        y.top += gravity +1

    #add gravity
    if gravity_movement_allow == True:
        for y in solid_moverect_list:
            y.top -= gravity
        for x in unsolid_moverect_list:
            x.top -= gravity
    
    #look if you can add button movement
    for y in solid_moverect_list:
        y.top -= player_y
        y.left -= player_x
        if player_rect.colliderect(y) == True:
            player_movement_allow = False
        y.top += player_y
        y.left += player_x

    #add button movement
    if player_x != 0 or player_y != 0:
        if player_movement_allow == True:
            for y in solid_moverect_list:
                y.top -= player_y
                y.left -= player_x
            for x in unsolid_moverect_list:
                x.top -= player_y
                x.left -= player_x

    #look if your in a block
    for y in solid_moverect_list:
        if player_rect.colliderect(y) == True:
            in_block = True

    #push you up if your stuck in a block
    if in_block == True:
        print("stuck")
        for y in solid_moverect_list:
            y.top += gravity
        for x in unsolid_moverect_list:
            x.top += gravity
    
    #background

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

    #ui level
    pygame.draw.rect(gameDisplay, (33, 33, 33), UI_rects[1])
    pygame.draw.rect(gameDisplay, (23, 23, 23), UI_rects[0])

    #debugging level
    #pygame.draw.rect(gameDisplay, GREEN, player_rect)      #enable for player collider


def main():
    width = 1000 #16*50
    height = 700 #16*30
    fps = 60
    schale = 2
    deltatime = 1 #don't chanche this
    world_seed = random.randint(1, 9999999999)

    player_x = 0
    player_y = 0
    player_speed = 5

    gravity = 5

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

    mainloop = True
    event_happened = True

    player_sprite = pygame.image.load("man with sword and shield.png")
    player_sprite = pygame.transform.scale(player_sprite, (32 * schale, 32 * schale))

    quit_rect = pygame.Rect(width-80, 0, 80, 60)
    test_rect = pygame.Rect(0, 0, 100, 100)
    grass_rect = pygame.Rect(0, height-50, width, 100)
    tree_rect = pygame.Rect(80, height-90, 20, 60)
    leafs_rect = pygame.Rect(70, height-130, 40, 40)
    player_rect = pygame.Rect(width/2-27, height/2-30, 45, 62)
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

    w_down, s_down, a_down, d_down = False, False, False, False

    while mainloop:
        events = pygame.event.get()
        mouse = pygame.mouse.get_pos()
        action = handle_events(events, quit_rect, test_rect)

        exit = action.get('exit')
        tmep_event_happened = action.get('event_happened')
        testPressed = action.get('test')
        
        if tmep_event_happened != False:
            w_down, s_down, a_down, d_down = action.get('w_down'), action.get('s_down'), action.get('a_down'), action.get('d_down')

        if exit:
            return True
        
        if testPressed:
            print("player_pos:" + str(player_rect) + 'ground pos:' + str(ground_rect))

        gameDisplay.fill(GRAY)

        rects_render(gameDisplay, w_down, s_down, a_down, d_down, player_x, player_y, player_speed, deltatime, unsolid_moverect_list, solid_moverect_list, player_rect, UI_rects, gravity)

        gameDisplay.blit(player_sprite, (width/2-32, height/2-32))
        gameDisplay.blit(font30.render('quit', True, WHITE), (width-60, 10))

        pygame.display.update()
        #delta time is milliseconds since the previous call
        deltatime = clock.tick(fps)


main()
pygame.quit()
quit()