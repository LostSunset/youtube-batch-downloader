import tkinter as tk
from tkinter import messagebox
from pytube import Playlist
import os

class YouTubePlaylistExtractor:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("YouTube 播放清單網址擷取工具")
        self.window.geometry("500x200")
        
        # 設定視窗置中
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - 500) // 2
        y = (screen_height - 200) // 2
        self.window.geometry(f"500x200+{x}+{y}")
        
        # 建立說明標籤
        self.label = tk.Label(
            self.window,
            text="請輸入 YouTube 播放清單網址：",
            font=("微軟正黑體", 12)
        )
        self.label.pack(pady=20)
        
        # 建立輸入框
        self.url_entry = tk.Entry(self.window, width=50)
        self.url_entry.pack(pady=10)
        
        # 建立確認按鈕
        self.submit_button = tk.Button(
            self.window,
            text="開始擷取",
            command=self.extract_urls,
            font=("微軟正黑體", 10)
        )
        self.submit_button.pack(pady=20)
        
    def extract_urls(self):
        try:
            # 獲取輸入的網址
            playlist_url = self.url_entry.get().strip()
            
            if not playlist_url:
                messagebox.showerror("錯誤", "請輸入播放清單網址！")
                return
                
            # 建立 Playlist 物件
            playlist = Playlist(playlist_url)
            
            # 取得所有影片網址
            video_urls = [url for url in playlist.video_urls]
            
            if not video_urls:
                messagebox.showerror("錯誤", "無法取得播放清單中的影片，請確認網址是否正確！")
                return
                
            # 將網址寫入文字檔
            output_file = "playlist_urls.txt"
            with open(output_file, "w", encoding="utf-8") as f:
                for url in video_urls:
                    f.write(f"{url}\n")
            
            messagebox.showinfo(
                "完成",
                f"已成功擷取 {len(video_urls)} 個影片網址並儲存至 {output_file}"
            )
            
        except Exception as e:
            messagebox.showerror("錯誤", f"發生錯誤：{str(e)}")
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = YouTubePlaylistExtractor()
    app.run()