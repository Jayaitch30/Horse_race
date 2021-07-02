import turtle
from turtle import Turtle
import random
import winsound
import time
import os
import ast
racecourse = turtle.Screen()
start = turtle.Turtle()
winner = turtle.Turtle()
moneyman = turtle.Turtle()
current_money = turtle.Turtle()
kincsem_bet = 0
BlackCaviar_bet = 0
PeppersPride_bet = 0
Eclipse_bet = 0
with open('money_data.txt', 'r') as f:
    current_coins = ast.literal_eval(f.read())
coins = current_coins
if coins == 0:
    coins = 10
gambler = ''
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
    current_money.speed('fastest')
    moneyman.speed('fastest')
    moneyman.penup()
    current_money.penup()
    moneyman.hideturtle()
    current_money.hideturtle()
    current_money.goto(-50, 250)

def buttonclick(x, y):
    if start.isvisible():
        if x > -89 and x < 89 and y > -44 and y < 44:
            start.hideturtle()
            bets()
class bets_function():
    def __init__(self, pos):
        self.pos = pos
        global gambler
        if self.pos[0] > -15 and self.pos[0] < 100 and self.pos[1] > 165 and self.pos[1] < 210:
            gambler = 'kincsem'
            place_bet()
        elif self.pos[0] > -15 and self.pos[0] < 100 and self.pos[1] > 13 and self.pos[1] < 55:
            gambler = "BlackCaviar"
            place_bet()
        elif self.pos[0] > -15 and self.pos[0] < 100 and self.pos[1] > -140 and self.pos[1] < -95:
            gambler = "PeppersPride"
            place_bet()
        elif self.pos[0] > -15 and self.pos[0] < 100 and self.pos[1] > -285 and self.pos[1] < -240:
            gambler = "Eclipse"
            place_bet()
        if self.pos[0] > -80 and self.pos[0] < -30 and self.pos[1] > 165 and self.pos[1] < 210:
            kincsem_add_bet()
        elif self.pos[0] > -80 and self.pos[0] < -30 and self.pos[1] > 10 and self.pos[1] < 55:
            BlackCaviar_add_bet()
        elif self.pos[0] > -80 and self.pos[0] < -30 and self.pos[1] > -135 and self.pos[1] < -100:
            PeppersPride_add_bet()
        elif self.pos[0] > -80 and self.pos[0] < -30 and self.pos[1] > -280 and self.pos[1] < -240:
            Eclipse_add_bet()
def place_bet():
    get_ready()
    game()
def get_ready():
    racecourse.bgpic(os.path.join('resources', 'race_track.gif'))
    moneyman.clear()
    global kincsem_bet
    global BlackCaviar_bet
    global PeppersPride_bet
    global Eclipse_bet
    global coins
    global gambler
    if gambler == 'kincsem':
        coins -= kincsem_bet
        with open('money_data.txt', 'w') as f:
            f.write(str(coins))
    if gambler == "BlackCaviar":
        coins -= BlackCaviar_bet
        with open('money_data.txt', 'w') as f:
            f.write(str(coins))
    if gambler == "PeppersPride":
        coins -= PeppersPride_bet
        with open('money_data.txt', 'w') as f:
            f.write(str(coins))
    if gambler == "Eclipse":
        coins -= Eclipse_bet
        with open('money_data.txt', 'w') as f:
            f.write(str(coins))

def kincsem_add_bet():
    global kincsem_bet
    global coins
    global BlackCaviar_bet
    global PeppersPride_bet
    global Eclipse_bet
    BlackCaviar_bet = 0
    PeppersPride_bet = 0
    Eclipse_bet = 0
    if kincsem_bet < coins:
        kincsem_bet += 1
        moneyman.clear()
        moneyman.goto(-145, 165)
        moneyman.write(kincsem_bet, align="center", font=("Comic Sans MS", 24, "normal"))
def BlackCaviar_add_bet():
    global BlackCaviar_bet
    global kincsem_bet
    global PeppersPride_bet
    global Eclipse_bet
    kincsem_bet = 0
    PeppersPride_bet = 0
    Eclipse_bet = 0
    global coins
    if BlackCaviar_bet < coins:
        BlackCaviar_bet += 1
        moneyman.clear()
        moneyman.goto(-143, 10)
        moneyman.write(BlackCaviar_bet, align="center", font=("Comic Sans MS", 24, "normal"))
