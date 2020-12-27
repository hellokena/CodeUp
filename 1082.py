n = int(input(), 16)
# 10 to 16 hex
# string to any int
for i in range(1, 16):
    print("%X*%X=%X"%(n,i,n*i))