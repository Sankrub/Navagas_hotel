from room import Room
from reserve import Reservation
import json


class Hotel:
    def __init__(self, owner, hotel_name, hotel_star=0):
        self.__hotel_name = hotel_name
        self.__hotel_star = hotel_star
        self.__owner = owner
        self.reserved_room = {}
        self.rooms = {}

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, other):
        if not isinstance(other, str):
            raise TypeError('Owner must be a string')
        self.__owner = other

    @property
    def hotel_name(self):
        return self.__hotel_name

    @hotel_name.setter
    def hotel_name(self, other):
        if not isinstance(other, str):
            raise TypeError('Hotel name must be a string')
        self.__hotel_name = other

    @property
    def hotel_star(self):
        return self.__hotel_star

    @hotel_star.setter
    def hotel_star(self, other):
        if not isinstance(other, int):
            raise TypeError('Hotel star must be an integer')
        self.__hotel_star = other

    def create_rooms(self):
        try:
            with open('accounts.json', 'r') as data_file:
                data_dct = json.load(data_file)
                for room_num in data_dct:
                    current_room = data_dct[room_num]
                    new_room = Room(current_room["Room Type"], current_room["Guest name"])
                    new_room.status = current_room["Status"]
                    self.rooms[room_num] = new_room
        except:
            self.create_rooms_empty()

    def create_rooms_empty(self):
        for i in range(15):
            if i <= 9:
                room_num = f"A{i + 1}"
                new_room = Room('Standard', "None")
                self.rooms[room_num] = new_room
            else:
                room_num = f"B{i + 1}"
                new_room = Room('Luxury', "None")
                self.rooms[room_num] = new_room

    # 1 (show all the room in this hotel)
    def show_room_list(self):
        print("This is our hotel rooms")
        print('Standard cost 5000 baht per day.')
        print('Luxury cost 8000 baht per day.')
        x = 0
        for room in self.rooms:
            if x < 9:
                print(f'{room}  -{self.rooms[room]}')
                x += 1
            else:
                print(f'{room} -{self.rooms[room]}')

    # 2 (show available room)
    def show_available_room(self):
        x = 0
        for room in self.rooms:
            if self.rooms[room].status == 'Available':
                if x == 5:
                    print()
                    x = 0
                print(f' - {room:>4}, Room Type: {self.rooms[room].room_type}, Status: {self.rooms[room].status}')
                x += 1

    # 2 (user will use this method to book the room)
    def reservation_room(self, room_num, user_name):
        room_num = room_num.upper()
        if room_num in self.rooms:
            if self.rooms[room_num].status == 'Available':
                self.rooms[room_num].guest_name = user_name
                self.rooms[room_num].status = "Reserved"
                # -----
                reservation = Reservation(user_name, room_num)
                time = f"{reservation.timestamp}"
                print(f'You reserved room at {time}')
                self.reserved_room[room_num] = self.rooms[room_num]  # find price
            else:
                print(f"This room {room_num} is not available.")
        else:
            print(f"This room number: {room_num} doesn't exist in this hotel.")
        self.save_data()

    # 2 (show price that user have to pay for the room base on class Room (standard and luxury room))
    def room_price(self, room_num):
        room_num = room_num.upper()
        if room_num in self.reserved_room:
            if self.reserved_room[room_num].room_type == 'Standard':
                print(f'{room_num}(Standard room)  cost 5000 baht.')
            elif self.reserved_room[room_num].room_type == "Luxury":
                print(f'{room_num}(Luxury room) cost 8000 baht.')

    # 3 (show information of booked room)
    def show_reservation_now(self):
        x = 0
        for room in self.rooms:
            if self.rooms[room].status == 'Reserved':
                if x == 5:
                    print()
                    x = 0
                print(f' - {room:>4}. Booked by {self.rooms[room].guest_name}')
                x += 1

    # 4 (user use this method to cancel their room)
    def cancel_reservation(self, room_num, user_name):
        room_num = room_num.upper()
        if room_num in self.rooms:
            if user_name == self.rooms[room_num].guest_name:
                self.rooms[room_num].guest_name = 'None'
                self.rooms[room_num].status = 'Available'
                print(f'Room number {room_num} have been canceled.')
            else:
                print(f'{user_name} did not reserved this room')
        else:
            print(f"This room number: {room_num} doesn't exist in this hotel.")
        self.save_data()

    # 5 (show reserved room in list form)
    def show_reservation_room(self):
        x = 0
        for room in self.rooms:
            if self.rooms[room].status == 'Reserved':
                if x == 5:
                    print()
                    x = 0
                print(f' - {room:>4} : Room Type: {self.rooms[room].room_type}, Status: {self.rooms[room].status}')
                x += 1

    def save_data(self):
        new_data = {}
        for room_num in self.rooms:
            new_room = self.rooms[room_num]
            new_data[room_num] = {
                "Room Type": new_room.room_type,
                "Guest name": new_room.guest_name,
                "Status": new_room.status
            }
        with open('accounts.json', 'w') as data_file:
            json.dump(new_data, data_file, indent=4)

    def __repr__(self):
        return f'Owner: {self.__owner}, Hotel: {self.__hotel_name}, Star: {self.__hotel_star}'
