class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, desc:str, proc:str, hd:int, mem:int, os:str, year:int, price:int):
        self.description = desc
        self.processor_type = proc
        self.hard_drive_capacity = hd
        self.memory = mem
        self.operating_system = os
        self.year_made = year
        self.price = price

    # What methods will you need?

    def refurbish(self, new_OS:str):
        if new_OS is not None:    
            self.operating_system = new_OS
        if self.year_made < 2000:
            self.price = 0
        elif self.year_made < 2012:
            self.price = 250
        elif self.year_made < 2018:
            self.price = 550
        else:
            self.price = 1000

        



    
        


    
