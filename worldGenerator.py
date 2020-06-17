from opensimplex import OpenSimplex
from openpyxl import Workbook

class world:
    def __init__(self, size, config_options, height = 60, amount_of_sky = 1, world_height = 300, world_width = 500, distance_between_raw = 10, seed = 1):
        self.height = height #the height of hills (less also meens more smoothness)
        self.world_height = world_height #how heigh te world is
        self.world_width = world_width # the width of the map
        self.distance_between_raw = distance_between_raw # !!! this must be divisible by world_width !!! 
        self.amount_of_sky = amount_of_sky #how much sky is applied at the top
        
        self.workbook = Workbook()
        self.sheet = self.workbook.active
        self.noise = OpenSimplex(seed=seed)
        
        self.mapHeight_maker()
        self.make_sheet_with_cordinats()
        
        self.workbook.save(filename="hello_world.xlsx")
        
    def mapHeight_maker(self):
        self.raw_mapHeight = []
        self.mapHeight = []

        #get raw noise data
        for x in range(0, int(self.world_width/self.distance_between_raw+2)):
            temp_noise = self.noise.noise2d(x=x, y=1)
            
            temp_noise = (temp_noise+1)/(2/self.height)
            temp_noise = int(temp_noise)
            
            self.raw_mapHeight.append(temp_noise)
            

        #edit raw noise data (extra distance between each point)
        for x in range(0, int(self.world_width/self.distance_between_raw)):
            temp_value = 0
            
            temp_difference_between_point = (self.raw_mapHeight[x]-self.raw_mapHeight[x+1])/self.distance_between_raw*-1
            
            for y in range(0, self.distance_between_raw):
                value = temp_difference_between_point + temp_value
                temp_value = value
                self.mapHeight.append(int(value+self.raw_mapHeight[x]))
                
    def make_sheet_with_cordinats(self):
        counter = 0
        #add blocks
        for x in self.mapHeight:
            counter +=1
            sheet_list = []
            
            for y in range(0, self.amount_of_sky): #add sky
                sheet_list.append(0)
            for y in range(0, x): #add more sky
                sheet_list.append(0)
            for y in range(0, self.world_height-x-self.amount_of_sky):
                sheet_list.append(1)
            
            for y in range(0, self.world_height): #add dirt
                temp_cor = sheet_list[y]
            
                self.sheet.cell(row=y+1, column=counter).value = str(temp_cor)