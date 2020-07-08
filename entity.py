import numpy


class Block:
    def __init__(self, block_type, a_chunk_pos, a_block_pos):

        self.block_type = block_type

        self.chunk_pos = a_chunk_pos
        self.block_pos = a_block_pos


class Chunk:
    def __init__(self, position, config_dict):

        self.chunk_pos = position
        self.config_dict = config_dict
        self.chunk = numpy.empty((self.config_dict["worldGen"]["chunk_size"], self.config_dict["worldGen"]["chunk_size"]), dtype=object)

    def add_block(self, block, pos=(1000, 1000)):
        self.chunk[pos] = block


class World:
    def __init__(self, height, width, config_dict):
        self.height = height
        self.width = width
        self.config_dict = config_dict

        self.world = numpy.empty((5, 5), dtype=object)

    def find_chunk(self, block_pos=(5, 5)):
        self.pos_chunk = [int((block_pos[0] - 0.1) / self.config_dict["worldGen"]["chunk_size"]),
                          int((block_pos[1] - 0.1) / self.config_dict["worldGen"]["chunk_size"])]  # x, y

    def find_block(self, x, y):
        print("does nothing yet")


class Variables:
    def __init__(self, display_info):

        self.display_info = display_info
        self.map_width = 32 * 200  # the map width
        self.map_height = 32 * 12  # the map height
        self.seed = 1  # seed
        self.display_width = self.display_info.current_w - 100  # width of your screen
        self.display_height = self.display_info.current_h - 100  # height of your screen
        self.first_frame_of_new_menu = True  # if True then this is the first frame of a new menu
        self.temp_first_frame_of_new_menu = True  # temp version of previous variable
        self.events = []
        self.event_dict = {}

        # playerController
        self.temp_jump_length = 0
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
