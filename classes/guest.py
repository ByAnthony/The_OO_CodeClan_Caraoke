class Guest:

    def __init__(self, name, wallet, favorite_song):
        self.name = name
        self.wallet = wallet
        self.favorite_song = favorite_song
        self.tab = []

    def sufficient_funds(self, item):
        return self.wallet >= item.price

    def buy_drink(self, drink):
        if self.sufficient_funds(drink):
            self.wallet -= drink.price

    def add_drinks(self, drinks):
        self.tab.append(drinks)
        return self.tab
    
    def guest_tab(self, room):
        tab = [room.fee] + self.tab
        return sum(tab)