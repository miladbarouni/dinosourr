import pgzrun
import os
from animation_game import *

os.environ["SDL_VIDEO_CENTERED"] = "1"

WIDTH = 1000
HEIGHT = 700

background_menu = Actor("background_menu" , (500 , 350))
button_start = Actor("button_start" , (500 , 350))
button_setting = Actor("button_start" , (100 , 100))
background_game1 = Actor("background_game" , (500 , 350))
background_game2 = Actor("background_game" , (1500 , 350))
mone = Actor("mone" , (1500 , 666))
runner = Actor("run1" , (500 , 400))
runner.images = ["run2","run3","run4","run5","run6","run7","run8","run9","run10","run11","run12"]
runner.fps = 15

runner_idle = Actor("run1" , (500 , 400))
runner_idle.images = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17"]
runner_idle.fps = 15

setting = False
sound = False
game = False
text = "sound_on"
jump = False
speed = 2
speed2 = 2

def update():
    global text , jump , speed

    if sound:
        text = "sound_off"
        sounds.sound.stop()
    else:
        text = "sound_on"
        sounds.sound.play()

    if keyboard.right:
        background_game1.x -= speed
        background_game2.x -= speed
        runner.animate()
        runner.flip_x = False
        mone.x -= speed

    elif keyboard.left and (background_game1.x <= 500 or background_game2.x <= 500):
        background_game1.x += speed2
        background_game2.x += speed2
        runner.animate()
        runner.flip_x = True
        mone.x += speed2

    else:
        if runner.flip_x:
            runner_idle.animate()
            runner.image = runner_idle.image
            runner_idle.flip_x = True
            runner.flip_x = True
        else:
            runner_idle.animate()
            runner.image = runner_idle.image
            runner_idle.flip_x = False         
            runner.flip_x = False         

    if background_game2.x == 500:
        background_game1.x = 1500
    if background_game1.x == 500:
        background_game2.x = 1500

    if jump and runner.y > 150:
        runner.y -= 5
    else:
        jump = False

    if jump == False and runner.y <= 400:
        runner.y += 5

    if runner.colliderect(mone) and mone.x <= 906 and runner.y >= 235:
        speed = 0
    else:
        speed = 2

    # print(mone.x)
    # print(runner.y)
def draw():
    global menu 

    def menu():
        background_menu.draw()
        button_start.draw()
        button_setting.draw()
        screen.draw.text("Start" , topleft = (430,335) , color = "black" , fontsize = 80)
        screen.draw.text("Setting" , topleft = (28,77) , color = "black" , fontsize = 60)
    menu()

    if setting:
        background_menu.draw()
        button_start.draw()
        button_setting.draw()
        screen.draw.text(f"{text}" , topleft = (430,335) , color = "black" , fontsize = 35)
        screen.draw.text("back" , topleft = (35,80) , color = "black" , fontsize = 60)  
    
    if game:
        background_game1.draw()
        background_game2.draw()
        runner.draw()
        mone.draw()

def on_mouse_down(pos):
    global setting , sound , game
    if game == False:
        if button_setting.collidepoint(pos) and setting == False:
            setting = True

        elif button_setting.collidepoint(pos) and setting:
            setting = False
            menu()



        if button_start.collidepoint(pos) and setting and sound == False:
            sound = True

        elif button_start.collidepoint(pos) and setting and sound:
            sound = False

    if button_start.collidepoint(pos) and setting == False:
        game = True

def on_key_down(key):
    global jump

    if key == keys.UP and runner.y >= 400:
        jump = True

pgzrun.go()