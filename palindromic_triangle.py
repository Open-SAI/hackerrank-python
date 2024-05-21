#for i in range (0, int(input())): 
#    for n in range (0, i):
#        print (i, end='')
#    print()
#    print((lambda i: i)(i))
#    print (range (0, i))
#print(list(map(serial:=lambda x: x*pow(10,x-1) + serial(x-1) if x>1 else x, range(1,int(input())))))
#print(list(map(lambda x: int(x*(pow(10,x)-1)/9), range(1,int(input())))))
#for serie in (list(map(lambda x: int(x*(pow(10,x)-1)/9), range(1,int(input()))))):print (serie)
#for count, line in enumerate(map((serie:=lambda x: pow(10,x-1) + serie(x-1) if x>1 else x),range(1,int(input()))),1): print (count*line)
#for count in range(1,int(input())+1):
#    print (count,((10**count)//2),end=':')
#    print (list(map(serie:=lambda x: pow(10,x-1)*x + serie(x-1) if x>1 else x,range(1,(count*2)-1))))
for count, line in enumerate(map((serie:=lambda x: pow(10,x-1) + serie(x-1) if x>1 else x),range(1,int(input())+1)),1): print (line*line)

