import threading
import random
import fitting_rooms


class Customer:
    def __init__(self, number_of_items, item_max_enforced):

        if item_max_enforced == "Y":
            max_items = 6

        if number_of_items == 0:
            self.number_of_items = random.randint(1,max_items)

        elif number_of_items > 20:
            self.nubmer_of_items = 20
            print("Item count defaulted to maximum value of 20")

        print(f"Customer arrived with {self.number_of_items} items")

        return