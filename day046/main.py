from top_100 import Top100Songs
from spotify import MySpotipy
from datetime import datetime

def safe_date_input():
    date = input("Please enter a date in the format YYYY-MM-DD: ")
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return date
    except ValueError:
        print("This is the incorrect date string format. It should be YYYY-MM-DD")
        return safe_date_input()

date = safe_date_input()
song_db = Top100Songs()



my_spotipy = MySpotipy()
song_ids = []
for song in song_db.get_top_100(date):
    song_data = my_spotipy.find_song(song)
    if(song_data == None):
        continue
    song_ids.append(song_data["id"])


playlist_id = my_spotipy.create_playlist(f"{date} Billboard 100")
my_spotipy.add_song_to_playlist(playlist_id,song_ids)
print("All Songs add to playlist")
