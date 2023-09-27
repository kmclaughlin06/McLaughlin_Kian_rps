#This file was created by Kian Mclaughlin
from random import randint 
'''
Goals:
When a user click on their choice, the computer randomly chooses and displays the result 

'''

# import package
import turtle
from turtle import *
# The os module allows us to access the current directory in order to access assets
import os
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))
# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')

# setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

rock_w, rock_h = 256, 280

paper_w, paper_h = 256, 204

scissors_w, scissors_h = 256, 170

exit_button_w, exit_button_h = 50, 40

play_again_button_w, play_again_button_h = 150,32

play_again_button = True


# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="black")


# canvas object
cv = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)


# setup the rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')
computer_rock_image = os.path.join(images_folder, 'computer_rock.gif')
# instantiate (create an instance of) the Turtle class for the rock
rock_instance = turtle.Turtle()
computer_rock_instance = turtle.Turtle()
# setup the paper image using the os module as paper_image
paper_image = os.path.join(images_folder, 'paper.gif')
computer_paper_image = os.path.join(images_folder, 'computer_paper.gif')
# instantiate (create an instance of) the Turtle class for the paper
paper_instance = turtle.Turtle()
computer_paper_instance = turtle.Turtle()
# setup the scissors image using the os module as scissors_image
scissors_image = os.path.join(images_folder, 'scissors.gif')
computer_scissors_image = os.path.join(images_folder, 'computer_scissors.gif')
# instantiate (create an instance of) the Turtle class for the scissors
scissors_instance = turtle.Turtle()
computer_scissors_instance = turtle.Turtle()

exit_button_image = os.path.join(images_folder, 'exit_button.gif')
exit_button_instance = turtle.Turtle()
play_again_button_image = os.path.join(images_folder, 'play_again_button.gif')
play_again_button_instance = turtle.Turtle()

def show_exit_button(x,y):
    screen.addshape(exit_button_image)
    exit_button_instance.shape(exit_button_image)
    exit_button_instance.penup()
    exit_button_instance.setpos(x,y)

def show_play_again_button(x,y):
    screen.addshape(play_again_button_image)
    play_again_button_instance.shape(play_again_button_image)
    play_again_button_instance.penup()
    play_again_button_instance.setpos(x,y)

def show_rock(x,y):
    # add the rock image as a shape
    screen.addshape(rock_image)
    # attach the rock_image to the rock_instance
    rock_instance.shape(rock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    rock_instance.penup()
    # set the position of the rock_instance
    rock_instance.setpos(x,y)

def show_computer_rock(x,y):
     screen.addshape(computer_rock_image)
     computer_rock_instance.shape(computer_rock_image)
     computer_rock_instance.penup()
     computer_rock_instance.penup()
     computer_rock_instance.setpos(x,y)

def show_paper(x,y):
    # add the paper image as a shape
    screen.addshape(paper_image)
    # attach the paper_image to the paper_instance
    paper_instance.shape(paper_image)
    # remove the pen option from the paper_instance so it doesn't draw lines when moved
    paper_instance.penup()
    # set the position of the paper_instance
    paper_instance.setpos(x,y)

def show_computer_paper(x,y):
     screen.addshape(computer_paper_image)
     computer_paper_instance.shape(computer_paper_image)
     computer_paper_instance.penup()
     computer_paper_instance.penup()
     computer_paper_instance.setpos(x,y)

def show_scissors(x,y):
    screen.addshape(scissors_image)
    scissors_instance.shape(scissors_image)
    scissors_instance.penup()
    scissors_instance.setpos(x,y)

def show_computer_scissors(x ,y):
     screen.addshape(computer_scissors_image)
     computer_scissors_instance.shape(computer_scissors_image)
     computer_scissors_instance.penup()
     computer_scissors_instance.penup()
     computer_scissors_instance.setpos(x,y)

# instantiate a generic turtle
# instantiate a turtle for writing text
text = turtle.Turtle()
text.color('red')
text.hideturtle()
text.penup()

# show_rock(-300, 0)
# show_paper(0, 0)
# show_scissors(300, 0)
# show_exit_button(-460,180)

# this function uses and x y value, an obj, and width and height 
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] - w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False

