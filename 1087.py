n = int(input())
sum = 0
iter = 0
while True:
    if sum >= n:
        break
    iter += 1
    sum += iter
print(sum)