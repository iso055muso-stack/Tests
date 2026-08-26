from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
import asyncio
import funksiyalar
from states import OyInRejasi

dp = Dispatcher()
TOKEN = "8895446803:AAFOfvBubtXMYRQKLeogV7GTeSYrF_5XJg0"

async def main():
    dp.message.register(funksiyalar.start_bosganda,CommandStart)
    dp.message.register(funksiyalar.sana,OyInRejasi.sana)
    dp.message.register(funksiyalar.vaqt,OyInRejasi.vaqt)
    dp.message.register(funksiyalar.oyin_turi,OyInRejasi.oyin_turi)
    dp.message.register(funksiyalar.joy,OyInRejasi.joy)
    dp.message.register(funksiyalar.ishtirokchilar,OyInRejasi.ishtirokchilar)
    dp.message.register(funksiyalar.jamoa,OyInRejasi.jamoa)
    dp.message.register(funksiyalar.kirish,OyInRejasi.kirish)
    dp.message.register(funksiyalar.keyin,OyInRejasi.keyin)
    dp.message.register(funksiyalar.musiqa,OyInRejasi.musiqa)
    dp.message.register(funksiyalar.izoh,OyInRejasi.izoh)
    bot = Bot(token=TOKEN,default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)

asyncio.run(main())


