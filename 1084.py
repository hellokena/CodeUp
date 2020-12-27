a,b,c = map(int, input().split())
iter = 0
for i in range(a):
    for j in range(b):
        for k in range(c):
            print(i, j, k)
            iter += 1;
print(iter)
