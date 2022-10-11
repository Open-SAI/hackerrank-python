if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

#for i in cX:
#    for j in cY:
#        for k in cZ:
#            print (cX[i],cY[j],cZ[k])
#permuta = []
#[ permuta.append([cX[i],cY[j],cZ[k]]) for i in cX for j in cY for k in cZ if (cX[i]+ cY[j] + cZ[k]) != n ]

print([ [i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i + j + k) != n ])

#print (permuta)
