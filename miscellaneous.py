def exit():
    print("exit")
    quit()

def menuManager(config_dict, menu_type = "NO INPUT"):
    print("go to " + str(menu_type))
    config_dict["variables"]["main"]["first_frame_of_new_menu"] = True
    config_dict["window"]["display_choser"] = str(menu_type)

def isfloat(x):
    try:
        float(x)
    except ValueError:
        return False
    else:
        return True

def isint(x):
    try:
        a = float(x)
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b

def gridmaker(x_range, y_range, append = []):
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
        return gridmaker(self.config_dict["worldGen"]["chunk_size"], self.config_dict["worldGen"]["chunk_size"])

    def make_chunks(self):
        chunk = self.make_chunk()
        return gridmaker(self.config_dict["variables"]["general"]["map_width"], self.config_dict["variables"]["general"]["map_height"], chunk)

def string_to_X(config_dict, string):
    string = string.replace("window_height", str(config_dict["window"]["window_height"]))
    string = string.replace("window_width", str(config_dict["window"]["window_width"]))
    
    if string[0] == "@":
        string = string.replace("@", "")
        mathString = mathString_to_list(string)
        string = mathString_to_number(mathString)
    elif string == "False":
        string = False
    elif string == "True":
        string = True
    else:
        string = string_to_number(string)
    
    return string

def mathString_to_list(string):
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
                
            mathList.append(string[temp_previous_counter:len(string)-1])
            goOn = False
    
    counter = 0
    for x in mathList:
        mathList[counter] = string_to_number(x)
        counter +=1
    
    return mathList

def string_to_number(string):
    if isint(string) == True:
        string = int(string)
    elif isfloat(string) == True:
        string = float(string)
    
    return string

def mathString_to_number(mathString):
    
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