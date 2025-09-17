"""
src/gui.py
Simple Tkinter GUI that demonstrates the MVP requirements:
- a mock local library (list of Song objects)
- ability to add songs to a playlist
- reorder songs (up/down)
- export playlist to M3U

This file intentionally keeps the UI basic so the MVP is easy to test.
"""

import tkinter as tk
from tkinter import messagebox, filedialog
from song import Song, demo_songs, afrobeats_songs
from playlist import Playlist
import os


class PlaylistGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Playlist Manager (Group 14)")
        self.root.geometry("720x360")

        self.playlist = Playlist("My Playlist")

        # Present mock songs + demo + Afrobeats
        self.library = [
            Song("Shape of You", "Ed Sheeran", 233),
            Song("Blinding Lights", "The Weeknd", 200),
            Song("Levitating", "Dua Lipa", 203),
            Song("Smells Like Teen Spirit", "Nirvana", 301),
        ] + demo_songs + afrobeats_songs   # merged all

        # Build UI frames
        self.left_frame = tk.Frame(root, padx=10, pady=10)
        self.right_frame = tk.Frame(root, padx=10, pady=10)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Library (left)
        tk.Label(self.left_frame, text="Library",
                 font=(None, 12, 'bold')).pack(anchor='w')
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(self.left_frame, textvariable=self.search_var)
        search_entry.pack(fill=tk.X)
        search_entry.bind("<Return>", lambda e: self.update_library_list())

        self.library_listbox = tk.Listbox(self.left_frame, height=15)
        self.library_listbox.pack(fill=tk.BOTH, expand=True)

        # Playlist (right)
        tk.Label(self.right_frame, text="Playlist",
                 font=(None, 12, 'bold')).pack(anchor='w')
        self.playlist_listbox = tk.Listbox(self.right_frame, height=15)
        self.playlist_listbox.pack(fill=tk.BOTH, expand=True)

        # Buttons
        btn_frame = tk.Frame(root, pady=6)
        btn_frame.pack(side=tk.BOTTOM)

        tk.Button(btn_frame, text="Add to Playlist",
                  command=self.add_selected).pack(side=tk.LEFT, padx=4)
        tk.Button(btn_frame, text="Remove Selected",
                  command=self.remove_selected).pack(side=tk.LEFT, padx=4)
        tk.Button(btn_frame, text="Move Up",
                  command=lambda: self.move_selected(-1)).pack(side=tk.LEFT, padx=4)
        tk.Button(btn_frame, text="Move Down",
                  command=lambda: self.move_selected(1)).pack(side=tk.LEFT, padx=4)
        tk.Button(btn_frame, text="Export M3U",
                  command=self.export_playlist).pack(side=tk.LEFT, padx=4)

        self.update_library_list()

    def update_library_list(self):
        # update the library listbox by running a regex search against mock library.
        q = self.search_var.get().strip()
        if not q:
            items = self.library
        else:
            import re
            try:
                pattern = re.compile(q, re.IGNORECASE)
                items = [s for s in self.library if pattern.search(
                    s.title) or pattern.search(s.artist)]
            except re.error:
                items = [s for s in self.library if q.lower(
                ) in s.title.lower() or q.lower() in s.artist.lower()]

        self.library_listbox.delete(0, tk.END)
        for s in items:
            self.library_listbox.insert(tk.END, str(s))
        self._displayed_library = items  # mapping for selection

    def add_selected(self):
        sel = self.library_listbox.curselection()
        if not sel:
            return
        song = self._displayed_library[sel[0]]
        self.playlist.add_song(song)
        self.refresh_playlist_view()

    def remove_selected(self):
        sel = self.playlist_listbox.curselection()
        if not sel:
            return
        idx = sel[0]
        title = self.playlist.songs[idx].title
        self.playlist.remove_song(title)
        self.refresh_playlist_view()

    def move_selected(self, direction: int):
        sel = self.playlist_listbox.curselection()
        if not sel:
            return
        idx = sel[0]
        new_idx = idx + direction
        if 0 <= new_idx < len(self.playlist.songs):
            self.playlist.reorder_song(idx, new_idx)
            self.refresh_playlist_view()
            self.playlist_listbox.selection_set(new_idx)

    def refresh_playlist_view(self):
        self.playlist_listbox.delete(0, tk.END)
        for s in self.playlist.songs:
            self.playlist_listbox.insert(tk.END, str(s))

    def export_playlist(self):
        path = filedialog.asksaveasfilename(defaultextension='.m3u',
                                            filetypes=[('M3U files', '*.m3u')],
                                            initialfile=f"{self.playlist.name}.m3u")
        if not path:
            return
        try:
            self.playlist.export_m3u(path)
            messagebox.showinfo(
                'Export', f'Playlist exported to: {os.path.abspath(path)}')
        except Exception as e:
            messagebox.showerror('Error', f'Could not export playlist: {e}')


if __name__ == '__main__':
    root = tk.Tk()
    app = PlaylistGUI(root)
    root.mainloop()
