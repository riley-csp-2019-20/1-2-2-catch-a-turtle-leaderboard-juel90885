# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl 
import random as brad
import leaderboard as lb

#-----game configuration----
shape = "turtle"
size = 5
color = "yellow"
score = 0
timer = 5
counter_interval = 1000 #1000 represents 1 second
time_up = False

# leaderboard variables
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your name:")

#-----initialize turtle-----
lilt = trtl.Turtle(shape = shape)
lilt.color("yellow")
lilt.shapesize(2)
lilt.speed(0)

#-----initialize score board-----
sb = trtl.Turtle()
sb.ht()
sb.penup()
sb.goto(-370,270)
font = ("Courier", 30, "bold")
sb.write("Score:", font = font)
sb.ht()
counter = trtl.Turtle()
counter.penup()
counter.goto(250,310)
counter.ht()

#-----game functions--------
def turtle_clicked(x,y):
    print("don't touch me!")
    change_position()
    score_counter()

def change_position():
    lilt.penup()
    lilt.ht()
    new_xpos = brad.randint(-400,400)
    new_ypos = brad.randint(-300,300)
    lilt.goto(new_xpos, new_ypos)
    lilt.st()

def score_counter():
    global score
    score += 1
    print(score)
    sb.write(score,font = font)
    sb.clear()
    sb.write(score,font = font)

def countdown():
  global timer, time_up
  counter.clear()
  if timer <= 0:
    game_end()
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font = font)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
def game_end():
  lilt.ht()
  lilt.goto(500,500)
  counter.goto(-300,120)
  counter.write("Time's Up, were you fast enough?", font = font)
  wn.bgcolor("red")
def size_down():
  global size
  size -= 1
  lilt.shapesize(size)

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global lilt

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, lilt, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, lilt, score)
#-----events----------------
lilt.onclick(turtle_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)

wn.mainloop()
