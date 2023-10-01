# Upright pyramid
num = 10
space = 10
for i in range(num):
    print(" "*space,i*"* ")
    space-=1
    
# Downward pyramid
for i in range(num,0,-1):
    print(" "*space,"* "*i)
    space+=1