from opensimplex import OpenSimplex
"""
from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

noise = OpenSimplex(seed=1)

noise.octaves = 8
noise.period = 20.0
noise.persistence = 0.8

test = []

for x in range(0, 100):
    for y in range(0,100):
        test.append(noise.noise2d(x=x, y=y))
        
        temp = noise.noise2d(x=x+1, y=y+1)
        
        sheet.cell(row=x+1, column=y+1).value = str(temp)
        print(x+1, y+1)
        
        
workbook.save(filename="hello_world.xlsx")
"""
class world:
    def __init__(self, size, config_options, seed = 1):
        self.noise = OpenSimplex(seed=seed)
        
        self.mapHeight_maker()
        
    def mapHeight_maker(self):
        self.mapHeight = []
        
        for x in range(0, 100):
            temp_noise = self.noise.noise2d(x=x, y=1)
            
            self.mapHeight.append(temp_noise)
        
        print(self.mapHeight)