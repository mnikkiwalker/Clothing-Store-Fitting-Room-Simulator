import fitting_rooms
import customer
import time




class Scenario:

    def __init__(self):
        room_count = input("Enter the number of rooms avialable (default 3): ")
        customer_count = input("Enter the number of customers: ")
        clothing_items = input("Enter the number of clothing itmes (0 for random): ")
        enforce_item_max = input("Enforce item maximum? (Y/N): ")

        fitting_rooms.DressingRoom(room_count)
        
        while customer_count > 0:
            customer.Customer(clothing_items, enforce_item_max)
            time.sleep(5)
            customer_count -= 1