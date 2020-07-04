
class exit:
    def __init__(self):
        print("exit")
        quit()

class menuManager:
    def __init__(self, config_options, entity_variables, menu_type = "NO INPUT"):
        print("go to" + str(menu_type))
        entity_variables.first_frame_of_new_menu = True
        config_options.displayer_choser = str(menu_type)
        