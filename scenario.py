import fitting_rooms
import customer
import time
import random
from datetime import datetime



class Scenario:

    def __init__(self):

        #inputs
        self.room_count = int(input("Enter the number of rooms avialable (default 3): "))
        self.customer_count = int(input("Enter the number of customers: "))
        self.clothing_items = int(input("Enter the number of clothing itmes (0 for random): "))
        self.enforce_item_max = input("Enforce item maximum? (Y/N): ")

        #collected metrics
        self.scenario_start = time.time()
        self.scenario_end = None
        self.total_wait = 0
        self.customers_serviced = 0
        self.total_room_minutes = 0
        self.avg_room_usage = 0

        #simulation header
        print()
        print("-"*20, " Simulation Log ", "-"*20)
        

    def start_scenario(self):

        rooms = fitting_rooms.DressingRoom(self.room_count)
        customers = []
        
        for i in range(self.customer_count):

            #customer arrives
            time_between_customers = random.randint(1,5)
            cust = customer.Customer(self.clothing_items, self.enforce_item_max, i+1, rooms)
            cust.start()

            customers.append(cust)

            #next customer
            time.sleep(time_between_customers)
            # self.customer_count -= 1

        #waits for threads to finish
        for c in customers:
            c.join()

        #sums metrics for each customer
        for c in customers:
            self.total_wait += c.wait_time
            self.total_room_minutes += c.time_in_room
            self.customers_serviced += c.serviced
        
        #executes after everyone leaves
        self.scenario_end = time.time()
        scenario_time = self.scenario_end - self.scenario_start
        print("The simulation is complete")
        print()
        print("-"*20, " Simulation Metrics ", "-"*20)
        print("Scenario start time: ", datetime.fromtimestamp(self.scenario_start))
        print("Scenario end time: ", datetime.fromtimestamp(self.scenario_end))
        print("Scenario elapsed time: ", round(scenario_time), "minutes")
        print("Customers serviced: ", self.customers_serviced)
        print("Avg room usage: ", round(self.total_room_minutes/self.room_count),"minutes")
        print("Total customer wait time: ", round(self.total_wait),"minutes")