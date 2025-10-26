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
from pyrogram.types import Message
from pyrogram.enums import ChatType
import logging
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
import asyncio
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
from config import DOWNLOAD_DIR, ALLOWED_GROUP_IDS, OWNER_ID, MAX_FILE_SIZE, PREMIUM_USERS, DAILY_LIMIT_FREE, DAILY_LIMIT_PREMIUM
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
from utils import (
    get_audio_tracks, select_audio_tracks, download_with_progress,
    upload_with_progress, create_track_selection_keyboard,
    create_quality_selection_keyboard, create_watermark_prompt, create_format_selection_keyboard,
    user_selections, sanitize_filename, validate_video_file, generate_thumbnail, check_daily_limit, safe_telegram_call, load_watermark_settings, cleanup_files
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
def register_video_handlers(app: Client):
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
        user_selections.setdefault(chat_id, {}).setdefault(user_id, {'processing': True, 'queue': [], 'original_message_id': message.id})
        user_selections[chat_id][user_id]['status'] = "Starting download..."
        msg = await safe_telegram_call(message.reply, "Starting download...")
        user_selections[chat_id][user_id]['status_message_id'] = msg.id
        await download_with_progress(client, message, path, chat_id, user_id)
        if not validate_video_file(path):
            await cleanup_files([path])
            await safe_telegram_call(client.edit_message_text, chat_id, msg.id, "Invalid video file.")
            user_selections[chat_id][user_id]['processing'] = False
            return
        tracks = get_audio_tracks(path)
        if not tracks:
            await cleanup_files([path])
            await safe_telegram_call(client.edit_message_text, chat_id, msg.id, "No audio tracks found.")
            user_selections[chat_id][user_id]['processing'] = False
            return
        user_selections[chat_id][user_id].update({'file_path': path, 'selected_tracks': set(), 'output_format': None, 'quality': None, 'watermark': None, 'status': 'Selecting tracks...', 'last_percent': 0})
        await safe_telegram_call(client.edit_message_text, chat_id, msg.id, "Select tracks:", reply_markup=await create_track_selection_keyboard(chat_id, user_id, tracks))
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
    @app.on_message(filters.text & filters.reply)
    async def handle_watermark_text(client: Client, message: Message):
        chat_id, user_id = message.chat.id, message.from_user.id
        if user_id not in user_selections.get(chat_id, {}) or not user_selections[chat_id][user_id].get('processing'):
            await safe_telegram_call(message.reply, "No active process.")
            return
        if user_selections[chat_id][user_id].get('status') != 'Waiting for watermark...':
            await safe_telegram_call(message.reply, "Not expecting a watermark input.")
            return
        watermark_text = message.text.strip()
        if not watermark_text:
            await safe_telegram_call(message.reply, "Watermark text cannot be empty.")
            return
        user_selections[chat_id][user_id]['watermark'] = watermark_text
        user_selections[chat_id][user_id]['status'] = "Selecting output format..."
        await safe_telegram_call(
            client.edit_message_text,
            chat_id,
            user_selections[chat_id][user_id]['status_message_id'],
            "Select output format:",
            reply_markup=await create_format_selection_keyboard()
        )
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
    @app.on_callback_query()
    async def handle_callback(client: Client, cq):
        chat_id, user_id = cq.message.chat.id, cq.from_user.id
        if user_id not in user_selections.get(chat_id, {}):
            await cq.answer("This is not your session.", show_alert=True)
            return
        data = cq.data
        status_message_id = user_selections[chat_id][user_id].get('status_message_id')
        if data.startswith("track_"):
            idx = int(data.split("_")[1])
            st = user_selections[chat_id][user_id]['selected_tracks']
            st.remove(idx) if idx in st else st.add(idx)
            tracks = get_audio_tracks(user_selections[chat_id][user_id]['file_path'])
            user_selections[chat_id][user_id]['status'] = "Selecting tracks..."
            await safe_telegram_call(
                client.edit_message_text,
                chat_id,
                status_message_id,
                "Select tracks:",
                reply_markup=await create_track_selection_keyboard(chat_id, user_id, tracks)
            )
        elif data == "done_tracks":
            if not user_selections[chat_id][user_id]['selected_tracks']:
                await safe_telegram_call(cq.message.reply, "Select at least one track.")
                return
            user_selections[chat_id][user_id]['status'] = "Selecting quality..."
            await safe_telegram_call(
                client.edit_message_text,
                chat_id,
                status_message_id,
                "Select video quality:",
                reply_markup=await create_quality_selection_keyboard()
            )
        elif data.startswith("quality_"):
            quality = data.split("_")[1]
            user_selections[chat_id][user_id]['quality'] = quality
            settings = load_watermark_settings(user_id)
            if settings.get('enabled', False) and settings.get('text'):
                user_selections[chat_id][user_id]['watermark'] = settings['text']
                user_selections[chat_id][user_id]['status'] = "Selecting output format..."
                await safe_telegram_call(
                    client.edit_message_text,
                    chat_id,
                    status_message_id,
                    "Select output format:",
                    reply_markup=await create_format_selection_keyboard()
                )
            else:
                user_selections[chat_id][user_id]['status'] = "Waiting for watermark..."
                user_selections[chat_id][user_id]['watermark_timeout'] = asyncio.get_event_loop().time() + 30
                await safe_telegram_call(
                    client.edit_message_text,
                    chat_id,
                    status_message_id,
                    "Reply with your watermark text (e.g., 'ABHI') within 30 seconds or click Skip Watermark.",
                    reply_markup=await create_watermark_prompt()
                )
                asyncio.create_task(watermark_timeout(client, chat_id, user_id, status_message_id))
        elif data == "watermark_text":
            user_selections[chat_id][user_id]['status'] = "Waiting for watermark..."
            user_selections[chat_id][user_id]['watermark_timeout'] = asyncio.get_event_loop().time() + 30
            await safe_telegram_call(
                client.edit_message_text,
                chat_id,
                status_message_id,
                "Reply with your watermark text (e.g., 'ABHI') within 30 seconds or click Skip Watermark.",
                reply_markup=await create_watermark_prompt()
            )
        elif data == "watermark_skip":
            user_selections[chat_id][user_id]['watermark'] = None
            user_selections[chat_id][user_id]['status'] = "Selecting output format..."
            await safe_telegram_call(
                client.edit_message_text,
                chat_id,
                status_message_id,
                "Select output format:",
                reply_markup=await create_format_selection_keyboard()
            )
        elif data.startswith("format_"):
            if user_selections[chat_id][user_id].get('status') == "Processing video...":
                await cq.answer("Video is already being processed. Please wait.", show_alert=True)
                return
            fmt = data.split("_")[1]
            info = user_selections[chat_id][user_id]
            info['output_format'] = fmt
            src = info['file_path']
            outname = info.get('default_name') or f"processed_{user_id}_{os.path.basename(src)}"
            dst = os.path.join(DOWNLOAD_DIR, sanitize_filename(outname))
            if fmt == "mkv": dst = os.path.splitext(dst)[0] + ".mkv"
            thumb = os.path.join(DOWNLOAD_DIR, f"{os.path.splitext(outname)[0]}.jpg")
            info['status'] = "Processing video..."
            await safe_telegram_call(client.edit_message_text, chat_id, status_message_id, "Processing video...")

            async def process_with_timeout():
                try:
                    # Run processing in a task with a 5-minute timeout
                    await asyncio.wait_for(
                        process_video_task(client, chat_id, user_id, src, dst, thumb, fmt, info, status_message_id),
                        timeout=300  # 5 minutes
                    )
                except asyncio.TimeoutError:
                    logger.error(f"Processing timed out for user {user_id}")
                    info['status'] = "Processing timed out"
                    await safe_telegram_call(client.edit_message_text, chat_id, status_message_id, "Processing timed out. Please try again.")
                    await cleanup_files([src, dst, thumb])
                    info['processing'] = False
                    if 'file_path' in info:
                        del info['file_path']
                except Exception as e:
                    logger.error(f"Processing failed for user {user_id}: {str(e)}")
                    info['status'] = f"Processing failed: {str(e)}"
                    await safe_telegram_call(client.edit_message_text, chat_id, status_message_id, f"Processing failed: {str(e)}")
                    await cleanup_files([src, dst, thumb])
                    info['processing'] = False
                    if 'file_path' in info:
                        del info['file_path']
                finally:
                    if info.get('queue'):
                        nxt = info['queue'].pop(0)
                        await handle_message(client, nxt)

            async def process_video_task(client, chat_id, user_id, src, dst, thumb, fmt, info, status_message_id):
                try:
                    select_audio_tracks(src, dst, list(info['selected_tracks']), fmt, quality=info.get('quality', 'medium'), watermark=info.get('watermark'), user_id=user_id)
                    generate_thumbnail(src, thumb)
                    cap = info.get('default_caption', "Here is your video.")
                    info['status'] = "Uploading video..."
                    await safe_telegram_call(client.edit_message_text, chat_id, status_message_id, "Uploading video...")
                    success = await upload_with_progress(client, chat_id, user_id, dst, cap, fmt, thumb, reply_to_message_id=info.get('original_message_id'))
                    if success:
                        info['status'] = "Completed"
                        await safe_telegram_call(client.edit_message_text, chat_id, status_message_id, "Completed")
                        await safe_telegram_call(cq.message.delete)
                    else:
                        info['status'] = "Upload failed"
                        await safe_telegram_call(client.edit_message_text, chat_id, status_message_id, "Upload failed. Please try again.")
                    await cleanup_files([src, dst, thumb])
                    info['processing'] = False
                    if 'file_path' in info:
                        del info['file_path']
                except Exception as e:
                    raise

            asyncio.create_task(process_with_timeout())
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
    async def watermark_timeout(client: Client, chat_id: int, user_id: int, status_message_id: int):
        try:
            await asyncio.sleep(30)
            if user_selections.get(chat_id, {}).get(user_id, {}).get('status') == "Waiting for watermark...":
                user_selections[chat_id][user_id]['watermark'] = None
                user_selections[chat_id][user_id]['status'] = "Selecting output format..."
                await safe_telegram_call(
                    client.edit_message_text,
                    chat_id,
                    status_message_id,
                    "Watermark input timed out. Select output format:",
                    reply_markup=await create_format_selection_keyboard()
                )
        except Exception as e:
            logger.error(f"Watermark timeout failed: {str(e)}")

# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
