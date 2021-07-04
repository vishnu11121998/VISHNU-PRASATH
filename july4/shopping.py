cart = {}
price = 0
quantity = 0
total = 0
while True:
    print("1.Add item\n2.remove\n3.View\n4Exit")
    x = int(input("Enter the your choice:"))
    if x == 1: 
        name = str(input("Enter the product name"))
        if name in cart.keys(): 
            input('The item is already there if you want to make change \n 1.add to existing \n 2. remove from the cart\n')
            option = int(input('Enter your option:'))
            if option == 1: 
                print("Existing Quantity from the cart is: ", quantity)
                new = int(input("Enter new quantity:"))
                quantity += new
                total = price * quantity
                cart[name] = [price, quantity, total]
            elif option == 2:
                new = int(input("Quantity to deduce:"))
                if new == 0:  
                    print('Quantity is 0 so it is get removed from the cart')
                    cart.pop(name)
                else:  
                    quantity -= new
                    if quantity == 0: 
                        print('The item is removed from the list')
                        cart.pop(name)
                    else:
                        print('The quantity has been changed')
                        total = price * quantity
                        cart[name] = [price, quantity, total]
        else:  
             price = int(input("Enter the product price:"))
             quantity = int(input("Enter the quantity of the item:"))
             total = price * quantity
             cart[name] = [price, quantity, total]
    elif x == 2:
        removeprod = str(input("Enter the item you want to remove:"))
        if removeprod in cart.keys():
            cart.pop(removeprod)
        else:
            print("Item is not present in the list of cart")
    elif x == 3:  
        print(cart)
        print("Item\tPrice\tQuantity\tTotal")
        for i in cart.keys():
            print(i, end="    ")
            for j in cart[i]:
                print(j, end="\t\t")
            print()
    elif x == 4:
        break
    else:
        print('Invalid')

    
    
