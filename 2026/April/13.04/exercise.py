position_x = 0
position_y = 0


def move_up() -> None:
    global position_y
    position_y += 1


def move_down() -> None:
    global position_y
    position_y -= 1


def move_left() -> None:
    global position_x
    position_x -= 1


def move_right() -> None:
    global position_x
    position_x += 1


while True:
    command = input("type up, down, left, right or exit: ").strip().lower()

    if command == "up":
        move_up()
    elif command == "down":
        move_down()
    elif command == "left":
        move_left()
    elif command == "right":
        move_right()
    elif command == "exit":
        break
    else:
        print("invalid command")
        continue

    print("position:", position_x, position_y)