entrees = {
    "Beef": 5,
    "Pork": 4,
    "Chicken": 4
}

sides = {
    "Beans": 1,
    "Rice": 1,
    "Eggs": 2
}

def printMenu(menu):
    """Pass a dict of key:values "Item": Cost to print all items and cost"""
    for key,value in menu.items():
        print(f"{key}: ${value}")

def orderItem(menu, prompt="Choose an item from the menu:\n"):
    """Returns tuple (order, cost). Prompt for item to order, check against menu for valid input"""
    while True:
        order = input(prompt)
        if order in menu.keys():
            cost = menu[order]
            print(f"You ordered {order} for ${cost}")
            return order, cost
        else:
            print("Invalid order")


order_list = []
total_cost = []

print("*Entrees*:")
printMenu(entrees)
print("*Sides*:")
printMenu(sides)

entree, cost = orderItem(entrees,"Choose an entree:\n")
order_list.append(entree)
total_cost.append(cost)

side, cost = orderItem(sides,"Choose first side:\n")
order_list.append(side)
total_cost.append(cost)

side, cost = orderItem(sides,"Choose second side:\n")
order_list.append(side)
total_cost.append(cost)

    
orderString = ", ".join(order_list[:-1])
lastItem = order_list[-1]

print(f"Your order of {orderString}, and {lastItem} comes to a total of ${sum(total_cost)}")
