class Room:
    def __init__(self,room_name):
        self.room_name = room_name
        self.guest_list = []
        self.song_list = []

    def check_in(self,guest_name):
        self.guest_list.append(guest_name)

    def count_guests_in_room(self):
        return len(self.guest_list)

    def check_out(self, guest):
        self.guest_list.remove(guest)

    # def check_out(self):
    #     remove guest from guest_list[]

    # def add_songs_to_room(self):
    #     add songs to song_list[]