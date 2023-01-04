#-------------------------------------------------------------------------
# Created By  : Tobi
# Created Date: 18/12/2022
# Last modified : 04/01/2023
# version ='1.0'

# status = draft
# Credits:
#https://stackoverflow.com/questions/12807079/how-to-determined-if-a-2-dimensional-list-contain-a-value
#https://trinket.io/sense-hat

            
# ------------------------------------------------------------------------
# Description
# SenseSnake - an 8x8 version of the game snake
# Go to https://trinket.io/sense-hat , delete the already exisiting code and replace it with this

import sense_hat
from time import sleep, time
import random

sense = sense_hat.SenseHat()
sense.clear()

#-----Variables
score = 0
dead = 0
start = 0
dif = 0
direction = 0
spawn = 0
game = 1

#-----Colors
apple = (255, 0, 0) #Red          (apple)
snake = (0, 255, 0) #Green        (snake head)
body = (0, 100, 0)  #Darker green (snake body)
b = (0, 0, 0)       #Black        (background)
g = (0, 255, 0)     #Green        (intro, death, win & menu)
w = (255, 255, 255) #White        (intro, death, win & menu)
r = (255, 0, 0)     #Red          (intro, death, win & menu)
t = (211, 141, 80)  #Tan          (intro)
o = (255, 100, 0)   #Orange       (menu)
p = (255, 0, 255)   #Purple       (menu)
y = (255, 255, 0)   #Yellow       (menu)
G = (100, 84, 0)    #Gold         (win)


#-----Sense hat directions/actions
up = sense_hat.DIRECTION_UP
left = sense_hat.DIRECTION_LEFT
right = sense_hat.DIRECTION_RIGHT
down = sense_hat.DIRECTION_DOWN
middle = sense_hat.DIRECTION_MIDDLE
press = sense_hat.ACTION_PRESSED

#-----3D list of frames for intro animation
frames1 = [
  [
  [w, w, w, w, w, w, t, w],
  [w, g, g, g, g, g, g, w],
  [w, g, w, w, w, w, w, w],
  [w, g, g, g, g, g, g, w],
  [w, w, w, w, w, w, g, w],
  [b, g, b, g, g, g, g, w],
  [g, g, g, w, w, w, w, w],
  [w, r, w, w, w, w, w, w]],

  [[w, w, w, w, w, w, w, t],
  [w, g, g, g, g, g, g, w],
  [w, g, w, w, w, w, w, w],
  [w, g, g, g, g, g, g, w],
  [w, w, w, w, w, w, g, w],
  [b, g, b, g, g, g, g, w],
  [g, g, g, w, w, w, w, w],
  [w, r, w, w, w, w, w, w]],

  [[w, w, w, w, w, w, w, w],
  [w, g, g, g, g, g, g, t],
  [w, g, w, w, w, w, w, w],
  [w, g, g, g, g, g, g, w],
  [w, w, w, w, w, w, g, w],
  [b, g, b, g, g, g, g, w],
  [g, g, g, w, w, w, w, w],
  [w, r, w, w, w, w, w, w]]]
  
