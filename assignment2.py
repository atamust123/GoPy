def print_map():
    for i in range(x * x):
        if i % x == 0 and i != 0:
            print()
        print("\t" + str(matrix[i]), end="")
    print()
    return


def is_finished():
    vertical_control = which_place % x
    while vertical_control < x * x:
        if matrix[vertical_control] == put:
            vertical_control += x
        else:
            break;
    if vertical_control >= x * x:
        return True
    horizontal_control = which_place // x
    for i in range(horizontal_control * x, x * (horizontal_control + 1)):
        if matrix[i] == put:
            if i == x * (horizontal_control + 1) - 1:
                return True
        elif matrix[i] != put:
            break
    for i in range(x):
        if matrix[i * (x + 1)] == put:
            if i == x - 1:
                return True
        else:
            break
    for i in range(x):
        if matrix[(i + 1) * (x - 1)] == put:
            if i == x - 1:
                return True
        elif matrix[(i + 1) * (x - 1)] != put:
            break

    return False


def control_and_put():
    if matrix[which_place] == put:
        print("You have made this choice before")
    elif matrix[which_place] != which_place:
        print("The other player select this cell before")
    else:
        matrix[which_place] = put
    return True


while True:
    try:
        x = int(input("What Size Game GoPy?"))
        break
    except ValueError:
        print("Enter a valid size")
        continue

matrix = [i for i in range(x * x)]
counter = 0
print_map()

while True:
    no_winner_flag = False
    if counter % 2 != 0:
        put = 'O'
    else:
        put = 'X'
    which_place = int(input("Player " + str(counter % 2 + 1) + " turn--> "))
    if which_place < 0 or which_place >= x * x:
        print("Please enter a valid number")
        print_map()
        counter += 1
        continue

    control_and_put()
    print_map()
    if is_finished():
        print("Winner: " + put)
        break
    for i in range(x * x):
        if matrix[i] == i:
            break
        elif matrix[i] != i:
            if i == x * x - 1:
                print("No winner")
                exit()
    counter += 1
