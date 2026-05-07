import fitting_rooms
import customer
import time
import random
import threading

#start/end time for scenario
#Elapsed time (from start/end)
#Number of customers serviced
#Avg room usage
#Total customer time spent in queue


class Scenario:

    def __init__(self):
        self.room_count = int(input("Enter the number of rooms avialable (default 3): "))
        self.customer_count = int(input("Enter the number of customers: "))
        self.clothing_items = int(input("Enter the number of clothing itmes (0 for random): "))
        self.enforce_item_max = input("Enforce item maximum? (Y/N): ")
        self.main_lock = threading.Lock()

    def start_scenario(self):

        rooms = fitting_rooms.DressingRoom(self.room_count)
        
        while self.customer_count > 0:

            #customer arrives
            time_between_customers = random.randint(1,5)
            cust = customer.Customer(self.clothing_items, self.enforce_item_max, self.customer_count, self.main_lock, rooms)
            print(f"Customer {self.customer_count} has arrived at the fitting room with {cust.number_of_items} items")

            #customer requests room
            response = rooms.request_room()

            #customer occupys room if available
            if response == "permitted":
                cust.occupy_room()

            #customer waits for room if not
            else:
                cust.enqueue()

            #next customer
            time.sleep(time_between_customers)
            customer_count -= 1