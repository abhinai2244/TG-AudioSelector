from collections import defaultdict
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
import os
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
import ffmpeg
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from tqdm import tqdm
import logging
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
import asyncio
import re
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
import json
from datetime import datetime, timedelta
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
from config import DOWNLOAD_DIR, MAX_FILE_SIZE, PREMIUM_USERS, DAILY_LIMIT_FREE, DAILY_LIMIT_PREMIUM
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --

logger = logging.getLogger(__name__)
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --

# Thread-safe storage
user_selections = defaultdict(lambda: defaultdict(dict))
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
status_messages = {}
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
daily_limits = defaultdict(lambda: {'count': 0, 'last_reset': datetime.now()})
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
last_update_time = defaultdict(lambda: 0)
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
last_message_content = defaultdict(lambda: "")  # Track last message content to avoid MESSAGE_NOT_MODIFIED

# JSON file for watermark settings
WATERMARK_SETTINGS_FILE = "watermark_settings.json"
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
def load_watermark_settings(user_id: int) -> dict:
    """Load watermark settings for a user from JSON file."""
    try:
        if os.path.exists(WATERMARK_SETTINGS_FILE):
            with open(WATERMARK_SETTINGS_FILE, 'r') as f:
                settings = json.load(f)
                return settings.get(str(user_id), {
                    "enabled": False,
                    "text": "",
                    "position": "left_top",
                    "font_size": 24
                })
        return {"enabled": False, "text": "", "position": "left_top", "font_size": 24}
    except Exception as e:
        logger.error(f"Error loading watermark settings for user {user_id}: {str(e)}")
        return {"enabled": False, "text": "", "position": "left_top", "font_size": 24}
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --        

def save_watermark_settings(user_id: int, settings: dict):
    """Save watermark settings for a user to JSON file."""
    try:
        all_settings = {}
        if os.path.exists(WATERMARK_SETTINGS_FILE):
            with open(WATERMARK_SETTINGS_FILE, 'r') as f:
                all_settings = json.load(f)
        all_settings[str(user_id)] = settings
        with open(WATERMARK_SETTINGS_FILE, 'w') as f:
            json.dump(all_settings, f, indent=4)
    except Exception as e:
        logger.error(f"Error saving watermark settings for user {user_id}: {str(e)}")

