import random

iterations = int(input("n = ").strip()) + 1

def calcprob(reps, z):
    nums = 6
    numlist = [0] * nums

    for i in range(reps):
        n = random.randint(1, nums)
        index = n - 1
        item = numlist[index]
        numlist[index] = item + 1 
    #print(numlist)

    x = 0
    for h in numlist:
        x += h
    #print(x)

    problist = []
    for j in range(len(numlist)):
        problist.append(round(numlist[j] / x, z + 1))
    
    #if z > 0:


    print(problist, f"{x:,d}")

for z in range(iterations):
    calcprob(10 ** (z + 1), z)