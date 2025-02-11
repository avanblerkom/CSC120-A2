from computer import *

class ResaleShop:
''''A class to represent a resale shop that buys and sells computers.'''
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
        # call inventory.remove(...) to remove the computer from the inventory
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
    def refurbish(self, computer:Computer, new_OS:str):
        # If the computer is in the inventory
        if computer in self.inventory:
            if new_OS is not None:    
                computer.operating_system = new_OS
            if computer.year_made < 2000:
                computer.price = 0
            elif computer.year_made < 2012:
                print("here")
                computer.price = 250
            elif computer.year_made < 2018:
                self.price = 550
            else:
                computer.price = 1000
        else:
            print("Item not found. Please select another item to refurbish.")

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
    resaleshop.refurbish(computer2, "Monterey")
    print(computer1.operating_system)
    print(computer1.price)


if __name__ == "__main__": 
    main()
    