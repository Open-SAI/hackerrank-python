from collections import Counter

shoes_number=int(input())
shoes_sizes=[int (size) for size in input().split()]
inventory=Counter(shoes_sizes)
customers=int(input())
user_input_order=[]
money_earned=0

for input_line in range(customers):
    print ("entry: ",input_line)
    shoe_size,price=input().split()
    user_input_order.append([int(shoe_size),int(price)])


print ("Shoes Number:", shoes_number)
print ("Shoes sizes:", shoes_sizes)
print ("Amount of customers", customers)
print ("User Input Order: ", user_input_order)
print ("Inventory: ", Counter(shoes_sizes))

for size, price in user_input_order:
    if size in shoes_sizes and inventory[int(size)]>0:
        money_earned+=int(price)
        print ("size:  ", size,"price: ", price, "availability: ", inventory[int(size)])
        shoes_sizes.remove(size)

print ("Remaining List:", shoes_sizes)

print ("TOTAL: ", money_earned)     
        
         
