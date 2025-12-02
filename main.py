import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    Message, 
    ReplyKeyboardMarkup, 
    KeyboardButton,
    FSInputFile
)
from aiogram.filters import Command,CommandStart
token = "8035405587:AAGiWmuaWK9IOZoYCgM-bN4e6xaXR6lejl8"
bot = Bot(token)
menu=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Start"),KeyboardButton(text="Help")],
        [KeyboardButton(text="Locatsiya",request_location=True)],
        [KeyboardButton(text="Number",request_contact=True,)],
        [KeyboardButton(text="Add"),KeyboardButton(text="Price"),KeyboardButton(text="Zakaz Qilish")]
    ],
    resize_keyboard=True
)
dp = Dispatcher()
@dp.message(CommandStart())
async def start(m:Message):
    await m.answer(f"{m.from_user.full_name}, Assalomu Alaykum botga xush kelibsiz!\nSiz bu botdan mana shu yerda berilgan gulingiz xaqida ma`lumot topa olasiz.\nManashu yerda berilgan gullarni rasmini ham ko`ra olasiz!\nXohlasangiz sotib olishingiz ham mumkun!",reply_markup=menu)
@dp.message(F.text=="Zakaz Qilish")
async def zakaz(m: Message):
    flowers = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Atirgul"), KeyboardButton(text="Lala"), KeyboardButton(text="Liliya")],
            [KeyboardButton(text="Orxideya"), KeyboardButton(text="Kaktus"), KeyboardButton(text="Nargiz")],
            [KeyboardButton(text="Peoniya"), KeyboardButton(text="Forsitiya")],
            [KeyboardButton(text="Lavanda"), KeyboardButton(text="Gordenziya")],
            [KeyboardButton(text="Freziya"), KeyboardButton(text="Kameliya")],
            [KeyboardButton(text="Xrizantema"), KeyboardButton(text="Begoniya"), KeyboardButton(text="Jasmin")],
            [KeyboardButton(text="<-Orqaga")]
        ],
        resize_keyboard=True
    )
    await m.answer("Qaysi gulni zakaz qilasiz?", reply_markup=flowers)
@dp.message(F.text=="Atirgul")
async def Rosa(m:Message):
    photo1=FSInputFile("flowers/image1.png")
    await m.answer(f"""
Atirgul (Rosa)
Ramziy ma`nosi: Sevgi, sadoqat
Ranglari: Qizil, oq, pushti, sariq, ko`k (sun`iy)
Parvarish: Quyoshli joy, o`rtacha sug`orish
                    """)
    await m.answer_photo(photo1,caption="Bu Atirgulning rasimi!")
    await m.answer("Sizning zakazingiz qabul qilindi!\nAgar olib borsak aloqaga chiqamiz yoki lacatsiya bo`yicha boramiz!")
@dp.message(F.text=="Lala")
async def Tulip(m:Message):
    photo2=FSInputFile("flowers/image2.png")
    await m.answer(f"""
Lala (Tulip)
Asli kelib chiqishi: Turkiya va Gollandiya mashhur
Ramzi: Tozalik va soddalik
Gullash davri: Bahorda
                    """)
    await m.answer_photo(photo2,caption="Bu Lalaning rasimi!")
    await m.answer("Sizning zakazingiz qabul qilindi!\nAgar olib borsak aloqaga chiqamiz yoki lacatsiya bo`yicha boramiz!")
@dp.message(F.text=="Liliya")
async def Lilium(m:Message):
    photo3=FSInputFile("flowers/image3.png")
    await m.answer(f"""
Liliya (Lilium)
Hidli va juda nafis gul
Ramzi: Poklik, go`zallik
Qorong`i va nam joylarda yaxshi o`sadi
                    """)
    await m.answer_photo(photo3,caption="Bu Liliyaning rasimi!")
    await m.answer("Sizning zakazingiz qabul qilindi!\nAgar olib borsak aloqaga chiqamiz yoki lacatsiya bo`yicha boramiz!")
@dp.message(F.text=="Orxideya")
async def Orchid(m:Message):
    photo4=FSInputFile("flowers/image4.png")
    await m.answer(f"""
Orxideya (Orchid)
Juda chiroyli, uy ichida o`stiriladi
Ramzi: Nofosat, nafislik
Mo`tadil yorug`lik talab qiladi
                    """)
    await m.answer_photo(photo4,caption="Bu Orxideyaning rasimi!")
    await m.answer("Sizning zakazingiz qabul qilindi!\nAgar olib borsak aloqaga chiqamiz yoki lacatsiya bo`yicha boramiz!")