def PeppersPride_add_bet():
    global BlackCaviar_bet
    global kincsem_bet
    global PeppersPride_bet
    global Eclipse_bet
    kincsem_bet = 0
    BlackCaviar_bet = 0
    Eclipse_bet = 0
    global coins
    if PeppersPride_bet < coins:
        PeppersPride_bet += 1
        moneyman.clear()
        moneyman.goto(-143, -140)
        moneyman.write(PeppersPride_bet, align="center", font=("Comic Sans MS", 24, "normal"))
def Eclipse_add_bet():
    global BlackCaviar_bet
    global kincsem_bet
    global PeppersPride_bet
    global Eclipse_bet
    kincsem_bet = 0
    BlackCaviar_bet = 0
    PeppersPride_bet = 0
    global coins
    if Eclipse_bet < coins:
        Eclipse_bet += 1
        moneyman.clear()
        moneyman.goto(-143, -290)
        moneyman.write(Eclipse_bet, align="center", font=("Comic Sans MS", 24, "normal"))
def bets():
    global coins
    global kincsem_bet
    global BlackCaviar_bet
    global PeppersPride_bet
    global Eclipse_bet
    kincsem_bet = 0
    BlackCaviar_bet = 0
    PeppersPride_bet = 0
    Eclipse_bet = 0
    racecourse.bgpic(os.path.join('resources', 'Bet_screen.gif'))
    current_money.clear()
    if racecourse.bgpic() == os.path.join('resources', 'Bet_screen.gif'):
        current_money.write("Coins: {}".format(coins), align="center",font=("Comic Sans MS", 24, "normal"))
    racecourse.onscreenclick(findpos)
    racecourse.listen()
def findpos(x, y):
    position = [x, y]
    bets_function(position)
def game():
    Kincsem = horses("Kincsem", 0, (-470, 230))
    BlackCaviar = horses("BlackCaviar", 0, (-470, 90))
    PeppersPride = horses("Peppers Pride", 0, (-470, -60))
    Eclipse = horses("Eclipse", 0, (-470, -220))
    Kincsem.showturtle()
    BlackCaviar.showturtle()
    PeppersPride.showturtle()
    Eclipse.showturtle()
    current_money.clear()
    while running:
        global coins
        if racecourse.bgpic() == os.path.join('resources', 'race_track.gif'):
            Kincsem.motion()
            if Kincsem.xcor() >= 450:
                winner.write("Kincsem is the winner!", align="center",font=("Comic Sans MS", 24, "normal"))
                time.sleep(3)
                coins += kincsem_bet*2
                with open('money_data.txt', 'w') as f:
                    f.write(str(coins))
                restart()
                bets()
        else:
            return bets()
        if racecourse.bgpic() == os.path.join('resources', 'race_track.gif'):
            BlackCaviar.motion()
            if BlackCaviar.xcor() >= 450:
                winner.write("Black Caviar is the winner!", align="center",font=("Comic Sans MS", 24, "normal"))
                coins += BlackCaviar_bet * 2
                with open('money_data.txt', 'w') as f:
                    f.write(str(coins))
                time.sleep(3)
                restart()
                bets()
        else:
            return bets()
        if racecourse.bgpic() == os.path.join('resources', 'race_track.gif'):
            PeppersPride.motion()
            if PeppersPride.xcor() >= 450:
                winner.write("Peppers Pride is the winner!", align="center",font=("Comic Sans MS", 24, "normal"))
                coins += PeppersPride_bet * 2
                with open('money_data.txt', 'w') as f:
                    f.write(str(coins))
                time.sleep(3)
                restart()
                bets()
        else:
            return bets()
        if racecourse.bgpic() == os.path.join('resources', 'race_track.gif'):
            Eclipse.motion()
            if Eclipse.xcor() >= 450:
                winner.write("Eclipse is the winner!", align="center",font=("Comic Sans MS", 24, "normal"))
                coins += Eclipse_bet * 2
                with open('money_data.txt', 'w') as f:
                    f.write(str(coins))
                time.sleep(3)
                restart()
                bets()
        else:
            return bets()
        def restart():
            Kincsem.hideturtle()
            BlackCaviar.hideturtle()
            PeppersPride.hideturtle()
            Eclipse.hideturtle()
            Kincsem.setposition(-470, 230)
            BlackCaviar.setposition(-470, 90)
            PeppersPride.setposition(-470, -60)
            Eclipse.setposition(-470, -220)
            winner.clear()



    racecourse.bye()

def kESC():
    if start.isvisible() or racecourse.bgpic() == os.path.join('resources', 'Bet_screen.gif'):
        racecourse.bye()
    else:
        global running
        running = False
running = True
racecourse.onkey(kESC, "Escape")
racecourse.listen()
init()
racecourse.mainloop()