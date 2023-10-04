"""
In this project I will be creating part one of the Sand Game.

File Name: Abdellatif_Project3 .py
Author: Rana Abdellatif
Date: 01/28/2023
Course: COMP 1352
Assignment: Project 3 - Sand Game Pt.2
Collaborators: None
Internet Source: None

How to use:

To use sand, click 's' key.
To use water, click 'w' key.
To use lava, which overpowers water, click 'l' key.
To use floor, click 'f' key.
To quit, click 'q' key.
"""
import dudraw

#draws sand particles
def draw_world(a_list: list):
    global key
    if dudraw.has_next_key_typed():
        key = dudraw.next_key_typed()

    for i in range(len(a_list)):
        for j in range(len(a_list[0])):
            if a_list[i][j] == 1:  
                dudraw.set_pen_color_rgb(158, 137, 84)
                dudraw.filled_rectangle(i,j,0.5,0.5)
            elif a_list[i][j] == 2:
                dudraw.set_pen_color(dudraw.BLUE)
                dudraw.filled_rectangle(i,j,0.5,0.5)
            elif a_list[i][j] == 3:
                dudraw.set_pen_color_rgb(245, 65, 5)
                dudraw.filled_rectangle(i,j,0.5,0.5)
            elif a_list[i][j] == 4:
                dudraw.set_pen_color(dudraw.BLACK)
                dudraw.filled_rectangle(i,j,0.5,0.5)
            elif a_list[i][j] == 0:
                dudraw.set_pen_color_rgb(197, 228, 237)
                dudraw.filled_rectangle(i,j,0.5,0.5)


#updates the_world with sand particle based on mouse position
def place_sand(a_list: list, i:int, j:int)->list:
    if i < 100 and i > 0 and j < 100 and j > 0:
        if a_list[i][j] == 0:
            a_list[i][j] = 1
            a_list[i][j+1] = 1
            a_list[i][j-1] = 1
            a_list[i+1][j] = 1
            a_list[i-1][j] = 1
            a_list[i+1][j+1] = 1
            a_list[i-1][j-1] = 1
            a_list[i-1][j+1] = 1
            a_list[i+1][j-1] = 1  
    return a_list

#simulates sand falling
def swap_sand_particle(a_list: list)->list:
    for j in range(1,len(a_list[0])):
        for i in range(len(a_list)):
            if a_list[i][j] == 1:
                if a_list[i][j-1] == 0:
                    a_list[i][j] = 0
                    a_list[i][j-1] = 1
                elif a_list[i][j-1] == 1:
                    a_list[i][j] = 1

                elif a_list[i-1][j] == 0:
                    a_list[i][j] = 0
                    a_list[i-1][j] = 1
                elif a_list[i+1][j] == 0:
                    a_list[i][j]= 0
                    a_list[i+1][j] = 1
    return a_list

#water 
def place_water(a_list: list, i:int, j: int)->list:
    if i < 100 and i > 0 and j < 100 and j > 0:
        if a_list[i][j] == 0 or a_list[i][j] == 1:
            a_list[i][j] = 2
            a_list[i][j+1] = 2
            a_list[i][j-1] = 2
            a_list[i+1][j] = 2
            a_list[i-1][j] = 2
            a_list[i+1][j+1] = 2
            a_list[i-1][j-1] = 2
            a_list[i-1][j+1] = 2
            a_list[i+1][j-1] = 2  
    return a_list


def swap_water_particle(a_list:list)->list:
    for j in range(1,len(a_list[0])):
        for i in range(len(a_list)):
            if a_list[i][j] == 2:
                if a_list[i][j-1] == 0:
                    a_list[i][j] = 0
                    a_list[i][j-1] = 2
                elif a_list[i][j-1] == 1:
                    a_list[i][j] = 1
                    a_list[i][j-1] = 2
                elif a_list[i][j-1] == 2:
                    a_list[i][j] = 2

                #water flows -> "swaps" with side

                elif a_list[i-1][j] == 0:
                    a_list[i][j] = 0
                    a_list[i-1][j] = 2
                elif a_list[i+1][j] == 0:
                    a_list[i][j]= 0
                    a_list[i+1][j] = 2                   
                elif a_list[i-1][j-1] == 0:
                    a_list[i][j] = 0
                    a_list[i-1][j-1] = 2                
                elif a_list[i+1][j-1] == 0:
                    a_list[i][j] = 0
                    a_list[i+1][j-1] = 2


    return a_list