@dp.message(F.text=="Kaktus")
async def Kaktus(m:Message):
    photo5=FSInputFile("flowers/image5.png")
    await m.answer(f"""
Kaktus guli
Juda kam sug`oriladi
Guli juda chiroyli, ammo kam ochiladi
Ramzi: Sabrlilik
                    """)
    await m.answer_photo(photo5,caption="Bu Kaktusning rasimi!")
    await m.answer("Sizning zakazingiz qabul qilindi!\nAgar olib borsak aloqaga chiqamiz yoki lacatsiya bo`yicha boramiz!")
@dp.message(F.text=="Nargiz")
async def Narcissus(m:Message):
    photo6=FSInputFile("flowers/image6.png")
    await m.answer(f"""
Nargiz (Narcissus)
Bahorda birinchi gullaydiganlardan
Ramzi: Umid, yangilanish
Sovuqqa chidamli
                    """)
    await m.answer_photo(photo6,caption="Bu Nargizning rasimi!")
    await m.answer("Sizning zakazingiz qabul qilindi!\nAgar olib borsak aloqaga chiqamiz yoki lacatsiya bo`yicha boramiz!")
@dp.message(F.text=="Peoniya")
async def Pion(m:Message):
    photo7=FSInputFile("flowers/image7.png")
    await m.answer(f"""
Atirgulning navdosi – Peoniya (Pion)
To`y va bayramlarda keng qo`llanadi
Ramzi: Baxt, farovonlik
Yirik guldasta hosil qiladi
                    """)
    await m.answer_photo(photo7,caption="Bu Peoniyaning rasimi!")
    await m.answer("Sizning zakazingiz qabul qilindi!\nAgar olib borsak aloqaga chiqamiz yoki lacatsiya bo`yicha boramiz!")
@dp.message(F.text=="Forsitiya")
async def Forsythia(m:Message):
    photo8=FSInputFile("flowers/image8.png")
    await m.answer(f"""
Forsitiya (Forsythia)
Erta bahor gullari
Yorqin sariq barglarga ega
Ramzi: Bahorning boshlanishi
                    """)
    await m.answer_photo(photo8,caption="Bu Forsitiyaning rasimi!")
    await m.answer("Sizning zakazingiz qabul qilindi!\nAgar olib borsak aloqaga chiqamiz yoki lacatsiya bo`yicha boramiz!")
@dp.message(F.text=="Lavanda")
async def Lavanda(m:Message):
    photo9=FSInputFile("flowers/image9.png")
    await m.answer(f"""
Lavanda
Xushbo`y, asabni tinchlantiradi
Mo`tadil issiq iqlimni yaxshi ko`radi
Ramzi: Tinchlik va musaffolik
                    """)
    await m.answer_photo(photo9,caption="Bu Lavandaning rasimi!")
    await m.answer("Sizning zakazingiz qabul qilindi!\nAgar olib borsak aloqaga chiqamiz yoki lacatsiya bo`yicha boramiz!")
@dp.message(F.text=="Gordenziya")
async def Hydrangea(m:Message):
    photo10=FSInputFile("flowers/image10.png")
    await m.answer(f"""
Gortenziya (Hydrangea)
Ranglari tuproq pH ga qarab o`zgaradi (ko`k, pushti, oq)
Ramzi: Do`stlik va minnatdorchilik
Soyali joylarni yaxshi ko`radi
                    """)
    await m.answer_photo(photo10,caption="Bu Gortenziyaning rasimi!")
    await m.answer("Sizning zakazingiz qabul qilindi!\nAgar olib borsak aloqaga chiqamiz yoki lacatsiya bo`yicha boramiz!")
@dp.message(F.text=="Freziya")
async def Hibiscus(m:Message):
    photo11=FSInputFile("flowers/image11.png")
    await m.answer(f"""
Freziya (Freesia)
Juda yoqimli hidga ega
Ko`pincha guldastalarda ishlatiladi
Ramzi: Ishonch va sadoqat
                    """)
    await m.answer_photo(photo11,caption="Bu Freziyaning rasimi!")
    await m.answer("Sizning zakazingiz qabul qilindi!\nAgar olib borsak aloqaga chiqamiz yoki lacatsiya bo`yicha boramiz!")
