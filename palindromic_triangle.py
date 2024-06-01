'''
This exercise must be print a palindromic number triangle for a entred integer number, example:

If we type n = 7:
 7

We get:
 1
 121
 12321
 1234321
 123454321
 12345654321
 1234567654321

The difficulty appears when the program only can  contain from one to two lines of code.

The use of "lambda functions" in his recursive mode, can be useful here, and there is an mathematical tip: the use of multiplication of series of numbers 1, 11, 111, 1111, 11111, ..., from the number theory. This type of multiplication has a behavior like the palindromic objective triangle.
'''
for count, line in enumerate(map((serie:=lambda x: pow(10,x-1) + serie(x-1) if x>1 else x),range(1,int(input())+1)),1): print (line*line)

