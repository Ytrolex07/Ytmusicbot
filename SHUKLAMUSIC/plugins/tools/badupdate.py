from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from SHUKLAMUSIC import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


app.on_message(
    filters.command("repo")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/2b077dc425b6e994300cf.jpg",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐕2 𝐌ᴜsɪᴄ 𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/Ytrolex07/Ytmusicbot/fork")
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐂ʜᴀᴛ 𝐁ᴏᴛ 𝐑ᴇᴘᴏ  🗡️", url=f"https://github.com/Ytrolex07/Ytmusicbot/fork")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐕1 𝐌ᴜsɪᴄ 𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/Ytrolex07/Ytmusicbot/fork")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐒ᴘᴀᴍ  𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/Ytrolex07/Ytmusicbot/fork")
                 ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/2b077dc425b6e994300cf.jpg",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐕2 𝐌ᴜsɪᴄ 𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/Ytrolex07/Ytmusicbot/fork")
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐂ʜᴀᴛ 𝐁ᴏᴛ 𝐑ᴇᴘᴏ  🗡️", url=f"https://github.com/Ytrolex07/Ytmusicbot/fork")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐕1 𝐌ᴜsɪᴄ 𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/Ytrolex07/Ytmusicbot/fork")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐒ᴘᴀᴍ  𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/Ytrolex07/Ytmusicbot/fork")
                 ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.private)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/2b077dc425b6e994300cf.jpg",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐕2 𝐌ᴜsɪᴄ 𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/Ytrolex07/Ytmusicbot/fork")
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐂ʜᴀᴛ 𝐁ᴏᴛ 𝐑ᴇᴘᴏ  🗡️", url=f"https://github.com/Ytrolex07/Ytmusicbot/fork")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐕1 𝐌ᴜsɪᴄ 𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/Ytrolex07/Ytmusicbot/fork")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐒ᴘᴀᴍ  𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/Ytrolex07/Ytmusicbot/fork")
                 ]
            ]
        ),
    )