@dp.message(F.text=="Kameliya")
async def Hibiscus(m:Message):
    photo12=FSInputFile("flowers/image12.png")
    await m.answer(f"""
Kameliya (Camellia)
Barglari yaltiroq, guli nozik
Ranglari: Oq, qizil, pushti
Ramzi: Muhabbat va hurmat
                    """)
    await m.answer_photo(photo12,caption="Bu Kameliyaning rasimi!")
    await m.answer("Sizning zakazingiz qabul qilindi!\nAgar olib borsak aloqaga chiqamiz yoki lacatsiya bo`yicha boramiz!")
@dp.message(F.text=="Xrizantema")
async def Hibiscus(m:Message):
    photo13=FSInputFile("flowers/image13.png")
    await m.answer(f"""
Xrizantema (Chrysanthemum)
Kuzda gullaydi
Ranglari juda ko`p: oq, sariq, qizil, binafsha
Ramzi: Uzoq umr va baxt
                    """)
    await m.answer_photo(photo13,caption="Bu Xrizantemaning rasimi!")
    await m.answer("Sizning zakazingiz qabul qilindi!\nAgar olib borsak aloqaga chiqamiz yoki lacatsiya bo`yicha boramiz!")
@dp.message(F.text=="Begoniya")
async def Hibiscus(m:Message):
    photo14=FSInputFile("flowers/image14.png")
    await m.answer(f"""
Begoniya (Begonia)
Uy ichida yaxshi o`sadi
Barglari ham dekorativ
Ramzi: Samimiylik va do`stlik
                    """)
    await m.answer_photo(photo14,caption="Bu Begoniyaning rasimi!")
    await m.answer("Sizning zakazingiz qabul qilindi!\nAgar olib borsak aloqaga chiqamiz yoki lacatsiya bo`yicha boramiz!")
@dp.message(F.text=="Jasmin")
async def Hibiscus(m:Message):
    photo15=FSInputFile("flowers/image15.png")
    await m.answer(f"""
Jasmin (Yasemin)
Juda kuchli va yoqimli hidli
Kechasi ham hid taratadi
Ramzi: Poklik va muhabbat
                    """)
    await m.answer_photo(photo15,caption="Bu Jasminning rasimi!")
    await m.answer("Sizning zakazingiz qabul qilindi!\nAgar olib borsak aloqaga chiqamiz yoki lacatsiya bo`yicha boramiz!")
@dp.message(F.text == "<-Orqaga")
async def send_back(message: Message):
    await message.answer("Asosiy menyu", reply_markup=menu)
@dp.message(F.text=="Locatsiya")
async def Rosa(m:Message):
    await m.answer(f"Siz locatsiya yubordingiz!\nBiz sizning locatsiyangizga qarab bu gulni yetkazib beramiz!")
@dp.message(F.text=="Number")
async def Rosa(m:Message):
    await m.answer(f"Siz raqamingizni tashladingiz!\nBiz agar gulni yetkazib bo`lsak sizga aloqaga chiqamiz!")
@dp.message(F.text=="Start")
async def Rosa(m:Message):
    await m.answer(f"Botga xush kelibsiz!\nBo`tdan foydalanishingiz mumkun!")
@dp.message(F.text=="Add")
async def Rosa(m:Message):
    await m.answer(f"""
\n1. Atirgul (Rosa)
\nRamziy ma`nosi: Sevgi, sadoqat
\nRanglari: Qizil, oq, pushti, sariq, ko`k (sun`iy)
\nParvarish: Quyoshli joy, o`rtacha sug`orish
\n2. Lala (Tulip)
\nAsli kelib chiqishi: Turkiya va Gollandiya mashhur
\nRamzi: Tozalik va soddalik
\nGullash davri: Bahorda
\n3. Liliya (Lilium)
\nHidli va juda nafis gul
\nRamzi: Poklik, go`zallik
\nQorong`i va nam joylarda yaxshi o`sadi
\n4. Orxideya (Orchid)
\nJuda chiroyli, uy ichida o`stiriladi
\nRamzi: Nofosat, nafislik
\nMo`tadil yorug`lik talab qiladi
\n5. Kaktus guli
\nJuda kam sug`oriladi
\nGuli juda chiroyli, ammo kam ochiladi
\nRamzi: Sabrlilik
\n6. Nargiz (Narcissus)
\nBahorda birinchi gullaydiganlardan
\nRamzi: Umid, yangilanish
\nSovuqqa chidamli
\n7. Atirgulning navdosi – Peoniya (Pion)
\nTo`y va bayramlarda keng qo`llanadi
\nRamzi: Baxt, farovonlik
\nYirik guldasta hosil qiladi
\n8. Forsitiya (Forsythia)
\nErta bahor gullari
\nYorqin sariq barglarga ega
\nRamzi: Bahorning boshlanishi
\n9. Lavanda
\nXushbo`y, asabni tinchlantiradi
\nMo`tadil issiq iqlimni yaxshi ko`radi
\nRamzi: Tinchlik va musaffolik
\n10. Gortenziya (Hydrangea)
\nRanglari tuproq pH ga qarab o`zgaradi (ko`k, pushti, oq)
\nRamzi: Do`stlik va minnatdorchilik
\nSoyali joylarni yaxshi ko`radi
\n11. Freziya (Freesia)
\nJuda yoqimli hidga ega
\nKo`pincha guldastalarda ishlatiladi
\nRamzi: Ishonch va sadoqat
\n12. Kameliya (Camellia)
\nBarglari yaltiroq, guli nozik
\nRanglari: Oq, qizil, pushti
\nRamzi: Muhabbat va hurmat
\n13. Xrizantema (Chrysanthemum)
\nKuzda gullaydi
\nRanglari juda ko`p: oq, sariq, qizil, binafsha
\nRamzi: Uzoq umr va baxt
\n14. Begoniya (Begonia)
\nUy ichida yaxshi o`sadi
\nBarglari ham dekorativ
\nRamzi: Samimiylik va do`stlik
\n15. Jasmin (Yasemin)
\nJuda kuchli va yoqimli hidli
\nKechasi ham hid taratadi
\nRamzi: Poklik va muhabbat
                    """)
