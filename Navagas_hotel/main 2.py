from hotel import Hotel
from login import Login


# menu of the hotel
def choose_command_menu():
    while True:
        print()
        print('----------------------------------------')
        print('1. Show every rooms in the hotel.')
        print('2. Reservation the room.')
        print('3. Display information of reservation')
        print('4. Cancel the reservation room.')
        print('5. Display all the reserved room')
        print('6. Display all the available room')
        print('7. Promotion for you (only when you reserved room)')
        print('0. Exit')
        try:
            menu_command = int(input('Select your choice: '))
            return menu_command
        except ValueError:
            print("You should select number 1 to 7")


# check which choice user selected
def run_menu(hotel, command):
    if command == 0:
        print("Thank you")
    elif command not in range(1, 8):
        print("This menu doesn't exist")
    elif command == 1:
        hotel.show_room_list()
    elif command == 2:
        hotel.show_available_room()
        print('----------------------------------------')
        room_num = str(input('Select room number: '))
        user_name = str(input('What is your username: '))
        hotel.reservation_room(room_num, user_name)
        hotel.room_price(room_num)
    elif command == 3:
        hotel.show_reservation_now()
    elif command == 4:
        room_num = str(input('Select room number: '))
        user_name = str(input('What is your username: '))
        hotel.cancel_reservation(room_num, user_name)
    elif command == 5:
        hotel.show_reservation_room()
    elif command == 6:
        hotel.show_available_room()
    elif command == 7:
        login = Login()
        login.login_interface()


hotel = Hotel('Yay', 'Navagas Hotel', 5)
print(hotel)
print(f'Welcome to {hotel.hotel_name}.')
hotel.create_rooms()
command = ''
while command != 0:
    command = choose_command_menu()
    run_menu(hotel, command)
