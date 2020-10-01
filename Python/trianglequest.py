for i in range(1,int(input())):
    #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(i *((10**i) - 1) // 9)

    # Math problem more than programming problem, had to look at discussion
    # boards to get it to click.
    # I had the idea to use powers of 10 since they increase the length of
    # a number by one space - but I was trying to figure out getting the
    # result to be 1, 11, 111, 1111... which turned out to be the right
    # approach anyway! So instead of arriving directly at the desired number
    # we go past it to and subtract one, giving us 9, 99, 999, etc. Then
    # divide by 9 and boom!