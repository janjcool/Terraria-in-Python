import configparser

class exit:
    def __init__(self):
        print("exit")
        quit()

class menuManager:
    def __init__(self, config_dict, entity_variables, menu_type = "NO INPUT"):
        print("go to " + str(menu_type))
        entity_variables.first_frame_of_new_menu = True
        config_dict["window"]["display_choser"] = str(menu_type)

def config():
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
                
        config_dict[str(x)] = dictionary
    
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
        