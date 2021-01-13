with open("globulete.txt","r") as f:
    a=int(f.readline())
with open("bradut.txt","w") as f:
    r=a+3
    albas=(a+r)-2
    s=str(r+a+albas)
    b.write(s)