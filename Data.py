from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

You can use me to generate pyrogram and telethon string session. Use the below buttons to know more!
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("⚜ Start Generating Session ⚜", callback_data="generate")],
        [InlineKeyboardButton(text=" Return Home ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton(" Start Generating Session ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton(" Start Generating Session ", callback_data="generate")],
        [InlineKeyboardButton(" Support Chat ", url="https://t.me/Official_LegendBot")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton(" About", callback_data="about")
        ],
        [InlineKeyboardButton("🇮🇳 Owner 🇮🇳", url="https://t.me/The_LegendBoy")],
    ]

    # Help Message
    HELP = """
» Click the below button or use /generate command to start generating session!
» Click the required button; [Pyrogram/Telethon]
» Enter the required variables when asked.
"""

    # About Message
    ABOUT = """
**About Me** 

A telegram bot to generate pyrogram and telethon string session...

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)
"""
