n = int(input())
sum = 0
f = 1
while True:
    sum += f
    if sum >= n:
        break
    f += 1
print(f)