import numpy

import config


class Block:
    def __init__(self, info_list: list, a_chunk_pos: tuple, a_block_pos: tuple):
        self.block_type: str
        self.sprite: str

        self.block_type = info_list[0]
        self.sprite = info_list[1]

        self.chunk_pos = a_chunk_pos
        self.block_pos = a_block_pos


class Chunk:
    def __init__(self, position: tuple, config_options: config.options):
        self.chunk_pos: tuple
        self.block_pos: tuple
        self.config_options: config.options

        self.chunk_pos = position
        self.config_options = config_options
        self.chunk = numpy.empty((self.config_options.chunk_size, self.config_options.chunk_size), dtype=object)

    def add_block(self, block, pos=(1000, 1000)):
        self.chunk[pos] = block


class World:
    def __init__(self, height: int, width: int, config_options: config.options):
        self.height = height
        self.width = width
        self.config_options = config_options

        self.world = numpy.empty((5, 5), dtype=object)

    def find_chunk(self, block_pos=(5, 5)):
        self.pos_chunk = [int((block_pos[0] - 0.1) / self.config_options.chunk_size),
                          int((block_pos[1] - 0.1) / self.config_options.chunk_size)]  # x, y

    def find_block(self, x, y):
        print("does nothing yet")


class Variables:
    def __init__(self, display_info):
        self.map_width: int
        self.map_height: int
        self.seed: int
        self.display_width: int
        self.display_height: int
        self.first_frame_of_new_menu: bool
        self.temp_first_frame_of_new_menu: bool

        self.display_info = display_info
        self.map_width = 32 * 200  # the map width
        self.map_height = 32 * 12  # the map height
        self.seed = 1  # seed
        self.display_width = self.display_info.current_w - 100  # width of your screen
        self.display_height = self.display_info.current_h - 100  # height of your screen
        self.first_frame_of_new_menu = True  # if True then this is the first frame of a new menu
        self.temp_first_frame_of_new_menu = True  # temp version of prevouise variable
        self.events = []
        self.event_dict = {}

        # playerController
        self.temp_jump_lenght = 0
        self.can_jump = True
        self.temp_player_crouching = True
        self.w_down = False
        self.s_down = False
        self.a_down = False
        self.d_down = False
        self.ctrl_down = False
        self.space_down = False

        # sprintLoader
        self.player_sprite_number = 0
        self.player_animation_timer = 0

        # main
        self.deltatime = 0
        self.mainloop = True