#-----3D list of frams for death animation
frames2 = [
  [
    [w, w, w, w, w, w, w, w],#0
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w]],
  [
    [w, w, w, w, w, w, w, w],#1
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, b],
    [w, w, w, w, w, w, w, g],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w]],
  [
    [w, w, w, w, w, w, w, w],#2
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, b],
    [w, w, w, w, w, w, w, g],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, g],
    [w, w, w, w, w, w, w, g],
    [w, w, w, w, w, w, w, g]],
  [
    [w, w, w, w, w, w, w, w],#3
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, b, g],
    [w, w, w, w, w, w, g, g],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, g],
    [w, w, w, w, w, w, w, g],
    [w, w, w, w, w, w, w, g]],
  [
    [w, w, w, w, w, w, w, w],#4
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, b, g],
    [w, w, w, w, w, w, g, g],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, g, g],
    [w, w, w, w, w, w, g, w],
    [w, w, w, w, w, w, g, g]],
  [
    [w, w, w, w, w, w, w, w],#5
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, b, g, g],
    [w, w, w, w, w, g, g, g],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, g, g],
    [w, w, w, w, w, w, g, w],
    [w, w, w, w, w, w, g, g]],
  [
    [w, w, w, w, w, w, w, w],#6
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, b, g, g],
    [w, w, w, w, w, g, g, g],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, g, g, g],
    [w, w, w, w, w, g, w, w],
    [w, w, w, w, w, g, g, g]],
  [
    [w, w, w, w, w, w, w, w],#7
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, b, g, g, w],
    [w, w, w, w, g, g, g, g],
    [w, w, w, w, w, w, w, g],
    [w, w, w, w, w, g, g, g],
    [w, w, w, w, w, g, w, w],
    [w, w, w, w, w, g, g, g]],
  [
    [w, w, w, w, w, w, w, w],#8
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, b, g, g, w],
    [w, w, w, w, g, g, g, g],
    [w, w, w, w, w, w, w, g],
    [w, w, w, w, g, g, g, g],
    [w, w, w, w, g, w, w, w],
    [w, w, w, w, g, g, g, g]],
  [
    [w, w, w, w, w, w, w, w],#9
    [w, w, w, w, w, w, w, w],
    [w, w, w, b, g, g, w, w],
    [w, w, w, g, g, g, g, w],
    [w, w, w, w, w, w, g, w],
    [w, w, w, w, g, g, g, w],
    [w, w, w, w, g, w, w, w],
    [w, w, w, w, g, g, g, g]],
  [
    [w, w, w, w, w, w, w, w],#10
    [w, w, w, w, w, w, w, w],
    [w, w, w, g, g, w, w, w],
    [w, w, b, g, g, r, g, w],
    [w, w, w, g, w, w, g, w],
    [w, w, w, w, g, g, g, w],
    [w, w, w, w, g, w, w, w],
    [w, w, w, w, g, g, g, g]],
  [
    [w, w, w, w, w, w, w, w],#11
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, r, w, w],
    [w, g, g, w, r, w, w, w],
    [w, g, g, w, w, g, g, w],
    [w, b, g, w, g, g, g, w],
    [w, w, w, w, g, w, w, w],
    [w, w, w, w, g, g, g, g]],
  [
    [w, w, w, w, w, w, w, w],#12
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w],
    [g, g, w, w, w, w, w, w],
    [g, g, g, w, w, g, g, w],
    [w, b, g, w, g, g, w, w],
    [w, w, w, w, g, g, g, g]],
  [
    [w, w, w, w, w, w, w, w],#13
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, g, w, w],
    [g, g, g, w, g, g, g, w],
    [g, g, b, w, g, g, g, g]]]

