import ctypes
import os
from PIL import Image, ImageDraw, ImageFont
import keyboard
import time
import random


white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 1920
dis_height = 1080
  
snake_block = 20
snakeSize = 50
snake_speed = 0.08

foodx = 0
foody = 0


def gameLoop():
    game_over = True
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(snakeSize, dis_width - snake_block) / 100.0) * 100.0
    foody = round(random.randrange(snakeSize, dis_height - snake_block) / 100.0) * 100.0
    
    img = Image.new('RGB', (dis_width, dis_height), '#202020')
    idraw = ImageDraw.Draw(img)
    time.sleep(0.1)

    img.save('test1.jpg')

    ctypes.windll.user32.SystemParametersInfoA(20, 0, os.path.abspath("D:/Python/game in desktop/test1.jpg").encode() , 0)

    while game_over:
        keyboard.wait('t')
        game_over = False

    while not game_over:
        while game_close:
            gameLoop()

        # if keyboard.is_pressed('u'):
        #     gameLoop()

        if keyboard.is_pressed('left arrow'):
            x1_change = -snake_block
            y1_change = 0

        elif keyboard.is_pressed('right arrow'):
            x1_change = snake_block
            y1_change = 0

        elif keyboard.is_pressed('up arrow'):
            y1_change = -snake_block
            x1_change = 0

        elif keyboard.is_pressed('down arrow'):
            y1_change = snake_block
            x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        time.sleep(snake_speed)
        
        img = Image.new('RGB', (dis_width, dis_height), '#202020')
        idraw = ImageDraw.Draw(img)

        for x in snake_List:
            idraw.rectangle((x[0] - snakeSize, x[1] - snakeSize, x[0], x[1]), fill='white')

        idraw.rectangle((foodx - snakeSize, foody - snakeSize, foodx, foody), fill='#cf0a2c')

        img.save('test1.jpg')

        ctypes.windll.user32.SystemParametersInfoA(20, 0, os.path.abspath("D:/Python/game in desktop/test1.jpg").encode() , 0)
            
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(snakeSize, dis_width - snake_block) / 100.0) * 100.0
            foody = round(random.randrange(snakeSize, dis_height - snake_block) / 100.0) * 100.0
            Length_of_snake += 10

gameLoop()


# python "D:/Python/game in desktop/game.py"