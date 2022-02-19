import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('green')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)



## 5. your code goes here

michelangelo.forward(98)
leonardo.forward(68)
for x in range(10):
    turtleranges1 = random.randrange(0, 10)
    turtleranges2 = random.randrange(0, 10)
    michelangelo.forward(turtleranges1)
    leonardo.forward(turtleranges2)
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

# Part B - complete part B here
leonardo.up()
michelangelo.down()
triangle= (360/3)
length= 50
for x in range(3): 
  michelangelo.forward(length)
  michelangelo.left(triangle)
michelangelo.down()
michelangelo.up()
michelangelo.clear()

michelangelo.down()
square= (360/4)
length= 40
for x in range(4): 
  michelangelo.forward(length)
  michelangelo.left(square)
michelangelo.down()
michelangelo.up()
michelangelo.clear()

michelangelo.down()
hexacon= (360/6)
length= 30
for x in range(6): 
  michelangelo.forward(length)
  michelangelo.left(hexacon)
michelangelo.down()
michelangelo.up()
michelangelo.clear()

michelangelo.down()
nonogon= (360/9)
length= 20
for x in range(9): 
  michelangelo.forward(length)
  michelangelo.left(nonogon)
michelangelo.down()
michelangelo.up()
michelangelo.clear()

michelangelo.down()
docogon= (360/12)
length= 10
for x in range(12): 
  michelangelo.forward(length)
  michelangelo.left(docogon)
michelangelo.down()
michelangelo.up()
michelangelo.clear()

window.exitonclick()