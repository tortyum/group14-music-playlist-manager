"""src/song.py
Song data class for the Music Playlist Manager.
Contains simple equality and string representation logic.
"""

from dataclasses import dataclass

@dataclass
class Song:
    title: str
    artist: str
    album: str = ""
    duration: str = ""

    def __str__(self) -> str:
        """Human-friendly representation used by the GUI and logs."""
        return f"{self.title} - {self.artist}"

    def to_dict(self) -> dict:
        """Convert to a serializable dict (useful if you later add JSON save)."""
        return {
            "title": self.title,
            "artist": self.artist,
            "album": self.album,
            "duration": self.duration,
        }