@dp.message(F.text=="Price")
async def Rosa(m:Message):
    await m.answer(f"""
\n1. Atirgul (Rosa) — Narxi: 15 000 so`m
\n2. Lala (Tulip) — Narxi: 12 000 so`m
\n3. Liliya (Lilium) — Narxi: 18 000 so`m
\n4. Orxideya (Orchid) — Narxi: 25 000 so`m
\n5. Kaktus guli — Narxi: 8 000 so`m
\n6. Nargiz (Narcissus) — Narxi: 14 000 so`m
\n7. Atirgulning navdosi – Peoniya (Pion) — Narxi: 22 000 so`m
\n8. Forsitiya (Forsythia) — Narxi: 10 000 so`m
\n9. Lavanda — Narxi: 13 000 so`m
\n10. Gortenziya (Hydrangea) — Narxi: 17 000 so`m
\n11. Freziya (Freesia) — Narxi: 11 000 so`m
\n12. Kameliya (Camellia) — Narxi: 19 000 so`m
\n13. Xrizantema (Chrysanthemum) — Narxi: 16 000 so`m
\n14. Begoniya (Begonia) — Narxi: 9 000 so`m
\n15. Jasmin (Yasemin) — Narxi: 20 000 so`m
                    """)
@dp.message(Command("Atirgul"))
async def Rosa(m:Message):
    photo1=FSInputFile("flowers/image1.png")
    await m.answer(f"""
Atirgul (Rosa)
Ramziy ma`nosi: Sevgi, sadoqat
Ranglari: Qizil, oq, pushti, sariq, ko`k (sun`iy)
Parvarish: Quyoshli joy, o`rtacha sug`orish
                    """)
    await m.answer_photo(photo1)
@dp.message(Command("Lala"))
async def Tulip(m:Message):
    photo2=FSInputFile("flowers/image2.png")
    await m.answer(f"""
Lala (Tulip)
Asli kelib chiqishi: Turkiya va Gollandiya mashhur
Ramzi: Tozalik va soddalik
Gullash davri: Bahorda
                    """)
    await m.answer_photo(photo2)
@dp.message(Command("Liliya"))
async def Lilium(m:Message):
    photo3=FSInputFile("flowers/image3.png")
    await m.answer(f"""
Liliya (Lilium)
Hidli va juda nafis gul
Ramzi: Poklik, go`zallik
Qorong`i va nam joylarda yaxshi o`sadi
                    """)
    await m.answer_photo(photo3)
@dp.message(Command("Orxideya"))
async def Orchid(m:Message):
    photo4=FSInputFile("flowers/image4.png")
    await m.answer(f"""
Orxideya (Orchid)
Juda chiroyli, uy ichida o`stiriladi
Ramzi: Nofosat, nafislik
Mo`tadil yorug`lik talab qiladi
                    """)
    await m.answer_photo(photo4)
