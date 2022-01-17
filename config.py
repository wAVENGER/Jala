"""
Mualliflik huquqini buzmagan holda kanallarda tarqatishingiz mumkin!
Loyiha muallifi: Arslonbek Xushboqov
Tarqatildi: @Api_Kod kanalida

Demo: @GoTarjimonBot
"""
from pyrogram import filters
API_ID = 1662626 #bu yerga my.telegram.org manzilidan olingan Api id kiritiladi
API_HASH = "5abb410f4fdb961906bceaf12ead92a"#bu yerga my.telegram.org manzilidan olingan Api hash kiritiladi
TOKEN =  "bot token"#@botfather dan olingan bot token

sudousers = [1204989672] #ahamiyatsiz
sudofilter = filters.user(sudousers)
