import sys
import os
import unittest  # noqa: E402

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))

from src.playlist import Playlist  # noqa: E402
from src.song import Song  # noqa: E402


class TestPlaylist(unittest.TestCase):

    def test_add_song(self):
        playlist = Playlist("Test")
        song = Song("Song1", "Artist1", 200)
        playlist.add_song(song)
        self.assertEqual(len(playlist.songs), 1)

    def test_remove_song(self):
        playlist = Playlist("Test")
        song = Song("Song1", "Artist1", 200)
        playlist.add_song(song)
        playlist.remove_song("Song1")
        self.assertEqual(len(playlist.songs), 0)


def test_add_and_remove_song():
    p = Playlist("Test")
    s = Song("A", "B")
    p.add_song(s)
    assert len(p.songs) == 1
    assert p.songs[0] == s
    p.remove_song("A")
    assert len(p.songs) == 0


def test_reorder_song():
    p = Playlist("Test")
    s1 = Song("s1", "a1")
    s2 = Song("s2", "a2")
    s3 = Song("s3", "a3")
    p.add_song(s1)
    p.add_song(s2)
    p.add_song(s3)
    p.reorder_song(0, 2)
    assert p.songs[2] == s1


if __name__ == "__main__":
    unittest.main()
