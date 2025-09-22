import pytest
from src.playlist import Playlist
from src.song import Song

def test_remove_song_not_in_playlist():
    p = Playlist('t')
    s = Song('Hello', 'Adele')
    p.add_song(s)

    # Try to remove a song that isn't there
    with pytest.raises(ValueError):
        p.remove_song('Not There')
