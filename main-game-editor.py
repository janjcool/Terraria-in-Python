"""
handy info:

first x then y
x = width
y = height
"""

from tkinter import *
from openpyxl import Workbook
import timeit


def callback(event):
    print ("clicked at " + str(event.x) + " " + str(event.y))

def new_grid_maker(file_name, sheet_name, width, height):
    wb = Workbook()
    new_grid_sheet = wb.active
    new_grid_sheet.title = str(sheet_name)

    temp_x_pos = 0
    temp_y_pos = 0

    start_timer_of_new_grid_maker = timeit.default_timer()

    for x in range(width):
        temp_x_pos += 1  
        temp_y_pos = 0

        print(str(temp_x_pos)+"/"+str(width))
        for i in range(height):
            
            temp_y_pos +=1

            line = (int(temp_x_pos)-1)*width + int(temp_y_pos)
            new_grid_sheet['A' + str(line)] = str(temp_x_pos)
            new_grid_sheet['B' + str(line)] = str(temp_y_pos)

    print("grid saved to local memory")
    stop_timer_of_new_grid_maker = timeit.default_timer()
    print('Time: ', stop_timer_of_new_grid_maker - start_timer_of_new_grid_maker)  

    wb.save("testniet.xltx")
    print("grid saved to drive")

def test_fuction(window):
    print("start of test_fuction")

    print(window.winfo_width())
    print(window.winfo_height())

def map_frame(window, screen_height, screen_width):
    map_frame = Frame(window, width=screen_width/15*11, height=200, bg = "#193bdf")
    #map_frame.grid(row = 1, column = 1)
    map_frame.focus_set()
    map_frame.bind("<Button-1>", callback)
    map_frame.pack()

def settings_frame(window, screen_height, screen_width):
    settings_frame = Frame(window, width=100, height=100, bg = "#d61f1f",)
    #map_frame.grid(row = 1, column = 1)
    settings_frame.pack()

def tkinter_console(window, screen_height, screen_width):
    tkinter_console = Label (window, bd = 5, text='test test dit moet lang', height = 20, width = 50, bg = "#808080")
    tkinter_console.pack()

def mainloop(window):
    print("hello")
    window.after(2000, lambda: mainloop(window)) # loop every 2 sec (1000 = 1 sec)


def main():
    window = Tk()
    window.title("game editor")
    
    window.geometry(str(1200)+'x'+str(700))

    screen_width = window.winfo_width()
    screen_height = window.winfo_height()

    print(screen_width)
    print(screen_height)

    window.after(2000, lambda: map_frame(window, screen_height, screen_width))
    window.after(2000, lambda: settings_frame(window, screen_height, screen_width))
    window.after(2000, lambda: tkinter_console(window, screen_height, screen_width))
    
    #button
    new_grid_button = Button(master=settings_frame, text='create new grid', command= lambda: new_grid_maker("test1", "sheet_3331", 100, 100))
    new_grid_button.pack()

    """

/////
het werkt niet want settings_frame zit in een fuctie en lijn 104 en 91 heeft die nodig dus moet ik return of zo gebreuken
////


    """

    #test button
    new_grid_button = Button(master=settings_frame, text='test button', command= lambda: test_fuction(window))
    new_grid_button.pack()

    window.after(2000, lambda: mainloop(window))
    window.mainloop()

if __name__ == '__main__':
    main()
