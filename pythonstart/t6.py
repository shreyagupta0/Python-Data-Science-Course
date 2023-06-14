from turtle import *

pencolor('purple')
pensize(3)
fillcolor('yellow')
speed('fast')
for i in range (10 , 0 , -1):
    begin_fill()
    circle(i*10)
    lt(25)
    end_fill()

mainloop()    