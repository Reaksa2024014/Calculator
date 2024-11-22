

# from yt_dlp import YoutubeDL

# def download_video(url, download_type):
#     if "youtube" not in url:
#         print("Please enter a valid YouTube URL.")
#         return

#     location = input("Enter the directory to save the file: ")

#     # Set download options based on the type
#     if download_type == "mp3":
#         ydl_opts = {
#             'format': 'bestaudio',  # Downloads audio without conversion to mp3
#             'outtmpl': f'{location}/%(title)s.%(ext)s',
#         }
#     elif download_type == "mp4":
#         ydl_opts = {
#             'format': 'bestvideo',  # Downloads only video without merging audio
#             'outtmpl': f'{location}/%(title)s.%(ext)s',
#         }
#     else:
#         print("Please select either 'mp3' or 'mp4'.")
#         return

#     # Download using YoutubeDL
#     with YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])

#     print("Download complete!")

# def main():
#     url = input("Enter YouTube URL: ")
#     download_type = input("Enter download type ('mp3' or 'mp4'): ")

#     download_video(url, download_type)

# if __name__ == "__main__":
#     main()






from pytube import YouTube
import tkinter as tk
import os
from tkinter import messagebox


def download_video():
    url = entry_url.get()

    # Validate URL and provide user-friendly error messages
    if not validate_url(url):
        messagebox.showerror("Invalid URL", "Please enter a valid YouTube URL.")
        return

    try:
        # Create the "downloads" directory if it doesn't exist
        if not os.path.exists("downloads"):
            os.makedirs("downloads")

        # Get download options from user (combine best of both responses)
        download_options = get_download_options(url)
        if not download_options:  # User canceled or error
            return

        # Download video based on options
        yt = YouTube(url)
        stream = yt.streams.filter(**download_options).first()
        stream.download(output_path="downloads")
        status_label.config(text="Download complete!")
    except Exception as e:
        messagebox.showerror("Download Error", f"An error occurred: {str(e)}")


def get_download_options(url):
    # Allow selecting video preview or download options (or both)
    preview_window = tk.Toplevel(root)
    preview_window.title("Download Options")

    preview_var = tk.IntVar()
    download_format_var = tk.StringVar()

    # Option for video preview (using external library like opencv or ffmpeg)
    preview_checkbox = tk.Checkbutton(preview_window, text="Preview Video", variable=preview_var)
    preview_checkbox.pack()

    # Option to choose format (MP4, MP3, etc.)
    download_format_label = tk.Label(preview_window, text="Download Format:")
    download_format_label.pack()

    download_format_options = ["Best", "MP4 (high quality)", "MP4 (low quality)", "MP3 (audio only)"]
    download_format_dropdown = tk.OptionMenu(preview_window, download_format_var, *download_format_options)
    download_format_dropdown.pack()

    def choose_options():
        selected_format = download_format_var.get()
        if selected_format == "Best":
            return {}  # Download in best available format
        elif selected_format == "MP4 (high quality)":
            return {"progressive": True, "file_extension": "mp4"}
        elif selected_format == "MP4 (low quality)":
            return {"progressive": True, "file_extension": "mp4", "resolution": "480p"}
        elif selected_format == "MP3 (audio only)":
            return {"only_audio": True}
        return None  # User canceled or invalid option

    download_button = tk.Button(preview_window, text="Download", command=choose_options)
    download_button.pack(pady=10)

    preview_window.grab_set()  # Block main window until preview selection is made
    download_options = choose_options()
    preview_window.destroy()

    return download_options


def validate_url(url):
    try:
        # Basic URL validation using YouTube class (may need additional checks for non-YouTube URLs)
        YouTube(url)
        return True
    except Exception:
        return False


# Create the main application window
root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("400x300")  # Increased height to accommodate options

# Create a label and entry widget for the video URL
url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack(pady=10)
entry_url = tk.Entry(root, width=50)
entry_url.pack(pady=5)

# Create a download button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack(pady=20)

# Create a status label to show download status
status_label = tk.Label(root, text="")
status_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()





