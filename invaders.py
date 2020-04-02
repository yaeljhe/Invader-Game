import turtle
import os
import math
import random


#Set up the screen
screen = turtle.Screen()
screen.bgcolor("Black")
screen.title("Space Invaders")
screen.bgpic("background2.gif")

#Register the shapes
screen.register_shape("invader.gif")
screen.register_shape("player.gif")

#Draw Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("White")
border_pen.penup()
border_pen.setpos(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Set the score to 0
score = 0

#Draw the score 
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align = "left", font = ("Arial", 14, "normal"))
score_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 20

# Create Enemy
enemyspeed = 3

#Choose number of enemies
number_of_enemies = 5
#Create an empty list of enemies
enemies = []

#Add enemies to the list 
for i in range(number_of_enemies):
    #Create the enemy
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    #y = random.randint(-250,-250)
    enemy.setposition(x,y)

# Create player bullet
bullet = turtle.Turtle()   
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 20

# Define bullet state
# ready - ready to fire
# fire - bullet is firing
bulletstate = "ready"

# Move player left
def move_left():
    x = player.xcor()
    x -= playerspeed
    # Player Boundary
    if x < -280:
        x = -280
    player.setx(x)
# Move player right
def move_right():
    x = player.xcor()
    x += playerspeed
    # Player Boundary
    if x > 280:
        x = 280
    player.setx(x)

def gameOver():
    player.hideturtle()
    for enemy in enemies:
        enemy.hideturtle()
    gameover_pen = turtle.Turtle()
    gameover_pen.speed(0)
    gameover_pen.color("red")
    gameover_pen.penup()
    gameover_pen.setposition(0,0)
    gamestring = "GAME OVER"
    gameover_pen.write(gamestring, False, align = "center", font = ("Arial", 44, "bold"))
    gameover_pen.hideturtle()


def fire_bullet():
    #Declare bulletstate as a global if it needs changed
    global bulletstate # changes in function are reflected globallly for this variable 
    if bulletstate == "ready":
        bulletstate = "fire"  
        #Move the bullet just above the player
        x = player.xcor()
        y = player.ycor() +10
        bullet.setpos(x,y)
        bullet.showturtle()
#Enemy has reach player ship
def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False
#Enemy has reached bottom of screen        
def enemyWins():
    for enemy in enemies:
        if enemy.ycor() < -270:
            enemy.sety(-270)
            return True
        else:
            return False

#Player has won games 
def playerWins():
    player.hideturtle()
    for enemy in enemies:
        enemy.hideturtle()
    gamewon_pen = turtle.Turtle()
    gamewon_pen.speed(0)
    gamewon_pen.color("gold")
    gamewon_pen.penup()
    gamewon_pen.setposition(0,0)
    wonstring = "YOU WIN"
    gamewon_pen.write(wonstring, False, align = "center", font = ("Arial", 44, "bold"))
    gamewon_pen.hideturtle()

#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left,"Left") # When left arrow key clicked, call function move_left
turtle.onkey(move_right, "Right") # When Right arrow key clicked, call function move_right
turtle.onkey(fire_bullet,"space") # When space key is clicked, call fire_bullet

#Main game loop
while True:

    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # Move the enemy side to side and down
        if enemy.xcor() > 280:
            #Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Change enemy direction
            enemyspeed *= -1 

        if enemy.xcor() < -280:
            #Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Change enemy direction
            enemyspeed *= -1

        #Check for a collision between the bullet and the enemy
        if isCollision(bullet,enemy):
            #Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setpos(0,-400)
            #Reset the enemy 
            enemy.setposition(-200,250)
            #Update the score
            score += 10 
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align = "left", font = ("Arial", 14, "normal"))
    #Game over display
    if isCollision(player,enemy) or enemyWins():
        gameOver()
        break

    #Player Wins
    if score == 100:
        playerWins()
        break
        
    #Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()   
        y += bulletspeed
        bullet.sety(y)    

    # check to see if the bullets has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

delay = input("Press enter to")