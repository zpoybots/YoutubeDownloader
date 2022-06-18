from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/teamosmani"), InlineKeyboardButton("Creator", url="https://telegram.me/ribajosmani") ],
        [InlineKeyboardButton(
            "🍿 Source Code 🍿", url="https://github.com/Ribaj")]
    ])
    welcomed = f"""Hey <b>{message.from_user.first_name}</b>\nA Simple YouTube Downloader Bot that can:
  ➠Muuqaalada YouTube Kala Dag Adigoo Linkga Past Ku dhaheysid.
  ➠ Download YouTube videos
  ➠ Download audio from YouTube videos \n\n Made with ♥️ by @ribajosmani"""
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
