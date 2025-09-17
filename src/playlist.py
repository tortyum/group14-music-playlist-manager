"""src/playlist.py
Playlist class: core logic for adding/removing/reordering/searching songs,
and exporting playlists in M3U format.

Keep all core logic here so it can be tested with pytest (separation of concerns).
"""

import re
from typing import List
from src.song import Song

class Playlist:
    def __init__(self, name: str):
        self.name = name
        self.songs: List[Song] = []

    def add_song(self, song: Song) -> None:
        """Add a Song object to the end of the playlist."""
        self.songs.append(song)

    def remove_song(self, title: str) -> None:
        """Remove all songs matching the given title (case-sensitive match to title field)."""
        self.songs = [s for s in self.songs if s.title != title]

    def reorder_song(self, old_index: int, new_index: int) -> None:
        """Move a song from old_index to new_index.
        Raises IndexError for invalid indices.
        """
        if old_index < 0 or old_index >= len(self.songs):
            raise IndexError(f"old_index out of range: {old_index}")
        if new_index < 0 or new_index >= len(self.songs):
            raise IndexError(f"new_index out of range: {new_index}")
        song = self.songs.pop(old_index)
        self.songs.insert(new_index, song)

    def search(self, query: str) -> List[Song]:
        """Search song title and artist using a regex (case-insensitive).
        If the query is not a valid regex, treat it as a literal string.
        """
        try:
            pattern = re.compile(query, re.IGNORECASE)
        except re.error:
            # escape and compile literal if regex invalid
            pattern = re.compile(re.escape(query), re.IGNORECASE)
        return [s for s in self.songs if pattern.search(s.title) or pattern.search(s.artist)]

    def export_m3u(self, filename: str) -> None:
        """Export the current playlist to an M3U file.
        The M3U will contain basic EXTINF lines and mock paths (title.mp3).
        If you later integrate real file paths, replace the mock path with the actual path.
        """
        with open(filename, "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            for song in self.songs:
                # EXTINF: <duration_in_seconds>,Artist - Title
                # using -1 (unknown) as duration for mock data
                f.write(f"#EXTINF:-1,{song.artist} - {song.title}\n")
                # mock file path: replace with real path if available
                f.write(f"{song.title}.mp3\n")