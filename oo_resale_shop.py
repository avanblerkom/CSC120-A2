from computer import *

class ResaleShop:

    # What attributes will it need?
    inventory = []
    
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory):
        #1. set up an attribute to store the inventory
        self.inventory = inventory


    # What methods will you need?
    def buy(self, computer: Computer):
        #1. call Computer(...) constructor to create a new Computer instance 
        self.inventory.append(computer)
        #2. call inventory.append(...) to add the new computer instance to the inventory
        return self.inventory.index(computer)
    
    def sell(self, computer: Computer):
        if computer in self.inventory:
            self.inventory.remove(computer)
            print("Item sold!")
    
    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for item in self.inventory:
                # Print its details
                print(f'Item ID: {self.inventory.index(item)} : {item}')
        else:
            print("No inventory to display.")

def main():
    computer1: Computer = Computer("1998 MacBook Pro", "Intel", 256, 16, "High Sierra", 2011, 1000)
    computer2: Computer = Computer("2024 MacBook Pro", "Intel", 300, 20, "High Sierra", 2024, 1500)
    resaleshop: ResaleShop = ResaleShop([])
    resaleshop.buy(computer1)
    resaleshop.buy(computer2)
    resaleshop.print_inventory()
    resaleshop.sell(computer2)
    resaleshop.print_inventory()
    print(computer1.price)
    Computer.refurbish(computer1, "Monterey")
    resaleshop.print_inventory()
    print(computer1.operating_system)
    print(computer1.price)


if __name__ == "__main__": 
    main()
    