def sanitize_filename(filename: str) -> str:
    if not isinstance(filename, str):
        filename = str(filename) if filename is not None else "default_video"
    return re.sub(r'[^\w\-\.]', '_', filename)
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
def validate_video_file(file_path: str) -> bool:
    try:
        probe = ffmpeg.probe(file_path)
        return any(stream['codec_type'] == 'video' for stream in probe['streams'])
    except Exception as e:
        logger.error(f"File validation failed for {file_path}: {str(e)}")
        return False
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
def get_audio_tracks(input_file: str):
    try:
        probe = ffmpeg.probe(input_file)
        audio_streams = [s for s in probe['streams'] if s['codec_type'] == 'audio']
        tracks = []
        for idx, stream in enumerate(audio_streams):
            track_name = stream.get('tags', {}).get('language', f"Track {idx}")
            if 'title' in stream.get('tags', {}):
                track_name += f" ({stream['tags']['title']})"
            tracks.append((idx, track_name))
        return tracks
    except Exception as e:
        logger.error(f"Error probing file {input_file}: {str(e)}")
        raise
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
def select_audio_tracks(input_file: str, output_file: str, selected_indices: list, output_format: str, quality: str = 'medium', watermark: str = None, user_id: int = None):
    try:
        probe = ffmpeg.probe(input_file)
        audio_streams = [s for s in probe['streams'] if s['codec_type'] == 'audio']
        if not audio_streams or not selected_indices:
            raise ValueError("No audio tracks selected")
        stream = ffmpeg.input(input_file)
        args = {'map': '0:v:0', 'c:v': 'libx264'}  # Use H.264 for compression
        # Set compression level based on quality
        quality_map = {'high': 18, 'medium': 23, 'low': 28}
        args['crf'] = str(quality_map.get(quality, 23))  # Default to medium
        args['preset'] = 'medium'  # Balance encoding speed and compression
        # Apply watermark if provided or enabled in settings
        if user_id:
            settings = load_watermark_settings(user_id)
            if settings.get('enabled', False) and settings.get('text'):
                watermark = settings['text']
        if watermark:
            # Map position to coordinates
            position_map = {
                'left_top': 'x=10:y=10',
                'right_top': 'x=(w-tw-10):y=10',
                'left_bottom': 'x=10:y=(h-th-10)',
                'right_bottom': 'x=(w-tw-10):y=(h-th-10)'
            }
            position = position_map.get(settings.get('position', 'left_top') if user_id else 'left_top', 'x=10:y=10')
            font_size = settings.get('font_size', 24) if user_id else 24
            args['vf'] = f"drawtext=text='{watermark}':fontcolor=white:fontsize={font_size}:box=1:boxcolor=black@0.5:boxborderw=5:{position}"
        for idx in selected_indices:
            args[f'map:{len(selected_indices)}'] = f'0:a:{idx}'
        args['c:a'] = 'copy'
        if output_format == "mkv":
            args['f'] = 'matroska'
        stream = ffmpeg.output(stream, output_file, **args)
        ffmpeg.run(stream, overwrite_output=True)
    except Exception as e:
        logger.error(f"Error processing file {input_file}: {str(e)}")
        raise
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
def generate_thumbnail(input_file: str, output_path: str):
    try:
        ffmpeg.input(input_file, ss='00:00:01').output(output_path, vframes=1, format='image2').run(overwrite_output=True)
    except Exception as e:
        logger.error(f"Thumbnail generation failed: {str(e)}")
        raise
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
def check_daily_limit(user_id: int) -> bool:
    now = datetime.now()
    user_data = daily_limits[user_id]
    if now - user_data['last_reset'] > timedelta(days=1):
        user_data['count'] = 0
        user_data['last_reset'] = now
    limit = DAILY_LIMIT_PREMIUM if user_id in PREMIUM_USERS else DAILY_LIMIT_FREE
    if user_data['count'] >= limit:
        return False
    user_data['count'] += 1
    return True
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
async def safe_telegram_call(func, *args, **kwargs):
    try:
        if func.__name__ == "edit_message_text":
            chat_id = args[0] if args else kwargs.get('chat_id')
            message_id = args[1] if len(args) > 1 else kwargs.get('message_id')
            new_text = args[2] if len(args) > 2 else kwargs.get('text')
            reply_markup = kwargs.get('reply_markup', None)
            key = f"{chat_id}_{message_id}"
            last_content = last_message_content.get(key, "")
            new_content = f"{new_text}_{str(reply_markup)}"
            if last_content == new_content:
                logger.debug(f"Skipping edit for unchanged content: {new_text}")
                return None
            last_message_content[key] = new_content
        return await func(*args, **kwargs)
    except Exception as e:
        if "FLOOD_WAIT" in str(e):
            wait_time = int(str(e).split("A wait of ")[1].split(" seconds")[0])
            logger.warning(f"Flood wait for {wait_time}s")
            await asyncio.sleep(wait_time)
            return await func(*args, **kwargs)
        elif "MESSAGE_NOT_MODIFIED" in str(e):
            logger.debug(f"Message not modified error ignored: {str(e)}")
            return None
        raise
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
async def download_with_progress(client: Client, message: Message, file_path: str, chat_id: int, user_id: int):
    try:
        file_size = message.video.file_size if message.video else message.document.file_size
        if file_size and file_size > MAX_FILE_SIZE:
            raise ValueError(f"File too large: {file_size} bytes")
        bar, last_percent = None, user_selections[chat_id][user_id].get('last_percent', 0)
        status_message_id = user_selections[chat_id][user_id].get('status_message_id')
        async def progress(cur, total):
            nonlocal bar, last_percent
            if not bar: bar = tqdm(total=total, unit='B', unit_scale=True, desc=f"Downloading {user_id}", leave=False)
            bar.n = cur; bar.refresh()
            percent = int((cur / total) * 100)
            if percent >= last_percent + 5 or cur == total:
                last_percent = percent
                user_selections[chat_id][user_id]['last_percent'] = percent
                pbar = "█" * (percent//5) + " " * (20-percent//5)
                await safe_telegram_call(
                    client.edit_message_text,
                    chat_id,
                    status_message_id,
                    f"Downloading: [{pbar} {percent}%]"
                )
            if cur == total: bar.close()
        await client.download_media(message, file_path, progress=progress)
        user = await client.get_users(user_id)
        user_name = user.username if user.username else user.first_name
        await safe_telegram_call(
            client.send_message,
            chat_id,
            f"@{user_name} your media has been downloaded, now select the tracks.",
            reply_to_message_id=message.id
        )
    except Exception as e:
        logger.error(f"Download failed: {str(e)}")
        await safe_telegram_call(
            client.edit_message_text,
            chat_id,
            status_message_id,
            f"Download failed: {str(e)}"
        )
        raise
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
async def upload_with_progress(client: Client, chat_id: int, user_id: int, file_path: str, caption: str, output_format: str, thumb: str = None, reply_to_message_id: int = None):
    max_retries = 5
    base_delay = 2
    for attempt in range(max_retries):
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File {file_path} does not exist")
            bar, last_percent = None, user_selections[chat_id][user_id].get('last_percent', 0)
            async def progress(cur, total):
                nonlocal bar, last_percent
                if not bar: bar = tqdm(total=total, unit='B', unit_scale=True, desc=f"Uploading {user_id}", leave=False)
                bar.n = cur; bar.refresh()
                percent = int((cur / total) * 100)
                if percent >= last_percent + 5 or cur == total:
                    last_percent = percent
                    user_selections[chat_id][user_id]['last_percent'] = percent
                    pbar = "█" * (percent//5) + " " * (20-percent//5)
                    await safe_telegram_call(
                        client.edit_message_text,
                        chat_id,
                        user_selections[chat_id][user_id]['status_message_id'],
                        f"Uploading: [{pbar} {percent}%]"
                    )
                if cur == total: bar.close()
            if output_format == "video":
                await safe_telegram_call(client.send_video, chat_id, file_path, caption=caption, progress=progress, thumb=thumb if thumb and os.path.exists(thumb) else None, file_name=sanitize_filename(os.path.basename(file_path)), reply_to_message_id=reply_to_message_id)
            else:
                await safe_telegram_call(client.send_document, chat_id, file_path, caption=caption, progress=progress, thumb=thumb if thumb and os.path.exists(thumb) else None, file_name=sanitize_filename(os.path.basename(file_path)), reply_to_message_id=reply_to_message_id)
            return True  # Successful upload
        except Exception as e:
            logger.error(f"Upload attempt {attempt + 1}/{max_retries} failed: {str(e)}")
            if attempt + 1 == max_retries:
                await safe_telegram_call(
                    client.edit_message_text,
                    chat_id,
                    user_selections[chat_id][user_id]['status_message_id'],
                    f"Upload failed after {max_retries} attempts: {str(e)}"
                )
                return False
            delay = base_delay * (2 ** attempt)  # Exponential backoff: 2s, 4s, 8s, 16s, 32s
            logger.info(f"Retrying upload after {delay}s delay")
            await asyncio.sleep(delay)
    return False
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
async def cleanup_files(files: list):
    """Attempt to delete files with retries for PermissionError."""
    max_retries = 3
    for file in files:
        if not os.path.exists(file):
            continue
        for attempt in range(max_retries):
            try:
                os.remove(file)
                logger.debug(f"Deleted file: {file}")
                break
            except PermissionError as e:
                logger.warning(f"PermissionError deleting {file}: {str(e)}, attempt {attempt + 1}/{max_retries}")
                if attempt + 1 == max_retries:
                    logger.error(f"Failed to delete {file} after {max_retries} attempts")
                    break
                await asyncio.sleep(1)  # Wait before retrying
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
async def update_status_message(client: Client, chat_id: int, user_id: int, status: str, force_update: bool = False):
    try:
        now = datetime.now().timestamp()
        if not force_update and now - last_update_time[chat_id] < 5:
            return
        last_update_time[chat_id] = now
        user_selections[chat_id][user_id]['status'] = status
        status_text = "\n".join(
            f"User {uid}: {user_selections[chat_id][uid].get('status','Idle')}"
            for uid in user_selections[chat_id] if isinstance(user_selections[chat_id][uid], dict)
        )
        if chat_id in status_messages:
            await safe_telegram_call(client.edit_message_text, chat_id, status_messages[chat_id], f"Current Status:\n{status_text}")
        else:
            msg = await safe_telegram_call(client.send_message, chat_id, f"Current Status:\n{status_text}")
            status_messages[chat_id] = msg.id
    except Exception as e:
        logger.error(f"Status update failed: {str(e)}")
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
async def create_track_selection_keyboard(chat_id: int, user_id: int, tracks: list):
    buttons = [[InlineKeyboardButton(f"{'✅ ' if idx in user_selections[chat_id][user_id].get('selected_tracks', set()) else ''}{name}", callback_data=f"track_{idx}") for idx, name in tracks]]
    buttons.append([InlineKeyboardButton("Done", callback_data="done_tracks")])
    return InlineKeyboardMarkup(buttons)
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
async def create_quality_selection_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("1080P", callback_data="quality_high")],
        [InlineKeyboardButton("720P", callback_data="quality_medium")],
        [InlineKeyboardButton("480P", callback_data="quality_low")]
    ])
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
async def create_watermark_prompt():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Add Text Watermark", callback_data="watermark_text")],
        [InlineKeyboardButton("Skip Watermark", callback_data="watermark_skip")]
    ])
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
async def create_format_selection_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Video (MP4)", callback_data="format_video")],
        [InlineKeyboardButton("Document (MKV)", callback_data="format_mkv")]
    ])

# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
