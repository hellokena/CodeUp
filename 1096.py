white = int(input())
array = [[0 for col in range(19)] for row in range(19)]
for i in range(white):
    x, y = map(int, input().split())
    array[x-1][y-1] = 1
for a in range(19):
    for b in range(19):
        print(array[a][b], end = ' ')
    print()