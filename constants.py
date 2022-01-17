"""
Mualliflik huquqini buzmagan holda kanallarda tarqatishingiz mumkin!
Loyiha muallifi: Arslonbek Xushboqov
Tarqatildi: @Api_Kod kanalida

Demo: @GoTarjimonBot
"""

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


default_lang = "en"

start_message_text = """
Assalomu alaykum {} \U0001F60E Men GoTarjimonBot ya'ni "Google Tarjimon Botman \ud83e\udd16

Menga har qanday soʻzni yuboring men uni ingliz tiliga tarjima qilib beraman boshqa tillarni tanlash uchun /language buyrugini yuboring.

**Mavjud buyruqlar:**
/developer - Bot dasturchisi haqida
/help - Botdan foydalanish boyicha qollanma
/language - Oʻzingiz uchun afzal tilni tanlang

Agar sizda shu bot yoki boshqa botlar' haqida fikringiz boʻlsa dasturchi__ - @LiderBoy ga murojaat qilishingiz mumkin!

Zavqlaning! ☺"""

start_message_reply_markup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "➕ Meni guruhga qoshing ➕",  url="http://t.me/GoTarjimonBot?startgroup=tr")
        ],
        [
            InlineKeyboardButton(  
                        "🔍 Inline izlash",
                        switch_inline_query_current_chat=" "
                    ),
            InlineKeyboardButton(
                "👨‍💻 Dasturchi",  url="https://t.me/LiderBoy"),
        ],
        [
            InlineKeyboardButton(
                "🆘 Yordam",  callback_data="help"),
            InlineKeyboardButton(
                "Xizmatlar 💚",  callback_data=b"Credits")
        ],
        [
            InlineKeyboardButton(
                "📣 Kanal",  url="https://t.me/Api_Kod"),
            InlineKeyboardButton(
                "Guruh 👥",  url="https://t.me/API_KOD_GROUP"),
        ]
    ]
)

help_markup = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🔙 Orqaga", callback_data="back")],
            ]
        )

credits = """Dasturchi 🧑‍💻
 • @LiderBoy
 • Sizga mukammal tarzda bot yaratib berishimiz mumkin
 • Iltimos lichkaga bot kodini sorab yozmang!

Kanal 💡
 • @QaynoqFakt"""

help_text = """
**GoTarjimon Bot**

GoTarjimon "G + Tarjimon" so'zi bo'lib, "Google Tarjimon" ma'nosini anglatadi.  Matnni (emojilar bilan) dunyoning boshqa tillaridan koʻplab tillarga tarjima qilishga yordam beradigan bot.

 GoTarjimon Bot turli xil tillarni aniqlay oladi, chunki u Google Translate API yordamida ishlaydi.

 GoTarjimon Bot-dan shaxsiy suhbatida foydalanishingiz mumkin.  Ammo GoTarjimon Bot Telegram Guruh & Kanal uchun mavjud emas.
 
**Qanday**
GoTarjimom Bot-ga nusxa ko'chirilgan matnni yoki boshqa tilga yo'naltirilgan xabarni yuborish kifoya, shunda siz o'zingiz xohlagan tilda tarjimani olasiz.  Qaysi til mavjudligini bilish uchun /language buyrugʻini yuborish kerak.

****Boshqa Yordam****

**Guruhlar**
/tr (til kodi) reply xabarni tarjima qilish  reply orqali

**Asosiy tilni o'zgartirmasdan shaxsiy suhbatda tarjima qiling**
/tr (til kodi) (xabar)

**Inline rejimida tarjima qiling**
@GoTarjimonBot (til kodi) (xabar)

---
Muammo bolsa? @LiderBoy ga murojaat qiling

Python dasturlash tilida yaratildi 💚
"""

developer_text = """
Arslonbek Xushboqov

Qiziqishi:  Dasturchilik ;
Yoshi:  15-yosh ;
Yonalishi:  Html & Css & Js & Python & sqlite3 ;
Aloqa:  935258004 ;
Email:  arslonbek68xushboqov@gmail.com ;
Yashash Joyi:  Qashqadaryo vil. Dehqonobod tumani ;
"""

language_text = """
**Tillar**

__Tarjima qilmoqchi bo'lgan tilni tanlang.__

•/lang (til kodi) 

Masalan: ```/lang uz``` 

Til kodlari ro'yxati: https://cloud.google.com/translate/docs/languages


"""

error_group_no_reply = """Tarjima qilish uchun xabarga javob bering"""

error_ocr_no_reply = """matnni olish uchun fotosuratga javob bering"""

lang_saved_message = """{} sizning asosiy tilingiz sifatida o'rnatildi."""

ocr_message_text = """```rasmdagi matn:``` \n\n {}"""

translate_string_one = """**\ud83c\udf10 Tarjima**:\n\n```{}```\n\n**🔍 Aniqlangan til:** {} \n\n **Tarjima qilingan**: {}"""

translate_string_two = """**\ud83c\udf10 Tarjima**:\n\n```{}```\n\n**🔍 Aniqlangan til:** {}"""

inline_text_string_one = """So'z tarjima qilindi {} dan {} ga"""
