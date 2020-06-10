import pygame
pygame.init()

class player_animation_list:
    def __init__(self, animation_type = "nothing", what_item = 0, size = 1):
        self.animation_type = animation_type
        self.what_item = what_item
        self.size = size

        def idle_animation(self):
            idle00 = pygame.image.load("art-assets/player/sprites/adventurer-idle-00.png")
            idle00 = pygame.transform.scale(idle00, (50 * size, 37 * size))
            idle01 = pygame.image.load("art-assets/player/sprites/adventurer-idle-01.png")
            idle01 = pygame.transform.scale(idle01, (50 * size, 37 * size))
            idle02 = pygame.image.load("art-assets/player/sprites/adventurer-idle-02.png")
            idle02 = pygame.transform.scale(idle02, (50 * size, 37 * size))
            idle03 = pygame.image.load("art-assets/player/sprites/adventurer-idle-03.png")
            idle03 = pygame.transform.scale(idle03, (50 * size, 37 * size))
            
            animation_list = [idle00, idle01, idle02, idle03]
            
            return animation_list[what_item]
        def idle_animation(self):
            run00 = pygame.image.load("art-assets/player/sprites/adventurer-run-00.png")
            run00 = pygame.transform.scale(run00, (50 * size, 37 * size))
            run01 = pygame.image.load("art-assets/player/sprites/adventurer-run-01.png")
            run01 = pygame.transform.scale(run01, (50 * size, 37 * size))
            run02 = pygame.image.load("art-assets/player/sprites/adventurer-run-02.png")
            run02 = pygame.transform.scale(run02, (50 * size, 37 * size))
            run03 = pygame.image.load("art-assets/player/sprites/adventurer-run-03.png")
            run03 = pygame.transform.scale(run03, (50 * size, 37 * size))
            run04 = pygame.image.load("art-assets/player/sprites/adventurer-run-04.png")
            run04 = pygame.transform.scale(run04, (50 * size, 37 * size))
            run05 = pygame.image.load("art-assets/player/sprites/adventurer-run-05.png")
            run05 = pygame.transform.scale(run05, (50 * size, 37 * size))
            
            animation_list = [run00, run01, run02, run03, run04, run05]
            
            return animation_list[what_item]
     
        if animation_type == "idle":
            idle_animation(self)
        elif animation_type == "run":
            run(self)
        else:
            print("Error 001: script sprint-loader; dit is geen animation type")
    
print(player_animation_list("idle", 2, 2))