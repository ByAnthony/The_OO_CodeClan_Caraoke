class Room:
    
    def __init__(self, name, guest_number):
        self.name = name
        self.guest_number = guest_number
        self.guests = []
        self.playlist = []

    def guest_count(self):
        for guest in self.guests:
            return len(guest)

    def check_in(self, guest_to_check_in):
        if len(guest_to_check_in) <= self.guest_number:
            self.guests.append(guest_to_check_in)
        else:
            return "This room is too small for your group. Please book a room with a greater capacity"

    def check_out(self, guest_to_check_out):
        self.guests.remove(guest_to_check_out)

    def song_count(self):
        for song in self.playlist:
            return len(song)

    def add_songs(self, song_to_add):
        self.playlist.append(song_to_add)

    def find_favorite_song(self, song_to_find):
        for song in self.playlist:
            if song == song_to_find:
                return song