#-----3D list of frames for win animation
frames3 = [
  [
    [w, w, w, w, w, w, w, w],#0
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w],
    [w, w, r, w, w, w, w, w],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w]],
  [
    [w, w, w, w, w, w, w, w],#1
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, b],
    [w, w, r, w, w, w, w, g],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w]],
  [
    [w, w, w, w, w, w, w, w],#2
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, b],
    [w, w, r, w, w, w, w, g],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, g],
    [w, w, w, w, w, w, w, g],
    [w, w, w, w, w, w, w, g]],
  [
    [w, w, w, w, w, w, w, w],#3
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, b, g],
    [w, w, r, w, w, w, g, g],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, g],
    [w, w, w, w, w, w, w, g],
    [w, w, w, w, w, w, w, g]],
  [
    [w, w, w, w, w, w, w, w],#4
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, b, g],
    [w, w, r, w, w, w, g, g],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, g, g],
    [w, w, w, w, w, w, g, w],
    [w, w, w, w, w, w, g, g]],
  [
    [w, w, w, w, w, w, w, w],#5
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, b, g, g],
    [w, w, r, w, w, g, g, g],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, g, g],
    [w, w, w, w, w, w, g, w],
    [w, w, w, w, w, w, g, g]],
  [
    [w, w, w, w, w, w, w, w],#6
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, b, g, g],
    [w, w, r, w, w, g, g, g],
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, g, g, g],
    [w, w, w, w, w, g, w, w],
    [w, w, w, w, w, g, g, g]],
  [
    [w, w, w, w, w, w, w, w],#7
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, b, g, g, w],
    [w, w, r, w, g, g, g, g],
    [w, w, w, w, w, w, w, g],
    [w, w, w, w, w, g, g, g],
    [w, w, w, w, w, g, w, w],
    [w, w, w, w, w, g, g, g]],
  [
    [w, w, w, w, w, w, w, w],#8
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, b, g, g, w],
    [w, w, r, w, g, g, g, g],
    [w, w, w, w, w, w, w, g],
    [w, w, w, w, g, g, g, g],
    [w, w, w, w, g, w, w, w],
    [w, w, w, w, g, g, g, g]],
  [
    [w, w, w, w, w, w, w, w],#9
    [w, w, w, w, w, w, w, w],
    [w, w, w, b, g, g, w, w],
    [w, w, r, w, g, g, g, w],
    [w, w, w, g, w, w, g, w],
    [w, w, w, w, g, g, g, w],
    [w, w, w, w, g, w, w, w],
    [w, w, w, w, g, g, g, g]],
  [
    [w, w, w, w, w, w, w, w],#10
    [w, w, w, w, w, w, w, w],
    [w, w, b, g, g, w, w, w],
    [w, w, r, g, g, g, g, w],
    [w, w, g, w, w, w, g, w],
    [w, w, w, w, g, g, g, w],
    [w, w, w, w, g, w, w, w],
    [w, w, w, w, g, g, g, g]],
  [
    [w, w, w, w, w, w, w, w],#11
    [w, w, w, w, w, w, w, w],
    [w, w, b, g, g, w, w, w],
    [w, w, g, g, g, g, g, w],
    [w, w, w, w, w, w, g, w],
    [w, w, w, g, g, g, g, w],
    [w, w, w, g, w, w, w, w],
    [w, w, w, g, g, g, g, g]],
  [
    [w, w, w, w, w, w, w, w],#12
    [w, w, w, w, w, w, w, w],
    [w, w, b, g, g, w, w, w],
    [w, w, g, g, g, g, w, w],
    [w, w, w, w, w, g, w, w],
    [w, w, w, g, g, g, w, w],
    [w, w, w, g, w, w, w, w],
    [w, w, w, g, g, g, g, g]],
  [
    [w, w, w, w, w, w, w, w],#13
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w],
    [w, b, b, g, g, b, b, w],
    [w, b, b, g, g, b, b, w],
    [w, g, g, g, g, g, g, w],
    [w, g, g, g, g, g, g, w],
    [w, w, w, w, g, g, w, w]],
  [
    [w, G, G, G, G, G, G, w],#14
    [w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w],
    [w, b, b, g, g, b, b, w],
    [w, b, b, g, g, b, b, w],
    [w, g, g, g, g, g, g, w],
    [w, g, g, g, g, g, g, w],
    [w, w, w, w, g, g, w, w]],
  [
    [w, G, G, G, G, G, G, w],#15
    [w, G, G, G, G, G, G, w],
    [w, w, w, w, w, w, w, w],
    [w, b, b, g, g, b, b, w],
    [w, b, b, g, g, b, b, w],
    [w, g, g, g, g, g, g, w],
    [w, g, g, g, g, g, g, w],
    [w, w, w, w, g, g, w, w]],
  [
    [w, G, w, G, G, w, G, w],#16
    [w, G, G, G, G, G, G, w],
    [w, G, G, G, G, G, G, w],
    [w, b, b, g, g, b, b, w],
    [w, b, b, g, g, b, b, w],
    [w, g, g, g, g, g, g, w],
    [w, g, g, g, g, g, g, w],
    [w, w, w, w, g, g, w, w]],
  [
    [w, w, w, w, w, w, w, w],#17
    [w, G, w, G, G, w, G, w],
    [w, G, G, G, G, G, G, w],
    [w, G, G, G, G, G, G, w],
    [w, b, b, g, g, b, b, w],
    [w, b, b, g, g, b, b, w],
    [w, g, g, g, g, g, g, w],
    [w, g, g, g, g, g, g, w]],
  [
    [w, G, w, G, G, w, G, w],#18
    [w, G, G, G, G, G, G, w],
    [w, G, G, G, G, G, G, w],
    [w, b, b, g, g, b, b, w],
    [w, b, b, g, g, b, b, w],
    [w, g, g, g, g, g, g, w],
    [w, g, g, g, g, g, g, w],
    [w, w, w, w, g, g, w, w]],
  [
    [r, G, r, G, G, r, G, r],#19
    [w, G, G, G, G, G, G, w],
    [w, G, G, G, G, G, G, w],
    [w, b, b, g, g, b, b, w],
    [w, b, b, g, g, b, b, w],
    [w, g, g, g, g, g, g, w],
    [w, g, g, g, g, g, g, w],
    [w, w, w, w, g, g, w, w]],
  [
    [r, G, r, G, G, r, G, r],#20
    [r, G, G, G, G, G, G, r],
    [w, G, G, G, G, G, G, w],
    [w, b, b, g, g, b, b, w],
    [w, b, b, g, g, b, b, w],
    [w, g, g, g, g, g, g, w],
    [w, g, g, g, g, g, g, w],
    [w, w, w, w, g, g, w, w]],
  [
    [r, G, r, G, G, r, G, r],#20
    [r, G, G, G, G, G, G, r],
    [r, G, G, G, G, G, G, r],
    [w, b, b, g, g, b, b, w],
    [w, b, b, g, g, b, b, w],
    [w, g, g, g, g, g, g, w],
    [w, g, g, g, g, g, g, w],
    [w, w, w, w, g, g, w, w]],
  [
    [r, G, r, G, G, r, G, r],#22
    [r, G, G, G, G, G, G, r],
    [r, G, G, G, G, G, G, r],
    [r, b, b, g, g, b, b, r],
    [w, b, b, g, g, b, b, w],
    [w, g, g, g, g, g, g, w],
    [w, g, g, g, g, g, g, w],
    [w, w, w, w, g, g, w, w]],
  [
    [r, G, r, G, G, r, G, r],#23
    [r, G, G, G, G, G, G, r],
    [r, G, G, G, G, G, G, r],
    [r, b, b, g, g, b, b, r],
    [r, b, b, g, g, b, b, r],
    [w, g, g, g, g, g, g, w],
    [w, g, g, g, g, g, g, w],
    [w, w, w, w, g, g, w, w]],
  [
    [r, G, r, G, G, r, G, r],#24
    [r, G, G, G, G, G, G, r],
    [r, G, G, G, G, G, G, r],
    [r, b, b, g, g, b, b, r],
    [r, b, b, g, g, b, b, r],
    [r, g, g, g, g, g, g, r],
    [w, g, g, g, g, g, g, w],
    [w, w, w, w, g, g, w, w]],
  [
    [r, G, r, G, G, r, G, r],#25
    [r, G, G, G, G, G, G, r],
    [r, G, G, G, G, G, G, r],
    [r, b, b, g, g, b, b, r],
    [r, b, b, g, g, b, b, r],
    [r, g, g, g, g, g, g, r],
    [r, g, g, g, g, g, g, r],
    [w, w, w, w, g, g, w, w]],
  [
    [r, G, r, G, G, r, G, r],#26
    [r, G, G, G, G, G, G, r],
    [r, G, G, G, G, G, G, r],
    [r, b, b, g, g, b, b, r],
    [r, b, b, g, g, b, b, r],
    [r, g, g, g, g, g, g, r],
    [r, g, g, g, g, g, g, r],
    [r, r, r, r, g, g, r, r]]]

