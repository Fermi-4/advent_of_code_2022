import numpy as np

PATH = "real.txt"

def get_val(n,r,c):
    v=n[r][c]
    left_row=True
    right_row=True
    top_col=True
    bottom_col=True
    for i in n[r][0:c]:
        if i >= v:
            left_row=False
            break
    for i in n[r][c+1:len(n[0])]:
        if i >= v:
            right_row=False
            break
    for i in range(0,r):
        if n[i][c] >= v:
            top_col=False
            break
    for i in range(r+1,len(n)):
        if n[i][c] >= v:
            bottom_col=False
            break
    if left_row | right_row | top_col | bottom_col:
        return 1
    else:
        return 0
with open(PATH, "r") as file:
    data = file.read()
print(data)
lines=data.split("\n")
i=0
numbers=[]
for l in lines:
    chars = [x for x in l]
    numbers.append([int(x) for x in chars])
rows=len(numbers)
cols=len(numbers[0])
data=np.zeros((rows,cols), dtype=int)
np.set_printoptions(threshold=np.inf)
for r in range(0,rows):
    print("processing row: [%i]" % r)
    for c in range(0,cols):
        if r==0 or r==rows-1:
            data[r][c]=1
        elif c==0 or c==cols-1:
            data[r][c]=1
        else:
            data[r][c]=get_val(numbers,r,c)
    print(numbers[r])
    print(data[r])
print("final data:")
print(data)
print(data.sum(axis=1).sum())





