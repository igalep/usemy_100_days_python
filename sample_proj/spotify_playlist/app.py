from sample_proj.spotify_playlist.spotify.spotify_client import Spotify
from sample_proj.spotify_playlist.billboard.billboard_hot_100 import BillboardHot100


def main():
    billboard = BillboardHot100()
    spotify = Spotify()

    required_date = input('Enter the date in YYYY-MM-DD format: or leave blank for today: ')

    title_artist_dic = billboard.get_billboard_hot_100(required_date)

    play_list_id = spotify.create_playlist(date=required_date, playlist_name='Python playlist')

    spotify.add_songs_to_playlist(playlist_id=play_list_id, songs_play_list=title_artist_dic)



if __name__=='__main__':
    main()