#-----3D list of all menu section frames
menus = [
  [
  [b, b, b, b, b, g, b, b],
  [b, b, g, b, g, b, b, b],
  [b, b, b, g, b, b, w, b],
  [b, b, b, b, b, b, b, w],
  [b, b, g, g, g, b, w, b],
  [b, b, b, g, g, b, b, b],
  [b, b, b, g, g, b, b, b],
  [b, b, g, g, g, g, b, b]],

  [[b, b, b, b, b, g, b, b],
  [b, b, g, b, g, b, b, b],
  [b, w, b, g, b, b, w, b],
  [w, b, b, b, b, b, b, w],
  [b, w, y, y, y, y, w, b],
  [b, b, b, y, y, y, b, b],
  [b, b, y, y, y, b, b, b],
  [b, b, y, y, y, y, b, b]],

  [[b, b, b, b, b, g, b, b],
  [b, b, g, b, g, b, b, b],
  [b, w, b, g, b, b, w, b],
  [w, b, b, b, b, b, b, w],
  [b, w, o, o, o, o, w, b],
  [b, b, b, o, o, o, b, b],
  [b, b, b, b, o, o, b, b],
  [b, b, o, o, o, o, b, b]],
  
  [[b, b, b, b, b, g, b, b],
  [b, b, g, b, g, b, b, b],
  [b, w, b, g, b, b, w, b],
  [w, b, b, b, b, b, b, w],
  [b, w, r, b, r, r, w, b],
  [b, b, r, r, r, r, b, b],
  [b, b, r, r, r, r, b, b],
  [b, b, b, b, r, r, b, b]],
  
  [[b, b, b, b, b, g, b, b],
  [b, b, g, b, g, b, b, b],
  [b, w, b, g, b, b, b, b],
  [w, b, b, b, b, b, b, b],
  [b, w, p, p, p, p, b, b],
  [b, b, p, p, p, b, b, b],
  [b, b, b, p, p, p, b, b],
  [b, b, p, p, p, p, b, b]]]

#-----Intro animation, plays 4 frames 3 times at 10 fps
for n in range(3):
  sense.set_pixels (sum(frames1[0], []))
  sleep(0.1)
  sense.set_pixels (sum(frames1[1], []))
  sleep(0.1)
  sense.set_pixels (sum(frames1[2], []))
  sleep(0.1)
  sense.set_pixels (sum(frames1[1], []))
  sleep(0.1)


