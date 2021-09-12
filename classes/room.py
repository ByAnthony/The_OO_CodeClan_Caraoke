class Room:
    
    def __init__(self, name, playlist, guest_number, fee):
        self.name = name
        self.playlist = playlist
        self.guest_list = []
        self.guest_number = guest_number
        self.fee = fee
        self.till = 0

    def guest_count(self):
        return len(self.guest_list)

    def check_in_guests(self, guest):
        if len(self.guest_list) <= self.guest_number and guest.wallet >= self.fee:
            self.guest_list.append(guest)
            self.till += self.fee
            guest.wallet -= self.fee
            

    def check_out_guests(self, guest):
        self.guest_list.remove(guest)
        
    def add_song(self, song):
        self.playlist.append(song)
        return self.playlist

    def find_favorite_song(self, song_to_find):
        for song in self.playlist:
            if song == song_to_find:
                return "Whoo!"
        return "Sorry, song not found"