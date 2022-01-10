from pydub import AudioSegment
import os, time, glob, datetime
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import PTN
import shutil


folder = 'C:/Users/Administrator/Downloads/Telegram Desktop'
msgid = 0
chatid = 0
vdir = folder + '/*'
a1 = '1.mp3'
a2 = '2.mp3'
a3 = '3.mp3'
a6 = '6.mp3'
aac = 'a2.aac'
main = folder.rsplit('/', 1)[1] + '\\'


def gettime(t2):
    try:
        tt2 = t2.split('.')[1]
        t2 = t2.split('.')[0]
        t2 = f'0{t2[:1]}:{t2[:3][1:]}:{t2[3:]}'
    except:
        tt2 = None
        t2 = f'0{t2[:1]}:{t2[:3][1:]}:{t2[3:]}'
    t2 = sum(x * int(t) for x, t in zip([1, 60, 3600], reversed(t2.split(":"))))
    if tt2 != None:
        t2 = f'{t2}{tt2[:1]}00'
    else:
        t2 = f'{t2}000'
    return t2

@bot.on_message(filters.text & filters.regex('/voicetag'))
async def start(bot, m):
    keyboard = []
    keyboard.append(refresh_button)
    try:
        for file in glob.glob(vdir):
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

@bot.on_message(filters.audio | filters.video | filters.document)
async def callback(bot, m):
    if not os.path.isdir('temp/'):
        os.makedirs('temp/')
    file = await bot.download_media(message=m, file_name='temp/')
    media = m.audio or m.video or m.document
    vname = media.file_name
    try:
        await m.reply("downloading..")
        #v = folder + '/' + vname
        #vname = vname.replace('.ts', '.mp4')
        
        n = PTN.parse(vname)
        title = n['title'].replace("-", " ")
        au2_1 = f'C:/All Projact Primer Pro/Audio Sound Serial Primer Pro Tag/{title}/2.1.mp3'
        
        t2t = await m.reply_text('تایم صوت 2 (2.2 + 2.1) رو بفرست')
        t22: Message = await bot.listen(m.chat.id, filters=filters.text)
        t3t = await m.reply_text('تایم صوت 3 رو بفرست\n3.mp3')
        t33: Message = await bot.listen(m.chat.id, filters=filters.text)
        t6t = await m.reply_text('تایم صوت 6 رو بفرست\n6.mp3')
        t66: Message = await bot.listen(m.chat.id, filters=filters.text)
        t2 = int(gettime(t22.text))
        t3_1, t3_2, t3_3, t3_4, t3_5 = t33.text.split()
        t3_1 = int(gettime(t3_1))
        t3_2 = int(gettime(t3_2))
        t3_3 = int(gettime(t3_3))
        t3_4 = int(gettime(t3_4))
        t3_5 = int(gettime(t3_5))
        t6 = int(gettime(t66.text))
        os.system(f'ffmpeg -i "{au2_1}" -i 2.2.mp3 -y 2.mp3')
        os.system(f'ffmpeg -i "{file}" -vn -i {a1} -vn -i {a2} -vn -i {a3} -vn -i {a6} -vn -filter_complex "[1]adelay=00000|00000[b]; [2]adelay={t2}|{t2}[c]; [3]adelay={t3_1}|{t3_1}[d]; [3]adelay={t3_2}|{t3_2}[e]; [3]adelay={t3_3}|{t3_3}[f]; [3]adelay={t3_4}|{t3_4}[g]; [3]adelay={t3_5}|{t3_5}[h]; [4]adelay={t6}|{t6}[i]; [0][b][c][d][e][f][g][h][i]amix=9" -c:a aac -b:a 125k -y {aac}')   
        time.sleep(10)
        #os.system(f'ffmpeg -i "{file}" -i {aac} -c copy -map 0:0 -map 1:0 -y "{vname}"')
        await m.reply_audio(audio=aac)
        try:
            os.remove(file)
        except:
            pass
    except Exception as e:
        print(e)

bot.run()
