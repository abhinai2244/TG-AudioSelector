# 🎵 Audio Selector Bot

[![Pyrogram](https://img.shields.io/badge/Pyrogram-Bot-blue)](https://docs.pyrogram.org/)
[![FFmpeg](https://img.shields.io/badge/Powered%20by-FFmpeg-red)](https://ffmpeg.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A **Telegram bot** built using [Pyrogram](https://docs.pyrogram.org/) that allows users to **upload video files**, **select specific audio tracks**, and **export the video** with the chosen audio tracks. Supports both **MP4 (video)** and **MKV (document)** formats.

---

## ✨ Features

- 📥 **Download videos from Telegram**: Supports files up to **4GB**.
- 🎧 **Audio track detection**: Automatically detects and lists audio tracks, with language and title tags if available.
- ✅ **Multi-track selection**: Choose multiple audio tracks using an intuitive **inline keyboard**.
- 📦 **Flexible output formats**: Export videos as **MP4 (video)** or **MKV (document)**.
- 📊 **Real-time progress**: Monitor download and upload progress with progress bars.
- ⚙️ **User customization**: Set default filenames and captions through user settings.
- ⏳ **Usage limits**: Free users are limited to **15 files per day**, while premium users can process up to **30**.
- 📚 **Queueing system**: Supports queueing for multiple files, ensuring smooth processing.
- ❌ **Cancel operations**: Easily cancel ongoing processes with the `/cancel` command.
- 🔍 **Status checks**: Check the bot's status with the `/status` command.
- 🆔 **Chat ID retrieval**: Get your chat ID with the `/getid` command.

> ⚠️ **Note**: This bot is designed for audio track selection and video processing only.

---

## 🛠 Requirements

- **Python 3.8+**
- **FFmpeg** (for audio extraction and video processing)

---

## 🚀 Getting Started

### 1. Clone the repository

```sh
git clone https://github.com/your-username/audio-selector-bot.git
cd audio-selector-bot
```

### 2. Install dependencies

Install the required Python packages using pip:

```sh
pip install -U -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the root directory and add the following variables:

```
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
```

- `API_ID` and `API_HASH`: Obtain these from [my.telegram.org](https://my.telegram.org).
- `BOT_TOKEN`: Get this from [@BotFather](https://t.me/BotFather) on Telegram.

### 4. Run the bot

```sh
python main.py
```

---

## 📖 Usage

1. **Start the bot**: Send the `/start` command to the bot in a private chat.
2. **Upload a video**: Send a video file to the bot as a video or document.
3. **Select audio tracks**: The bot will display a list of available audio tracks. Use the inline keyboard to select the desired tracks.
4. **Choose output format**: Select whether you want the output as an **MP4 (video)** or **MKV (document)**.
5. **Wait for processing**: The bot will download, process, and upload the video with the selected audio tracks.

---

## 🤝 Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Pyrogram](https://docs.pyrogram.org/)
- [FFmpeg](https://ffmpeg.org/)
- The open-source community
