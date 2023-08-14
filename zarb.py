def  zarb( ):
    row=int(input("Enter a number for row:"))
    col=int(input("Enter a numberfor col : "))
    for i in range(0,row+1):
        for j in range(0,col+1):
            if i==0 and j==0:
                print(" x  _|",end=" ")
            elif i==0:
                print("_",j,"_|",end="  ")
            elif j==0:
                print("_",i,"_|",end="  ")
            else:
                print("_",i*j,"_|",end="  ")
        print()
zarb( )       




