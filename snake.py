import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class MusicPlayerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Music Player")
        self.geometry("1200x800")
        self.configure(bg="#121212")

        self.create_sidebar()
        self.create_main_content()
        self.create_player_bar()

    def create_sidebar(self):
        sidebar = tk.Frame(self, width=300, bg="#121212")
        sidebar.pack(side=tk.LEFT, fill=tk.Y)

        # Home and Search buttons
        tk.Button(sidebar, text="Ana sayfa", bg="#121212", fg="white", bd=0).pack(pady=10, padx=10, anchor="w")
        tk.Button(sidebar, text="Ara", bg="#121212", fg="white", bd=0).pack(pady=10, padx=10, anchor="w")

        # Playlist section
        playlist_frame = tk.Frame(sidebar, bg="#121212")
        playlist_frame.pack(fill=tk.BOTH, expand=True, pady=20)

        tk.Label(playlist_frame, text="Çalma Listeleri", bg="#121212", fg="white", font=("Arial", 12, "bold")).pack(
            anchor="w", padx=10)

        playlists = ["Beğenilen Şarkılar", "Koyu", "T-favs", "62. Çalma Listem", "fuga a etnico", "affiro"]
        for playlist in playlists:
            tk.Button(playlist_frame, text=playlist, bg="#121212", fg="white", bd=0, anchor="w").pack(pady=5, padx=10,
                                                                                                      fill=tk.X)

    def create_main_content(self):
        main_content = tk.Frame(self, bg="#121212")
        main_content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Navigation buttons
        nav_frame = tk.Frame(main_content, bg="#121212")
        nav_frame.pack(fill=tk.X, pady=10)
        tk.Button(nav_frame, text="<", bg="#121212", fg="white", bd=0).pack(side=tk.LEFT, padx=5)
        tk.Button(nav_frame, text=">", bg="#121212", fg="white", bd=0).pack(side=tk.LEFT, padx=5)

        # Daily Mixes section
        tk.Label(main_content, text="atezism İçin Derlendi", bg="#121212", fg="white", font=("Arial", 24, "bold")).pack(
            anchor="w", padx=20, pady=20)

        mixes_frame = tk.Frame(main_content, bg="#121212")
        mixes_frame.pack(fill=tk.BOTH, expand=True, padx=20)

        daily_mixes = ["Daily Mix 1", "Daily Mix 2", "Daily Mix 3", "Daily Mix 4", "Daily Mix 5", "Daily Mix 6"]
        for i, mix in enumerate(daily_mixes):
            mix_frame = tk.Frame(mixes_frame, bg="#282828", width=150, height=200)
            mix_frame.grid(row=i // 3, column=i % 3, padx=10, pady=10)
            mix_frame.pack_propagate(False)

            # Placeholder for album art
            canvas = tk.Canvas(mix_frame, width=130, height=130, bg="#181818", highlightthickness=0)
            canvas.pack(pady=(10, 5))

            tk.Label(mix_frame, text=mix, bg="#282828", fg="white").pack()

    def create_player_bar(self):
        player_bar = tk.Frame(self, height=100, bg="#181818")
        player_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Placeholder for currently playing song
        tk.Label(player_bar, text="Loading - Central Cee", bg="#181818", fg="white").pack(side=tk.LEFT, padx=20)

        # Placeholder for player controls
        controls_frame = tk.Frame(player_bar, bg="#181818")
        controls_frame.pack(expand=True)

        tk.Button(controls_frame, text="Play", bg="#181818", fg="white", bd=0).pack(side=tk.LEFT, padx=5)

        # Placeholder for progress bar
        ttk.Progressbar(controls_frame, length=400).pack(side=tk.LEFT, padx=20)


if __name__ == "__main__":
    app = MusicPlayerApp()
    app.mainloop()