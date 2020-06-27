import numpy

class block:
    def __init__(self, info_list, chunk_pos, block_pos):
        self.block_type = info_list[0]
        self.sprite = info_list[1]
        
        self.chunk_pos = chunk_pos
        self.block_pos = block_pos
        
class chunk:
    def __init__(self, position, config_options):
        self.chunk_pos = position
        self.config_options = config_options
        self.chunk = numpy.empty((self.config_options.chunk_size, self.config_options.chunk_size), dtype=object)
        
    def add_block(self, block, pos = (1000, 1000)):
        self.chunk[pos] = block
        

class world:
    def __init__(self, height, width, config_options):
        self.height = height
        self.width = width
        self.config_options = config_options
        
        self.world = numpy.empty( (5, 5), dtype=object)
    
    def find_chunk(self, block_pos = (5, 5)):
        self.pos_chunk = [int((block_pos[0]-0.1) / self.config_options.chunk_size), int((block_pos[1]-0.1) / self.config_options.chunk_size)] #x, y
    
    def find_block(self, x, y):
        print("does nothing yet")
        
class variables:
    def __init__(self):
        self.map_width = 32 * 200 #the map width
        self.map_height = 32 * 12#the map height
        self.seed = 1 #seed