# function that passes through wn onlick
#options for computer to choose from

def cpu_choice():
    choices = ["rock", "paper", "scissors"]
    return choices[randint(0,2)]
        
#sets initial text command for player to follow
text.setpos(-175,150)
text.write("Choose Rock, Paper, or Scissors", False, "left", ("Arial", 24, "normal"))

#showing what the computer chooses on the screen
def show_computer_choice(cpu_choice):
    if cpu_choice == "rock":
        print("cpu rock")
        text.setpos(150,150)
        text.write("Computer chose rock", False, "left", ("Arial", 24, "normal"))
        show_computer_rock(300, 0)
        text.setpos(-50,0)
        text.write("VS", False, "left", ("Arial", 50, "normal"))
    elif cpu_choice == "paper":
        print("cpu paper")
        show_computer_paper(300, 0)
        text.setpos(150,150)
        text.write("Computer chose paper", False, "left", ("Arial", 24, "normal"))
        text.setpos(-50,0)
        text.write("VS", False, "left", ("Arial", 50, "normal"))
    elif cpu_choice == "scissors":
        print("cpu scissors")
        show_computer_scissors(300, 0)
        text.setpos(135,150)
        text.write("Computer chose scissors", False, "left", ("Arial", 24, "normal"))
        text.setpos(-50,0)
        text.write("VS", False, "left", ("Arial", 50, "normal"))

#function for when user collides with the image it picks that image as the item to play

