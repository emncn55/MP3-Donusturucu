from pathlib import Path
import threading
import tkinter as tk
from tkinter import messagebox, ttk

from yt_dlp import YoutubeDL


class MP3DownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube MP3 Dönüştürücü")
        self.root.geometry("620x300")
        self.root.resizable(False, False)

        self.download_folder = Path.home() / "Downloads"
        self.download_folder.mkdir(parents=True, exist_ok=True)

        self.url_var = tk.StringVar()
        self.status_var = tk.StringVar(value="Video bağlantısını gir.")

        self.create_interface()

    def create_interface(self):
        main_frame = ttk.Frame(self.root, padding=25)
        main_frame.pack(fill="both", expand=True)

        title = ttk.Label(
            main_frame,
            text="YouTube MP3 Dönüştürücü",
            font=("Segoe UI", 18, "bold"),
        )
        title.pack(pady=(0, 20))

        ttk.Label(
            main_frame,
            text="Video bağlantısı:",
            font=("Segoe UI", 10),
        ).pack(anchor="w")

        self.url_entry = ttk.Entry(
            main_frame,
            textvariable=self.url_var,
            font=("Segoe UI", 11),
        )
        self.url_entry.pack(fill="x", pady=(6, 15))
        self.url_entry.focus()

        self.download_button = ttk.Button(
            main_frame,
            text="MP3 Olarak İndir",
            command=self.start_download,
        )
        self.download_button.pack(fill="x", ipady=7)

        self.progress_bar = ttk.Progressbar(
            main_frame,
            mode="indeterminate",
        )
        self.progress_bar.pack(fill="x", pady=(18, 8))

        ttk.Label(
            main_frame,
            textvariable=self.status_var,
            font=("Segoe UI", 9),
        ).pack(anchor="w")

        ttk.Label(
            main_frame,
            text=f"Kayıt konumu: {self.download_folder}",
            font=("Segoe UI", 8),
            foreground="gray",
        ).pack(anchor="w", pady=(8, 0))

        self.root.bind("<Return>", lambda event: self.start_download())

    def start_download(self):
        url = self.url_var.get().strip()

        if not url:
            messagebox.showwarning(
                "Bağlantı eksik",
                "Lütfen bir video bağlantısı gir.",
            )
            return

        if not url.startswith(("http://", "https://")):
            messagebox.showwarning(
                "Geçersiz bağlantı",
                "Lütfen geçerli bir video bağlantısı gir.",
            )
            return

        self.download_button.config(state="disabled")
        self.url_entry.config(state="disabled")
        self.progress_bar.start(10)
        self.status_var.set("Video bilgileri alınıyor...")

        download_thread = threading.Thread(
            target=self.download_mp3,
            args=(url,),
            daemon=True,
        )
        download_thread.start()

    def update_status(self, text):
        self.root.after(
            0,
            lambda: self.status_var.set(text),
        )

    def progress_hook(self, data):
        status = data.get("status")

        if status == "downloading":
            percentage = data.get("_percent_str", "").strip()
            speed = data.get("_speed_str", "").strip()

            status_text = f"İndiriliyor: {percentage}"

            if speed:
                status_text += f" | Hız: {speed}"

            self.update_status(status_text)

        elif status == "finished":
            self.update_status("MP3 formatına dönüştürülüyor...")

    def download_mp3(self, url):
        download_options = {
            "format": "bestaudio/best",
            "outtmpl": str(
                self.download_folder
                / "%(title).150B [%(id)s].%(ext)s"
            ),
            "noplaylist": True,
            "windowsfilenames": True,
            "progress_hooks": [self.progress_hook],
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }

        try:
            with YoutubeDL(download_options) as downloader:
                downloader.download([url])

            self.root.after(0, self.download_completed)

        except Exception as error:
            error_message = str(error)

            self.root.after(
                0,
                lambda message=error_message: self.download_failed(message),
            )

    def download_completed(self):
        self.progress_bar.stop()
        self.download_button.config(state="normal")
        self.url_entry.config(state="normal")
        self.status_var.set("MP3 başarıyla indirildi.")

        messagebox.showinfo(
            "İndirme tamamlandı",
            "MP3 dosyası Downloads klasörüne kaydedildi.",
        )

        self.url_var.set("")
        self.url_entry.focus()

    def download_failed(self, error_message):
        self.progress_bar.stop()
        self.download_button.config(state="normal")
        self.url_entry.config(state="normal")
        self.status_var.set("İndirme başarısız oldu.")

        messagebox.showerror(
            "İndirme hatası",
            error_message,
        )


if __name__ == "__main__":
    window = tk.Tk()
    application = MP3DownloaderApp(window)
    window.mainloop()