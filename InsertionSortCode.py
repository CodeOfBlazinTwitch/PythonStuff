given_list = [10,30,25,60,80,75,35,90]

def InsertionSort(z):
    counter = 0
    a = z[0]
    b = []
    while len(z) > 1:
        for x in z:
            if a >= z[counter]:
                a = z[counter]
            counter += 1
        z.pop(z.index(a))
        b.append(a)
        counter = 0
        a = z[0]
        print("Given list:",z)
        print("Sorted list:",b)
    b.append(z[0])
    return b

print(InsertionSort(given_list))
