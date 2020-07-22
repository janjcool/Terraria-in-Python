import configparser
import miscellaneous as misc
import pprint


def config(display_info):
    files = ("config.ini", "entity_variables.ini", "template.ini")
    config_dict = {}
    variables = {}
    templates = {}

    for i in files:
        config = configparser.ConfigParser()
        config.read('config/' + str(i))
        
        for x in config.sections():
            dictionary = {}
            
            for y in config[str(x)]:
                if misc.isint(config[str(x)][str(y)]) == True:
                    dictionary[str(y)] = int(config[str(x)][str(y)])
                    
                elif misc.isfloat(config[str(x)][str(y)]) == True:
                    dictionary[str(y)] = float(config[str(x)][str(y)])
                    
                elif x == "colors":
                    color_list = []
                    
                    for k in config[str(x)][str(y)].split(", "):
                        color_list.append(int(k))
                    dictionary[str(y)] = color_list
                
                elif config[str(x)][str(y)] == "False":
                    dictionary[str(y)] = False
                
                elif config[str(x)][str(y)] == "True":
                    dictionary[str(y)] = True
                    
                else:
                    dictionary[str(y)] = config[str(x)][str(y)]
                    
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
                
    config_dict["variables"] = variables
    config_dict["template"] = templates

    return config_dict

def UI_config_file(config_dict):
    files = ("mainMenu", "game", "gameMenu", "optionsMenu", "worldGen")
    UI_config_dict = {}
    
    for i in files:
        config = configparser.ConfigParser()
        config.read('config/UI/' + str(i) + ".ini")
        dictionary = {}
        
        for x in config.sections():
            temp_dictionary = {}
            
            for y in config[str(x)]:
                temp_list = []
                for k in config[str(x)][str(y)].split(", "):
                    k = misc.string_to_X(config_dict, k)
                    temp_list.append(k)
                    
                temp_dictionary[str(y)] = temp_list
        
            dictionary[str(x)] = temp_dictionary
        UI_config_dict[str(i)] = dictionary
        
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(UI_config_dict)
    
    return UI_config_dict