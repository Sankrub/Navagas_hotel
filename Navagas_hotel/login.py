import json
from turtle import Turtle, Screen, TurtleScreen


class Login:
    def __init__(self):
        self.screen = Screen()
        TurtleScreen._RUNNING = True
        self.show = Turtle()
        self.one = Turtle()
        self.two = Turtle()


    def read_information(self):  # read data from accounts
        with open('accounts.json', 'r') as data_file:
            data_dct = json.load(data_file)
        return data_dct

    def login_interface(self):  # first screen
        self.screen.setup(width=500, height=750)
        self.screen.clear()
        self.screen.title("Last Vegas Hotel")
        self.show.setheading(0)
        self.screen.tracer(0)
        self.screen.bgcolor('Pink')
        self.show.pencolor('white')
        self.show.goto(0, -90)
        self.show.pensize(5)
        self.show.circle(50)  # build circle
        self.show.penup()
        self.show.goto(230, 300)
        self.show.write('NAVAGAS HOTEL', move=False, align='right',
                        font=("Display", 40, "bold"))  # Title top of the page
        self.show.goto(0, 70)
        self.show.write('LOGIN TO SEE PROMOTION', move=False, align='center',
                        font=("Display", 25, "bold"))  # click login
        self.show.goto(0, -50)
        self.show.pencolor('Black')
        self.show.write('CLICK ANYWHERE TO LOGIN', move=False, align='center', font=("Display", 13, "bold"))
        self.screen.onclick(self.screen_A)
        self.screen.mainloop()

    def screen_A(self, x, y):  # second screen if already reserved room
        data_dct = self.read_information()
        username = self.screen.textinput('Your Username', 'Pleas type')
        room_num = self.screen.textinput('Your room number', 'Pleas type')
        room_num = room_num.upper()
        if room_num in data_dct:
            if data_dct[room_num]['Guest name'] == username and data_dct[room_num]['Status'] == 'Reserved':
                self.screen_for_st()
            else:
                print('Your username might be wrong or you did not reserved this room.')
        else:
            print(f"This room number: {room_num} doesn't exist in this hotel")

    def screen_for_st(self):  # import picture promotion
        self.screen.clear()
        self.screen.addshape('new_pro.gif')
        self.one.shape('new_pro.gif')
