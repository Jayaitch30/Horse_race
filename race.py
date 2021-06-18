import turtle
from turtle import Turtle
import random
import winsound
import time
import os
racecourse = turtle.Screen()
start = turtle.Turtle()
winner = turtle.Turtle()
class horses(Turtle):
    def __init__(self, name, move, position):
        super().__init__(shape=os.path.join('resources', 'horse.gif'), visible=True)
        self.name = name
        self.move = move
        self.penup()
        self.setposition(position)
        self.speed = 0.01
    def motion(self):
        self.move = random.randint(10, 100)
        self.goto(self.xcor() + self.move, self.ycor())
        self.shape(os.path.join('resources', 'horse.gif'))

def init():
    winsound.PlaySound(os.path.join('resources', 'Peaky Focking Blinders'), winsound.SND_ASYNC)
    winner.hideturtle()
    racecourse.addshape(os.path.join('resources', 'start_horse_race.gif'))
    racecourse.addshape(os.path.join('resources', 'horse.gif'))
    start.shape(os.path.join('resources', 'start_horse_race.gif'))
    racecourse.setup(1000, 600)
    racecourse.bgpic(os.path.join('resources', 'race_track.gif'))
    racecourse.title("Horse race")
    racecourse.onscreenclick(buttonclick, 1)
    racecourse.listen()

def buttonclick(x, y):
    if start.isvisible():
        if x > -89 and x < 89 and y > -44 and y < 44:
            start.hideturtle()
            game()

def game():
    Kincsem = horses("Kincsem", 0, (-470, 230))
    BlackCaviar = horses("BlackCaviar", 0, (-470, 90))
    PeppersPride = horses("Peppers Pride", 0, (-470, -60))
    Eclipse = horses("Eclipse", 0, (-470, -220))
    while running:
        Kincsem.motion()
        if Kincsem.xcor() >= 450:
            winner.write("Kincsem is the winner!", align="center",font=("Comic Sans MS", 24, "normal"))
            time.sleep(3)
            restart()
        BlackCaviar.motion()
        if BlackCaviar.xcor() >= 450:
            winner.write("Black Caviar is the winner!", align="center",font=("Comic Sans MS", 24, "normal"))
            time.sleep(3)
            restart()
        PeppersPride.motion()
        if PeppersPride.xcor() >= 450:
            winner.write("Peppers Pride is the winner!", align="center",font=("Comic Sans MS", 24, "normal"))
            time.sleep(3)
            restart()
        Eclipse.motion()
        if Eclipse.xcor() >= 450:
            winner.write("Eclipse is the winner!", align="center",font=("Comic Sans MS", 24, "normal"))
            time.sleep(3)
            restart()
        def restart():
            Kincsem.setposition(-470, 230)
            BlackCaviar.setposition(-470, 90)
            PeppersPride.setposition(-470, -60)
            Eclipse.setposition(-470, -220)
            winner.clear()


    racecourse.bye()

def kESC():
    if start.isvisible():
        racecourse.bye()
    else:
        global running
        running = False
running = True
racecourse.onkey(kESC, "Escape")
racecourse.listen()
init()
racecourse.mainloop()