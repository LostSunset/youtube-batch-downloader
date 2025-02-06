import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os
import threading

class YouTubeDownloader:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("YouTube 批量下載工具")
        self.window.geometry("600x400")
        
        # 設定視窗置中
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - 600) // 2
        y = (screen_height - 400) // 2
        self.window.geometry(f"600x400+{x}+{y}")
        
        # 建立下載路徑選擇按鈕
        self.path_button = tk.Button(
            self.window,
            text="選擇下載位置",
            command=self.select_download_path,
            font=("微軟正黑體", 10)
        )
        self.path_button.pack(pady=10)
        
        # 顯示選擇的下載路徑
        self.path_label = tk.Label(
            self.window,
            text="尚未選擇下載位置",
            font=("微軟正黑體", 10),
            wraplength=500
        )
        self.path_label.pack(pady=5)
        
        # 建立檔案選擇按鈕
        self.file_button = tk.Button(
            self.window,
            text="選擇網址清單檔案",
            command=self.select_url_file,
            font=("微軟正黑體", 10)
        )
        self.file_button.pack(pady=10)
        
        # 顯示選擇的檔案路徑
        self.file_label = tk.Label(
            self.window,
            text="尚未選擇檔案",
            font=("微軟正黑體", 10),
            wraplength=500
        )
        self.file_label.pack(pady=5)
        
        # 建立開始下載按鈕
        self.download_button = tk.Button(
            self.window,
            text="開始下載",
            command=self.start_download,
            font=("微軟正黑體", 10)
        )
        self.download_button.pack(pady=10)
        
        # 建立進度顯示文字框
        self.progress_text = tk.Text(
            self.window,
            height=12,
            width=50,
            font=("Consolas", 10)
        )
        self.progress_text.pack(pady=10, padx=20)
        
        # 初始化變數
        self.download_path = ""
        self.url_file_path = ""
        
    def select_download_path(self):
        self.download_path = filedialog.askdirectory()
        if self.download_path:
            self.path_label.config(text=f"下載位置：{self.download_path}")
        
    def select_url_file(self):
        self.url_file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt")]
        )
        if self.url_file_path:
            self.file_label.config(text=f"檔案位置：{self.url_file_path}")
    
    def update_progress(self, message):
        self.progress_text.insert(tk.END, message + "\n")
        self.progress_text.see(tk.END)
    
    def download_videos(self):
        try:
            # 讀取網址清單
            with open(self.url_file_path, 'r', encoding='utf-8') as f:
                urls = f.read().splitlines()
            
            # 切換到下載目錄
            os.chdir(self.download_path)
            
            # 處理每個網址
            for i, url in enumerate(urls, 1):
                if url.strip():  # 跳過空行
                    self.update_progress(f"正在下載第 {i}/{len(urls)} 個影片: {url}")
                    
                    # 執行 yt-dlp 命令
                    command = ['yt-dlp', '--cookies-from-browser', 'firefox', url]
                    process = subprocess.Popen(
                        command,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        universal_newlines=True
                    )
                    
                    # 即時輸出下載進度
                    for line in process.stdout:
                        self.update_progress(line.strip())
                    
                    # 等待程序完成
                    process.wait()
                    
                    if process.returncode == 0:
                        self.update_progress(f"第 {i} 個影片下載完成\n")
                    else:
                        self.update_progress(f"第 {i} 個影片下載失敗\n")
            
            self.update_progress("所有下載任務完成！")
            messagebox.showinfo("完成", "所有影片已下載完成！")
            
        except Exception as e:
            self.update_progress(f"發生錯誤：{str(e)}")
            messagebox.showerror("錯誤", f"下載過程中發生錯誤：{str(e)}")
        
        finally:
            # 重新啟用按鈕
            self.download_button.config(state=tk.NORMAL)
    
    def start_download(self):
        if not self.download_path or not self.url_file_path:
            messagebox.showerror("錯誤", "請先選擇下載位置和網址清單檔案！")
            return
        
        # 確認 yt-dlp 是否已安裝
        try:
            subprocess.run(['yt-dlp', '--version'], capture_output=True)
        except FileNotFoundError:
            messagebox.showerror("錯誤", "未找到 yt-dlp，請確認是否已正確安裝！")
            return
        
        # 禁用下載按鈕
        self.download_button.config(state=tk.DISABLED)
        
        # 在新執行緒中執行下載
        threading.Thread(target=self.download_videos, daemon=True).start()
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = YouTubeDownloader()
    app.run()