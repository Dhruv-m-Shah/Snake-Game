# -*- coding: utf-8 -*-
"""
Created on Sat May 11 21:53:58 2019

@author: dhruv
"""
import pygame
import random

pygame.init()

win = pygame.display.set_mode((19*40, 19*40))
pygame.display.set_caption("Snake Game")
score = -1

def end_screen():
    Letters = pygame.image.load('SnakeGameText.png')
    back_ground = pygame.image.load('loading_screen.png')
    back_ground = pygame.transform.scale(back_ground, (672, 420))
    gameDisplay = pygame.display.set_mode((700, 450))
    gameDisplay.blit(back_ground, (14, 15))
    gameDisplay.blit(Letters, (125, 15))
    pygame.display.update()
    myfont = pygame.font.SysFont('Comic Sans MS', 70)
    GameOver = myfont.render("GAME OVER", False, (255, 255, 255))
    Score = myfont.render("Score: " + str(score), False, (255, 255, 255))
    win.blit(GameOver,(66, 73))
    win.blit(Score,(66, 150))
    return True
def detect_collision():
    for i in range(1, len(square_array)):
        if(square_array[i][0] == square_array[0][0] and square_array[i][1] == square_array[0][1]):
            return end_screen()
    return False 


def initialsetup():
        pygame.draw.rect(win, (51, 102, 0), (0, 0, 19*40, 20))
        pygame.draw.rect(win, (51, 102, 0), (0, 0, 20, 19*40))
        pygame.draw.rect(win, (51, 102, 0), (0, 19*40-20, 19*40, 20))
        pygame.draw.rect(win, (51, 102, 0), (19*40-20, 0, 20, 19*40))
        for i in range(18):
            for j in range(18):
                if((i+j)%2 == 0):
                    pygame.draw.rect(win, (0, 153, 0), (20+40*j, 20+40*i, 40, 40))
                if((i+j)%2 == 1):
                    pygame.draw.rect(win, (0, 204, 0), (20+40*j, 20+40*i, 40, 40))
        pygame.display.update()


def pos_update():
    for i in range(len(square_array)):
        pygame.draw.rect(win, (255, 0, 0), (square_array[i][0]*40+20, square_array[i][1]*40+20, 40, 40))

def update_square_array():
    
        for i in range(len(square_array)):
            if(square_moves[i] == "R"):
                square_array[i] = (square_array[i][0]+1, square_array[i][1])
            if(square_moves[i] == "L"):
                square_array[i] = (square_array[i][0]-1, square_array[i][1])
            if(square_moves[i] == "U"):
                square_array[i] = (square_array[i][0], square_array[i][1]-1)
            if(square_moves[i] == "D"):
                    square_array[i] = (square_array[i][0], square_array[i][1]+1)
                    
        for i in range(len(square_array)):
            if(square_array[i][0]<0):
                square_array[i]= (17, square_array[i][1])
            if(square_array[i][0]>17):
                square_array[i] = (0, square_array[i][1])
            if(square_array[i][1]<0):
                square_array[i] = (square_array[i][0], 17)
            if(square_array[i][1]>17):
                square_array[i] = (square_array[i][0], 0)
                

                    
        for i in range(len(square_array)):
            for j in range(len(turns)):
                if(turns[j]!="DONE"):
                    if(square_array[i][0] == turn_position[j][0] and square_array[i][1] == turn_position[j][1]):
                        square_moves[i] = turns[j]
                        if(i == len(square_array) - 1):
                            turns[j] = "DONE"
                            turn_position[j] = (-1, -1)

        pos_update()

            
def snake_longer():
    
    t = len(square_array)-1
    if(square_moves[t] == "U"):
        square_array.append((square_array[t][0], square_array[t][1]+1))
        square_moves.append("U")
    if(square_moves[t] == "D"):
        square_array.append((square_array[t][0], square_array[t][1]-1))
        square_moves.append("D")
    if(square_moves[t] == "R"):
        square_array.append((square_array[t][0]-1, square_array[t][1]))
        square_moves.append("R")
    if(square_moves[t] == "L"):
        square_array.append((square_array[t][0]+1, square_array[t][1]))
        square_moves.append("L")
    
    update_square_array()
    

def biting_sound():
    apple_biting_sound = pygame.mixer.Sound('AppleBitingSound.wav')
    pygame.mixer.music.load('AppleBitingSound.wav')
    pygame.mixer.music.play(1)
    
def is_food_eaten():
    if(square_array[0][0] == x1 and square_array[0][1] == y1):
        biting_sound()
        snake_longer()
        food_location()
        update_score()
def update_score():
    global score
    score+=1
    pygame.font.init()
    global myfont
    global scoretoprint
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    scoretoprint = myfont.render("Score: " + str(score), False, (255, 255, 255))
            
def food_location():
    global x1
    global y1
    x1 = random.randint(0, 17)
    y1 = random.randint(0, 17)
    
def loading_screen():
    Letters = pygame.image.load('SnakeGameText.png')
    back_ground = pygame.image.load('loading_screen.png')
    start_button = pygame.image.load('StartButtonGreen.png')
    back_ground = pygame.transform.scale(back_ground, (672, 420))
    gameDisplay = pygame.display.set_mode((700, 450))
    gameDisplay.blit(back_ground, (14, 15))
    gameDisplay.blit(Letters, (125, 15))
    start_button = pygame.transform.scale(start_button, (128, 48))
    gameDisplay.blit(start_button, (60, 130))
    pygame.display.update()
    while(True):
        pygame.event.get()
        pos = pygame.mouse.get_pos()
        if(pygame.mouse.get_pressed()[0] and pos[0]>=60 and pos[0]<=187 and pos[1]>=130 and pos[1]<=177):
            break
    win = pygame.display.set_mode((19*40, 19*40))
        

def main():
    update_score()
    run = True
    food_location()
    global square_array
    square_array = [(1, 1)]
    global square_moves
    square_moves = ["U"]
    global moves
    moves = []
    global curdir
    curdir = "U"
    global turns
    turns = []
    global turn_position
    turn_position = []
    loading_screen()
    while run:
        pygame.event.get()
        pygame.time.delay(100)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and curdir!="R":
            if(len(square_array)>1):
                turns.append("L")
                turn_position.append((square_array[0][0], square_array[0][1]))
            square_moves[0] = "L"
            curdir = "L"
        if keys[pygame.K_RIGHT] and curdir!="L":
            if(len(square_array)>1):
                turns.append("R")
                turn_position.append((square_array[0][0], square_array[0][1]))
            square_moves[0] = "R"
            curdir = "R"
        if keys[pygame.K_UP] and curdir!="D":
            if(len(square_array)>1):
                turns.append("U")
                turn_position.append((square_array[0][0], square_array[0][1]))
            square_moves[0] = "U"
            curdir = "U"
        if keys[pygame.K_DOWN] and curdir!="U":
            if(len(square_array)>1):
                turns.append("D")
                turn_position.append((square_array[0][0], square_array[0][1]))
            square_moves[0] = "D"
            curdir = "D"
        initialsetup()
        update_square_array()
        if(detect_collision()):
            run = False
            pygame.display.update()
            continue
        is_food_eaten()
        pygame.draw.circle(win, (255,0, 0), (40+40*x1, 40+40*y1), 20)
        win.blit(scoretoprint,(660, 735))
        pygame.display.update()

main()
