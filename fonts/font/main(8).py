import os, datetime, glob
from pyrogram import Client, filters
from pyromod import listen
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata



previous_cut_time = '00:00:00 02:00:04'


if 'BOT_TOKEN' in os.environ:
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    API_ID = os.environ.get("API_ID")
    API_HASH = os.environ.get("API_HASH")
else:
    BOT_TOKEN = "5011115624:AAHVeC2gYJDLzx94CYSmAHvSGJ2RYM4CFzE"
    API_ID = "4328913"
    API_HASH = "3230ec801f78a517c9a2ad6bebb7f7b4"


Bot = Client(
    ":memory:",
    bot_token = BOT_TOKEN,
    api_id = API_ID,
    api_hash = API_HASH
)

refresh_button = [
    InlineKeyboardButton(
        text='Refresh List',
        callback_data='refresh'
    )
]

msgid = 0
chatid = 0
@Bot.on_message(filters.text)
async def start(bot, m):
    keyboard = []
    keyboard.append(refresh_button)
    try:
        for file in glob.glob('C:/dlmacvin/1aa/*'):
            keyboard.append(
                [
                    InlineKeyboardButton(
                        text=file.rsplit('/', 1)[1].replace('1aa\\', ''),
                        callback_data=file.rsplit('/', 1)[1].replace('1aa\\', '')
                    )
                ]
            )
    except Exception as e:
        print(e)
        return
    keyboard.append(refresh_button)
    #await bot.send_message(chat_id=id, text="Which one?", reply_markup=InlineKeyboardMarkup(keyboard))
    await m.reply_text(text="Which one?", reply_markup=InlineKeyboardMarkup(keyboard))


@Bot.on_callback_query()
async def callback(bot, update):
    global chatid
    global msgid
    global previous_cut_time
    if update.data == "refresh":
        keyboard = []
        keyboard.append(refresh_button)
        try:
            for file in glob.glob('C:/dlmacvin/1aa/*'):
                keyboard.append(
                    [
                        InlineKeyboardButton(
                            text=file.rsplit('/', 1)[1].replace('1aa\\', ''),
                            callback_data=file.rsplit('/', 1)[1].replace('1aa\\', '')
                        )
                    ]
                )
        except Exception as e:
            print(e)
            return
        keyboard.append(refresh_button)
        await update.message.edit(text="Which one?", reply_markup=InlineKeyboardMarkup(keyboard))
        return
    try:
        for file in glob.glob('C:/dlmacvin/1aa/*'):
            if file.rsplit('/', 1)[1].replace('1aa\\', '') == update.data:
                name = file.rsplit('/', 1)[1].replace('1aa\\', '')
                input = 'C:/dlmacvin/1aa/' + name
                metadata = extractMetadata(createParser(input))
                duration = metadata.get('duration').seconds
                dtime = str(datetime.datetime.fromtimestamp(duration)+datetime.timedelta(hours=0)).split(' ')[1][:12]
                ask = await update.message.reply_text(f'تایم کل ویدیو : {dtime} \n\nجهت کات ویدیو تایم را به این صورت ارسال کنید \n 00:00:00 02:10:00 \n\nOr send /previous to keep the previous cut time.')
                time: Message = await bot.listen(update.message.chat.id, filters=filters.text)
                if time.text == "/previous":
                    start, end = previous_cut_time.split()
                else:
                    start, end = time.text.split()
                    previous_cut_time = f'{start} {end}'
                await time.delete(True)
                await ask.delete()
                process_msg = await update.message.reply_text('Processing..')
                ext = '.' + file.rsplit('.', 1)[1]
                end_sec = sum(x * int(t) for x, t in zip([1, 60, 3600], reversed(end.split(":"))))
                os.system(f'''ffmpeg -ss {start} -i "{input}" -to {end} -c copy "C:/dlmacvin/1aa/videos/{name.replace(ext, '-0'+ext)}"''')
                cut_steps = []
                dif = duration - int(end_sec)
                for i in range(dif // 10):
                    cut_steps.append(i * 10)
                #cut_steps.append(duration)
                for step in cut_steps:
                    stp = str(end_sec + step)
                    os.system(f'''ffmpeg -ss {start} -i "{input}" -to {stp} -c copy "C:/dlmacvin/1aa/videos/{name.replace(ext, '-'+str(step/10)+ext)}"''')
                await process_msg.delete()
                if chatid == 0:
                    msg = await update.message.reply_text('Done! ' + name)
                    msgid = msg.message_id
                elif chatid != 0:
                    try:
                        await bot.edit_message_text(update.message.chat.id, msgid, 'Done! ' + name)
                    except:
                        await bot.edit_message_text(update.message.chat.id, msgid, 'تمام')
                chatid = update.message.from_user.id
    except:
        pass



Bot.run()
