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
from pyrogram import Client, filters
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
from pyrogram.enums import ChatType, ChatAction, ParseMode
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
from datetime import datetime
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
import asyncio
import random
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
import logging
from config import DOWNLOAD_DIR, ALLOWED_GROUP_IDS, OWNER_ID, MAX_FILE_SIZE, PREMIUM_USERS, DAILY_LIMIT_FREE, DAILY_LIMIT_PREMIUM
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
from utils import (
    get_audio_tracks, select_audio_tracks, download_with_progress,
    upload_with_progress, create_track_selection_keyboard,
    create_format_selection_keyboard, user_selections, update_status_message,
    sanitize_filename, validate_video_file, generate_thumbnail, check_daily_limit,
    safe_telegram_call
)
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
daily_limits={}
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
# Sticker and images
START_PIC = "https://telegra.ph/HgBotz-08-09-5"
ABOUT_PIC = "https://telegra.ph/HgBotz-08-09-6"
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
stickers = [
    "CAACAgUAAxkBAAEOXBhoCoKZ76jevKX-Vc5v5SZhCeQAAXMAAh4KAALJrhlVZygbxFWWTLw2BA"
]
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
welcome_text = "<i><blockquote>Wᴇʟᴄᴏᴍᴇ, ʙᴀʙʏ… ɪ’ᴠᴇ ʙᴇᴇɴ ᴄʀᴀᴠɪɴɢ ʏᴏᴜʀ ᴘʀᴇsᴇɴᴄᴇ ғᴇᴇʟs ᴘᴇʀғᴇᴄᴛ ɴᴏᴡ ᴛʜᴀᴛ ʏᴏᴜ’ʀᴇ ʜᴇʀᴇ.</blockquote></i>"
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
def register_handlers(app: Client):
    @app.on_message(filters.command("getid"))
    async def get_chat_id(client: Client, message: Message):
        await safe_telegram_call(message.reply, f"Chat ID: {message.chat.id}, Chat Type: {message.chat.type}")
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
    @app.on_message(filters.command("us"))
    async def set_user_settings(client: Client, message: Message):
        try:
            chat_id, user_id = message.chat.id, message.from_user.id
            args = message.text.split(maxsplit=2)[1:]
            if chat_id not in user_selections:
                user_selections[chat_id] = {}
            if user_id not in user_selections[chat_id]:
                user_selections[chat_id][user_id] = {'status': 'Idle', 'last_percent': 0}
            if not args:
                config = user_selections[chat_id][user_id]
                limit = DAILY_LIMIT_PREMIUM if user_id in PREMIUM_USERS else DAILY_LIMIT_FREE
                daily_data = daily_limits.get(user_id, {'count': 0})
                remaining = max(0, limit - daily_data['count'])
                response = (f"**User Configuration for {user_id}:**\n"
                            f"- Default Filename: {config.get('default_name','Not set')}\n"
                            f"- Default Caption: {config.get('default_caption','Not set')}\n"
                            f"- Daily Limit: {limit} videos\n"
                            f"- Remaining Today: {remaining} videos\n"
                            f"- Status: {config.get('status','Idle')}")
                await safe_telegram_call(message.reply, response)
                return
            if len(args) < 2:
                await safe_telegram_call(message.reply, "Usage: /us <filename> <caption>")
                return
            default_name, default_caption = sanitize_filename(args[0]), args[1]
            user_selections[chat_id][user_id]['default_name'] = default_name
            user_selections[chat_id][user_id]['default_caption'] = default_caption
            await safe_telegram_call(message.reply, f"Settings updated:\nFilename: {default_name}\nCaption: {default_caption}")
        except Exception as e:
            logger.error(f"Error in set_user_settings: {str(e)}")
            await safe_telegram_call(message.reply, f"An error occurred: {str(e)}")
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
    @app.on_message(filters.command("status"))
    async def show_status(client: Client, message: Message):
        chat_id = message.chat.id
        status_text = "\n".join(
            f"User {uid}: {user_selections[chat_id][uid].get('status','Idle')}"
            for uid in user_selections.get(chat_id, {}) if isinstance(user_selections[chat_id][uid], dict)
        )
        await safe_telegram_call(message.reply, f"Current Status:\n{status_text}" if status_text else "No active processes.")
        
    @app.on_message(filters=filters.video | filters.document)
    async def handle_message(client: Client, message: Message):
        chat_id, user_id = message.chat.id, message.from_user.id
        if user_id != OWNER_ID and chat_id not in ALLOWED_GROUP_IDS:
            logger.info(f"Unauthorized access attempt: user_id={user_id}, chat_id={chat_id}, allowed_ids={ALLOWED_GROUP_IDS}")
            await safe_telegram_call(message.reply, "This bot is not authorized here.")
            return
        if user_id != OWNER_ID and message.chat.type not in [ChatType.GROUP, ChatType.SUPERGROUP]:
            await safe_telegram_call(message.reply, "This bot works only in groups.")
            return
        if not check_daily_limit(user_id):
            limit = DAILY_LIMIT_PREMIUM if user_id in PREMIUM_USERS else DAILY_LIMIT_FREE
            await safe_telegram_call(message.reply, f"Daily limit of {limit} videos reached.")
            return
        if user_selections.get(chat_id, {}).get(user_id, {}).get('processing'):
            user_selections[chat_id][user_id]['queue'].append(message)
            pos = len(user_selections[chat_id][user_id]['queue'])
            await safe_telegram_call(message.reply, f"You already have a process. Queue position: {pos}")
            return
        if not message.video and not message.document:
            await safe_telegram_call(message.reply, "Please send a video file.")
            return
        size = message.video.file_size if message.video else message.document.file_size
        if size and size > MAX_FILE_SIZE:
            await safe_telegram_call(message.reply, f"File size exceeds {MAX_FILE_SIZE} bytes")
            return
        name = message.video.file_name if message.video else message.document.file_name
        if not name:
            name = f"video_{message.id}.mp4"
        if user_id in user_selections.get(chat_id, {}) and 'default_name' in user_selections[chat_id][user_id]:
            name = user_selections[chat_id][user_id]['default_name']
        path = os.path.join(DOWNLOAD_DIR, f"{user_id}_{sanitize_filename(name)}")
        user_selections.setdefault(chat_id, {}).setdefault(user_id, {'processing': True, 'queue': []})
        await update_status_message(client, chat_id, user_id, "Starting download...")
        await download_with_progress(client, message, path, chat_id, user_id)
        if not validate_video_file(path):
            os.remove(path)
            await safe_telegram_call(message.reply, "Invalid video file.")
            user_selections[chat_id][user_id]['processing'] = False
            return
        tracks = get_audio_tracks(path)
        if not tracks:
            os.remove(path)
            await safe_telegram_call(message.reply, "No audio tracks found.")
            user_selections[chat_id][user_id]['processing'] = False
            return
        user_selections[chat_id][user_id].update({'file_path': path, 'selected_tracks': set(), 'output_format': None, 'status': 'Selecting tracks', 'last_percent': 0})
        await safe_telegram_call(message.reply, "Select tracks:", reply_markup=await create_track_selection_keyboard(chat_id, user_id, tracks))
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# ----------------------------------------
    @app.on_callback_query()
    async def handle_callback(client: Client, cq):
        chat_id, user_id = cq.message.chat.id, cq.from_user.id
        if user_id not in user_selections.get(chat_id, {}):
            await cq.answer("This is not your session.", show_alert=True)
            return
        data = cq.data
        if data.startswith("track_"):
            idx = int(data.split("_")[1])
            st = user_selections[chat_id][user_id]['selected_tracks']
            st.remove(idx) if idx in st else st.add(idx)
            tracks = get_audio_tracks(user_selections[chat_id][user_id]['file_path'])
            await safe_telegram_call(cq.message.edit_reply_markup, await create_track_selection_keyboard(chat_id, user_id, tracks))
            await update_status_message(client, chat_id, user_id, "Selecting tracks...")
        elif data == "done_tracks":
            if not user_selections[chat_id][user_id]['selected_tracks']:
                await safe_telegram_call(cq.message.reply, "Select at least one track.")
                return
            await safe_telegram_call(cq.message.edit_reply_markup, None)
            await safe_telegram_call(cq.message.reply, "Select output format:", reply_markup=await create_format_selection_keyboard())
            await update_status_message(client, chat_id, user_id, "Selecting output format...")
        elif data.startswith("format_"):
            fmt = data.split("_")[1]
            info = user_selections[chat_id][user_id]
            info['output_format'] = fmt
            src = info['file_path']
            outname = info.get('default_name') or f"processed_{user_id}_{os.path.basename(src)}"
            dst = os.path.join(DOWNLOAD_DIR, sanitize_filename(outname))
            if fmt == "mkv": dst = os.path.splitext(dst)[0] + ".mkv"
            thumb = os.path.join(DOWNLOAD_DIR, f"{os.path.splitext(outname)[0]}.jpg")
            await update_status_message(client, chat_id, user_id, "Processing video...")
            select_audio_tracks(src, dst, list(info['selected_tracks']), fmt)
            generate_thumbnail(src, thumb)
            cap = info.get('default_caption', "Here is your video.")
            await update_status_message(client, chat_id, user_id, "Uploading video...")
            await upload_with_progress(client, chat_id, user_id, dst, cap, fmt, thumb)
            for f in [src, dst, thumb]:
                if os.path.exists(f): os.remove(f)
            user_selections[chat_id][user_id]['processing'] = False
            del user_selections[chat_id][user_id]['file_path']
            await update_status_message(client, chat_id, user_id, "Completed")
            await safe_telegram_call(cq.message.edit_reply_markup, None)
            if user_selections[chat_id][user_id]['queue']:
                nxt = user_selections[chat_id][user_id]['queue'].pop(0)
                await handle_message(client, nxt)
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# ---------------------------------------- 
    @app.on_message(filters.command("cancel"))
    async def cancel_process(client: Client, message: Message):
        chat_id, user_id = message.chat.id, message.from_user.id
        if user_id not in user_selections.get(chat_id, {}) or not user_selections[chat_id][user_id].get('processing'):
            await safe_telegram_call(message.reply, "No active process to cancel.")
            return
        user_selections[chat_id][user_id]['processing'] = False
        path = user_selections[chat_id][user_id].get('file_path')
        if path and os.path.exists(path):
            os.remove(path)
        await safe_telegram_call(message.reply, "Process cancelled and temporary files deleted.")
        if user_selections[chat_id][user_id]['queue']:
            nxt = user_selections[chat_id][user_id]['queue'].pop(0)
            await handle_message(client, nxt)
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# ----------------------------------------
    @app.on_message(filters.command("start"))
    async def start_cmd(client, message):
        user_id = message.from_user.id

        # Typing + animated intro
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)
        msg = await message.reply_text(welcome_text, parse_mode=ParseMode.HTML)
        await asyncio.sleep(0.1)
        await msg.edit_text("<b><i><pre>Sᴛᴀʀᴛɪɴɢ...</pre></i></b>", parse_mode=ParseMode.HTML)
        await asyncio.sleep(0.1)
        await msg.delete()

        # Sticker
        await client.send_chat_action(message.chat.id, ChatAction.CHOOSE_STICKER)
        await message.reply_sticker(random.choice(stickers))

        # Main buttons
        buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about"),
                InlineKeyboardButton("Sᴜᴩᴩᴏʀᴛ", url="https://t.me/clutch008"),
            ],
            [
                InlineKeyboardButton("Dᴇᴠᴇʟᴏᴩᴇʀ", url="https://t.me/clutch008"),
            ],
        ])

        caption = (
            f"<pre>Hᴇʏᴏ ᴄᴜᴛɪᴇ</pre>\n"
            f"<b><blockquote>›› ɪ’ᴍ ᴀ ʜᴀɴᴅʏ ᴀᴜᴅɪᴏ ꜱᴇʟᴇᴄᴛᴏʀ ʙᴏᴛ ᴍᴀᴅᴇ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴄʜᴏᴏꜱᴇ ᴏʀ ʀᴇᴍᴏᴠᴇ ᴀᴜᴅɪᴏ ᴛʀᴀᴄᴋꜱ ꜰʀᴏᴍ ʏᴏᴜʀ ᴠɪᴅᴇᴏꜱ!</b></blockquote>\n"
            f"<b><blockquote>◈ <a href='https://t.me/clutch008'>ABHI : ᴡʜᴇʀᴇ ᴀʀɪsᴇ</a></b></blockquote>"
        )

        if START_PIC:
            await app.send_photo(
                chat_id=message.chat.id,
                photo=START_PIC,
                caption=caption,
                reply_markup=buttons
            )
        else:
            await app.send_message(
                chat_id=message.chat.id,
                text=caption,
                reply_markup=buttons
            )
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# ----------------------------------------
    @app.on_callback_query(filters.regex("about"))
    async def about_cb(client, callback_query):
        about_buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Bᴀᴄᴋ", callback_data="back"),
                InlineKeyboardButton("Cʟᴏsᴇ", callback_data="close")
            ]
        ])

        about_caption = (
            "<b><blockquote>Hᴇʏ ᴅᴇᴀʀ ᴍʏ ɴᴀᴍᴇ Iuno</b></blockquote>\n"
            f"<b><blockquote>◈ Oᴡɴᴇʀ : <a href='https://t.me/clutch008'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n"
            f"◈ Dᴇᴠᴇʟᴏᴩᴇʀ : <a href='https://t.me/clutch008'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n"
            f"◈ Mᴀɪɴ Cʜᴀɴɴᴇʟ : <a href='https://t.me/+HzquTipfQsA1YWFl'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n"
            f"◈ Uᴩᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ : <a href='https://t.me/BOTSKINGDOMS'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b></blockquote>"
        )

        await callback_query.message.edit_media(
            media=InputMediaPhoto(media=ABOUT_PIC, caption=about_caption, parse_mode=ParseMode.HTML),
            reply_markup=about_buttons
        )
        await callback_query.answer()
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# ----------------------------------------
    @app.on_callback_query(filters.regex("close"))
    async def close_cb(client, callback_query):
        try:
            await callback_query.message.delete()
        except Exception:
            pass
        await callback_query.answer("Closed.")
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# ----------------------------------------
    @app.on_callback_query(filters.regex("back"))
    async def back_cb(client, callback_query):
        main_buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about"),
                InlineKeyboardButton("Sᴜᴩᴩᴏʀᴛ", url="https://t.me/clutch008"),
            ],
            [
                InlineKeyboardButton("Dᴇᴠᴇʟᴏᴩᴇʀ", url="https://t.me/clutch008"),
            ],
        ])

        main_caption = (
            f"<pre>Hᴇʏᴏ ᴄᴜᴛɪᴇ</pre>\n"
            f"<b><blockquote>›› ɪ’ᴍ ᴀ ʜᴀɴᴅʏ ᴀᴜᴅɪᴏ ꜱᴇʟᴇᴄᴛᴏʀ ʙᴏᴛ ᴍᴀᴅᴇ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴄʜᴏᴏꜱᴇ ᴏʀ ʀᴇᴍᴏᴠᴇ ᴀᴜᴅɪᴏ ᴛʀᴀᴄᴋꜱ ꜰʀᴏᴍ ʏᴏᴜʀ ᴠɪᴅᴇᴏꜱ!</b></blockquote>\n"
            f"<b><blockquote>◈ <a href='https://t.me/clutch008'>ABHI : ᴡʜᴇʀᴇ ᴀʀɪsᴇ</a></b></blockquote>"
        )

        if START_PIC:
            await callback_query.message.edit_media(
                media=InputMediaPhoto(media=START_PIC, caption=main_caption, parse_mode=ParseMode.HTML),
                reply_markup=main_buttons
            )
        else:
            await callback_query.message.edit_text(
                text=main_caption,
                reply_markup=main_buttons,
                parse_mode=ParseMode.HTML
            )
        await callback_query.answer()
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# ----------------------------------------
