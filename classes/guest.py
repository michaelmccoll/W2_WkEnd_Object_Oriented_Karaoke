class Guest:
    def __init__(self,guest_name,fav_song,wallet):
        self.guest_name = guest_name
        self.fav_song = fav_song
        self.wallet = wallet
    
    def reduce_wallet(self,amount):
        self.wallet -= amount

    def fav_song_on_list(self,song_list):
        return [print("Whoohoo") for song in song_list if song == self.fav_song] 