while True:
  while game == 1:
    #-----Menu screen, choose the difficulty level by pressing left or right, and press up to start the game
    while start == 0:
      for event in sense.stick.get_events():
        if event.direction == right and event.action == press and dif != 4:
          dif = dif + 1
        elif event.direction == left and event.action == press and dif != 0:
          dif = dif - 1
        elif event.direction == up and event.action == press or event.direction == middle and event.action == press:
          start = 1
      sense.set_pixels (sum(menus[dif], []))
    #-----Start game
    if spawn == 0:
      #-----Draws empty map
      map = [
      [b, b, b, b, b, b, b, b],
      [b, b, b, b, b, b, b, b],
      [b, b, b, b, b, b, b, b],
      [b, b, b, b, b, b, b, b],
      [b, b, b, b, b, b, b, b],
      [b, b, b, b, b, b, b, b],
      [b, b, b, b, b, b, b, b],
      [b, b, b, b, b, b, b, b]]
      
      #-----Chooses random points to draw the snake and apple in the beginning
      #-----sx and sy -> snake coordinates
      #-----ax and ay -> apple coordinates
      sx = random.randint(0, 7)
      sy = random.randint(0, 7)
      map[sx][sy] = snake
      snakepos = [[sx, sy]]
      ax = random.randint(0, 7)
      ay = random.randint(0, 7)
      map[ax][ay] = apple
      sense.set_pixels (sum(map, []))
      spawn = 1
      #-----Changes direction based on the last given event
    for event in sense.stick.get_events():
      if event.direction == up and event.action == press and cdir != 2:
        direction = 1
      elif event.direction == down and event.action == press and cdir != 1:
        direction = 2
      elif event.direction == right and event.action == press and cdir !=4:
        direction = 3
      elif event.direction == left and event.action == press and cdir != 3:
        direction = 4
      #-----Changes one coordinate based on chosen direction
    if direction == 1:
      map[sx][sy] = b
      sx = sx - 1
    elif direction == 2:
      map[sx][sy] = b
      sx = sx + 1
    elif direction == 3:
      map[sx][sy] = b
      sy = sy + 1
    elif direction == 4:
      map[sx][sy] = b
      sy = sy - 1
      #-----Check to see if snake is out of bounds
    if sx == 8 or sy == 8 or sx == -1 or sy == -1:
      dead = 1
    
    try:
      #-----Check to see if snake has run into itself
      if map[sx][sy] == body:
        dead = 1
      map[sx][sy] = snake
    except:
      dead = 1
      #-----Triggers when both coordinates of the apple and snake are the same
    if sx == ax and sy == ay:
      score = score + 1
      ax = random.randint(0, 7)
      ay = random.randint(0, 7)
      map[ax][ay] = apple
      #-----Adds current location to snakepos and shifts all other datapoints along
    snakepos.append ([0])
    n = len(snakepos) - 1
    while n >= 0 :
      m = n - 1
      snakepos[n] = snakepos[m]
      n = n - 1
    snakepos[0] = [sx, sy]
    o = score
    if o >= 1:
      sxb = snakepos[o + 1][0]
      syb = snakepos[o + 1][1]
      map [sxb][syb] = b
      while o >= 1:
        sxb = snakepos[o][0]
        syb = snakepos[o][1]
        map[sxb][syb] = body
        o = o - 1
    
    #-----Exits While loop upon death
    if dead == 1:
      game = 0
      break
    
    #-----Keeps the list from growing to a bigger length than what is needed in order to reduce latency
    if len(snakepos) >= score + 3:
      r = score + 2
      snakepos.pop(r)
      
      #-----Check to make sure new apple isn't spawned onto snake
    while any(apple in sublist for sublist in map) == False:
        ax = random.randint(0, 7)
        ay = random.randint(0, 7)
        if map[ax][ay] == b:
          map[ax][ay] = apple
          
    cdir = direction
      
      #-----Draws all pixels onto the background
    sense.set_pixels (sum(map, []))
      #-----Determines the gameplay speed and difficulty
    sleep(1/(2*(dif+1)))
  
      #-----Prints the score after game over
  if score >=63 :
    for n in range(27):
      sense.set_pixels (sum(frames3[n], []))
      sleep(0.2)
  else:
    for n in range(14):
      sense.set_pixels (sum(frames2[n], []))
      sleep(0.2)
    sleep(1)
  score = str(score)
  sense.show_message(score, scroll_speed = 0.1, text_colour = (0, 100, 0), back_colour = w)
  game = 1
  direction = 0
  snakepos = []
  score = 0
  spawn = 0
  dead = 0
  start = 0
