import pygame
pygame.init()

class mainMenu:
    def __init__(self, gameDisplay, config_rects_mainMenu, config_colors, config_options, config_fonts):
        self.gameDisplay = gameDisplay
        self.config_colors, self.config_rects_mainMenu, self.config_options, self.config_fonts = config_colors, config_rects_mainMenu, config_options, config_fonts
        
        self.main()
    
    def main(self):
        
        #background
        self.gameDisplay.fill(self.config_colors.GRAY)
        
        #UI
        self.gameDisplay.blit(self.config_rects_mainMenu.UI_rects_list[1], (int(self.config_options.width/2-125), int(self.config_options.height/2-50)))

class gameMenu:
    def __init__(self, gameDisplay, config_rects_gameMenu, config_colors, config_options, config_fonts):
        self.gameDisplay = gameDisplay
        self.config_colors, self.config_rects_gameMenu, self.config_options, self.config_fonts = config_colors, config_rects_gameMenu, config_options, config_fonts
        
        self.main()
    
    def main(self):
        
        #UI
        self.gameDisplay.blit(self.config_rects_gameMenu.UI_rects_list[2], (int(self.config_options.width/2-125), int(self.config_options.height/2-125)))
        self.gameDisplay.blit(self.config_rects_gameMenu.UI_rects_list[3], (int(self.config_options.width/2-125), int(self.config_options.height/2+25)))

class game:
    def __init__(self, gameDisplay, config_rects_game, config_colors, config_options, config_fonts):
        self.gameDisplay = gameDisplay
        self.config_colors, self.config_rects_game, self.config_options, self.config_fonts = config_colors, config_rects_game, config_options, config_fonts
        
        self.main()
    
    def main(self):
         
        #background
        self.gameDisplay.fill(self.config_colors.GRAY)
        self.gameDisplay.blit(self.config_rects_game.background_list_game[0], (0, 0))

        #floor
        pygame.draw.rect(self.gameDisplay, (16, 89, 15), self.config_rects_game.solid_moverect_list[0])
        pygame.draw.rect(self.gameDisplay, (150, 85, 6), self.config_rects_game.solid_moverect_list[2])

        #for ground
        pygame.draw.rect(self.gameDisplay, self.config_colors.GREEN, self.config_rects_game.unsolid_moverect_list[1])
        pygame.draw.rect(self.gameDisplay, (122, 84, 38), self.config_rects_game.unsolid_moverect_list[2])
        pygame.draw.rect(self.gameDisplay, self.config_colors.GREEN, self.config_rects_game.unsolid_moverect_list[3])
        pygame.draw.rect(self.gameDisplay, (122, 84, 38), self.config_rects_game.unsolid_moverect_list[0])
        pygame.draw.rect(self.gameDisplay, (107, 58, 22), self.config_rects_game.solid_moverect_list[1])
        
        #debugging 
        pygame.draw.rect(self.gameDisplay, self.config_colors.GREEN, self.config_rects_game.player_rect)      #enable for player collider
        
        #player
        self.gameDisplay.blit(self.config_rects_game.player_sprite, (int(self.config_options.width/2-32), int(self.config_options.height/2-32)))

        #UI
        pygame.draw.rect(self.gameDisplay, (33, 33, 33), self.config_rects_game.UI_rects_list_game[0])