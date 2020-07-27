def exit():
    print("exit")
    quit()

def menuManager(config_dict, UI_config_dict, menu_type = "NO INPUT"):
    #this is a function that changes the menu
    UI_config_dict["renderer class"].reset_render_type()
    config_dict["variables"]["main"]["firstframe"] = True
    print("go to " + str(menu_type))
    config_dict["window"]["display_choser"] = str(menu_type)

def isfloat(x):
    #this is a function that checks if x is a float
    try:
        float(x)
    except ValueError:
        return False
    else:
        return True

def isint(x):
    #this is a function that checks if x is a float
    try:
        a = float(x)
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b

def gridmaker(x_range, y_range, append = []):
    #this makes a grid
    width = []
    for x in range(0, int(x_range)):
        height = []
        for y in range(0, int(y_range)):                
            height.append(append)
        width.append(height)
    
    del x, y    
    return width

class World:
    def __init__(self, config_dict):
        self.config_dict = config_dict

    def find_chunk(self, block_pos=(5, 5)): #height, width
        #this finds a chunk with a block position
        return (int((block_pos[0] - 0.1) / self.config_dict["worldGen"]["chunk_size"]), # x
                int((block_pos[1] - 0.1) / self.config_dict["worldGen"]["chunk_size"])) # y

    def find_block(self, x, y):
        #this finds a block pos in chunk pos with block pos
        print("does nothing yet")
        
    def make_block(self, block_type, pos):
        #this makes a block
        if  not (isinstance(block_type, str) and isinstance(pos, tuple)):
            print("world.make_block wrong type:")
            print("    " + str(block_type) + ": " + str(type(block_type)))
            print("    " + str(pos) + ": " + str(type(pos)))
            
        return [block_type, pos]

    def make_chunk(self):
        #this makes a chunk
        return gridmaker(self.config_dict["worldGen"]["chunk_size"], self.config_dict["worldGen"]["chunk_size"])

    def make_chunks(self):
        #this makes a grid of chunks (depended on how many chunks in the map fits)
        chunk = self.make_chunk()
        return gridmaker(self.config_dict["variables"]["general"]["map_width"], self.config_dict["variables"]["general"]["map_height"], chunk)

def string_to_X(config_dict, string):
    #this converst a string to a type of variables (example: "True" -> True)
    string = string.replace("window_height", str(config_dict["window"]["window_height"]))
    string = string.replace("window_width", str(config_dict["window"]["window_width"]))
    
    if string[0] == "@":
        string = string.replace("@", "")
        mathString = mathString_to_mathList(string)
        string = mathList_to_number(mathString)
    elif string == "False":
        string = False
    elif string == "True":
        string = True
    else:
        string = string_to_number(string)
    
    return string

def mathString_to_mathList(string):
    #this converts a mathString to a list (example: "100/2" -> [100, "/", 2])
    goOn = True
    counter = 0
    previous_counter = 0
    mathList = []
    while goOn:
        counter += 1
        if string[counter+previous_counter].isnumeric():
            pass
        else:
            temp_previous_counter = previous_counter
            if temp_previous_counter != 0:
                temp_previous_counter = temp_previous_counter+1
            
            mathList.append(string[temp_previous_counter:previous_counter+counter])
            mathList.append(string[previous_counter+counter:previous_counter+counter+1])
            previous_counter = counter + previous_counter
            counter = 0
            
        if previous_counter + counter == len(string)-1:
            temp_previous_counter = previous_counter
            if temp_previous_counter != 0:
                temp_previous_counter = temp_previous_counter+1
                
            mathList.append(string[temp_previous_counter:len(string)])
            goOn = False
    
    counter = 0
    for x in mathList:
        mathList[counter] = string_to_number(x)
        counter +=1
    
    return mathList

def string_to_number(string):
    #this converts a string to a number (with use of isfloat function and isint function)
    if isint(string) == True:
        string = int(string)
    elif isfloat(string) == True:
        string = float(string)
    
    return string

def mathList_to_number(mathString):
    #this converts a mathList (see the function mathString_to_mathList) to a number (example: [100, "/", 2] -> 50)
    counter = -1
    for x in mathString:
        counter += 1
        if x == "/":
            temp_number = mathString[counter-1]/mathString[counter+1]
            mathString[counter] = temp_number
            del mathString[counter+1]
            del mathString[counter-1]
        elif x == "*":
            temp_number = mathString[counter-1]*mathString[counter+1]
            mathString[counter] = temp_number
            del mathString[counter+1]
            del mathString[counter-1]
    
    counter = -1
    for x in mathString:
        counter += 1
        if x == "+":
            temp_number = mathString[counter-1]+mathString[counter+1]
            mathString[counter] = temp_number
            del mathString[counter+1]
            del mathString[counter-1]
        elif x == "-":
            temp_number = mathString[counter-1]-mathString[counter+1]
            mathString[counter] = temp_number
            del mathString[counter+1]
            del mathString[counter-1]    
    return int(mathString[0])