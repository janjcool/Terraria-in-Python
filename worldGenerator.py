from opensimplex import OpenSimplex
import entity
import numpy

class world:
    def __init__(self, config_options, entity_variables):
        self.config_options = config_options
        self.entity_variables = entity_variables
        self.world_class = entity.world(entity_variables.map_height, entity_variables.map_width, config_options)
        #self.world = self.world_class.world
        
        self.mapHeight_maker()
        self.chunk_maker()
        self.make_sheet_with_cordinats()

    def mapHeight_maker(self):
        self.raw_mapHeight = []
        self.mapHeight = []
        noise = OpenSimplex(seed=self.entity_variables.seed)

        #get raw noise data
        for x in range(0, int(self.entity_variables.map_width/self.config_options.distance_between_raw+2)):
            noise_ouput = noise.noise2d(x=x, y=1)
            
            noise_ouput = (noise_ouput+1)/(2/self.config_options.mountain_steepness)
            noise_ouput = int(noise_ouput)
            
            self.raw_mapHeight.append(noise_ouput)
            

        #edit raw noise data (extra distance between each point)
        for x in range(0, int(self.entity_variables.map_width/self.config_options.distance_between_raw)):
            temp_value = 0
            
            temp_difference_between_point = (self.raw_mapHeight[x]-self.raw_mapHeight[x+1])/self.config_options.distance_between_raw*-1
            
            for y in range(0, self.config_options.distance_between_raw):
                value = temp_difference_between_point + temp_value
                temp_value = value
                self.mapHeight.append(int(value+self.raw_mapHeight[x]))
                
    def chunk_maker(self):
        self.world_class.world = self.world = numpy.empty( (int(self.entity_variables.map_height/self.config_options.chunk_size), int(self.entity_variables.map_width/self.config_options.chunk_size)), dtype=object)
        
        for x in range(0, int(self.entity_variables.map_height/self.config_options.chunk_size)):
            for y in range(0, int(self.entity_variables.map_width/self.config_options.chunk_size)):                
                self.world_class.world[x, y] = entity.chunk((x, y), self.config_options)
    
    def make_sheet_with_cordinats(self):
        
        #add blocks
        counter = 0
        for x in self.mapHeight:
            for y in range(0, self.config_options.amount_of_sky): #add sky
                self.world_class.find_chunk((y,counter))
                temp_block_pos = [(y-self.world_class.pos_chunk[0]*self.config_options.chunk_size)-1, (counter-self.world_class.pos_chunk[1]*self.config_options.chunk_size)-1]
                temp_block = entity.block(self.config_options.sky, self.world_class.pos_chunk, temp_block_pos)
                self.world_class.world[self.world_class.pos_chunk[0], self.world_class.pos_chunk[1]].add_block(temp_block, (temp_block_pos[0], temp_block_pos[1]))          

            for i in range(0, x): #add more sky
                self.world_class.find_chunk((y + i,counter))
                temp_block_pos = [(y + i-self.world_class.pos_chunk[0]*self.config_options.chunk_size)-1, (counter-self.world_class.pos_chunk[1]*self.config_options.chunk_size)-1]
                temp_block = entity.block(self.config_options.sky, self.world_class.pos_chunk, temp_block_pos)
                self.world_class.world[self.world_class.pos_chunk[0], self.world_class.pos_chunk[1]].add_block(temp_block, (temp_block_pos[0], temp_block_pos[1]))    

            for q in range(0, self.entity_variables.map_height-x-self.config_options.amount_of_sky+2):
                self.world_class.find_chunk((y + i + q,counter))
                temp_block_pos = [(y + i + q-self.world_class.pos_chunk[0]*self.config_options.chunk_size)-1, (counter-self.world_class.pos_chunk[1]*self.config_options.chunk_size)-1]
                temp_block = entity.block(self.config_options.dirt, self.world_class.pos_chunk, temp_block_pos)
                self.world_class.world[self.world_class.pos_chunk[0], self.world_class.pos_chunk[1]].add_block(temp_block, (temp_block_pos[0], temp_block_pos[1]))    
            
            counter += 1