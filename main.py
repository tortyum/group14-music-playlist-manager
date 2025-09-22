# main.py
"""
Entry point for the Music Playlist Manager.
Runs the GUI application.
"""

from src.gui import PlaylistGUI
import tkinter as tk


def main():
    root = tk.Tk()
    app = PlaylistGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
