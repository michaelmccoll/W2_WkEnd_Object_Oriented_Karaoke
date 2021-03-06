class Guest:
    def __init__(self,guest_name,fav_song,wallet):
        self.guest_name = guest_name
        self.fav_song = fav_song
        self.wallet = wallet
    
    def reduce_wallet(self,amount):
        self.wallet -= amount