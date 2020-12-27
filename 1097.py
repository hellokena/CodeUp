array = [[0 for col in range(19)] for row in range(19)]

###
for i in range(19):
    p = list(map(int,input().split()))
    array[i] = p

n = int(input())
for i in range(n):
    x,y = map(int, input().split())
    #x축
    for a in range(19):
        array[x-1][a] = abs(array[x-1][a]-1)
    for b in range(19):
        array[b][y-1] = abs(array[b][y-1]-1)
    #array[x-1][y-1] = abs(array[x-1][y-1]-1)

for j in range(19):
    for k in range(19):
        print(array[j][k], end = ' ')
    print()
