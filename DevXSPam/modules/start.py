from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("• ᴄᴏᴍᴍᴀɴᴅs •", data="help_back")
    ],
    [
        Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/The_Radiux_Network"),
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/Radiux_Support")
    ],
    [
        Button.url("• sᴏᴜʀᴄᴇ •", "https://te.legra.ph/file/2e1ae025e30642b4efe9c.jpg")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"➥ **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [𝐑ᴀᴅɪᴜx](https://t.me/The_RealRadiux)**\n\n"
        TEXT += f"➥ **𝐑ᴀᴅɪᴜx-𝐒ᴘᴀᴍ ᴠᴇʀsɪᴏɴ :** `M3.3`\n"
        TEXT += f"➥ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `3.11.3`\n"
        TEXT += f"➥ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                    event.chat_id,
                    "https://graph.org/file/b777cdffcd91feee7c328.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
                )
