# notice that 10**i always has more than i digits so we only need brute force numbers 2..9 to the i-th power

LIMIT = 22 # limit experimentally determined
count = 0
for i in range(1, LIMIT):
    for digit in range(2, 10):
        if len(str(digit**i)) == i: count +=1
print(count+1) # adding 1**1

# output: 49
