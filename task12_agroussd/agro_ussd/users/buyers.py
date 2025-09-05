from users.user import User


class Buyer(User):
    def __init__(self, name, age, state, lga):
        super().__init__(name, age, state, lga)