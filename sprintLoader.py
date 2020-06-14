import pygame
pygame.init()

class player_animation_chooser:
    def __init__(self, player_animation_timer = 0, character_bigness = 1, player_crouching = False, player_running_to_left = False, jumping = False, gravity_movement_allow = False, player_running_to_right = False, player_sprite_number = 0):

        if player_crouching == True and player_running_to_left == True:
            if player_animation_timer == 0:
                player_sprite_number += 1
            if player_sprite_number >= 4:
                player_sprite_number = 0
            
            player_sprite = player_animation_type("crouch", character_bigness, 4, player_sprite_number, True)
            self.player_sprite = player_sprite.player_sprite
        elif player_crouching == True:
            if player_animation_timer == 0:
                player_sprite_number += 1
            if player_sprite_number >= 4:
                player_sprite_number = 0
            
            player_sprite = player_animation_type("crouch", character_bigness, 4, player_sprite_number)
            self.player_sprite = player_sprite.player_sprite
        elif jumping == True and player_running_to_left:
            player_sprite = player_animation_type("jump", character_bigness, 4, 2, True)
            self.player_sprite = player_sprite.player_sprite
        elif jumping == True:
            player_sprite = player_animation_type("jump", character_bigness, 4, 2)
            self.player_sprite = player_sprite.player_sprite
        elif gravity_movement_allow == True and player_running_to_right == True:
            if player_animation_timer == 0:
                player_sprite_number += 1
            if player_sprite_number >= 2:
                player_sprite_number = 0
            
            player_sprite = player_animation_type("fall", character_bigness, 2, player_sprite_number)
            self.player_sprite = player_sprite.player_sprite
        elif gravity_movement_allow == True and player_running_to_left == True:
            if player_animation_timer == 0:
                player_sprite_number += 1
            if player_sprite_number >= 2:
                player_sprite_number = 0
            
            player_sprite = player_animation_type("fall", character_bigness, 2, player_sprite_number, True)
            self.player_sprite = player_sprite.player_sprite   
        elif player_running_to_left == True:
            if player_animation_timer == 0:
                player_sprite_number += 1
            if player_sprite_number >= 6:
                player_sprite_number = 0
            
            player_sprite = player_animation_type("run", character_bigness, 6, player_sprite_number, True)
            self.player_sprite = player_sprite.player_sprite
        elif player_running_to_right == True:
            if player_animation_timer == 0:
                player_sprite_number += 1
            if player_sprite_number >= 6:
                player_sprite_number = 0
            
            player_sprite = player_animation_type("run", character_bigness, 6, player_sprite_number)
            self.player_sprite = player_sprite.player_sprite
        elif gravity_movement_allow == True:
            if player_animation_timer == 0:
                player_sprite_number += 1
            if player_sprite_number >= 2:
                player_sprite_number = 0
            
            player_sprite = player_animation_type("fall", character_bigness, 2, player_sprite_number)
            self.player_sprite = player_sprite.player_sprite
        else:
            if player_animation_timer == 0:
                player_sprite_number += 1
            if player_sprite_number >= 4:
                player_sprite_number = 0
            
            player_sprite = player_animation_type("idle", character_bigness, 4, player_sprite_number)
            self.player_sprite = player_sprite.player_sprite
        
        self.player_sprite_number = player_sprite_number

class player_animation_type:
    def __init__(self, animation_type = "nothing", size = 1, amount_of_sprites = 1, player_sprite_number = 0, flip_horizontal = False):
        
        animation_list = []
        
        for x in range(0, amount_of_sprites):
            temp_animation = pygame.image.load("art-assets/player/sprites/adventurer-" + animation_type + "-0" + str(x) + ".png")
            temp_animation = pygame.transform.scale(temp_animation, (int(50 * size), int(37 * size)))
            if flip_horizontal == True:
                temp_animation = pygame.transform.flip(temp_animation, True, False)
            
            animation_list.append(temp_animation)
        
        if player_sprite_number > amount_of_sprites-1:
                player_sprite_number = 0
                
        self.player_sprite = animation_list[player_sprite_number]