with open("input.txt","r") as f:
    x=int(f.readline())
with open("output.txt","w") as f:
    z1,z2,z3,z4,z5=str(x-2),str(x-1),str(x),str(x+1),str(x+2)
    f.write(z1)
    f.write(' ')
    f.write(z2)
    f.write(' ')
    f.write(z3)
    f.write(' ')
    f.write(z4)
    f.write(' ')
    f.write(z5)
    f.write(' ')