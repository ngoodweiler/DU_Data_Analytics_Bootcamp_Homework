run = "y"
i = 0
j = 10

while run == "y":
    for x in range(i,j):
        print(x)
    run = input("Would you like to continue? y/n")
    i = i + 10
    j = j + 10