def mouse_pos(x, y):
    if collide (x,y, exit_button_instance, exit_button_w, exit_button_h):
        turtle.bye()
    elif collide(x,y,play_again_button_instance, play_again_button_w, play_again_button_h):# if collide with play again it will run main function to loop the game
        paper_instance.shape("blank")
        scissors_instance.shape("blank")
        rock_instance.shape("blank")
        computer_paper_instance.shape("blank")
        computer_scissors_instance.shape("blank")
        computer_rock_instance.shape("blank")
        main()
        
    elif collide(x,y,rock_instance, rock_w, rock_h):
        print ("rock")
        text.clear()
        text.setpos(-400,150)
        text.write("You chose rock", False, "left", ("Arial", 24, "normal"))
        paper_instance.shape("blank")
        scissors_instance.shape("blank")
        rock_instance.shape("blank")
        show_rock(-300,0)
        cpuPick = cpu_choice() #plays user choiec against human choice to see who wins
        show_computer_choice(cpuPick)
        if cpuPick == "rock":
            print("tie")
            text.clear()
            rock_instance.shape("blank")
            computer_rock_instance.shape("blank")
            show_rock(0,0)
            show_computer_rock(0,0)
            rock_instance.shape("blank")
            show_rock(-300,0)
            show_computer_rock(300,0)
            text.setpos(-80,150)
            text.write("Its a Tie!", False, "left", ("Arial", 24, "normal"))
            show_play_again_button (0,-175)
        elif cpuPick == "paper":
            print("lose")
            text.clear()
            rock_instance.shape("blank")
            computer_paper_instance.shape("blank")
            show_rock(0,0)
            show_computer_paper(0,0)
            rock_instance.shape("blank")
            show_computer_paper(0,0)
            text.setpos(-80,150)
            text.write("You Lose!", False, "left", ("Arial", 24, "normal"))
            show_play_again_button (0,-175)
        elif cpuPick == "scissors":
            print("win")
            text.clear()
            rock_instance.shape("blank")
            computer_scissors_instance.shape("blank")
            show_rock(0,0)
            show_computer_scissors(0,0)
            computer_scissors_instance.shape("blank")
            show_rock(0,0)
            text.setpos(-80,150)
            text.write("You Won!", False, "left", ("Arial", 24, "normal"))
            show_play_again_button (0,-175)

    elif collide(x,y,paper_instance, paper_w, paper_h):
        print("paper")
        text.clear()
        text.setpos(-400,150)
        text.write("You chose paper", False, "left", ("Arial", 24, "normal"))
        rock_instance.shape("blank")
        scissors_instance.shape("blank")
        paper_instance.shape("blank")
        show_paper(-300,0)
        cpuPick = cpu_choice()
        show_computer_choice(cpuPick)
        text.clear
        if cpuPick == "paper":
            print("tie")
            text.clear()
            paper_instance.shape("blank")
            computer_paper_instance.shape("blank")
            show_paper(0,0)
            show_computer_paper(0,0)
            paper_instance.shape("blank")
            show_paper(-300,0)
            show_computer_paper(300,0)
            text.setpos(-80,150)
            text.write("Its a Tie!", False, "left", ("Arial", 24, "normal"))
            show_play_again_button (0,-175)
        elif cpuPick == "rock":
            print("win")
            text.clear()
            paper_instance.shape("blank")
            computer_rock_instance.shape("blank")
            show_paper(0,0)
            show_computer_rock(0,0)
            computer_rock_instance.shape("blank")
            show_paper(0,0)
            text.setpos(-80,150)
            text.write("You Won!", False, "left", ("Arial", 24, "normal"))
            show_play_again_button (0,-175)
        elif cpuPick == "scissors":
            print("lose")
            text.clear()
            paper_instance.shape("blank")
            computer_scissors_instance.shape("blank")
            show_paper(0,0)
            show_computer_scissors(0,0)
            paper_instance.shape("blank")
            show_computer_scissors(0,0)
            text.setpos(-80,150)
            text.write("You Lose!", False, "left", ("Arial", 24, "normal"))
            show_play_again_button (0,-175)

    elif collide(x,y,scissors_instance, scissors_w, scissors_h):
        print("scissors")
        text.clear()
        text.setpos(-400,150)
        text.write("You chose scissors", False, "left", ("Arial", 24, "normal"))
        paper_instance.shape("blank")
        rock_instance.shape("blank")
        scissors_instance.shape("blank")
        show_scissors(-300,0)
        cpuPick = cpu_choice()
        show_computer_choice(cpuPick)
        text.clear
        if cpuPick == "scissors":
            print("tie")
            text.clear()
            scissors_instance.shape("blank")
            computer_scissors_instance.shape("blank")
            show_scissors(0,0)
            show_computer_scissors(0,0)
            paper_instance.shape("blank")
            show_scissors(-300,0)
            show_computer_scissors(300,0)
            text.setpos(-80,150)
            text.write("Its a Tie!", False, "left", ("Arial", 24, "normal"))
            show_play_again_button (0,-175)
        elif cpuPick == "rock":
            print("lose")
            text.clear()
            scissors_instance.shape("blank")
            computer_rock_instance.shape("blank")
            show_scissors(0,0)
            show_computer_rock(0,0)
            scissors_instance.shape("blank")
            show_computer_rock(0,0)
            text.setpos(-80,150)
            text.write("You Lose!", False, "left", ("Arial", 24, "normal"))
            show_play_again_button (0,-175)
        elif cpuPick == "paper":
            print("win")
            text.clear()
            scissors_instance.shape("blank")
            computer_paper_instance.shape("blank")
            show_scissors(0,0)
            show_computer_paper(0,0)
            computer_paper_instance.shape("blank")
            show_scissors(0,0)
            text.setpos(-80,150)
            text.write("You Won!", False, "left", ("Arial", 24, "normal"))
            show_play_again_button (0,-175)
            
        
    else:
        print("choose something valid")
        text.clear()
        text.setpos(-125,150)
        text.write("Choose something valid!", False, "left", ("Arial", 24, "normal"))
        



    
# user this to get mouse position
# runs mainloop for Turtle - required to be last

    #defining main function for loop
def main():
        text.clear()
        text.setpos(-175,150)
        text.write("Choose Rock, Paper, or Scissors", False, "left", ("Arial", 24, "normal"))
        show_rock(-300, 0)
        show_paper(0, 0)
        show_scissors(300, 0)
        show_exit_button(-460,180)
        screen.onclick(mouse_pos)



main()

screen.mainloop()