given_list = [5,4,2,3,1]

def BubbleSort(z):
    counter = 0
    counter2 = 0
    print("Starting List ----->", z)
    while counter2 < len(z) - 1:
        counter = 0
        while counter < len(z) - 1:
            if z[counter] > z[counter + 1]:
                z[counter], z[counter + 1] = z[counter + 1],z[counter]
            counter += 1
        counter2 += 1
    return z
        
        
print("Final Bubble Sorted List ----->", BubbleSort(given_list))
