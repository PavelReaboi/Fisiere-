with open("numere.txt","r") as f:
    x=int(f.readline())
    y=int(f.readline())
if x>y:
    min=str(y)
else:
    min=str(x)
with open("minim.txt","w") as f:
    m.write(min)