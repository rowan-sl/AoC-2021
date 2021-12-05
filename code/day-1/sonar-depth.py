with open("input/day-1.txt") as f:
    rdata = f.read()
data = rdata.splitlines()

print(data)

last = None
num_increases = 0
for i in data:
    i = int(i)
    print(i, end=" ")
    if last == None:
        print("n/a")
        last = i
    else:
        if i > last:
            print("inc")
            num_increases += 1
        else:
            print("dec")
        last = i

print(num_increases)
# correct answer: 1184