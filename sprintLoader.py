import pygame
pygame.init()

class player_animation:
    def __init__(self, animation_type = "nothing", size = 1, player_sprite_number = 0):
        self.animation_type = animation_type
        self.size = size
        self.player_sprite_number = player_sprite_number
        
        if animation_type == "idle":
            idle00 = pygame.image.load("art-assets/player/sprites/adventurer-idle-00.png")
            idle00 = pygame.transform.scale(idle00, (int(50 * size), int(37 * size)))
            idle01 = pygame.image.load("art-assets/player/sprites/adventurer-idle-01.png")
            idle01 = pygame.transform.scale(idle01, (int(50 * size), int(37 * size)))
            idle02 = pygame.image.load("art-assets/player/sprites/adventurer-idle-02.png")
            idle02 = pygame.transform.scale(idle02, (int(50 * size), int(37 * size)))
            idle03 = pygame.image.load("art-assets/player/sprites/adventurer-idle-03.png")
            idle03 = pygame.transform.scale(idle03, (int(50 * size), int(37 * size)))
            
            animation_list = [idle00, idle01, idle02, idle03]
            self.player_sprite = animation_list[player_sprite_number]
            
        elif animation_type == "run right":
            run00 = pygame.image.load("art-assets/player/sprites/adventurer-run-00.png")
            run00 = pygame.transform.scale(run00, (int(50 * size), int(37 * size)))
            run01 = pygame.image.load("art-assets/player/sprites/adventurer-run-01.png")
            run01 = pygame.transform.scale(run01, (int(50 * size), int(37 * size)))
            run02 = pygame.image.load("art-assets/player/sprites/adventurer-run-02.png")
            run02 = pygame.transform.scale(run02, (int(50 * size), int(37 * size)))
            run03 = pygame.image.load("art-assets/player/sprites/adventurer-run-03.png")
            run03 = pygame.transform.scale(run03, (int(50 * size), int(37 * size)))
            run04 = pygame.image.load("art-assets/player/sprites/adventurer-run-04.png")
            run04 = pygame.transform.scale(run04, (int(50 * size), int(37 * size)))
            run05 = pygame.image.load("art-assets/player/sprites/adventurer-run-05.png")
            run05 = pygame.transform.scale(run05, (int(50 * size), int(37 * size)))     
            
            animation_list = [run00, run01, run02, run03, run04, run05]
            self.player_sprite = animation_list[player_sprite_number]
            
        elif animation_type == "run left":
            run00 = pygame.image.load("art-assets/player/sprites/adventurer-run-00.png")
            run00 = pygame.transform.scale(run00, (int(50 * size), int(37 * size)))
            run00 = pygame.transform.flip(run00, True, False)
            run01 = pygame.image.load("art-assets/player/sprites/adventurer-run-01.png")
            run01 = pygame.transform.scale(run01, (int(50 * size), int(37 * size)))
            run01 = pygame.transform.flip(run01, True, False)
            run02 = pygame.image.load("art-assets/player/sprites/adventurer-run-02.png")
            run02 = pygame.transform.scale(run02, (int(50 * size), int(37 * size)))
            run02 = pygame.transform.flip(run02, True, False)
            run03 = pygame.image.load("art-assets/player/sprites/adventurer-run-03.png")
            run03 = pygame.transform.scale(run03, (int(50 * size), int(37 * size)))
            run03 = pygame.transform.flip(run03, True, False)
            run04 = pygame.image.load("art-assets/player/sprites/adventurer-run-04.png")
            run04 = pygame.transform.scale(run04, (int(50 * size), int(37 * size)))
            run04 = pygame.transform.flip(run04, True, False)
            run05 = pygame.image.load("art-assets/player/sprites/adventurer-run-05.png")
            run05 = pygame.transform.scale(run05, (int(50 * size), int(37 * size)))     
            run05 = pygame.transform.flip(run05, True, False)
            
            animation_list = [run00, run01, run02, run03, run04, run05]
            self.player_sprite = animation_list[player_sprite_number]
        
        elif animation_type == "crouch right":
            crouch00 = pygame.image.load("art-assets/player/sprites/adventurer-crouch-00.png")
            crouch00 = pygame.transform.scale(crouch00, (int(50 * size), int(37 * size)))
            crouch01 = pygame.image.load("art-assets/player/sprites/adventurer-crouch-01.png")
            crouch01 = pygame.transform.scale(crouch01, (int(50 * size), int(37 * size)))
            crouch02 = pygame.image.load("art-assets/player/sprites/adventurer-crouch-02.png")
            crouch02 = pygame.transform.scale(crouch02, (int(50 * size), int(37 * size)))
            crouch03 = pygame.image.load("art-assets/player/sprites/adventurer-crouch-03.png")
            crouch03 = pygame.transform.scale(crouch03, (int(50 * size), int(37 * size)))
            
            animation_list = [crouch00, crouch01, crouch02, crouch03]
            self.player_sprite = animation_list[player_sprite_number]
            
        elif animation_type == "crouch left":
            crouch00 = pygame.image.load("art-assets/player/sprites/adventurer-crouch-00.png")
            crouch00 = pygame.transform.scale(crouch00, (int(50 * size), int(37 * size)))
            crouch00 = pygame.transform.flip(crouch00, True, False)
            crouch01 = pygame.image.load("art-assets/player/sprites/adventurer-crouch-01.png")
            crouch01 = pygame.transform.scale(crouch01, (int(50 * size), int(37 * size)))
            crouch01 = pygame.transform.flip(crouch01, True, False)
            crouch02 = pygame.image.load("art-assets/player/sprites/adventurer-crouch-02.png")
            crouch02 = pygame.transform.scale(crouch02, (int(50 * size), int(37 * size)))
            crouch02 = pygame.transform.flip(crouch02, True, False)
            crouch03 = pygame.image.load("art-assets/player/sprites/adventurer-crouch-03.png")
            crouch03 = pygame.transform.scale(crouch03, (int(50 * size), int(37 * size)))
            crouch03 = pygame.transform.flip(crouch03, True, False)
            
            animation_list = [crouch00, crouch01, crouch02, crouch03]
            self.player_sprite = animation_list[player_sprite_number]
            
        else:
            print("Error 001: script sprint-loader; dit is geen animation type")
            animation_list = []