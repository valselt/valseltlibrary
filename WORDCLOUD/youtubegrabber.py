import requests
import csv
import tkinter as tk
from tkinter import messagebox, filedialog
import threading
import time

def get_video_ids_from_channel(channel_id, api_key):
    base_url = "https://www.googleapis.com/youtube/v3/search"
    video_ids = []
    next_page_token = None

    while True:
        params = {
            "key": api_key,
            "channelId": channel_id,
            "part": "id",
            "order": "date",
            "maxResults": 50,
            "pageToken": next_page_token
        }
        
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            for item in data.get("items", []):
                if item["id"]["kind"] == "youtube#video":
                    video_ids.append(item["id"]["videoId"])
            next_page_token = data.get("nextPageToken")
            if not next_page_token:
                break
        else:
            print("Error:", response.status_code)
            break

    return video_ids

def get_video_data(video_id, api_key):
    base_url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        "id": video_id,
        "key": api_key,
        "part": "snippet,statistics"
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        video_data = response.json()
        if "items" in video_data and len(video_data["items"]) > 0:
            return video_data["items"][0]
    return None

def save_to_csv(video_data_list, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Menulis header
        writer.writerow(["Video ID", "Title", "Description", "URL", "Published At", "View Count"])
        # Menulis data video
        for video_data in video_data_list:
            writer.writerow([
                video_data["id"],
                video_data["snippet"]["title"],
                video_data["snippet"]["description"],
                f"https://www.youtube.com/watch?v={video_data['id']}",
                video_data["snippet"]["publishedAt"],
                video_data["statistics"]["viewCount"]
            ])

def process_data(channel_id, api_key, save_path):
    video_ids = get_video_ids_from_channel(channel_id, api_key)
    video_data_list = []
    
    for video_id in video_ids:
        video_info = get_video_data(video_id, api_key)
        if video_info:
            video_data_list.append(video_info)

    if video_data_list:
        save_to_csv(video_data_list, save_path)
        messagebox.showinfo("Success", "Metadata YouTube has been created!")
    else:
        messagebox.showwarning("Warning", "No video data found.")

def start_processing():
    channel_id = channel_id_entry.get()
    api_key = api_key_entry.get()

    if not channel_id or not api_key:
        messagebox.showerror("Error", "Please enter both Channel ID and API Key.")
        return

    # Menampilkan dialog untuk memilih lokasi penyimpanan
    save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    
    if not save_path:
        return

    # Menampilkan efek loading
    loading_window = tk.Toplevel(root)
    loading_window.title("Processing")
    loading_label = tk.Label(loading_window, text="Processing... Please wait.")
    loading_label.pack(pady=20)
    
    # Menjalankan proses di thread terpisah
    def run():
        process_data(channel_id, api_key, save_path)
        time.sleep(1)  # Simulasi waktu pemrosesan
        loading_window.destroy()  # Menutup jendela loading

    threading.Thread(target=run).start()

# Membuat jendela utama
root = tk.Tk()
root.title("YouTube Metadata Fetcher")

# Input untuk Channel ID
tk.Label(root, text="Channel ID:").pack(pady=5)
channel_id_entry = tk.Entry(root, width=50)
channel_id_entry.pack(pady=5)

# Input untuk API Key
tk.Label(root, text="API Key:").pack(pady=5)
api_key_entry = tk.Entry(root, show='*', width=50)
api_key_entry.pack(pady=5)

# Tombol untuk memulai proses
start_button = tk.Button(root, text="Fetch Metadata", command=start_processing)
start_button .pack(pady=10)

# Menjalankan aplikasi
root.mainloop()