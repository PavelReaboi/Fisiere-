with open("numar.txt","r") as f:
    x=int(f.readline())
with open("inmultire.txt","w") as f:
    i=str(x)+'*1='+str(x*1)+'\n'
    f.write(i)
    i=str(x)+'*2='+str(x*2)+'\n'
    f.write(i)
    i=str(x)+'*3='+str(x*3)+'\n'
    f.write(i)
    i=str(x)+'*4='+str(x*4)+'\n'
    f.write(i)
    i=str(x)+'*5='+str(x*5)+'\n'
    f.write(i)
    i=str(x)+'*6='+str(x*6)+'\n'
    f.write(i)
    i=str(x)+'*7='+str(x*7)+'\n'
    f.write(i)
    i=str(x)+'*8='+str(x*8)+'\n'
    f.write(i)
    i=str(x)+'*9='+str(x*9)+'\n'
    f.write(i)
    i=str(x)+'*10='+str(x*10)
    f.write(i)