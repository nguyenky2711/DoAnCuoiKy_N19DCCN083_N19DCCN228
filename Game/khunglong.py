import pgzero
import pgzrun
from pgzhelper import *
import pygame
import random
WIDTH=800
HEIGHT=480

score=0
velocity = 5.5
time_velocity =0.6
check_point = 10

background=Actor('background')
runner=Actor('run1')
runner.x=100
runner.y=400
run_images=['run1','run2','run3','run4','run5','run6','run7','run8']
runner.images=run_images

obstacels=[]
obstacels_timeout=0

height_up=0
weight=1
game_over=False
max_score=0
stop = False
check_sounds=False
def update():
    pygame.display.set_caption('KHỦNG LONG BAY')   
    global obstacels_timeout,score,height_up,weight,game_over,obstacels,stop, velocity,check_point, time_velocity,max_score,check_sounds
    runner.next_image()
    #thoi gian sinh cay
    obstacels_timeout += time_velocity
    # den 80 cay xuong rong moi xuat hien(toc do sinh cay xuong rong)
    if(game_over == False):
        if obstacels_timeout>60:
            if(score >= 10):
                if(random.randint(0,1) == 1): 
                    tree=Actor('catus.2png')  
                    tree.y=420             
                else:  
                    tree=Actor('bird3') 
                    tree.y=430
            else: 
                tree=Actor('catus.2png') 
                tree.y=420  
            tree.x=850
            obstacels.append(tree)
            obstacels_timeout=0
            
        #cay xuong rong chay tu phai sang trai    
        for tree in obstacels:
            tree.x-=  velocity
            # độ khó tăng dần 
            if(score % check_point == 0  and score > 0):            
                velocity += 0.01
                time_velocity += 0.002
            #tinh diem 
            if tree.x<-10:
                score+=1
                obstacels.remove(tree)  
            if(max_score < score):
                max_score = score  
                
            if(max_score==score and check_sounds==True):
                sounds.max_score.play()
                check_sounds=False
        if keyboard.up and runner.y==400:
            height_up=-22
            sounds.impact.set_volume(0.5)
            sounds.impact.play() 
        runner.y+=height_up
        height_up+=weight
        if runner.y>400:
            height_up=0
            runner.y=400
        if runner.collidelist(obstacels)!=-1: #va cham
            game_over=True
            obstacels=[]
            sounds.gameover.set_volume(0.7)
            sounds.gameover.play()
        if keyboard.p:
            if(stop == False):
                stop = True
                pause() 
        if keyboard.q:
            pygame.quit()
            quit() 
    else :        
        if keyboard.space:
            game_over=False
            score=0
            velocity =5.5
            time_velocity =0.6
            check_point = 10
            obstacels=[]
            check_sounds=True
def pause():
    paused=True
    screen.draw.text('Game Pause!',(250,200),color=(0,0,0), fontsize=60)
    screen.draw.text('Press C to continue play ',(250,250),color=(0,0,0), fontsize=40)    
    screen.draw.text('Press Q to quit game ',(250,300),color=(0,0,0), fontsize=40)
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused=False  
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
            pygame.display.update()
            clock.tick(60) 

def draw():
    background.draw()
    if game_over:
        screen.draw.text('Game Over!',(250,200),color=(0,0,0), fontsize=60)
        screen.draw.text('Final Score:'+str(score),(250,250),color=(0,0,0), fontsize=50)
        screen.draw.text('Press Space to play again',(250,300),color=(0,0,0), fontsize=50)
        screen.draw.text('Highest Score:'+ str(max_score),(250,350),color=(0,0,0), fontsize=30)
    else:
        x =10
        runner.draw()
        screen.draw.text('Score: '+str(score),(x,15),color=(255,0,255), fontsize=45)
        if(max_score > 0):
            screen.draw.text('Highest Score: '+str(max_score),(x+ 150,30),color=(255,0,255), fontsize=20)
        for tree in obstacels:
            tree.draw()

pgzrun.go()