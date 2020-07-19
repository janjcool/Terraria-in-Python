from opensimplex import OpenSimplex
import entity
import numpy
import sys

class World:
    def __init__(self, config_dict, world):
        self.config_dict = config_dict
        self.world_class = entity.World(config_dict)
        self.world = world
        
        self.mapHeight_maker()
        self.world["world"] = self.world_class.make_chunks()
        self.make_sheet_with_cordinats()
        
        print(sys.getsizeof(self.world["world"]))

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
    
    def make_sheet_with_cordinats(self):
        
        #add blocks
        counter = 0
        for x in self.mapHeight:
            for y in range(0, self.config_dict["worldGen"]["amount_of_sky"]): #add sky
                temp_chunk_pos = self.world_class.find_chunk((y,counter))
                temp_block_pos_in_chunk = ((y-temp_chunk_pos[0]*self.config_dict["worldGen"]["chunk_size"])-1, (counter-temp_chunk_pos[1]*self.config_dict["worldGen"]["chunk_size"])-1)
                temp_block = self.world_class.make_block("sky", temp_block_pos_in_chunk)
                self.world["world"][temp_chunk_pos[0]][temp_chunk_pos[1]][temp_block_pos_in_chunk[0]][temp_block_pos_in_chunk[1]] = temp_block

            for i in range(0, x): #add more sky
                temp_chunk_pos = self.world_class.find_chunk((y + i,counter))
                temp_block_pos_in_chunk = ((y + i-temp_chunk_pos[0]*self.config_dict["worldGen"]["chunk_size"])-1, (counter-temp_chunk_pos[1]*self.config_dict["worldGen"]["chunk_size"])-1)
                temp_block = self.world_class.make_block("sky", temp_block_pos_in_chunk)   
                self.world["world"][temp_chunk_pos[0]][temp_chunk_pos[1]][temp_block_pos_in_chunk[0]][temp_block_pos_in_chunk[1]] = temp_block

            for q in range(0, self.config_dict["variables"]["general"]["map_height"]-x-self.config_dict["worldGen"]["amount_of_sky"]+2):
                temp_chunk_pos = self.world_class.find_chunk((y + i + q,counter))
                temp_block_pos_in_chunk = ((y + i + q-temp_chunk_pos[0]*self.config_dict["worldGen"]["chunk_size"])-1, (counter-temp_chunk_pos[1]*self.config_dict["worldGen"]["chunk_size"])-1)
                temp_block = self.world_class.make_block("dirt", temp_block_pos_in_chunk)
                self.world["world"][temp_chunk_pos[0]][temp_chunk_pos[1]][temp_block_pos_in_chunk[0]][temp_block_pos_in_chunk[1]] = temp_block
            
            counter += 1