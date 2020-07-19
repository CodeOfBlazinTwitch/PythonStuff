numbers = []
x = int(input("How Many Numbers: "))
while x > 0:
    numbers.append(int(input("Number: ")))
    x -= 1
    
newList = []

counter3 = 0
counter = 0
counter2 = 0
sumy = 0
for z in numbers:
    if counter3 > 0:
        counter = counter3
        sumy = 0
        while counter >= 0:
            sumy += numbers[counter]
            counter -= 1
        newList.append(sumy)
    else:
        newList.append(z)
    counter3 += 1
print(newList)
