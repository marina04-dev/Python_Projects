import turtle
import time
import random


WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'orange', 'yellow', 'black','purple','pink', 'brown', 'cyan']


def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Invalid Input! Try Again!!!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Invalid Number Input! Only 2 to 10 can race!")

def create_turtles(colors):
    turtles = []
    spacing_x = WIDTH//(len(colors)+1)
    for i,color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2+(i+1)*spacing_x, -HEIGHT//2+20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(colors):
    turtles_race = create_turtles(colors)
    while True:
        for racer in turtles_race:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            x, y = racer.pos()
            if y >= HEIGHT//2-10:
                return colors[turtles_race.index(racer)]


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtles Racing!")

racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
print("The winner is the turtle with the color: " + winner)
time.sleep(5)

