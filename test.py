input = "x**2 + 2*x + 1"

for curr in range(3):
    copy_input = input
    for x in range(len(input)):
        if input[x] == "x":
            copy_input = copy_input[:x] + str(curr) + copy_input[x+1:]
            print(copy_input)
    print(eval(copy_input))