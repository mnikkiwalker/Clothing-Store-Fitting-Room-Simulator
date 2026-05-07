import threading
import time



class DressingRoom:
    def __init__(self, room_count=3):
        self.available_rooms = threading.Semaphore(room_count)

    def request_room(self):
        #check if rooms available
        if self.available_rooms.acquire(blocking=False):
            return "permitted"
        
        else:
            return "denied"

    def release_room(self):
        #iterate room up 1
        return
