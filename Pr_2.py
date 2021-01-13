with open("numere.txt","r") as f:
    x=int(f.readline())
    y=int(f.readline())
if x>y:
    min=str(y*3)
    max=str(x*2)
else:
    min=str(x*3)
    max=str(y*2)
with open("produs.txt","w") as f:
    f.write(min)
    f.write('\n')
    f.write(max)