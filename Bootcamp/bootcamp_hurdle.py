def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
state = 0 #0 = right, 1 = up, 2 = down, 3 = jump
while not at_goal():
    if state == 0:
        if wall_in_front():
            turn_left()
            state = 1
        else:
            move()
    elif state == 1:
        if wall_on_right():
            move()
        else:
          turn_right()
          state = 3
    elif state == 3:
         move()
         turn_right()
         state = 2
    elif state == 2:
        if wall_in_front():
            turn_left()
            state = 0
        else:
            move()