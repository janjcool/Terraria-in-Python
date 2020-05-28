from opensimplex import OpenSimplex
import pygame
import random
pygame.init()

def handle_events(events, quit_button, test_button):
    for event in events:
        if event.type == pygame.QUIT:
            return {'exit': True}
        elif event.type == pygame.MOUSEBUTTONDOWN:
                # 1 is the left mouse button, 2 is middle, 3 is right.
                if event.button == 1:
                    # `event.pos` is the mouse position.
                    if quit_button.collidepoint(event.pos):
                        print("exit")
                        return {'exit': True}
                    if test_button.collidepoint(event.pos):
                        print("this button does nothing")
                        
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

def main():
    width = 16*50
    height = 16*30
    fps = 60
    world_seed = random.randint(1, 99999999)

    player_x = 0
    player_y = 0
    player_speed = 5

    schale = 2

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

    quit_button = pygame.Rect(width-80, 0, 80, 60)
    test_button = pygame.Rect(width/2-50, height/2-50, 100, 100)

    w_down, s_down, a_down, d_down = False, False, False, False
    deltatime = 1

    while mainloop:

        events = pygame.event.get()
        mouse = pygame.mouse.get_pos()
        action = handle_events(events, quit_button, test_button)

        exit = action.get('exit')
        tmep_event_happened = action.get('event_happened')
        
        if tmep_event_happened != False:
            w_down, s_down, a_down, d_down = action.get('w_down'), action.get('s_down'), action.get('a_down'), action.get('d_down')
        
        
        if w_down:
            player_y -= 0.25 * player_speed * deltatime
        elif s_down:
            player_y += 0.25 * player_speed * deltatime
        elif a_down:
            player_x -= 0.25 * player_speed * deltatime
        elif d_down:
            player_x += 0.25 * player_speed * deltatime

        if exit:
            return True

        gameDisplay.fill(GRAY)

        pygame.draw.rect(gameDisplay, (23, 23, 23), quit_button)
        pygame.draw.rect(gameDisplay, BLUE, test_button)

        gameDisplay.blit(player_sprite, (player_x, player_y))
        gameDisplay.blit(font30.render('quit', True, WHITE), (width-60, 10))

        pygame.display.update()
        #delta time is milliseconds since the previous call
        deltatime = clock.tick(fps)


main()
pygame.quit()
quit()