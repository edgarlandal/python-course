# functions
def exc1():
    print("=== List ===")

    colors = ["white", "black"]
    print(colors)

    colors.append("red")
    colors.append("blue1")
    print(colors)

    # read elements
    print(colors[0])
    print(colors[2])

    # travel with the loop
    for color in colors:
        print(color)

def exc2():
    numbers = [87, 72, 111, 91, 75, 9, 145, 62, 126, 121, 150, 65, 85, 44, 54]

    for num in numbers:
        print(num)

    print("--------------------")

    count = len(numbers);
    print("There are " + str(count) + " numbers in the list")

    print("--------------------")

    total = 0
    count = 0
    count_lower = 0

    for num in numbers:
        total += num

        if num > 100:
            count += 1
        if num < 100:
            count_lower += 1

    print(total)
    print(count)
    print(count_lower)

def how_many_times(color):
    colors = ["Red", "yEllow", "BLUE", "RED", "GreeN", "YELLOW", "reD", "green"]
    
    count = 0
    
    for cl in colors:
        if cl.lower() == color.lower():
            count += 1
    
    print("There are "+ str(count) + " ocurrences of " + color)

# call the fns
exc1()
exc2()

how_many_times("rEd")
how_many_times("BlUe")