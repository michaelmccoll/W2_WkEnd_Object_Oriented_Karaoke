class Room:
    def __init__(self,room_name,capacity,fee):
        self.room_name = room_name
        self.capacity = capacity
        self.fee = fee
        self.guest_list = []
        self.song_list = []
        self.till = 0

    def check_in(self,guest_name):
        self.guest_list.append(guest_name)

    def count_guests_in_room(self):
        return len(self.guest_list)

    def check_out(self, guest):
        self.guest_list.remove(guest)

    def add_song_to_room(self,song_name):
        self.song_list.append(song_name)

    def fee_transaction(self,fee):
        self.till += self.fee

    def check_in_advanced(self,guest):
        if len(self.guest_list) > self.capacity:
            return print("Room now full, try another")
        if guest.wallet < self.fee:
            return print("You do not have enough money to pay fee")
        guest.reduce_wallet(self.fee)
        self.fee_transaction(self.fee)
        self.guest_list.append(guest.guest_name)
        self.capacity -= 1