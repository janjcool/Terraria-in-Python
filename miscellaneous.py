import configparser
import pprint

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
    files = ("config.ini", "entity_variables.ini", "template.ini")
    config_dict = {}
    variables = {}
    templates = {}

    for i in files:
        config = configparser.ConfigParser()
        config.read('save-data/' + str(i))
        
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
                
                elif config[str(x)][str(y)] == "False":
                    dictionary[str(y)] = False
                
                elif config[str(x)][str(y)] == "True":
                    dictionary[str(y)] = True
                    
                else:
                    dictionary[str(y)] = config[str(x)][str(y)]
                    
            print(dictionary)
            if x == "window":
                dictionary["display_width"] = display_info.current_w - 100
                dictionary["display_height"] = display_info.current_h - 100
            
            elif x == "general":
                dictionary["events"] = []
                dictionary["event_dict"] = {}
                    
            if i == "config.ini":
                config_dict[str(x)] = dictionary
            elif i == "entity_variables.ini":
                variables[str(x)] = dictionary
            elif i == "template.ini":
                templates[str(x)] = dictionary

    config_dict["entity_variables"] = variables
    config_dict["template"] = templates

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
        