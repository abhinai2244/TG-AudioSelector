from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import logging
import asyncio
import json
import os
from utils import load_watermark_settings, save_watermark_settings, safe_telegram_call

logger = logging.getLogger(__name__)

WATERMARK_SETTINGS_FILE = "watermark_settings.json"

def register_us_handlers(app: Client):
    @app.on_message(filters.command("us"))
    async def handle_us_command(client: Client, message):
        chat_id, user_id = message.chat.id, message.from_user.id
        settings = load_watermark_settings(user_id)
        toggle_status = "ON" if settings.get('enabled', False) else "OFF"
        watermark_text = settings.get('text', 'None')
        position = settings.get('position', 'left_top').replace('_', ' ').title()
        font_size = settings.get('font_size', 24)
        font_size_label = {16: 'Small', 24: 'Medium', 32: 'Large'}.get(font_size, 'Medium')
        status_message = (
            f"Watermark Settings for @{message.from_user.username or message.from_user.first_name}:\n"
            f"Toggle: {toggle_status}\n"
            f"Text: {watermark_text}\n"
            f"Position: {position}\n"
            f"Font Size: {font_size_label}"
        )
        await safe_telegram_call(
            message.reply,
            status_message,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Configure Watermark", callback_data="watermark_config")]
            ])
        )

    @app.on_callback_query(filters.regex(r"^(watermark_|position_|font_size_)"))
    async def handle_watermark_callback(client: Client, cq):
        chat_id, user_id = cq.message.chat.id, cq.from_user.id
        data = cq.data
        settings = load_watermark_settings(user_id)
        toggle_status = "ON" if settings.get('enabled', False) else "OFF"
        watermark_text = settings.get('text', 'None')
        position = settings.get('position', 'left_top').replace('_', ' ').title()
        font_size = settings.get('font_size', 24)
        font_size_label = {16: 'Small', 24: 'Medium', 32: 'Large'}.get(font_size, 'Medium')

        try:
            if data == "watermark_config":
                await safe_telegram_call(
                    client.edit_message_text,
                    chat_id,
                    cq.message.id,
                    (
                        f"Watermark Settings:\n"
                        f"Toggle: {toggle_status}\n"
                        f"Text: {watermark_text}\n"
                        f"Position: {position}\n"
                        f"Font Size: {font_size_label}\n\n"
                        f"Select an option:"
                    ),
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("Watermark Text", callback_data="watermark_text")],
                        [InlineKeyboardButton("Position", callback_data="watermark_position")],
                        [InlineKeyboardButton("Font Size", callback_data="watermark_font_size")],
                        [InlineKeyboardButton(f"Toggle Watermark ({toggle_status})", callback_data="watermark_toggle")]
                    ])
                )
            elif data == "watermark_text":
                settings['awaiting_text'] = True
                save_watermark_settings(user_id, settings)
                await safe_telegram_call(
                    client.edit_message_text,
                    chat_id,
                    cq.message.id,
                    "Reply with your watermark text (e.g., 'ABHI') within 30 seconds.",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("Cancel", callback_data="watermark_config")]
                    ])
                )
                asyncio.create_task(watermark_text_timeout(client, chat_id, user_id, cq.message.id))
            elif data == "watermark_position":
                await safe_telegram_call(
                    client.edit_message_text,
                    chat_id,
                    cq.message.id,
                    "Select watermark position:",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("Left Top", callback_data="position_left_top")],
                        [InlineKeyboardButton("Right Top", callback_data="position_right_top")],
                        [InlineKeyboardButton("Left Bottom", callback_data="position_left_bottom")],
                        [InlineKeyboardButton("Right Bottom", callback_data="position_right_bottom")],
                        [InlineKeyboardButton("Back", callback_data="watermark_config")]
                    ])
                )
            elif data == "watermark_font_size":
                await safe_telegram_call(
                    client.edit_message_text,
                    chat_id,
                    cq.message.id,
                    "Select font size:",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("Small", callback_data="font_size_16")],
                        [InlineKeyboardButton("Medium", callback_data="font_size_24")],
                        [InlineKeyboardButton("Large", callback_data="font_size_32")],
                        [InlineKeyboardButton("Back", callback_data="watermark_config")]
                    ])
                )
            elif data == "watermark_toggle":
                settings['enabled'] = not settings.get('enabled', False)
                save_watermark_settings(user_id, settings)
                toggle_status = "ON" if settings['enabled'] else "OFF"
                await safe_telegram_call(
                    client.edit_message_text,
                    chat_id,
                    cq.message.id,
                    (
                        f"Watermark Settings:\n"
                        f"Toggle: {toggle_status}\n"
                        f"Text: {watermark_text}\n"
                        f"Position: {position}\n"
                        f"Font Size: {font_size_label}\n\n"
                        f"Watermark {'enabled' if settings['enabled'] else 'disabled'}. Select an option:"
                    ),
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("Watermark Text", callback_data="watermark_text")],
                        [InlineKeyboardButton("Position", callback_data="watermark_position")],
                        [InlineKeyboardButton("Font Size", callback_data="watermark_font_size")],
                        [InlineKeyboardButton(f"Toggle Watermark ({toggle_status})", callback_data="watermark_toggle")]
                    ])
                )
            elif data.startswith("position_"):
                position = data.split("_", 1)[1]
                settings['position'] = position
                save_watermark_settings(user_id, settings)
                position = position.replace('_', ' ').title()
                await safe_telegram_call(
                    client.edit_message_text,
                    chat_id,
                    cq.message.id,
                    (
                        f"Watermark Settings:\n"
                        f"Toggle: {toggle_status}\n"
                        f"Text: {watermark_text}\n"
                        f"Position: {position}\n"
                        f"Font Size: {font_size_label}\n\n"
                        f"Position updated. Select an option:"
                    ),
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("Watermark Text", callback_data="watermark_text")],
                        [InlineKeyboardButton("Position", callback_data="watermark_position")],
                        [InlineKeyboardButton("Font Size", callback_data="watermark_font_size")],
                        [InlineKeyboardButton(f"Toggle Watermark ({toggle_status})", callback_data="watermark_toggle")]
                    ])
                )
            elif data.startswith("font_size_"):
                font_size = int(data.split("_")[-1])
                settings['font_size'] = font_size
                save_watermark_settings(user_id, settings)
                font_size_label = {16: 'Small', 24: 'Medium', 32: 'Large'}.get(font_size, 'Medium')
                await safe_telegram_call(
                    client.edit_message_text,
                    chat_id,
                    cq.message.id,
                    (
                        f"Watermark Settings:\n"
                        f"Toggle: {toggle_status}\n"
                        f"Text: {watermark_text}\n"
                        f"Position: {position}\n"
                        f"Font Size: {font_size_label}\n\n"
                        f"Font size updated. Select an option:"
                    ),
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("Watermark Text", callback_data="watermark_text")],
                        [InlineKeyboardButton("Position", callback_data="watermark_position")],
                        [InlineKeyboardButton("Font Size", callback_data="watermark_font_size")],
                        [InlineKeyboardButton(f"Toggle Watermark ({toggle_status})", callback_data="watermark_toggle")]
                    ])
                )
        except Exception as e:
            logger.error(f"Callback handling failed for {data}: {str(e)}")
            await cq.answer(f"Error: {str(e)}", show_alert=True)

    @app.on_message(filters.text & filters.reply)
    async def handle_watermark_text(client: Client, message: Message):
        chat_id, user_id = message.chat.id, message.from_user.id
        settings = load_watermark_settings(user_id)
        if not settings.get('awaiting_text', False):
            await safe_telegram_call(message.reply, "Not expecting a watermark input.")
            return
        watermark_text = message.text.strip()
        if not watermark_text:
            await safe_telegram_call(message.reply, "Watermark text cannot be empty.")
            return
        settings['text'] = watermark_text
        settings['awaiting_text'] = False
        save_watermark_settings(user_id, settings)
        toggle_status = "ON" if settings.get('enabled', False) else "OFF"
        position = settings.get('position', 'left_top').replace('_', ' ').title()
        font_size = settings.get('font_size', 24)
        font_size_label = {16: 'Small', 24: 'Medium', 32: 'Large'}.get(font_size, 'Medium')
        await safe_telegram_call(
            client.edit_message_text,
            chat_id,
            message.reply_to_message.id,
            (
                f"Watermark Settings:\n"
                f"Toggle: {toggle_status}\n"
                f"Text: {watermark_text}\n"
                f"Position: {position}\n"
                f"Font Size: {font_size_label}\n\n"
                f"Watermark text updated. Select an option:"
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Watermark Text", callback_data="watermark_text")],
                [InlineKeyboardButton("Position", callback_data="watermark_position")],
                [InlineKeyboardButton("Font Size", callback_data="watermark_font_size")],
                [InlineKeyboardButton(f"Toggle Watermark ({toggle_status})", callback_data="watermark_toggle")]
            ])
        )

    async def watermark_text_timeout(client: Client, chat_id: int, user_id: int, message_id: int):
        """Handle watermark text input timeout after 30 seconds."""
        try:
            await asyncio.sleep(30)
            settings = load_watermark_settings(user_id)
            if settings.get('awaiting_text', False):
                settings['awaiting_text'] = False
                save_watermark_settings(user_id, settings)
                toggle_status = "ON" if settings.get('enabled', False) else "OFF"
                watermark_text = settings.get('text', 'None')
                position = settings.get('position', 'left_top').replace('_', ' ').title()
                font_size = settings.get('font_size', 24)
                font_size_label = {16: 'Small', 24: 'Medium', 32: 'Large'}.get(font_size, 'Medium')
                await safe_telegram_call(
                    client.edit_message_text,
                    chat_id,
                    message_id,
                    (
                        f"Watermark Settings:\n"
                        f"Toggle: {toggle_status}\n"
                        f"Text: {watermark_text}\n"
                        f"Position: {position}\n"
                        f"Font Size: {font_size_label}\n\n"
                        f"Watermark text input timed out. Select an option:"
                    ),
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("Watermark Text", callback_data="watermark_text")],
                        [InlineKeyboardButton("Position", callback_data="watermark_position")],
                        [InlineKeyboardButton("Font Size", callback_data="watermark_font_size")],
                        [InlineKeyboardButton(f"Toggle Watermark ({toggle_status})", callback_data="watermark_toggle")]
                    ])
                )
        except Exception as e:
            logger.error(f"Watermark text timeout failed: {str(e)}")