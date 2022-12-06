from turtle import *

def curve():
    for i in range(200):
        
        right(1)
        forward(1)

begin_fill()
speed(2)
color('#ffb6c1')
pensize(5)
left(140)
forward(113)
curve()
left(120)
curve()
forward(112)
end_fill()

up()
setpos(-68,95)
down()

color('Black')
write('I LOVE YOU', font=('Times New Roman', 12, 'bold'))