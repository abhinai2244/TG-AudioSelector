# 🎵 Audio Selector Bot
# STAR THE REPO IT HELPS US A ALOT 
# NEXT I WILL ADD MERGING VIDEOS FOR THIS REPO IF U SHOW US SUPPORT 

[![Pyrogram](https://img.shields.io/badge/Pyrogram-Bot-blue)](https://docs.pyrogram.org/)
[![FFmpeg](https://img.shields.io/badge/Powered%20by-FFmpeg-red)](https://ffmpeg.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A **Telegram bot** built using [Pyrogram](https://docs.pyrogram.org/) that allows users to **upload video files**,  
**select specific audio tracks**, and **export the video** with chosen audio tracks.  

Supports **MP4 (video)** and **MKV (document)** formats.  

---

## ✨ Features

- 📥 Download videos from Telegram (up to **4GB**)
- 🎧 Detect and list audio tracks (with language/title tags if available)
- ✅ Select multiple audio tracks via **inline keyboard**
- 📦 Choose output format: **MP4 (video)** or **MKV (document)**
- 📊 Progress bars for download/upload
- ⚙️ User settings for default filename/caption
- ⏳ Daily usage limits (**15 for free users, 30 for premium**)
- 📚 Queue support for multiple files
- ❌ Cancel ongoing processes with `/cancel`
- 🔍 Status checks with `/status`
- 🆔 Get chat ID with `/getid`

> ⚠️ This bot is **not** an anime bot – it’s purely for  
> **audio track selection and video processing**.

---

## 🛠 Requirements

- **Python 3.8+**
- **FFmpeg** (for audio extraction and video processing)

### Install Python packages
```sh
pip install -U pyrogram tqdm ffmpeg-python
