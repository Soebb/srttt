
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
        
chnls = "-1001516208383 -1001166919373 -1001437520825 -1001071120514 -1001546442991 -1001322014891 -1001409508844 -1001537554747 -1001462444753 -1001146657589 -1001592624165 -1001588137496"
CHANNELS = set(int(x) for x in chnls.split())
   
@Client.on_message((filters.video | filters.document) & filters.channel & ~filters.edited)
async def caption(bot, message):
    media = message.video or message.document
    
    if (message.chat.id == -1001516208383) and (media is not None) and (media.file_name is not None):
        await message.edit(f"{media.file_name.replace('.mp4', '').replace('.mkv', '').replace('.webm', '')}\n\n🆔👉 @dlmacvin_music")
        return
    if (media is not None) and (media.file_name is not None):
        m = media.file_name.replace("@turk7media - ", "").replace("@dlmacvin2 - ", "").replace("@dlmacvin - ", "").replace("@dlmacvin_new - ", "").replace("-", " ").replace("HardSub", "Hard-Sub").replace("Hard Sub", "Hard-Sub").replace(".mkv", "").replace(".", " ").replace("_", " ").replace("Hardsub", "Hard-Sub").replace("0p", "0P").replace("Fragmanı", "").replace("mp4", "").replace("Fragmanlarım", "").replace("ı", "i").replace("İ", "I").replace("ö", "o").replace("Ö", "O").replace("Ü", "U").replace("ü", "u").replace("ë", "e").replace("Ë", "E").replace("Ä", "A").replace("ç", "c").replace("Ç", "C").replace("ş", "s").replace("Ş", "S").replace("ğ", "g").replace("Ğ", "G").replace("ä", "a")
        D = m.replace("720P", "").replace("E20", "").replace("E120", "").replace("E220", "").replace("E320", "").replace("E420", "")
        N = m
        Z = media.file_name
        fa = " "
        tz = " "
        Lo = " "
        Q = " "
        Fucc = " "
        E = None
        X = None
        Ee = None
        if "Sen Cal Kapimi" in m:
            fa += "#تو_در_خانه_ام_را_بزن"
            X = "Sen Cal Kapimi"
        if "Dokhtarane Gol Foroosh" in m:
            fa += "#دختران_گل_فروش"
            X = "Dokhtarane Gol Foroosh"
        if "Marasli" in m:
            fa += "#اهل_ماراش"
            X = "Marasli"
        if "Kalp Yarasi" in m:
            fa += "#زخم_قلب"
            X = "Kalp Yarasi"
        if "Dunya Hali" in m:
            fa += "#احوال_دنیایی"
            X = "Dunya Hali"
        if "Ver Elini Ask" in m:
            fa += "#دستت_را_بده_عشق"
            X = "Ver Elini Ask"
        if "Ezel" in m:
            fa += "#ایزل"
            X = "Ezel"
        if "Ikimizin Sirri" in m:
            fa += "#راز_ما_دو_نفر"
            X = "Ikimizin Sirri"
        if "Dirilis Ertugrul" in m:
            fa += "#قیام_ارطغرل"
            X = "Dirilis Ertugrul"
        if "Yemin" in m:
            fa += "#قسم"
            X = "Yemin"
        
        if "Ask i Memnu" in m:
            fa += "#عشق_ممنوع"
            X = "Ask i Memnu"
        if "Bozkir Arslani Celaleddin" in m:
            fa += "#جلال_الدین_خوارزمشاهی"
            X = "Bozkir Arslani Celaleddin"
        if "Kazara Ask" in m:
            fa += "#عشق_تصادفی"
            X = "Kazara Ask"
        if "Bas Belasi" in m:
            fa += "#بلای_جون"
            X = "Bas Belasi"
        if "Ask Mantik Intikam" in m:
            fa += "#عشق_منطق_انتقام"
            X = "Ask Mantik Intikam"
        if "Baht Oyunu" in m:
            fa += "#بازی_بخت"
            X = "Baht Oyunu"
        if "Ada Masali" in m:
            fa += "#قصه_جزیره"
            X = "Ada Masali"
        if "Askin Tarifi" in m:
            fa += "#طرز_تهیه_عشق"
            X = "Askin Tarifi"
        if "Yesilcam" in m:
            fa += "#سینمای_قدیم_ترکیه"
            X = "Yesilcam"
        if "Camdaki Kiz" in m:
            fa += "#دختر_پشت_پنجره"
            X = "Camdaki Kiz"
        if "Bir Zamanlar Kibris" in m:
            fa += "#روزی_روزگاری_در_قبرس"
            X = "Bir Zamanlar Kibris"
        if "Teskilat" in m:
            fa += "#تشکیلات"
            X = "Teskilat"
        if "Kardeslerim" in m:
            fa += "#خواهر_و_برادرانم"
            X = "Kardeslerim"
        if "Ogrenci Evi" in m:
            fa += "#خانه_دانشجویی"
            X = "Ogrenci Evi"
        if "Sihirli Annem" in m:
            fa += "#مادر_سحرآمیز_من"
            X = "Sihirli Annem"
        if "Yetis Zeynep" in m:
            fa += "#برس_زینب"
            X = "Yetis Zeynep"
        if "Hukumsuz" in m:
            fa += "#بی_قانون"
            X = "Hukumsuz"
        if "Saygi" in m:
            fa += "#احترام"
            X = "Saygi"
        if "Vahsi Seyler" in m:
            fa += "#چیز_های_وحشی"
            X = "Vahsi Seyler"
        if "Seref Bey" in m:
            fa += "#آقای_شرف"
            X = "Seref Bey"
        if "Gibi" in m:
            fa += "#مانند"
            X = "Gibi"
        if "Iste Bu Benim Masalim" in m:
            fa += "#این_داستان_من_است"
            X = "Iste Bu Benim Masalim"
        if "Son Yaz" in m:
            fa += "#آخرین_تابستان"
            X = "Son Yaz"
        if "Akinci" in m:
            fa += "#مهاجم"
            X = "Akinci"
        if "Kirmizi Oda" in m:
            fa += "#اتاق_قرمز"
            X = "Kirmizi Oda"
        if "Emanet" in m:
            fa += "#امانت"
            X = "Emanet"
        if "Ibo Show" in m:
            fa += "#برنامه_ایبو_شو"
            X = "Ibo Show"
        if "EDHO" in m:
            fa += "#راهزنان"
            X = "EDHO"
        if "Uyanis Buyuk Selcuklu" in m:
            fa += "#بیداری_سلجوقیان_بزرگ"
            X = "Uyanis Buyuk Selcuklu"
        if "Yasak Elma" in m:
            fa += "#سیب_ممنوعه"
            X = "Yasak Elma"
        if "Sadakatsiz" in m:
            fa += "#بی_صداقت #بی_وفا"
            X = "Sadakatsiz"
        if "Bir Zamanlar Cukurova" in m:
            fa += "#روزی_روزگاری_چوکورا"
            X = "Bir Zamanlar Cukurova"
        if "Gonul Dagi" in m:
            fa += "#کوه_دل"
            X = "Gonul Dagi"
        if "Ufak Tefek Cinayetler" in m:
            fa += "#خرده_جنایت_ها"
            X = "Ufak Tefek Cinayetler"
        if "Sibe Mamnooe" in m:
            fa += "#سیب_ممنوعه"
            X = "Sibe Mamnooe"
        if "Setare Shomali" in m:
            fa += "#ستاره_شمالی"
            X = "Setare Shomali"
        if "Otaghe Ghermez" in m:
            fa += "#اتاق_قرمز"
            X = "Otaghe Ghermez"
        if "Mojeze Doctor" in m:
            fa += "#دکتر_معجزه_گر"
            X = "Mojeze Doctor"
        if "Mucize Doktor" in m:
            fa += "#دکتر_معجزه_گر"
            X = "Mucize Doktor"
        if "Be Eshghe To Sogand" in m:
            fa += "#به_عشق_تو_سوگند"
            X = "Be Eshghe To Sogand"
        if "Eshgh Az No" in m:
            fa += "#عشق_از_نو"
            X = "Eshgh Az No"
        if "Eshghe Mashroot" in m:
            fa += "#عشق_مشروط"
            X = "Eshghe Mashroot"
        if m.__contains__("Cukurova") and not m.__contains__("Bir"):
            fa += "#روزی_روزگاری_چکوروا"
            X = "Cukurova"
        if "Yek Jonun Yek Eshgh" in m:
            fa += "#یک_جنون_یک_عشق"
            X = "Yek Jonun Yek Eshgh"
        if "2020" in m:
            fa += "#2020"
            X = "2020"
        if "Hekim" in m:
            fa += "#حکیم_اوغلو"
            X = "Hekim"
        if "Godal" in m:
            fa += "#گودال"
            X = "Godal"
        if ("Cukur" in m) and not m.__contains__("Cukurova"):
            fa += "#گودال"
            X = "Cukur"
        if "Khaneh Man" in m:
            fa += "#سرنوشتت_خانه_توست"
            X = "Khaneh Man"
        if "Alireza" in m:
            fa += "#علیرضا"
            X = "Alireza"
        if "Dokhtare Safir" in m:
            fa += "#دختر_سفیر"
            X = "Dokhtare Safir"
        if "Marashli" in m:
            fa += "#ماراشلی - #اهل_ماراش"
            X = "Marashli"
        if "Zarabane Ghalb" in m:
            fa += "#ضربان_قلب"
            X = "Zarabane Ghalb"
        if "Aparteman Bigonahan" in m:
            fa += "#آپارتمان_بی_گناهان"
            X = "Aparteman Bigonahan" 
        if "Hayat Agaci" in m:
            fa += "#درخت_زندگی"
            X = "Hayat Agaci" 
        if "Ruya" in m:
            fa += "#رویا"
            X = "Ruya" 
        if "Uzak Sehrin Masali" in m:
            fa += "#داستان_شهری_دور"
            X = "Uzak Sehrin Masali"
        if "Icimizden Biri" in m:
            fa += "#یکی_از_میان_ما"
            X = "Icimizden Biri"
        if "Kocaman Ailem" in m:
            fa += "#خانواده_بزرگم"
            X = "Kocaman Ailem"
        if "Insanlik Sucu" in m:
            fa += "#جرم_انسانیت"
            X = "Insanlik Sucu"
        if "Tutsak" in m:
            fa += "#اسیر "
            X = "Tutsak"
        if "Fazilet Hanim ve Kızlari" in m:
            fa += "#فضیلت_خانم_و_دخترانش"
            X = "Fazilet Hanim ve Kızlari"
        if "Ferhat Ile Sirin" in m:
            fa += "#فرهاد_و_شیرین"
            X = "Ferhat Ile Sirin"
        if "Gel Dese Ask" in m:
            fa += "#عشق_صدا_میزند"
            X = "Gel Dese Ask"			
        if "Gibi" in m:
            fa += "#مانند"
            X = "Gibi"
        if "Halka" in m:
            fa += "#حلقه"
            X = "Halka"
        if "Hercai" in m:
            fa += "#هرجایی"
            X = "Hercai"
        if "Hizmetciler" in m:
            fa += "#خدمتکاران"
            X = "Hizmetciler"
        if "Istanbullu Gelin" in m:
            fa += "#عروس_استانبولی"
            X = "Istanbullu Gelin"
        if "Kalp Atisi " in m:
            fa += "#ضربان_قلب"
            X = "Kalp Atisi "
        if "Kara Sevda" in m:
            fa += "#کاراسودا #عشق_بی_پایان"
            X = "Kara Sevda"
        if "Kardes Cocuklari" in m:
            fa += "#خواهرزاده_ها"
            X = "Kardes Cocuklari"
        if "Kimse Bilmez" in m:
            fa += "#کسی_نمیداند"
            X = "Kimse Bilmez"
        if "Kursun" in m:
            fa += "#گلوله"
            X = "Kursun"
        if "Kuzey Yildizi Ilk Ask" in m:
            fa += "#ستاره_شمالی_عشق_اول"
            X = "Kuzey Yildizi Ilk Ask"
        if "Kuzgun" in m:
            fa += "#کلاغ #کوزگون"
            X = "Kuzgun"
        if "Meryem" in m:
            fa += "#مریم"
            X = "Meryem"
        if "Muhtesem Ikili" in m:
            fa += "#زوج_طلایی"
            X = "Muhtesem Ikili"
        if "Nefes Nefese" in m:
            fa += "#نفس_زنان"
            X = "Nefes Nefese"
        if "Ogretmen" in m:
            fa += "#معلم"
            X = "Ogretmen"
        if "Olene Kadar" in m:
            fa += "#تا_حد_مرگ"
            X = "Olene Kadar"
        if "Sahsiyet" in m:
            fa += "#شخصیت"
            X = "Sahsiyet"			
        if "Sahin Tepesi" in m:
            fa += "#تپه_شاهین"
            X = "Sahin Tepesi"
        if "Savasci" in m:
            fa += "#جنگجو"
            X = "Savasci"
        if "Sefirin Kizi" in m:
            fa += "#دختر_سفیر"
            X = "Sefirin Kizi"
        if "Sevgili Gecmis" in m:
            fa += "#گذشته_ی_عزیز"
            X = "Sevgili Gecmis"
        if "Sheref Bey" in m:
            fa += "#آقای_شرف"
            X = "Sheref Bey"
        if "Sihirlis Annem" in m:
            fa += "#مادر_جادویی_من"
            X = "Sihirlis Annem"
        if "The Protector" in m:
            fa += "#محافظ"
            X = "The Protector"
        if "Vahsi Seyler" in m:
            fa += "#چیزهای_وحشی"
            X = "Vahsi Seyler"
        if "Vurgun" in m:
            fa += "#زخمی"
            X = "Vurgun"
        if "Ya Istiklal Ya Olum" in m:
            fa += "#یا_استقلال_یا_مرگ"
            X = "Ya Istiklal Ya Olum"
        if ("Yalanci" in m) and not m.__contains__("Yalancilar ve Mumlari"):
            fa += "#دروغگو"
            X = "Yalanci"
        if "El Kizi" in m:
            fa += "#دختر_مردم"
            X = "El Kizi"
        if "Masumlar Apartmani" in m:
            fa += "#آپارتمان_بیگناهان"
            X = "Masumlar Apartmani"
        if "Yalancilar ve Mumlari" in m:
            fa += "#دروغگو_ها_و_شمع_هایشان"
            X = "Yalancilar ve Mumlari"
        if "Lise Devriyesi" in m:
            fa += "#گشت_مدرسه"
            X = "Lise Devriyesi"
        if "Evlilik Hakkinda Her Sey" in m:
            fa += "#همه_چیز_درباره_ازدواج"
            X = "Evlilik Hakkinda Her Sey"
        if "Son Yaz" in m:
            fa += "#آخرین_تابستان"
            X = "Son Yaz"
        if "Barbaroslar Akdenizin Kilici" in m:
            fa += "#بارباروس_ها_شمشیر_دریای_مدیترانه"
            X = "Barbaroslar Akdenizin Kilici"
        if "Bir Ask Hikayesi" in m:
            fa += "#حکایت_یک_عشق"
            X = "Bir Ask Hikayesi"
        if "Carpisma" in m:
            fa += "#تصادف"
            X = "Carpisma"
        if "Cocuk" in m:
            fa += "#بچه"
            X = "Cocuk"
        if "Lise Devriyesi" in m:
            fa += "#گشت_مدرسه"
            X = "Lise Devriyesi"
        if "Kurulus Osman" in m:
            fa += "#قیام_عثمان"
            X = "Kurulus Osman"
        if "Kanunsuz Topraklar" in m:
            fa += "#سرزمین_های_بی_قانون"
            X = "Kanunsuz Topraklar"

			
        if Z.__contains__("Fragman") or m.__contains__("Bolum") or m.__contains__("bolum") or Z.__contains__("fragman"):
            if " Bolum" in m:
                bul = " Bolum"
            elif " bolum" in m:
                bul = " bolum"
            elif not m.__contains__(" Bolum") and not m.__contains__(" bolum"):
                if "Bolum" in m:
                    bul = "Bolum"
                elif "bolum" in m:
                    bul = "bolum"
            Jn = m.split(f"{bul}")[1]
            if "2" in Jn:
                tz += "#دوم"
            elif "1" in Jn:
                tz += "#اول"
            elif "3" in Jn:
                tz += "#سوم"
            elif "4" in Jn:
                tz += "#چهارم"
            elif "5" in Jn:
                tz += "#پنجم"
            elif "6" in Jn:
                tz += "#ششم"
            if X is None:
                Ghi = m.split(f"{bul}")[-2]
                X = Ghi.rsplit(' ', 1)[0]
                Ee = Ghi.rsplit(' ', 1)[1]
                
                print(f"X = {X}")
                
                print(f"Ee = {Ee}")
                # X = X.replace(' ', '_')
                # if X.startswith("_"):
                    # X = X.split("_", 1)[1]
                Lo += f"#{X.replace(' ', '_')}"
            # if (X is not None) and (X.__contains__("a") or X.__contains__("o") or X.__contains__("i") or X.__contains__("c") or X.__contains__("b") or X.__contains__("e") or X.__contains__("l") or X.__contains__("n") or X.__contains__("m")):
            else:
                Yd = X.replace(" ", "_")
                Lo += "#" + f"{Yd}"
                V = m.replace(f"{X}", "")
                Ee = V.split(f"{bul}", -1)[0]
            
            Tzz = tz.replace("#", "")
            date = " "

            if "Ask Mantik Intikam" in m:
                date += "شنبه ساعت 2:30 بامداد از رسانه اینترنتی دی ال مکوین"
            if "Kirmizi Oda" in m:
                date += "شنبه از رسانه اینترنتی دی ال مکوین"
            if "Son Yaz" in m:
                date += "یکشنبه از رسانه اینترنتی دی ال مکوین"
            if "Kardeslerim" in m:
                date += "یکشنبه ساعت 2:30 بامداد از رسانه اینترنتی دی ال مکوین"
            if "Yalancilar ve Mumlari" in m:
                date += "یکشنبه ساعت 2:30 از رسانه اینترنتی دی ال مکوین"
            if "Teskilat" in m:
                date += "دو شنبه از رسانه اینترنتی دی ال مکوین"
            if "Gonul Dagi" in m:
                date += "دو شنبه از رسانه اینترنتی دی ال مکوین"
            if "Ikimizin Sirri" in m:
                date += "دو شنبه از رسانه اینترنتی دی ال مکوین"
            if "Yargi" in m:
                date += "دو شنبه از رسانه اینترنتی دی ال مکوین"
            if ("Yalanci" in m) and not m.__contains__("Yalancilar ve Mumlari"):
                date += "شنبه از رسانه اینترنتی دی ال مکوین"
            if "Ada Masali" in m:
                date += "چهار شنبه ساعت 2:30 بامداد از رسانه اینترنتی دی ال مکوین"
            if "Baht Oyunu" in m:
                date += "چهار شنبه ساعت 2:30 بامداد از رسانه اینترنتی دی ال مکوین"
            if "Evlilik Hakkinda Her Sey" in m:
                date += "چهار شنبه از رسانه اینترنتی دی ال مکوین"
            if "Icimizden Biri" in m:
                date += "چهار شنبه از رسانه اینترنتی دی ال مکوین"
            if "Masumlar Apartmani" in m:
                date += "چهار شنبه از رسانه اینترنتی دی ال مکوین"
            if "Sadakatsiz" in m:
                date += "پنج شنبه از رسانه اینترنتی دی ال مکوین"
            if "Kurulus Osman" in m:
                date += "پنج شنبه ساعت 2:30 بامداد از رسانه اینترنتی دی ال مکوین"
            if "Kanunsuz Topraklar" in m:
                date += "پنج شنبه از رسانه اینترنتی دی ال مکوین"
            if "Dunya Hali" in m:
                date += "پنج شنبه از رسانه اینترنتی دی ال مکوین"
            if "Yasak Elma" in m:
                date += "سه شنبه ساعت 2:30 بامداد از رسانه اینترنتی دی ال مکوین"
            if "Sen Cal Kapimi" in m:
                date += "پنجشنبه ساعت 2:30 بامداد از رسانه اینترنتی دی ال مکوین"
            if "Kalp Yarasi" in m:
                date += "سه شنبه ساعت 2:30 بامداد از رسانه اینترنتی دی ال مکوین"
            if "Bir Zamanlar Cukurova" in m:
                date += "جمعه ساعت 2:30 بامداد از رسانه اینترنتی دی ال مکوین"
            if "Barbaroslar Akdeniz'in Kılıcı" in m:
                date += "جمعه از رسانه اینترنتی دی ال مکوین"
            if "Barbaroslar" in m:
                date += "جمعه از رسانه اینترنتی دی ال مکوین"
            if "Uzak Sehrin Masali" in m:
                date += "جمعه از رسانه اینترنتی دی ال مکوین"
            if "Elkizi" in m:
                date += "یکشنبه از رسانه اینترنتی دی ال مکوین"
            
            FA = fa.replace("#", "").replace("_", " ")
            MSG = f"⬇️ تیزر{Tzz} قسمت {Ee} ({FA} ) {Lo} ، بازیرنویس چسبیده"
            msg = await message.edit(f"{MSG.replace('  ', ' ').replace('720P', '').replace('1080P', '').replace('480P', '').replace('240P', '')}\n\n🔻 پخش {date}\n\n🆔👉 @dlmacvin_new")
               
        if (not m.__contains__("Bolum")) and (N.__contains__("E0") or N.__contains__("E1") or N.__contains__("E2") or N.__contains__("E3") or N.__contains__("E4") or N.__contains__("E5") or N.__contains__("E6") or N.__contains__("E7") or N.__contains__("E8") or N.__contains__("E9")):
            if '720P' in m:
                Q += '720'
            if '480P' in m:
                Q += '480'
            if '1080P' in m:
                Q += '1080'
            if '240P' in m:
                Q += '240'
            if m.__contains__("720P") or m.__contains__("1080P") or m.__contains__("240P") or m.__contains__("480P"):

                q = f"\n🔹کیفیت : {Q}"
            else:
                q = ""
            if 'E0' in N:
                O = N.split("E0")[1]
                T = O.split()[0]
                if T.startswith("0"):
                    E = f"{T.replace('0', '')}"
                else:
                    E = f"{T}"
                n = N.split("E0")[0]
            if 'E1' in N:
                O = N.split("E1")[1]
                T = O.split()[0]
                E = '1' + f"{T}"
                n = N.split("E1")[0]
            if 'E2' in N:
                O = N.split("E2")[1]
                T = O.split()[0]
                E = '2' + f"{T}"
                n = N.split("E2")[0]
            if 'E3' in N:
                O = N.split("E3")[1]
                T = O.split()[0]
                E = '3' + f"{T}"
                n = N.split("E3")[0]
            if 'E4' in N:
                O = N.split("E4")[1]
                T = O.split()[0]
                E = '4' + f"{T}"
                n = N.split("E4")[0]
            if 'E5' in N:
                O = N.split("E5")[1]
                T = O.split()[0]
                E = '5' + f"{T}"
                n = N.split("E5")[0]
            if 'E6' in N:
                O = N.split("E6")[1]
                T = O.split()[0]
                E = '6' + f"{T}"
                n = N.split("E6")[0]
            if 'E7' in N:
                O = N.split("E7")[1]
                T = O.split()[0]
                E = '7' + f"{T}"
                n = N.split("E7")[0]
            if 'E8' in N:
                O = N.split("E8")[1]
                T = O.split()[0]
                E = '8' + f"{T}"
                n = N.split("E8")[0]
            if 'E9' in N:
                O = N.split("E9")[1]
                T = O.split()[0]
                E = '9' + f"{T}"
                n = N.split("E9")[0]
            H = fa.replace("_", " ").replace("#", "")
            if not "Hard-Sub" in m:
                Fucc += f"🔺{H} قسمت {E} \n🔸 دوبله فارسی"
                Fuc = f"{Fucc}{q.replace('  ', ' ')} \n🆔👉 @dlmacvin_new | {fa}"

                print(Fuc)
                msg = await message.edit(Fuc)
            else:
                if "O Ses Turkiye" in m:
                    Fucc += f"♨️ مسابقه{fa} ( {n}) بازیرنویس چسبیده\n👌قسمت : {E.replace('Hard-Sub', '')}"
                else:
                    Fucc += f"♨️ سریال{fa} ( {n}) بازیرنویس چسبیده\n👌قسمت : {E.replace('Hard-Sub', '')}"
                Fuc = f"{Fucc}{q.replace('  ', ' ')} \n🔻تماشای آنلاین بدون فیلتر شکن: \n🆔👉 @dlmacvin_new"

                print(Fuc)
                msg = await message.edit(Fuc)
        elif (m.__contains__("0P")) and (not N.__contains__("E0") and not m.__contains__("bolum") and not m.__contains__("Fragman") and not m.__contains__("Bolum") and not N.__contains__("E1") and not N.__contains__("E2") and not N.__contains__("E3") and not N.__contains__("E4") and not N.__contains__("E5") and not N.__contains__("E6") and not N.__contains__("E7") and not N.__contains__("E8") and not N.__contains__("E9")):
            if " 20" in D:
                f = D.split("20", 1)[0]
                U = D.split("20", 1)[1]
                K = U.split()[0]
                Y = '20' + f"{K}"
                YR = f"\n👌سال : {Y}"
            if " 19" in D:
                f = D.split("19", 1)[0]
                U = D.split("19", 1)[1]
                K = U.split()[0]
                Y = '19' + f"{K}"
                YR = f"\n👌سال : {Y}"
            if (not D.__contains__("19")) and (not D.__contains__("20")):
                P = m.split("0P")[0]
                f = P.replace("72", "").replace("48", "").replace("108", "").replace("24", "")
                YR = f"\n👌سال :"
            if '720P' in m:
                Q += '720'
            if '480P' in m:
                Q += '480'
            if '1080P' in m:
                Q += '1080'
            if '240P' in m:
                Q += '240'
            if m.__contains__("720P") or m.__contains__("1080P") or m.__contains__("240P") or m.__contains__("480P"):
                G = f"\n🔹کیفیت : {Q}"
                q = G.replace(".1", " ").replace(".mkv", " ").replace("  ", " ")
            else:
                q = ""
            YrR = f"{YR.replace('720P', '').replace('480P', '').replace('1080P', '').replace('240P', '').replace('mkv', '').replace('mp4', '')}"
            msg = await message.edit(f"♨️ فیلم {f.replace('Hard-Sub', '').replace(' 20', '').replace('  ', ' ')} بازیرنویس چسبیده{YrR} {q} \n🔻تماشای آنلاین بدون فیلتر شکن: \n🆔👉 @dlmacvin_new")
            cpshn = f"⬇️فیلم () {f.replace('Hard-Sub', '').replace(' 20', '').replace('  ', ' ')} ، بازیرنویس چسبیده \n\n⬇️1080👉\n⬇️720👉\n⬇️480👉\n⬇️240👉\n\n🆔👉 @dlmacvin_new"
            await bot.send_message(chat_id=-1001457054266, text=cpshn, parse_mode='markdown')

        if message.chat.id in CHANNELS:
            return
             
        # Duble Haaye Tak File
        if (message.chat.id == -1001457054266):
            try:
                if "Ghermez" in media.file_name:
                    await msg.copy(chat_id=-1001166919373)
                    await bot.copy_message(chat_id=-1001457054266, from_chat_id=-1001441684079, message_id=msgid, caption=kap, parse_mode='markdown')
    
                elif media.file_name.__contains__("Cukurova") and media.file_name.__contains__("Duble"):
                    await msg.copy(chat_id=-1001437520825) 
                    await bot.copy_message(chat_id=-1001457054266, from_chat_id=-1001441684079, message_id=msgid, caption=kap, parse_mode='markdown')
    
                elif "Mojeze Doctor" in media.file_name:
                    await msg.copy(chat_id=-1001071120514)
                    await bot.copy_message(chat_id=-1001457054266, from_chat_id=-1001441684079, message_id=msgid, caption=kap, parse_mode='markdown')
    
                elif "Yek Jonun Yek Eshgh" in media.file_name:
                    await msg.copy(chat_id=-1001546442991)
                    await bot.copy_message(chat_id=-1001457054266, from_chat_id=-1001441684079, message_id=msgid, caption=kap, parse_mode='markdown')
    
                elif media.file_name.__contains__("2020") and media.file_name.__contains__("Duble"):
                    await msg.copy(chat_id=-1001322014891)
                    await bot.copy_message(chat_id=-1001457054266, from_chat_id=-1001441684079, message_id=msgid, caption=kap, parse_mode='markdown')
    
                elif "Eshghe Mashroot" in media.file_name:
                    await msg.copy(chat_id=-1001409508844)
                    await bot.copy_message(chat_id=-1001457054266, from_chat_id=-1001441684079, message_id=msgid, caption=kap, parse_mode='markdown')
    
                elif "Alireza" in media.file_name:
                    await msg.copy(chat_id=-1001537554747)
                    
                elif "Eshgh Az No" in media.file_name:
                    await msg.copy(chat_id=-1001462444753)
                    
                elif "Setare Shomali" in media.file_name:
                    await msg.copy(chat_id=-1001146657589)
                    
                elif "Be Eshghe To Sogand" in media.file_name:
                    await msg.copy(chat_id=-1001592624165)
                    await bot.copy_message(chat_id=-1001457054266, from_chat_id=-1001441684079, message_id=msgid, caption=kap, parse_mode='markdown')
    
                elif "Aparteman Bigonahan" in media.file_name:
                    await msg.copy(chat_id=-1001588137496)
                    await bot.copy_message(chat_id=-1001457054266, from_chat_id=-1001441684079, message_id=msgid, caption=kap, parse_mode='markdown')
    
            except Exception as error:
                print(error)
