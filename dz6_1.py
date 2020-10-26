a=100000
b = False
for i in list(range(2,a)):
    for j in range(2, int((i/2)+1)):
            if(i % j !=0): 
                b = True
            else:
                b = False
                break
    if(b == True):
        print(i)