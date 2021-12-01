with open("input/day-1.txt") as f:
    rdata = f.read()
data = rdata.splitlines()

last = None

increases = 0
for i, v in enumerate(data):
    try:
        v1 = int(data[i])
        v2 = int(data[i+1])
        v3 = int(data[i+2])
    except IndexError:
        break
    
    vsum = v1+v2+v3
    
    print(v1, v2, v3, vsum, end=" ")
    
    if last is None:
        print("n/a")
        last = vsum
    else:
        if vsum > last:
            print("inc")
            increases += 1
        else:
            print("dec")
        last = vsum

print(increases)
#correct answer: 1158
