import pygame
import conwaylife



def create_field(w, h):
    for y in range(1,h+1): 
        for x in range(1,w+1):
            pygame.draw.rect(window, color_of_field, pygame.Rect((10+2)*(y), (10+2)*(x), 10, 10))
    pygame.display.flip()

def draw_field(w, h):
    rect_arr = []
    for y in range(1,h+1): 
        for x in range(1,w+1):
            rect = pygame.Rect((10+2)*(y), (10+2)*(x), 10, 10)
            pygame.draw.rect(window, color_of_field, rect)
            rect_arr.append(rect)
    return rect_arr

def update_field(field:conwaylife.Field):
    for y in range(1, field.y_field+1):
        for x in range(1,field.x_field+1):
            if field.field[y][x] == 1:
                rect = pygame.Rect((10+2)*(y), (10+2)*(x), 10, 10)
                pygame.draw.rect(window, color_of_cells, rect)
            else: 
                rect = pygame.Rect((10+2)*(y), (10+2)*(x), 10, 10)
                pygame.draw.rect(window, color_of_field, rect)
    pygame.display.flip()

def change_color_of_celss_in_field():
    global rect_arr
    global color_of_cells
    global color_of_field
    for rect in rect_arr:
        collide =  [rect.x, rect.y] if isinstance(rect, pygame.Rect) else rect
        color = window.get_at(collide)
        if color == color_of_field or color == color_of_cells:
            pass
        else:
            pygame.draw.rect(window, color_of_cells, rect)


def change_color_of_field_in_field():
    global rect_arr
    global color_of_cells
    global color_of_field
    for rect in rect_arr:
        collide =  [rect.x, rect.y] if isinstance(rect, pygame.Rect) else rect
        color = window.get_at(collide)
        if color == color_of_cells or color == color_of_cells:
            pass
        else:
            pygame.draw.rect(window, color_of_field, rect)