@dp.message(Command("Kaktus"))
async def Kaktus(m:Message):
    photo5=FSInputFile("flowers/image5.png")
    await m.answer(f"""
Kaktus guli
Juda kam sug`oriladi
Guli juda chiroyli, ammo kam ochiladi
Ramzi: Sabrlilik
                    """)
    await m.answer_photo(photo5)
@dp.message(Command("Nargiz"))
async def Narcissus(m:Message):
    photo6=FSInputFile("flowers/image6.png")
    await m.answer(f"""
Nargiz (Narcissus)
Bahorda birinchi gullaydiganlardan
Ramzi: Umid, yangilanish
Sovuqqa chidamli
                    """)
    await m.answer_photo(photo6)
@dp.message(Command("Peoniya"))
async def Pion(m:Message):
    photo7=FSInputFile("flowers/image7.png")
    await m.answer(f"""
Atirgulning navdosi – Peoniya (Pion)
To`y va bayramlarda keng qo`llanadi
Ramzi: Baxt, farovonlik
Yirik guldasta hosil qiladi
                    """)
    await m.answer_photo(photo7)
@dp.message(Command("Forsitiya"))
async def Forsythia(m:Message):
    photo8=FSInputFile("flowers/image8.png")
    await m.answer(f"""
Forsitiya (Forsythia)
Erta bahor gullari
Yorqin sariq barglarga ega
Ramzi: Bahorning boshlanishi
                    """)
    await m.answer_photo(photo8)
@dp.message(Command("Lavanda"))
async def Lavanda(m:Message):
    photo9=FSInputFile("flowers/image9.png")
    await m.answer(f"""
Lavanda
Xushbo`y, asabni tinchlantiradi
Mo`tadil issiq iqlimni yaxshi ko`radi
Ramzi: Tinchlik va musaffolik
                    """)
    await m.answer_photo(photo9)
@dp.message(Command("Gordenziya"))
async def Hydrangea(m:Message):
    photo10=FSInputFile("flowers/image10.png")
    await m.answer(f"""
Gortenziya (Hydrangea)
Ranglari tuproq pH ga qarab o`zgaradi (ko`k, pushti, oq)
Ramzi: Do`stlik va minnatdorchilik
Soyali joylarni yaxshi ko`radi
                    """)
    await m.answer_photo(photo10)
@dp.message(Command("Freziya"))
async def Hibiscus(m:Message):
    photo11=FSInputFile("flowers/image11.png")
    await m.answer(f"""
Freziya (Freesia)
Juda yoqimli hidga ega
Ko`pincha guldastalarda ishlatiladi
Ramzi: Ishonch va sadoqat
                    """)
    await m.answer_photo(photo11)
@dp.message(Command("Kameliya"))
async def Hibiscus(m:Message):
    photo12=FSInputFile("flowers/image12.png")
    await m.answer(f"""
Kameliya (Camellia)
Barglari yaltiroq, guli nozik
Ranglari: Oq, qizil, pushti
Ramzi: Muhabbat va hurmat
                    """)
    await m.answer_photo(photo12)
@dp.message(Command("Xrizantema"))
async def Hibiscus(m:Message):
    photo13=FSInputFile("flowers/image13.png")
    await m.answer(f"""
Xrizantema (Chrysanthemum)
Kuzda gullaydi
Ranglari juda ko`p: oq, sariq, qizil, binafsha
Ramzi: Uzoq umr va baxt
                    """)
    await m.answer_photo(photo13)
@dp.message(Command("Begoniya"))
async def Hibiscus(m:Message):
    photo14=FSInputFile("flowers/image14.png")
    await m.answer(f"""
Begoniya (Begonia)
Uy ichida yaxshi o`sadi
Barglari ham dekorativ
Ramzi: Samimiylik va do`stlik
                    """)
    await m.answer_photo(photo14)
@dp.message(Command("Jasmin"))
async def Hibiscus(m:Message):
    photo15=FSInputFile("flowers/image15.png")
    await m.answer(f"""
Jasmin (Yasemin)
Juda kuchli va yoqimli hidli
Kechasi ham hid taratadi
Ramzi: Poklik va muhabbat
                    """)
    await m.answer_photo(photo15)
@dp.message(F.text=="Help")
async def Help(m:Message):
    await m.answer("""
/Atirgul
/Lala
/Liliya
/Orxideya
/Kaktus
/Nargiz
/Peoniya
/Forsitiya
/Lavanda
/Gortenziya
/Freziya
/Kameliya
/Xrizantema
/Begoniya
/Jasmin
""")
async def main():
    print("Bot started...")
    await dp.start_polling(bot)
if __name__=="__main__":

    asyncio.run(main())
