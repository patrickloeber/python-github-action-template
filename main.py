from pyrogram import Client, filters
from pyrogram import enums


api_id = 23136380
api_hash = "6ae6541159e229499615953de667675c"

#---------config--------------#
tagchaneel = "-1002008420751"
idchannel = "-1002008420751"
channel = [-1002008420751]
#-----------------------------#

app = Client("copy" , api_id , api_hash)

@app.on_message(filters.text & filters.me)
async def mes_handler(client, message):

    chatid = message.chat.id
    text = message.text

    if text == "help":
        await message.reply_text('`انلاینم!🦦`')

@app.on_message(filters.text & filters.chat(channel))
async def mes_handler(client, message):

    chatid = message.chat.id
    text = message.text

    if 'vlass://' in text or 'vmess://' in text or 'ss://' in text or  'trojan://' in text:
        text1 = '`{text}`' + '\n' + tagchaneel
        await app.send_message(idchannel, text)





app.run()
