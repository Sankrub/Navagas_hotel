class Room:
    def __init__(self, room_type, guest_name=None):
        self.room_type = room_type
        self.guest_name = guest_name
        self.status = 'Available'

    def room_price(self, room_num):
        if room_num['Room type'] == 'Standard':
            return 5000
        elif room_num['Room type'] == "Luxury":
            return 8000

    def __repr__(self):
        return f'(Room Type: {self.room_type}, Username: {self.guest_name},Status: {self.status})'
