"""
handy info:

first x then y
x = width
y = height
"""

from tkinter import *
import linecache


def callback(event):
    print ("clicked at " + str(event.x) + " " + str(event.y))

def new_grid_maker(file_name, width, height):
    new_grid_file = open(file_name + ".txt","w+")

    temp_x_pos = 0
    temp_y_pos = 0

    for x in range(width):
        temp_x_pos += 1  
        temp_y_pos = 0
        for i in range(height):
            temp_y_pos +=1
            print(str(temp_x_pos) + ", " + str(temp_y_pos))
            new_grid_file.write(str(temp_x_pos) + ", " + str(temp_y_pos) + "\r\n")

    print("new grid made")
    new_grid_file.close()

def get_line(file_name, line):
    return linecache.getline(file_name+'.txt', int(line))

def get_line_of_pos(file_name, x, y):
    line = (int(x)-1)*500 + int(y)
    return linecache.getline(file_name+'.txt', int(line))


def main():
    width = 800
    height = 500

    print(get_line("test", 10192))
    print(get_line_of_pos("test", 21, 192))

    window = Tk()
    window.title("game editor")
    window.geometry(str(width)+'x'+str(height))

    frame = Frame(window, width=width, height=height)
    frame.focus_set()
    frame.bind("<Button-1>", callback)
    frame.pack()

    window.mainloop()

if __name__ == '__main__':
    main()
