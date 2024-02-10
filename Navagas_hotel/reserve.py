from datetime import datetime



class Reservation:
    def __init__(self, username, room_num):
        self.room_num = room_num
        self.username = username
        self.timestamp = datetime.now()


    def __repr__(self):
        return f'Booked by {self.username}, (Timestamp = {self.timestamp})'
