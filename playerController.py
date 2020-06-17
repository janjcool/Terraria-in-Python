import pygame
pygame.init()

class movement:
    def __init__(self, event_dict, playerController_variables, config_rects_game, config_options, temp_jump_lenght, can_jump, temp_player_crouching):
        self.temp_jump_lenght = temp_jump_lenght
        self.playerController_variables = playerController_variables #w, s, a, d, ctrl, space
        one_pixel_movement_allow, jump_movement_allow, self.gravity_movement_allow = True, True, True
        player_on_the_ground, self.jumping, in_block, player_movement_allow = False, False, False, True
        self.player_running_to_right, self.player_running_to_left, self.player_crouching = False, False, False
        middle_player_jump, self.can_jump, self.temp_player_crouching = False, can_jump, temp_player_crouching
        temp_jump = 0
        player_x = 0
        player_y = 0
        
        movement_event_happened = event_dict.get('movement_event_happened')
        ctrl_event_happened = event_dict.get('ctrl_event_happened')
        space_event_happened = event_dict.get('space_event_happened')
        
        if movement_event_happened != False:
            self.playerController_variables = [event_dict.get('w_down'), event_dict.get('s_down'), event_dict.get('a_down'), event_dict.get('d_down'), playerController_variables[4], playerController_variables[5]]
        if ctrl_event_happened != False:
            self.playerController_variables[4] = event_dict.get('ctrl_down')
        if space_event_happened != False:
            self.playerController_variables[5] = event_dict.get('space_down')

        #add movement of wasd
        if self.playerController_variables[0]: # w is disabled
            player_y -= 0 * config_options.player_speed
        elif self.playerController_variables[1]: # s is disabled
            player_y += 0 * config_options.player_speed 
        elif self.playerController_variables[2]: # a is enabled
            if self.playerController_variables[4]:
                player_x -= 1 * config_options.player_crouching_speed
            else:
                player_x -= 1 * config_options.player_speed
        elif self.playerController_variables[3]: # d is enabled
            if self.playerController_variables[4]:
                player_x += 1 * config_options.player_crouching_speed
            else:
                player_x += 1 * config_options.player_speed
            
        #calculate crouching
        if temp_player_crouching == True:
            config_rects_game.player_rect.height += 32
            config_rects_game.player_rect.top -= 32
            
        
        if self.playerController_variables[4]:
            config_rects_game.player_rect.height -= 32
            config_rects_game.player_rect.top += 32
            self.player_crouching = True
            self.temp_player_crouching = True
        else:
            self.temp_player_crouching = False
        
        #look if player is on the ground
        for rects in config_rects_game.solid_moverect_list:
            rects.top -= 1
            if config_rects_game.player_rect.colliderect(rects) == True:
                player_on_the_ground = True
            rects.top += 1
        
        #calculate jump
        if playerController_variables[5]:
            if player_on_the_ground == True and self.temp_jump_lenght != 0:
                self.temp_jump_lenght = 0
                self.can_jump = True
            if playerController_variables[5]:
                if self.temp_jump_lenght == config_options.jump_lenght:
                    self.can_jump = False
                    middle_player_jump = True
                if self.can_jump == True:
                    self.temp_jump_lenght += 1
                    player_y -= 5
                    self.jumping = True
        
        #look if you can jump
        for rects in config_rects_game.solid_moverect_list:
            rects.top += temp_jump
            if config_rects_game.player_rect.colliderect(rects) == True:
                jump_movement_allow = False
            rects.top -= temp_jump

        #add jump
        if jump_movement_allow == True:
            for rects in config_rects_game.solid_moverect_list:
                rects.top += temp_jump
            for rects in config_rects_game.unsolid_moverect_list:
                rects.top += temp_jump
        
        if self.jumping != True:  
            #look if you can add gravity
            for rects in config_rects_game.solid_moverect_list:
                rects.top -= config_options.gravity
                if config_rects_game.player_rect.colliderect(rects) == True:
                    self.gravity_movement_allow = False
                rects.top += config_options.gravity

            #add gravity
            if self.gravity_movement_allow == True:
                for rects in config_rects_game.solid_moverect_list:
                    rects.top -= config_options.gravity
                for rects in config_rects_game.unsolid_moverect_list:
                    rects.top -= config_options.gravity
        
        #look if you can add button movement
        for rect in config_rects_game.solid_moverect_list:
            rect.top -= player_y
            rect.left -= player_x
            if config_rects_game.player_rect.colliderect(rect) == True:
                player_movement_allow = False
            rect.top += player_y
            rect.left += player_x

        #add button movement
        if player_x != 0 or player_y != 0:
            if player_movement_allow == True:
                for rect in config_rects_game.solid_moverect_list:
                    rect.top -= player_y
                    rect.left -= player_x
                for rect in config_rects_game.unsolid_moverect_list:
                    rect.top -= player_y
                    rect.left -= player_x
                
            if player_x > 0:
                self.player_running_to_right = True
            if player_x < 0:
                self.player_running_to_left = True
        
        #look if you can add 1 pixel down
        for rects in config_rects_game.solid_moverect_list:
            rects.top -= 1
            if config_rects_game.player_rect.colliderect(rects) == True:
                one_pixel_movement_allow = False
            rects.top += 1

        #add 1 pixel down
        if self.gravity_movement_allow != True:
            if one_pixel_movement_allow == True:
                for rects in config_rects_game.solid_moverect_list:
                    rects.top -= 1
                for rects in config_rects_game.unsolid_moverect_list:
                    rects.top -= 1
        
        #look if your in a block
        for rect in config_rects_game.solid_moverect_list:
            if config_rects_game.player_rect.colliderect(rect) == True:
                in_block = True
        
        #push you up if your stuck in a block
        if in_block == True:
            print("stuck")
            for rect in config_rects_game.solid_moverect_list:
                rect.top += config_options.gravity
            for rect in config_rects_game.unsolid_moverect_list:
                rect.top += config_options.gravity
