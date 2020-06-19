import pygame
pygame.init()

class movement:
    def __init__(self, event_dict, playerController_variables, config_rects_game, config_options, temp_jump_lenght, can_jump, temp_player_crouching):
        self.temp_jump_lenght = temp_jump_lenght
        self.playerController_variables = playerController_variables #w, s, a, d, ctrl, space
        self.temp_player_crouching = temp_player_crouching
        self.event_dict = event_dict
        self.config_rects_game = config_rects_game
        self.config_options = config_options
        self.can_jump = can_jump
        
        self.gravity_movement_allow = True
        self.jumping = False
        self.player_running_to_left = False
        self.player_running_to_right = False
        self.player_crouching = False
        
        self.player_movement_allow = True
        self.one_pixel_movement_allow = True
        self.jump_movement_allow = True
        self.middle_player_jump = False
        self.in_block = False
        self.player_on_the_ground = False
        self.temp_jump = 0
        self.player_x = 0
        self.player_y = 0
        
        self.main()
    
    def main(self):        
        movement_event_happened = self.event_dict.get('movement_event_happened')
        ctrl_event_happened = self.event_dict.get('ctrl_event_happened')
        space_event_happened = self.event_dict.get('space_event_happened')
        
        if movement_event_happened != False:
            self.playerController_variables = [self.event_dict.get('w_down'), self.event_dict.get('s_down'), self.event_dict.get('a_down'), self.event_dict.get('d_down'), self.playerController_variables[4], self.playerController_variables[5]]
        if ctrl_event_happened != False:
            self.playerController_variables[4] = self.event_dict.get('ctrl_down')
        if space_event_happened != False:
            self.playerController_variables[5] = self.event_dict.get('space_down')

        #add movement of wasd
        if self.playerController_variables[0]: # w is disabled
            self.player_y -= 0 * self.config_options.player_speed
        elif self.playerController_variables[1]: # s is disabled
            self.player_y += 0 * self.config_options.player_speed 
        elif self.playerController_variables[2]: # a is enabled
            if self.playerController_variables[4]:
                self.player_x -= 1 * self.config_options.player_crouching_speed
            else:
                self.player_x -= 1 * self.config_options.player_speed
        elif self.playerController_variables[3]: # d is enabled
            if self.playerController_variables[4]:
                self.player_x += 1 * self.config_options.player_crouching_speed
            else:
                self.player_x += 1 * self.config_options.player_speed
            
        #calculate crouching
        if self.temp_player_crouching == True:
            self.config_rects_game.player_rect.height += 32
            self.config_rects_game.player_rect.top -= 32
            
        
        if self.playerController_variables[4]:
            self.config_rects_game.player_rect.height -= 32
            self.config_rects_game.player_rect.top += 32
            self.player_crouching = True
            self.temp_player_crouching = True
        else:
            self.temp_player_crouching = False
        
        #look if player is on the ground
        for rects in self.config_rects_game.solid_moverect_list:
            rects.top -= 1
            if self.config_rects_game.player_rect.colliderect(rects) == True:
                self.player_on_the_ground = True
            rects.top += 1
        
        #calculate jump
        if self.playerController_variables[5]:
            if self.player_on_the_ground == True and self.temp_jump_lenght != 0:
                self.temp_jump_lenght = 0
                self.can_jump = True
            if self.playerController_variables[5]:
                if self.temp_jump_lenght == self.config_options.jump_lenght:
                    self.can_jump = False
                    self.middle_player_jump = True
                if self.can_jump == True:
                    self.temp_jump_lenght += 1
                    self.player_y -= 5
                    self.jumping = True
        
        #look if you can jump
        for rects in self.config_rects_game.solid_moverect_list:
            rects.top += self.temp_jump
            if self.config_rects_game.player_rect.colliderect(rects) == True:
                self.jump_movement_allow = False
            rects.top -= self.temp_jump

        #add jump
        if self.jump_movement_allow == True:
            for rects in self.config_rects_game.solid_moverect_list:
                rects.top += self.temp_jump
            for rects in self.config_rects_game.unsolid_moverect_list:
                rects.top += self.temp_jump
        
        if self.jumping != True:  
            #look if you can add gravity
            for rects in self.config_rects_game.solid_moverect_list:
                rects.top -= self.config_options.gravity
                if self.config_rects_game.player_rect.colliderect(rects) == True:
                    self.gravity_movement_allow = False
                rects.top += self.config_options.gravity

            #add gravity
            if self.gravity_movement_allow == True:
                for rects in self.config_rects_game.solid_moverect_list:
                    rects.top -= self.config_options.gravity
                for rects in self.config_rects_game.unsolid_moverect_list:
                    rects.top -= self.config_options.gravity
        
        #look if you can add button movement
        for rect in self.config_rects_game.solid_moverect_list:
            rect.top -= self.player_y
            rect.left -= self.player_x
            if self.config_rects_game.player_rect.colliderect(rect) == True:
                self.player_movement_allow = False
            rect.top += self.player_y
            rect.left += self.player_x

        #add button movement
        if self.player_x != 0 or self.player_y != 0:
            if self.player_movement_allow == True:
                for rect in self.config_rects_game.solid_moverect_list:
                    rect.top -= self.player_y
                    rect.left -= self.player_x
                for rect in self.config_rects_game.unsolid_moverect_list:
                    rect.top -= self.player_y
                    rect.left -= self.player_x
                
            if self.player_x > 0:
                self.player_running_to_right = True
            if self.player_x < 0:
                self.player_running_to_left = True
        
        #look if you can add 1 pixel down
        for rects in self.config_rects_game.solid_moverect_list:
            rects.top -= 1
            if self.config_rects_game.player_rect.colliderect(rects) == True:
                self.one_pixel_movement_allow = False
            rects.top += 1

        #add 1 pixel down
        if self.gravity_movement_allow != True:
            if self.one_pixel_movement_allow == True:
                for rects in self.config_rects_game.solid_moverect_list:
                    rects.top -= 1
                for rects in self.config_rects_game.unsolid_moverect_list:
                    rects.top -= 1
        
        #look if your in a block
        for rect in self.config_rects_game.solid_moverect_list:
            if self.config_rects_game.player_rect.colliderect(rect) == True:
                self.in_block = True
        
        #push you up if your stuck in a block
        if self.in_block == True:
            print("stuck")
            for rect in self.config_rects_game.solid_moverect_list:
                rect.top += self.config_options.gravity
            for rect in self.config_rects_game.unsolid_moverect_list:
                rect.top += self.config_options.gravity