def create_pattern(pattern):

    global field, rect_arr
    global mouse
    global FIELD_WIDTH
    global FIELD_HEIGTH
    global control_pattern
    for rect in rect_arr:
            collide =  [rect.x, rect.y] if isinstance(rect, pygame.Rect) else rect
            if collide[0] <= mouse[0] and collide[0]+10 >= mouse[0] and collide[1] <= mouse[1] and collide[1]+10 >= mouse[1]:
                for coor in pattern:
                    if (coor[0]+(collide[0]//12)-1) > FIELD_WIDTH:
                        x = coor[0]+(collide[0]//12)-FIELD_WIDTH-1
                    else: x = coor[0]+(collide[0]//12)-1
                    if (coor[1]+(collide[1]//12)-2) > FIELD_HEIGTH:
                        y = coor[1]+(collide[1]//12)-FIELD_HEIGTH-2
                    else: y = coor[1]+(collide[1]//12)-2
                    start_arr.append([x, y])
                    control_pattern = None
    field.empty()
    for item in start_arr:
        field = field.place(item[0], item[1], 1)
    update_field(field)

def color_time_buttons(time_1x_button, time_05x_button,time_15x_button,time_100x_button, coloring):
    global window, WINDOW_WIDTH, WINDOW_HEIGHT
    pygame.draw.rect(window, (10,110,100,255), time_1x_button)
    pygame.draw.rect(window, (10,110,100,255), time_05x_button)
    pygame.draw.rect(window, (10,110,100,255), time_15x_button)
    pygame.draw.rect(window, (10,110,100,255), time_100x_button)
    if coloring == 1:
        pygame.draw.rect(window, (140,6,6,255), time_1x_button)
    elif coloring == 5:
        pygame.draw.rect(window, (140,6,6,255), time_05x_button)
    elif coloring == 15:
        pygame.draw.rect(window, (140,6,6,255), time_15x_button)
    elif coloring == 100:
        pygame.draw.rect(window, (140,6,6,255), time_100x_button)
    time_1x_text = my_font.render('1x', False, (200, 200, 165))
    window.blit(time_1x_text, (WINDOW_WIDTH-60, WINDOW_HEIGHT-55))
    time_05x_text = my_font.render('0.5x', False, (180, 180, 180))
    window.blit(time_05x_text, (WINDOW_WIDTH-124, WINDOW_HEIGHT-55))
    time_15x_text = my_font.render('2x', False, (180, 180, 180))
    window.blit(time_15x_text, (WINDOW_WIDTH-170, WINDOW_HEIGHT-55))
    time_100x_text = my_font.render('10x', False, (180, 180, 180))
    window.blit(time_100x_text, (WINDOW_WIDTH-233, WINDOW_HEIGHT-55))


#Options and Const
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
FIELD_WIDTH = 60
FIELD_HEIGTH = 60

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('arial', 30)
pygame.display.set_caption('Conway')
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

BIRD_IMAGE = pygame.image.load('C:/Entwicklung/Python3/Conway/vogel.png').convert()
BIRD_ARR = [[5,1], [6,1] , [1,2], [2,2], [3,2], [4,2] , [6,2], [7,2], [1,3], [2,3] , [3,3], [4,3], [5,3], [6,3] , [2,4], [3,4], [4,4], [5,4]]
F_IMAGE = pygame.image.load('C:/Entwicklung/Python3/Conway/fPento.png').convert()
F_ARR = [[2,1], [3,1] , [1,2], [2,2], [2,3]]

color_of_cells = (255,0,0, 255)
color_of_field = (10,10,10,255)

FIELD_SIZE = [FIELD_WIDTH*12, FIELD_HEIGTH*12]
start_arr = []
fps = 100

running = True
field = conwaylife.Field(FIELD_WIDTH, FIELD_HEIGTH)

for item in start_arr:
    field = field.place(item[0], item[1], 1)



mouseClicked = False 
window.fill((25, 25, 25))
start = False
#create_field(FIELD_WIDTH, FIELD_HEIGTH)

#Create Start-Button
start_button = pygame.Rect(10, WINDOW_HEIGHT-50, 100, 50)
pygame.draw.rect(window, "green", start_button)
text_start_button = my_font.render('Start', False, (0, 0, 0))

#Create Reset-Button
reset_button = pygame.Rect(150, WINDOW_HEIGHT-50, 100, 50)
pygame.draw.rect(window, "blue", reset_button)
text_reset_button = my_font.render('Reset', False, (200, 200, 200))


#Create Color_Pallete for Cells
cell_pallette_start_button = my_font.render('Cells', False, (180, 180, 180))
window.blit(cell_pallette_start_button, (WINDOW_WIDTH-100, 10))
blue_color_button = pygame.Rect(WINDOW_WIDTH-100, 50, 50, 50)
pygame.draw.rect(window, "blue", blue_color_button)
red_color_button = pygame.Rect(WINDOW_WIDTH-100, 105, 50, 50)
pygame.draw.rect(window, "red", red_color_button)
green_color_button = pygame.Rect(WINDOW_WIDTH-100, 160, 50, 50)
pygame.draw.rect(window, "green", green_color_button)
purple_color_button = pygame.Rect(WINDOW_WIDTH-100, 215, 50, 50)
pygame.draw.rect(window, (255,0,255,255), purple_color_button)

#Create Color_Pallete for Field
field_pallette_start_button = my_font.render('Field', False, (180, 180, 180))
window.blit(field_pallette_start_button, (WINDOW_WIDTH-200, 10))
black_color_button = pygame.Rect(WINDOW_WIDTH-200, 50, 50, 50)
pygame.draw.rect(window, (10,10,10,255), black_color_button)
dark_grey_color_button = pygame.Rect(WINDOW_WIDTH-200, 105, 50, 50)
pygame.draw.rect(window, (100,100,100,255), dark_grey_color_button)
grey_color_button = pygame.Rect(WINDOW_WIDTH-200, 160, 50, 50)
pygame.draw.rect(window, (180,180,180,255), grey_color_button)
white_color_button = pygame.Rect(WINDOW_WIDTH-200, 215, 50, 50)
pygame.draw.rect(window, (255,255,255,255), white_color_button)

#Create Pattern-Palette
bird_pattern_button = BIRD_IMAGE.get_rect()
bird_pattern_button.center = WINDOW_WIDTH-150, WINDOW_HEIGHT-450
window.blit(BIRD_IMAGE, bird_pattern_button)
pygame.draw.rect(window, "black", bird_pattern_button, 1)

f_pattern_button = F_IMAGE.get_rect()
f_pattern_button.center = WINDOW_WIDTH-150, WINDOW_HEIGHT-370
window.blit(F_IMAGE, f_pattern_button)
pygame.draw.rect(window, "black", f_pattern_button, 1)


#Create Time-Palette

time_1x_button = pygame.Rect(WINDOW_WIDTH-70, WINDOW_HEIGHT-60, 50, 50)
time_05x_button = pygame.Rect(WINDOW_WIDTH-125, WINDOW_HEIGHT-60, 50, 50)
time_15x_button = pygame.Rect(WINDOW_WIDTH-180, WINDOW_HEIGHT-60, 50, 50)
time_100x_button = pygame.Rect(WINDOW_WIDTH-235, WINDOW_HEIGHT-60, 50, 50)



color_time_buttons(time_1x_button, time_05x_button, time_15x_button, time_100x_button, 1)


#Erstelle Feld das erste Mal
rect_arr = draw_field(FIELD_WIDTH, FIELD_HEIGTH)
control_pattern = None




#Window Schleife
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            mouseClicked = True
        if event.type == pygame.MOUSEBUTTONUP :
            mouseClicked = False

    mouse = pygame.mouse.get_pos()


    #Start-Button Handling
    window.blit(text_start_button, (35, WINDOW_HEIGHT-45))
    if start_button.collidepoint(mouse) and mouseClicked and not start:
        start = True
        pygame.draw.rect(window, "red", start_button)
        text_start_button = my_font.render('Stop', False, (0, 0, 0))
    elif start_button.collidepoint(mouse) and mouseClicked and start:
        start = False
        start_arr = []
        for rect in rect_arr:
            collide =  [rect.x, rect.y] if isinstance(rect, pygame.Rect) else rect
            color = window.get_at(collide)
            if color == color_of_cells:
                start_arr.append([collide[0]//12, collide[1]//12])
        pygame.draw.rect(window, "green", start_button)
        text_start_button = my_font.render('Start', False, (0, 0, 0))

        pygame.display.update()
        pygame.time.wait(100)
    
    #Reset-Button Handling
    window.blit(text_reset_button, (170, WINDOW_HEIGHT-45))
    if reset_button.collidepoint(mouse) and mouseClicked:
        start = False
        field.empty()
        start_arr= []
        for item in start_arr: 
            field = field.place(item[0], item[1], 1)
        update_field(field)
        pygame.draw.rect(window, "green", start_button)
        text_start_button = my_font.render('Start', False, (0, 0, 0))
        pygame.time.wait(100)

    #Drawing Celss handling
    if mouseClicked and start == False and not control_pattern:
        for rect in rect_arr:
            collide =  [rect.x, rect.y] if isinstance(rect, pygame.Rect) else rect
            color = window.get_at(collide)
            if collide[0] <= mouse[0] and collide[0]+10 >= mouse[0] and collide[1] <= mouse[1] and collide[1]+10 >= mouse[1] and color != color_of_cells:
                 pygame.draw.rect(window, color_of_cells, rect)
                 start_arr.append([collide[0]//12, collide[1]//12] )
                 
            elif collide[0] <= mouse[0] and collide[0]+10 >= mouse[0] and collide[1] <= mouse[1] and collide[1]+10 >= mouse[1] and color == color_of_cells:
                 pygame.draw.rect(window, color_of_field, rect)
                 start_arr.remove([collide[0]//12, collide[1]//12])
        field.empty()
        for item in start_arr:
            field = field.place(item[0], item[1], 1)

    #Color Palette handling Cells
    if green_color_button.collidepoint(mouse) and mouseClicked: 
        color_of_cells = (0,255,0,255)
        change_color_of_celss_in_field()
    elif blue_color_button.collidepoint(mouse) and mouseClicked: 
        color_of_cells = (0,0,255, 255)
        change_color_of_celss_in_field()
    elif red_color_button.collidepoint(mouse) and mouseClicked: 
        color_of_cells = (255,0,0,255)
        change_color_of_celss_in_field()
    elif purple_color_button.collidepoint(mouse) and mouseClicked: 
        color_of_cells = (255,0,255,255)
        change_color_of_celss_in_field()

        


    #Color Palette handling Field
    if black_color_button.collidepoint(mouse) and mouseClicked: 
        color_of_field = (0,0,0,255)
        change_color_of_field_in_field()
    elif dark_grey_color_button.collidepoint(mouse) and mouseClicked: 
        color_of_field = (100,100,100,255)
        change_color_of_field_in_field()
    elif grey_color_button.collidepoint(mouse) and mouseClicked: 
        color_of_field = (180,180,180,255)
        change_color_of_field_in_field()
    elif white_color_button.collidepoint(mouse) and mouseClicked: 
        color_of_field = (255,255,255,255)
        change_color_of_field_in_field()
    
    #Patter Pallete handling 
    if bird_pattern_button.collidepoint(mouse) and mouseClicked and not start: 
        control_pattern = "Bird"
    elif f_pattern_button.collidepoint(mouse) and mouseClicked and not start: 
        control_pattern = "f"
    if mouseClicked and control_pattern == "Bird":  
        create_pattern(BIRD_ARR)  
    elif mouseClicked and control_pattern == "f":  
        create_pattern(F_ARR)  
    
    #Time Pallete handling 
    if time_1x_button.collidepoint(mouse) and mouseClicked: 
        fps = 100
        color_time_buttons(time_1x_button, time_05x_button, time_15x_button, time_100x_button, 1)
    elif time_100x_button.collidepoint(mouse) and mouseClicked : 
        fps = 10
        color_time_buttons(time_1x_button, time_05x_button, time_15x_button, time_100x_button, 100)
    elif time_15x_button.collidepoint(mouse) and mouseClicked : 
        fps = 50
        color_time_buttons(time_1x_button, time_05x_button, time_15x_button, time_100x_button, 15)
    elif time_05x_button.collidepoint(mouse) and mouseClicked : 
        fps = 150 
        color_time_buttons(time_1x_button, time_05x_button, time_15x_button, time_100x_button, 5)


        
    mouseClicked = False
    pygame.display.update()
   

    if start == True:
        pygame.time.wait(fps)
        field.run_return()
        update_field(field)
    


pygame.quit()
