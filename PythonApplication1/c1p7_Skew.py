def skew ( genome ) :
    """ progress along a DNA string to (attempt) identify OriC based on G-C evolution 

    Based on a text string input, identifies variation of ( G - C ) evolution along the string
    Output must show every step of this evolution
    """
    count = 0
    output = ["", ""]
    output[0] += str(count) + " " 
    min = 999
    for x in range(0, len(genome)):
        i = genome[x]
        if i == "G":
            count += 1
        elif i == "C":
            count -= 1
        output[0] += str(count) + " "
        if min > count:
            output[1] = str(x + 1) + " "
            min = count
        elif min == count:
            output[1] += str(x + 1) + " "
    return output
