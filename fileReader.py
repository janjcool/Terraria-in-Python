import configparser
import miscellaneous as misc
import pygame


def config(display_info):
    #this is a function that reads the config files
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
    #this is a function that reads the UI config files
    files = ("MainMenu", "Game", "GameMenu", "OptionsMenu", "WorldGen")
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
        
    UI_config_dict = UI_config_converter(config_dict, UI_config_dict)
    
    return UI_config_dict

def UI_config_converter(config_dict, UI_config_dict):
    #this is a function that converts the UI_config dictionary to pygame rects
    
    for i in UI_config_dict:
        for x in UI_config_dict[str(i)]:
            if x == "images":
                for y in UI_config_dict[str(i)][str(x)]:
                    temp_image = pygame.image.load(str(UI_config_dict[str(i)][str(x)][str(y)][2]))
                    temp_image = pygame.transform.scale(temp_image, (UI_config_dict[str(i)][str(x)][str(y)][5], UI_config_dict[str(i)][str(x)][str(y)][6]))
                    UI_config_dict[str(i)][str(x)][str(y)].insert(0, temp_image)
            elif x == "rects":
                for y in UI_config_dict[str(i)][str(x)]:
                    temp_rect = pygame.Rect(UI_config_dict[str(i)][str(x)][str(y)][0], UI_config_dict[str(i)][str(x)][str(y)][1], UI_config_dict[str(i)][str(x)][str(y)][2], UI_config_dict[str(i)][str(x)][str(y)][3])
                    UI_config_dict[str(i)][str(x)][str(y)].insert(0, temp_rect)
                    del UI_config_dict[str(i)][str(x)][str(y)][1:5]
            elif x == "text":
                for y in UI_config_dict[str(i)][str(x)]:
                    temp_text = pygame.font.Font(str(UI_config_dict[str(i)][str(x)][str(y)][2]), UI_config_dict[str(i)][str(x)][str(y)][3]).render(str(UI_config_dict[str(i)][str(x)][str(y)][4]), True, config_dict["colors"][str(UI_config_dict[str(i)][str(x)][str(y)][5])])
                    UI_config_dict[str(i)][str(x)][str(y)].insert(0, temp_text)
            else:
                print("one of the sections in a UI config file is wrong (this is how to wrong sections was write: " + str(x) + ")")
    
    return UI_config_dict