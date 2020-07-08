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