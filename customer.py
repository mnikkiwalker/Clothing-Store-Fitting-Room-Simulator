import threading
import random
import time


class Customer(threading.Thread):
    def __init__(self, number_of_items, item_max_enforced, customer_number, shared_lock, rooms):
        super().__init__()

        self.number_of_items = number_of_items
        self.item_max_enforced = item_max_enforced
        self.customer_number = customer_number
        self.lock = shared_lock
        self.wait_time = 0
        self.rooms = rooms

        if self.item_max_enforced == "Y":
            max_items = 6

        if self.number_of_items == 0:
            self.number_of_items = random.randint(1,max_items)

        elif self.number_of_items > 20:
            self.number_of_items = 20
            print("Item count defaulted to maximum value of 20")
    
    def occupy_room(self):

        with self.lock:
            self.rooms.available_rooms.acquire()
            print(f"Customer {self.customer_number} has entered a fitting room")

        while self.number_of_items > 0:

            #minutes translated to second so the sim runs quicker
            time_for_item = random.randint(1,3)
            time.sleep(time_for_item)
            self.number_of_items -= 1

        with self.lock:
            self.rooms.available_rooms.release()
            print(f"Customer {self.customer_number} has left a fitting room")

    def enqueue(self):

        start_wait = time.time()

        room_ready = False

        while not room_ready:
            with self.lock:
                if self.rooms.available_rooms.acquire(blocking=False):
                    room_ready = True
                    self.occupy_room()
                else:
                    time.sleep(1)

        self.wait_time = time.time() - start_wait

        


