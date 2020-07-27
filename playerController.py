class movement:
    def __init__(self, UI_config_dict, config_dict):
        self.UI_config_dict = UI_config_dict
        self.config_dict = config_dict
        
        self.gravity_movement_allow = True
        self.jumping = False
        self.player_running_to_left = False
        self.player_running_to_right = False
        self.player_crouching = False
        
        self.player_movement_allow = True
        self.one_pixel_movement_allow = True
        self.jump_movement_allow = False
        self.middle_player_jump = False
        self.in_block = False
        self.player_on_the_ground = False
        self.temp_jump = 0
        self.player_x = 0
        self.player_y = 0
        self.solid_moverect_list = []
        self.unsolid_moverect_list = []
        
        for x in UI_config_dict["Game"]["rects"]:
            if UI_config_dict["Game"]["rects"][str(x)]["solid state"] == 0:
                self.unsolid_moverect_list.append(UI_config_dict["Game"]["rects"][str(x)]["pygame object"])
            elif UI_config_dict["Game"]["rects"][str(x)]["solid state"] == 1:
                self.solid_moverect_list.append(UI_config_dict["Game"]["rects"][str(x)]["pygame object"])
        
        self.main()
    
    def main(self):        
        movement_event_happened = self.config_dict["variables"]["general"]["event_dict"].get('movement_event_happened')
        ctrl_event_happened = self.config_dict["variables"]["general"]["event_dict"].get('ctrl_event_happened')
        space_event_happened = self.config_dict["variables"]["general"]["event_dict"].get('space_event_happened')
        
        if movement_event_happened != False:
            self.config_dict["variables"]["playerController"]["w_down"] = self.config_dict["variables"]["general"]["event_dict"].get('w_down')
            self.config_dict["variables"]["playerController"]["s_down"] = self.config_dict["variables"]["general"]["event_dict"].get('s_down')
            self.config_dict["variables"]["playerController"]["a_down"] = self.config_dict["variables"]["general"]["event_dict"].get('a_down')
            self.config_dict["variables"]["playerController"]["d_down"] = self.config_dict["variables"]["general"]["event_dict"].get('d_down')
            
        if ctrl_event_happened != False:
            self.config_dict["variables"]["playerController"]["ctrl_down"] = self.config_dict["variables"]["general"]["event_dict"].get('ctrl_down')
        if space_event_happened != False:
            self.config_dict["variables"]["playerController"]["space_down"] = self.config_dict["variables"]["general"]["event_dict"].get('space_down')

        #add movement of wasd
        if self.config_dict["variables"]["playerController"]["w_down"]: # w is disabled
            self.player_y -= 0 * self.config_dict["player"]["player_speed"]
        elif self.config_dict["variables"]["playerController"]["s_down"]: # s is disabled
            self.player_y += 0 * self.config_dict["player"]["player_speed"]
        elif self.config_dict["variables"]["playerController"]["a_down"]: # a is enabled
            if self.config_dict["variables"]["playerController"]["ctrl_down"]:
                self.player_x -= 1 * self.config_dict["player"]["player_crouching_speed"]
            else:
                self.player_x -= 1 * self.config_dict["player"]["player_speed"]
        elif self.config_dict["variables"]["playerController"]["d_down"]: # d is enabled
            if self.config_dict["variables"]["playerController"]["ctrl_down"]:
                self.player_x += 1 * self.config_dict["player"]["player_crouching_speed"]
            else:
                self.player_x += 1 * self.config_dict["player"]["player_speed"]
            
        #calculate crouching
        if self.config_dict["variables"]["playerController"]["temp_player_crouching"] == True:
            self.UI_config_dict["Game"]["rects"]["player"]["pygame object"].height += 32
            self.UI_config_dict["Game"]["rects"]["player"]["pygame object"].top -= 32
            
        
        if self.config_dict["variables"]["playerController"]["ctrl_down"]:
            self.UI_config_dict["Game"]["rects"]["player"]["pygame object"].height -= 32
            self.UI_config_dict["Game"]["rects"]["player"]["pygame object"].top += 32
            self.player_crouching = True
            self.config_dict["variables"]["playerController"]["temp_player_crouching"] = True
        else:
            self.config_dict["variables"]["playerController"]["temp_player_crouching"] = False
        
        #look if player is on the ground
        for rects in self.solid_moverect_list:
            rects.top -= 1
            if self.UI_config_dict["Game"]["rects"]["player"]["pygame object"].colliderect(rects) == True:
                self.player_on_the_ground = True
            rects.top += 1
        
        #calculate jump
        if self.config_dict["variables"]["playerController"]["space_down"]:
            if self.player_on_the_ground == True and self.config_dict["variables"]["playerController"]["temp_jump_length"] != 0:
                self.config_dict["variables"]["playerController"]["temp_jump_length"] = 0
                self.config_dict["variables"]["playerController"]["can_jump"] = True
            if self.config_dict["variables"]["playerController"]["space_down"]:
                if self.config_dict["variables"]["playerController"]["temp_jump_length"] == self.config_dict["player"]["jump_length"]:
                    self.config_dict["variables"]["playerController"]["can_jump"] = False
                    self.middle_player_jump = True
                if self.config_dict["variables"]["playerController"]["can_jump"] == True:
                    self.config_dict["variables"]["playerController"]["temp_jump_length"] += 1
                    self.player_y -= 5
                    self.jumping = True
        
        #look if you can jump
        for rects in self.solid_moverect_list:
            rects.top += self.temp_jump
            if self.UI_config_dict["Game"]["rects"]["player"]["pygame object"].colliderect(rects) == True:
                self.jump_movement_allow = False
            rects.top -= self.temp_jump

        #add jump
        if self.jump_movement_allow == True:
            for rects in self.solid_moverect_list:
                rects.top += self.temp_jump
            for rects in self.unsolid_moverect_list:
                rects.top += self.temp_jump
        
        if self.jumping != True:  
            #look if you can add gravity
            for rects in self.solid_moverect_list:
                rects.top -= self.config_dict["world"]["gravity"]
                if self.UI_config_dict["Game"]["rects"]["player"]["pygame object"].colliderect(rects) == True:
                    self.gravity_movement_allow = False
                rects.top += self.config_dict["world"]["gravity"]

            #add gravity
            if self.gravity_movement_allow == True:
                for rects in self.solid_moverect_list:
                    rects.top -= self.config_dict["world"]["gravity"]
                for rects in self.unsolid_moverect_list:
                    rects.top -= self.config_dict["world"]["gravity"]
        
        #look if you can add button movement
        for rect in self.solid_moverect_list:
            rect.top -= self.player_y
            rect.left -= self.player_x
            if self.UI_config_dict["Game"]["rects"]["player"]["pygame object"].colliderect(rect) == True:
                self.player_movement_allow = False
            rect.top += self.player_y
            rect.left += self.player_x

        #add button movement
        if self.player_x != 0 or self.player_y != 0:
            if self.player_movement_allow == True:
                for rect in self.solid_moverect_list:
                    rect.top -= self.player_y
                    rect.left -= self.player_x
                for rect in self.unsolid_moverect_list:
                    rect.top -= self.player_y
                    rect.left -= self.player_x
                
            if self.player_x > 0:
                self.player_running_to_right = True
            if self.player_x < 0:
                self.player_running_to_left = True
        
        #look if you can add 1 pixel down
        for rects in self.solid_moverect_list:
            rects.top -= 1
            if self.UI_config_dict["Game"]["rects"]["player"]["pygame object"].colliderect(rects) == True:
                self.one_pixel_movement_allow = False
            rects.top += 1

        #add 1 pixel down
        if self.gravity_movement_allow != True:
            if self.one_pixel_movement_allow == True:
                for rects in self.solid_moverect_list:
                    rects.top -= 1
                for rects in self.unsolid_moverect_list:
                    rects.top -= 1
        
        #look if your in a Block
        for rect in self.solid_moverect_list:
            if self.UI_config_dict["Game"]["rects"]["player"]["pygame object"].colliderect(rect) == True:
                self.in_block = True
        
        #push you up if your stuck in a Block
        if self.in_block == True:
            print("stuck")
            for rect in self.solid_moverect_list:
                rect.top += self.config_dict["world"]["gravity"]
            for rect in self.unsolid_moverect_list:
                rect.top += self.config_dict["world"]["gravity"]