#lava
def place_lava(a_list: list, i: int, j:int)->list:
    if i < 100 and i > 0 and j < 100 and j > 0:
        if a_list[i][j] == 0 or a_list[i][j] == 1 or a_list[i][j] == 2:
            a_list[i][j] = 3
            a_list[i][j] = 3
            a_list[i][j+1] = 3
            a_list[i][j-1] = 3
            a_list[i+1][j] = 3
            a_list[i-1][j] = 3
            a_list[i+1][j+1] = 3
            a_list[i-1][j-1] = 3
            a_list[i-1][j+1] = 3
            a_list[i+1][j-1] = 3   
    return a_list

def swap_lava_particle(a_list:list)->list:
    for j in range(1,len(a_list[0])):
        for i in range(len(a_list)):
            if a_list[i][j] == 3:
                if a_list[i][j-1] == 0:
                    a_list[i][j] = 0
                    a_list[i][j-1] = 3
                elif a_list[i][j-1] == 1:
                    a_list[i][j] = 1
                    a_list[i][j-1] = 3
                elif a_list[i][j-1] == 2:
                    a_list[i][j] = 3
                elif a_list[i][j] == 3:
                    a_list[i][j] = 3

                elif a_list[i-1][j] == 0:
                    a_list[i][j] = 0
                    a_list[i-1][j] = 3
                elif a_list[i-1][j] == 1:
                    a_list[i][j] = 1
                    a_list[i-1][j] = 3
                elif a_list[i-1][j] == 2:
                    a_list[i][j] = 3
                
                elif a_list[i+1][j] == 0:
                    a_list[i][j] = 0
                    a_list[i+1][j] = 3
                elif a_list[i+1][j] == 1:
                    a_list[i][j] = 1
                    a_list[i+1][j] = 3
                elif a_list[i+1][j] == 2:
                    a_list[i][j] = 3
            
    return a_list

#floor
def place_floor(a_list: list, i: int, j:int)->list:
    if i < 100 and i > 0 and j < 100 and j > 0:
        if a_list[i][j] == 0:
            a_list[i][j] = 4
            a_list[i][j+1] = 4
            a_list[i][j-1] = 4
            a_list[i+1][j] = 4
            a_list[i-1][j] = 4
            a_list[i+1][j+1] = 4
            a_list[i-1][j-1] = 4
            a_list[i-1][j+1] = 4
            a_list[i+1][j-1] = 4    
    return a_list




#main
dudraw.set_canvas_size(500,500)
dudraw.set_x_scale(0,100)
dudraw.set_y_scale(0,100)
#key = ''
the_world = []
for i in range(100):
    inner_list = []
    for j in range(100):
        inner_list.append(0)
    the_world.append(inner_list)

#if dudraw.mouse_clicked('f') == True:
key = ''
while key != 'q':
    dudraw.clear_rgb(197, 228, 237)

    draw_world(the_world)
    if dudraw.mouse_is_pressed():
        x = int(dudraw.mouse_x())
        y = int(dudraw.mouse_y())

        if key == 's':
            the_world = place_sand(the_world,x,y)
            
        elif key == 'w':
            the_world = place_water(the_world,x,y)

        elif key == 'l':
            the_world = place_lava(the_world,x,y)

        elif key == 'f':
            the_world = place_floor(the_world,x,y)
            
    swap_sand_particle(the_world)
    swap_lava_particle(the_world)
    swap_water_particle(the_world)




       # swap_particle(the_world)

    dudraw.show(30)

    if dudraw.has_next_key_typed():
        key = dudraw.next_key_typed()