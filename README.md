# YouTube Playlist Downloader Tool
# YouTube 批量下載工具 & 播放清單擷取工具  
[🇹🇼 繁體中文](docs/README_ZH.md) | [English](docs/README_EN.md)

這是一個用於下載 YouTube 播放清單的工具集，包含兩個主要程式：
1. 播放清單網址擷取工具
2. 批量影片下載工具

## 功能特點

### 播放清單網址擷取工具 (playlist_extractor.py)
- 提供簡潔的圖形介面
- 自動擷取播放清單中所有影片網址
- 將結果儲存為文字檔
- 支援錯誤處理和操作提示

### 批量影片下載工具 (batch_downloader.py)
- 圖形化介面操作
- 支援選擇下載目標資料夾
- 使用 yt-dlp 進行下載
- 支援 Firefox cookies（可下載會員限定影片）
- 即時顯示下載進度
- 支援批量處理多個影片

## 系統需求

- Python 3.6 或更高版本
- Firefox 瀏覽器（用於 cookies）
- Windows/macOS/Linux

## 安裝指南

1. 克隆倉庫：
```bash
git clone https://github.com/your-username/youtube-playlist-downloader.git
cd youtube-playlist-downloader
```

2. 安裝依賴套件：
```bash
pip install -r requirements.txt
```

## 使用方法

### 步驟 1：擷取播放清單網址

1. 執行播放清單網址擷取工具：
```bash
python playlist_extractor.py
```

2. 在彈出的視窗中輸入 YouTube 播放清單網址
3. 點擊「開始擷取」
4. 程式會在同目錄下生成 `playlist_urls.txt` 檔案

### 步驟 2：下載影片

1. 執行批量下載工具：
```bash
python batch_downloader.py
```

2. 點擊「選擇下載位置」按鈕，選擇要儲存影片的資料夾
3. 點擊「選擇網址清單檔案」按鈕，選擇先前產生的 `playlist_urls.txt`
4. 點擊「開始下載」，等待下載完成

## 建立執行檔

使用 PyInstaller 建立獨立執行檔：

```bash
pip install pyinstaller
pyinstaller --onefile playlist_extractor.py
pyinstaller --onefile batch_downloader.py
```

執行檔將會產生在 `dist` 資料夾中。

## 常見問題

### Q: 為什麼需要使用 Firefox？
A: 程式使用 Firefox 的 cookies 來支援下載會員限定影片。如果只下載公開影片，可以修改程式碼移除 cookies 相關設定。

### Q: 下載速度較慢怎麼辦？
A: 可以嘗試更新 yt-dlp 到最新版本：
```bash
pip install --upgrade yt-dlp
```

### Q: 如何回報問題？
A: 請在 GitHub Issues 頁面提交問題，並提供以下資訊：
- 使用的作業系統
- Python 版本
- 錯誤訊息
- 重現步驟

## 貢獻指南

歡迎提交 Pull Request！請確保：
1. 程式碼符合 PEP 8 規範
2. 新功能包含適當的錯誤處理
3. 更新相關文檔

## 版權聲明

本專案採用 MIT 授權條款 - 詳見 [LICENSE](LICENSE) 檔案

## 更新日誌

### v1.0.0 (2024-02-06)
- 初始發布
- 實現基本功能
- 新增使用說明文檔