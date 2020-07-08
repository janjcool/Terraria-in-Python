import pygame

class player_animation_chooser:
    def __init__(self, playerController_class, config_dict):
        self.config_dict = config_dict
        
        if self.config_dict["variables"]["sprintLoader"]["player_animation_timer"] == self.config_dict["player"]["player_animation_speed"]:
            self.config_dict["variables"]["sprintLoader"]["player_animation_timer"] = 0
        else:
            self.config_dict["variables"]["sprintLoader"]["player_animation_timer"] += 1
        
        
        if playerController_class.player_crouching and playerController_class.player_running_to_left:
            self.sprite_chooser("crouch", self.config_dict["player"]["character_bigness"], 4, True)
            
        elif playerController_class.player_crouching:
            self.sprite_chooser("crouch", self.config_dict["player"]["character_bigness"], 4, False)
            
        elif playerController_class.jumping and playerController_class.player_running_to_left:
            self.sprite_chooser("jump", self.config_dict["player"]["character_bigness"], 4, True, False, 2)
            
        elif playerController_class.jumping:
            self.sprite_chooser("jump", self.config_dict["player"]["character_bigness"], 4, False, False, 2)
            
        elif playerController_class.gravity_movement_allow and playerController_class.player_running_to_right:
            self.sprite_chooser("fall", self.config_dict["player"]["character_bigness"], 2, False)
            
        elif playerController_class.gravity_movement_allow and playerController_class.player_running_to_left:
            self.sprite_chooser("fall", self.config_dict["player"]["character_bigness"], 2, True)
            
        elif playerController_class.player_running_to_left:
            self.sprite_chooser("run", self.config_dict["player"]["character_bigness"], 6, True)
            
        elif playerController_class.player_running_to_right:
            self.sprite_chooser("run", self.config_dict["player"]["character_bigness"], 6, False)
            
        elif playerController_class.gravity_movement_allow:
            self.sprite_chooser("fall", self.config_dict["player"]["character_bigness"], 2, False)
            
        else:
            self.sprite_chooser("idle", self.config_dict["player"]["character_bigness"], 4, False)

    def sprite_chooser(self, animation_type, size = 1, amount_of_sprites = 1, flip_horizontal = False, more_than_1_sprite = True, sprite_number = 0):
        animation_list = []
        
        if more_than_1_sprite:
            if 0 == self.config_dict["variables"]["sprintLoader"]["player_animation_timer"]:
                self.config_dict["variables"]["sprintLoader"]["player_sprite_number"] += 1
            if self.config_dict["variables"]["sprintLoader"]["player_sprite_number"] >= amount_of_sprites:
                self.config_dict["variables"]["sprintLoader"]["player_sprite_number"] = 0
        else:
            self.config_dict["variables"]["sprintLoader"]["player_sprite_number"] = sprite_number
        
        for x in range(0, amount_of_sprites):
            temp_animation = pygame.image.load("art-assets/player/sprites/adventurer-" + animation_type + "-0" + str(x) + ".png")
            temp_animation = pygame.transform.scale(temp_animation, (int(50 * size), int(37 * size)))
            if flip_horizontal:
                temp_animation = pygame.transform.flip(temp_animation, True, False)
            
            animation_list.append(temp_animation)
        
        if self.config_dict["variables"]["sprintLoader"]["player_sprite_number"] > (amount_of_sprites - 1):
                self.config_dict["variables"]["sprintLoader"]["player_sprite_number"] = 0
                
        self.player_sprite = animation_list[self.config_dict["variables"]["sprintLoader"]["player_sprite_number"]]