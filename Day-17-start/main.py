class User:

    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

    def introduce_self(self):
        print(f"Hi, I'm {self.first_name} {self.last_name}")

user_1 = User("Chukwuemeka", "Ngumoha")
user_1.introduce_self()