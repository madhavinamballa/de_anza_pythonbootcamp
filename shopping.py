# ask user to enter item_name,quantity,cost save them in a dictionary 
# ask user Would you like to enter another item?Type 'c' for continue or 'q' to quit
# if user says c then ask enter item_name,quantity,cost
# save all the dictionaries in to a list and print the list 
grocery_item = {} 
grocery_history = [] 

stop = False 

while not stop:
    item_name = input("Item name:\n")   
    quantity = input("Quantity purchased:\n")   
    cost = input("Price per item:\n")
    grocery_item = {'name':item_name, 'number': int(quantity), 'price': float(cost)}
    grocery_history.append(grocery_item)
    user_input = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n")
    if user_input == 'q':
      stop = True
    
grand_total = 0  
print(grocery_history)
print(grocery_item)
