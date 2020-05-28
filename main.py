"""
dit is de tutorial die ik aan het volgen was:
http://rogueliketutorials.com/tutorials/tcod/
(ik zat in het midden van deel 2)
"""

import tcod as libtcod

from entity import Entity
from render_functions import clear_all, render_all

def handle_keys(key):
    # Movement keys
    if key.vk == libtcod.KEY_UP:
        return {'move': (0, -1)}
    elif key.vk == libtcod.KEY_DOWN:
        return {'move': (0, 1)}
    elif key.vk == libtcod.KEY_LEFT:
        return {'move': (-1, 0)}
    elif key.vk == libtcod.KEY_RIGHT:
        return {'move': (1, 0)}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}

    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}

    # No key was pressed
    return {}

def main():
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 45

    player = Entity(int(screen_width / 2), int(screen_height / 2), '@', libtcod.white)
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), '@', libtcod.yellow)
    entities = [npc, player]

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)       #set font to file in this folder
    libtcod.console_init_root(screen_width, screen_height, 'libtcod tutorial revised', False)       #make the screen
    con = libtcod.console_new(screen_width, screen_height)      #give the console the name con

    key = libtcod.Key()         #store key pres
    mouse = libtcod.Mouse()         #stores mouse position

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)        #check for event of the variable key and mouse

        render_all(con, entities, screen_width, screen_height)
        libtcod.console_flush()         #renders everyting in the screen
        clear_all(con, entities)

        action = handle_keys(key)       #set the return of the function handle_keys to action (this function returns a dictionary)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            player.move(dx, dy)

        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())


if __name__ == '__main__':
    main()