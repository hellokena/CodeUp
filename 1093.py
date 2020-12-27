n = int(input())
attend1 = map(int, input().split())
attend2 = [0]*23
for i in attend1:
    attend2[i-1] += 1
for j in attend2:
    print(j, end = ' ')