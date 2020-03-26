'''A robot moves in a plane starting from the original point (0,0).
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps.
Please write a program to compute the distance from current position
after a sequence of movement and original point.
If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be: (-1.0, 2.0)'''


def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def validate_movement(mov_list):
    if ((mov_list[0].upper() not in ['UP', 'DOWN', 'LEFT', 'RIGHT']) or
       not(is_float(mov_list[1]))):
        print("[WARNING] Invalid command! Try Again")
        return False
    else:
        return True


def movement_tracker(command, pos):
    if command[0].upper() == "UP":
        pos[1] += float(command[1])
    elif command[0].upper() == "DOWN":
        pos[1] -= float(command[1])
    elif command[0].upper() == "LEFT":
        pos[0] -= float(command[1])
    elif command[0].upper() == "RIGHT":
        pos[0] += float(command[1])
    return pos


def main():
    pos = [0.0, 0.0]
    print("MOVE ROBOT MOVE!")
    flag = True
    while(flag):
        command = input("MOVE : ").strip().split(" ")
        if not(validate_movement(command)):
            continue
        pos = movement_tracker(command, pos)
        flag = True if input("Continue(Y/N)? ").upper() == 'Y' else False
    print("\n└[∵]┘ ROBOT's position on 2D plane : ({0}, {1})".format(*pos))


if __name__ == "__main__":
    main()
