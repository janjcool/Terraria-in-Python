import configparser

class exit:
    def __init__(self):
        print("exit")
        quit()

class menuManager:
    def __init__(self, config_dict, menu_type = "NO INPUT"):
        print("go to " + str(menu_type))
        config_dict["variables"]["main"]["first_frame_of_new_menu"] = True
        config_dict["window"]["display_choser"] = str(menu_type)

def config(display_info):
    config = configparser.ConfigParser()
    config.read('save-data/config.ini')
    
    config_dict = {}
    
    for x in config.sections():
        dictionary = {}
        
        for y in config[str(x)]:
            if isint(config[str(x)][str(y)]) == True:
                dictionary[str(y)] = int(config[str(x)][str(y)])
                
            elif isfloat(config[str(x)][str(y)]) == True:
                dictionary[str(y)] = float(config[str(x)][str(y)])
                
            elif x == "colors":
                color_list = []
                
                for i in config[str(x)][str(y)].split(", "):
                    color_list.append(int(i))
                dictionary[str(y)] = color_list
                
            else:
                dictionary[str(y)] = config[str(x)][str(y)]
                
        if x == "window":
            dictionary["display_width"] = display_info.current_w - 100
            dictionary["display_height"] = display_info.current_h - 100
                
        config_dict[str(x)] = dictionary

    entity_variables = configparser.ConfigParser()
    entity_variables.read('save-data/entity_variables.ini')
    
    variables = {}
    
    for x in entity_variables.sections():
        dictionary = {}
        
        for y in entity_variables[str(x)]:
            if isint(entity_variables[str(x)][str(y)]) == True:
                dictionary[str(y)] = int(entity_variables[str(x)][str(y)])
                
            elif isfloat(entity_variables[str(x)][str(y)]) == True:
                dictionary[str(y)] = float(entity_variables[str(x)][str(y)])
                
            elif entity_variables[str(x)][str(y)] == "False":
                dictionary[str(y)] = False
                
            elif entity_variables[str(x)][str(y)] == "True":
                dictionary[str(y)] = True
                
            else:
                dictionary[str(y)] = entity_variables[str(x)][str(y)]
        
        if x == "general":
            dictionary["events"] = []
            dictionary["event_dict"] = {}
                
        variables[str(x)] = dictionary
    
    config_dict["variables"] = variables
    
    return config_dict

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
        