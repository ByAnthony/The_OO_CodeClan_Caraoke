class Guest:
    
    def __init__(self, name, money, favorite_song):
        self.name = name
        self.money = money
        self.favorite_song = favorite_song

    def sufficient_money(self, venue):
        return self.money >= venue.fee

    def entry_fee(self, entry):
        if self.sufficient_money(entry):
            self.money -= entry.fee