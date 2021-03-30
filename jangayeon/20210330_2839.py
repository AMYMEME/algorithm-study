weight = int(input())
total = 0
while True:
    if (weight % 5) == 0:
        total =total + (weight//5)
        print(total)
        break
    weight = weight-3
    total =total+ 1
    if weight < 0:
        print("-1")
        break