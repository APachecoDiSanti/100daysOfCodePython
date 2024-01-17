# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_around()
    turn_left()

# The strategy is to follow the right edge of the maze
# Prevent moving right four times to prevent loops
times_moving_right = 0
while not at_goal():
    if right_is_clear() and times_moving_right < 3:
        turn_right()
        move()
        times_moving_right += 1
    elif front_is_clear():
        move()
        times_moving_right = 0
    else:
        turn_left()
        times_moving_right = 0