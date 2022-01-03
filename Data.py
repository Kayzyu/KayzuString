from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Halo {}

Selamat datang {}

Jika kamu tidak percaya bot ini, 
1) gausah baca pesan ini
2) blokir bot atau delete chat

Bot ini Bekerja Untuk Membantu Kamu Mendapatkan String Session Via Bot. Rekomendasi Jika Ingin Mengambil String Gunakan Akun Lain, Agar Tidak Delay. Terimakasih
By @Kayzuuuuu
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("💥ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ💥​", callback_data="generate")],
        [InlineKeyboardButton(text="ʙᴀᴄᴋ​", callback_data="home")]
    ]
    
    generate_button = [
        [InlineKeyboardButton("ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱɪᴏɴ🔥", callback_data="generate")],
       
            [InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ᴍᴇ​​", callback_data="help")],
            [InlineKeyboardButton("ᴀʙᴏᴜᴛ​", callback_data="about")],
        [InlineKeyboardButton("ɪɴꜰᴏ ʙᴏᴛ ʟᴀɪɴɴʏᴀ​", url="https://t.me/KayzuSupport")],
    ]

    # Helpl

    # About Message
    ABOUT = """
**About This Bot** 

Sebuah telegram bot untuk mengambil pyrogram dan telethon string session by @KayzuStringBot

Group Support : [Gabung](https://t.me/KayzuSupport)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @Kayzuuuuu
    """
