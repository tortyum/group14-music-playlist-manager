# tests/test_playlist.py
import os
import tempfile
from src.song import Song
from src.playlist import Playlist

def test_add_and_remove_song():
    p = Playlist('t')
    s = Song('A', 'B')
    p.add_song(s)
    assert len(p.songs) == 1
    assert p.songs[0] == s
    p.remove_song('A')
    assert len(p.songs) == 0

def test_reorder_song():
    p = Playlist('t')
    s1 = Song('s1', 'a1')
    s2 = Song('s2', 'a2')
    s3 = Song('s3', 'a3')
    p.add_song(s1)
    p.add_song(s2)
    p.add_song(s3)
    p.reorder_song(0, 2)
    assert p.songs[2] == s1
    # move last to first
    p.reorder_song(2, 0)
    assert p.songs[0] == s1

def test_export_m3u(tmp_path):
    p = Playlist('t')
    s1 = Song('s1', 'a1')
    s2 = Song('s2', 'a2')
    p.add_song(s1)
    p.add_song(s2)
    out = tmp_path / 'out.m3u'
    p.export_m3u(str(out))
    assert out.exists()
    content = out.read_text(encoding='utf-8')
    assert '#EXTM3U' in content
    assert 'a1 - s1' in content