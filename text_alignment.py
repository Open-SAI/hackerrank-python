# This script is based in the hacker rank challenge "Text Alignment" but with odd number validation.
# The line of the upper and bottom cone drawing was simplified, the last ljust() and first rjust() respectively were removed and it works fine.

while True:
    thickness = int(input()) #This must be an odd number
    if thickness % 2 != 0:
        break
    else:
        print("Please enter an odd number.")
c = 'H'

#Top Cone
for i in range(thickness-1,-1,-1):
    print((c*i).rjust(thickness-1)+c+(c*i))

for i in range(thickness+1): 
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

for i in range((thickness+1)//2): 
    print((c*thickness*5).center(thickness*6)) 

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

for i in range(thickness-1,-1,-1):
    print(((c*(thickness-i-1))+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))