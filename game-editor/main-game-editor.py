import tcod as libtcod
import time

def handle_keys(key):
    # Movement keys
    if key.c == ord('w'):
        return {'move_y': (-1)}
    elif key.c == ord('s'):
        return {'move_y': (1)}
    elif key.c == ord('a'):
        return {'move_x': (-1)}
    elif key.c == ord('d'):
        return {'move_x': (1)}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}

    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}

    if key.vk == libtcod.KEY_SPACE:
        return {'enter': True}

    # No key was pressed
    return {}

def save_pos(player_x, player_y):
    print("x:%s y:%s" % (player_x, player_y))


def main():
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width/2)
    player_y = int(screen_height/2)

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(screen_width, screen_height, 'roguelike game', False)

    key = libtcod.console_check_for_keypress()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():

        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        libtcod.console_put_char(0, player_x, player_y, ' ', libtcod.BKGND_NONE)
        
        action = handle_keys(key)
        
        move_x = action.get('move_x')
        move_y = action.get('move_y')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')
        enter = action.get('enter')

        """        #this is for finding the right key_code
        key_visuliser = libtcod.console_check_for_keypress()
        print(key_visuliser)
        time.sleep(3)
        #"""

        if move_x:
            player_x += move_x
        if move_y:
            player_y += move_y

        if exit:
            return True

        if fullscreen:
                    libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

        libtcod.console_set_default_foreground(0, libtcod.white)
        libtcod.console_put_char(0, player_x, player_y, '@', libtcod.BKGND_NONE)
        libtcod.console_flush()

        if enter:
            save_pos(player_x, player_y)


if __name__ == '__main__':
    main()