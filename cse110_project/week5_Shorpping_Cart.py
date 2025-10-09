#Shopping CART

#Creat Empty Cart

items = []
prices = []

while True:
    print("Menu shopping Cart:")
    print("1. Add an Item")
    print("2. View Cart")
    print("3. Remove an Item")
    print("Compute Total")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        choice_item = input("What would you like to add? ").strip()

        try:
            choice_price = float(input(f"What is the price of {choice_item} "))
            items.append(choice_item)
            prices.append(choice_price)
            print(f"'{choice_item}' has been added to Cart")
        except ValueError:
            print("Invalid price. Please enter a number.")
    #view cart
    elif choice == "2":
        if not items:
            print("The shopping cart is empty.")
        else:
            print("The contents of the shopping cart are: ")
            for i in range(len(items)):
                print(f"{i+1}. {items[i]} - ${prices[i]:.2f}")
        
    #Remove Item
    elif choice == "3":
        if not items:
            print("The shopping cart is empty")
        else:
            print("The contents of the shopping cart are: ")
            for i in range(len(items)):
                print(f"{i+1}. {items[i]} - ${prices[i]:.2f}")
        try:
            remove_index = int(input("What item will you like to remove? "))
            if 1 <= remove_index <= len(items):
                remove_item = items.pop(remove_index -1)
                prices.pop(remove_index -1)
                print(f"'{remove_item}' has been remove from the cart.")
            else:
                print("Sorry, that is not a valid item number.")
        except ValueError:
            print("Invalid input. please enter a number.")
    #Compute total
    elif choice == "4":
        if not items:
            print("Invalid price. Please enter a number.")
        else:
            total = sum(prices)
            print(f"The total price of the items in the shopping cart is ${total:.2f}")
    #Quit
    elif choice == "5":
        print("Thank you. Goodbye!!!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")