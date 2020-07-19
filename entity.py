import miscellaneous as misc

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
    def __init__(self, config_dict):
        self.config_dict = config_dict

    def find_chunk(self, block_pos=(5, 5)): #height, width
        return (int((block_pos[0] - 0.1) / self.config_dict["worldGen"]["chunk_size"]), # x
                int((block_pos[1] - 0.1) / self.config_dict["worldGen"]["chunk_size"])) # y

    def find_block(self, x, y):
        print("does nothing yet")
        
    def make_block(self, block_type, pos):
        if  not (isinstance(block_type, str) and isinstance(pos, tuple)):
            print("world.make_block wrong type:")
            print("    " + str(block_type) + ": " + str(type(block_type)))
            print("    " + str(pos) + ": " + str(type(pos)))
            
        return [block_type, pos]

    def make_chunk(self):
        return misc.gridmaker(self.config_dict["worldGen"]["chunk_size"], self.config_dict["worldGen"]["chunk_size"])

    def make_chunks(self):
        chunk = self.make_chunk()
        return misc.gridmaker(self.config_dict["variables"]["general"]["map_width"], self.config_dict["variables"]["general"]["map_height"], chunk)