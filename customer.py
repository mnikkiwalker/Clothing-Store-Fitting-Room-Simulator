import threading
import random
import time


class Customer(threading.Thread):
    def __init__(self, number_of_items, item_max_enforced, customer_number, rooms):
        super().__init__()

        self.number_of_items = number_of_items
        self.item_max_enforced = item_max_enforced
        self.customer_number = customer_number
        self.rooms = rooms

        #metrics
        self.wait_time = 0
        self.time_in_room = 0
        self.serviced = 0

        #establish number of items protocol
        if self.item_max_enforced == "Y":
            max_items = 6

        else:
            max_items = 20

        if self.number_of_items == 0:
            self.number_of_items = random.randint(1,max_items)

        elif self.number_of_items > 20:
            self.number_of_items = 20
            print("Item count defaulted to maximum value of 20")

    def run(self):
        # This is what happens in the background
        print(f"Customer {self.customer_number} has arrived with {self.number_of_items} items")
        
        # Check for a room immediately
        if self.rooms.request_room():
            self.occupy_room()
        else:
            self.enqueue()
    

    def enqueue(self):

        print(f"Customer {self.customer_number} has entered the queue")

        start_wait = time.time()
        self.rooms.available_rooms.acquire() 
        self.wait_time = time.time() - start_wait
        print(f"Customer {self.customer_number} has left the queue after {round(self.wait_time)} minutes")
        self.occupy_room()


    def occupy_room(self):

        occupy_start = time.time()
        print(f"Customer {self.customer_number} has entered the fitting room")

        while self.number_of_items > 0:

            #minutes translated to second so the sim runs quicker
            time_for_item = random.randint(1,3)
            time.sleep(time_for_item)
            self.number_of_items -= 1


        #####serviced
        self.rooms.release_room()
        occupy_end = time.time()

        #metrics
        self.time_in_room = occupy_end - occupy_start
        self.serviced = 1

        print(f"Customer {self.customer_number} has left the fitting room")

        
        

        


