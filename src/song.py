"""
src/song.py
Song data class for the Music Playlist Manager.
Contains equality, string representation, and demo songs.
"""

from dataclasses import dataclass


@dataclass
class Song:
    title: str
    artist: str
    duration: int = 0   # duration in seconds
    album: str = ""     # optional album field

    def __str__(self) -> str:
        # representation used by the GUI and logs.
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{self.title} - {self.artist} ({minutes}:{seconds:02d})"

    def to_dict(self) -> dict:
        # Convert to a serializable dict
        return {
            "title": self.title,
            "artist": self.artist,
            "album": self.album,
            "duration": self.duration,
        }


# afrobeats Songs
afrobeats_songs = [
    Song("Calm Down", "Rema", 238),
    Song("Last Last", "Burna Boy", 213),
    Song("Peru", "Fireboy DML", 210),
    Song("Essence", "Wizkid ft. Tems", 260),
    Song("Ku Lo Sa", "Oxlade", 178),
    Song("Terminator", "Asake", 201),
    Song("Sungba Remix", "Asake ft. Burna Boy", 220),
    Song("Jaho", "Kizz Daniel", 195),
    Song("On The Low", "Burna Boy", 233),
    Song("True Love", "Wizkid", 250),
]
