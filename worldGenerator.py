from opensimplex import OpenSimplex
import entity
import numpy

class World:
    def __init__(self, config_dict):
        self.config_dict = config_dict
        self.world_class = entity.World(config_dict["variables"]["general"]["map_height"], config_dict["variables"]["general"]["map_width"], config_dict)
        #self.World = self.world_class.World
        
        self.mapHeight_maker()
        self.chunk_maker()
        self.make_sheet_with_cordinats()

    def mapHeight_maker(self):
        self.raw_mapHeight = []
        self.mapHeight = []
        noise = OpenSimplex(seed=self.config_dict["variables"]["general"]["seed"])

        #get raw noise data
        for x in range(0, int(self.config_dict["variables"]["general"]["map_width"]/self.config_dict["worldGen"]["distance_between_raw"]+2)):
            noise_output = noise.noise2d(x=x, y=1)
            
            noise_output = (noise_output+1)/(2/self.config_dict["worldGen"]["mountain_steepness"])
            noise_output = int(noise_output)
            
            self.raw_mapHeight.append(noise_output)
            

        #edit raw noise data (extra distance between each point)
        for x in range(0, int(self.config_dict["variables"]["general"]["map_width"]/self.config_dict["worldGen"]["distance_between_raw"])):
            temp_value = 0
            
            temp_difference_between_point = (self.raw_mapHeight[x]-self.raw_mapHeight[x+1])/self.config_dict["worldGen"]["distance_between_raw"]*-1
            
            for y in range(0, self.config_dict["worldGen"]["distance_between_raw"]):
                value = temp_difference_between_point + temp_value
                temp_value = value
                self.mapHeight.append(int(value+self.raw_mapHeight[x]))
                
    def chunk_maker(self):
        self.world_class.world = self.world = numpy.empty( (int(self.config_dict["variables"]["general"]["map_height"]/self.config_dict["worldGen"]["chunk_size"]), int(self.config_dict["variables"]["general"]["map_width"]/self.config_dict["worldGen"]["chunk_size"])), dtype=object)
        
        for x in range(0, int(self.config_dict["variables"]["general"]["map_height"]/self.config_dict["worldGen"]["chunk_size"])):
            for y in range(0, int(self.config_dict["variables"]["general"]["map_width"]/self.config_dict["worldGen"]["chunk_size"])):                
                self.world_class.world[x, y] = entity.Chunk((x, y), self.config_dict)
    
    def make_sheet_with_cordinats(self):
        
        #add blocks
        counter = 0
        for x in self.mapHeight:
            for y in range(0, self.config_dict["worldGen"]["amount_of_sky"]): #add sky
                self.world_class.find_chunk((y,counter))
                temp_block_pos = [(y-self.world_class.pos_chunk[0]*self.config_dict["worldGen"]["chunk_size"])-1, (counter-self.world_class.pos_chunk[1]*self.config_dict["worldGen"]["chunk_size"])-1]
                temp_block = entity.Block("sky", self.world_class.pos_chunk, temp_block_pos)
                self.world_class.world[self.world_class.pos_chunk[0], self.world_class.pos_chunk[1]].add_block(temp_block, (temp_block_pos[0], temp_block_pos[1]))          

            for i in range(0, x): #add more sky
                self.world_class.find_chunk((y + i,counter))
                temp_block_pos = [(y + i-self.world_class.pos_chunk[0]*self.config_dict["worldGen"]["chunk_size"])-1, (counter-self.world_class.pos_chunk[1]*self.config_dict["worldGen"]["chunk_size"])-1]
                temp_block = entity.Block("sky", self.world_class.pos_chunk, temp_block_pos)
                self.world_class.world[self.world_class.pos_chunk[0], self.world_class.pos_chunk[1]].add_block(temp_block, (temp_block_pos[0], temp_block_pos[1]))    

            for q in range(0, self.config_dict["variables"]["general"]["map_height"]-x-self.config_dict["worldGen"]["amount_of_sky"]+2):
                self.world_class.find_chunk((y + i + q,counter))
                temp_block_pos = [(y + i + q-self.world_class.pos_chunk[0]*self.config_dict["worldGen"]["chunk_size"])-1, (counter-self.world_class.pos_chunk[1]*self.config_dict["worldGen"]["chunk_size"])-1]
                temp_block = entity.Block("dirt", self.world_class.pos_chunk, temp_block_pos)
                self.world_class.world[self.world_class.pos_chunk[0], self.world_class.pos_chunk[1]].add_block(temp_block, (temp_block_pos[0], temp_block_pos[1]))    
            
            counter += 1