from aiogram import types
from aiogram.fsm.context import FSMContext

from states import OyInRejasi


async def start_bosganda(message: types.Message, state: FSMContext):
    await state.set_state(OyInRejasi.sana)
    await message.answer("Assalomu alaykum! O'yin rejasini tuzamiz.\n""📅 Avval bugungi sanani yozing.\n""Masalan: 2025-08-27")


async def sana(message: types.Message, state: FSMContext):
    await state.update_data(sana=message.text)
    await state.set_state(OyInRejasi.vaqt)
    await message.answer("Qabul qilindi ✅\n""🕒 Endi o'yin boshlanish vaqtini yozing.\n""Masalan: 18:00")


async def vaqt(message: types.Message, state: FSMContext):
    await state.update_data(vaqt=message.text)
    await state.set_state(OyInRejasi.oyin_turi)
    await message.answer("⚽ O'yin turini yozing.\n""Masalan: futbol, shaxmat, voleybol")


async def oyin_turi(message: types.Message, state: FSMContext):
    await state.update_data(oyin_turi=message.text)
    await state.set_state(OyInRejasi.joy)
    await message.answer("📍 O'yin joyini yozing.\n""Masalan: Sport zal, Bog'")


async def joy(message: types.Message, state: FSMContext):
    await state.update_data(joy=message.text)
    await state.set_state(OyInRejasi.ishtirokchilar)
    await message.answer("👥 Ishtirokchilar sonini yozing.")


async def ishtirokchilar(message: types.Message, state: FSMContext):
    await state.update_data(ishtirokchilar=message.text)
    await state.set_state(OyInRejasi.jamoa)
    await message.answer("🎽 Jamoa nomini yozing.")


async def jamoa(message: types.Message, state: FSMContext):
    await state.update_data(jamoa=message.text)
    await state.set_state(OyInRejasi.kirish)
    await message.answer("🎟 Kirish bepulmi?\n""Ha yoki yo'q deb yozing.")


async def kirish(message: types.Message, state: FSMContext):
    await state.update_data(kirish=message.text)
    await state.set_state(OyInRejasi.keyin)
    await message.answer("☕ O'yindan keyin qayerga borasiz?\n""Masalan: Choyxona, Uyga")


async def keyin(message: types.Message, state: FSMContext):
    await state.update_data(keyin=message.text)
    await state.set_state(OyInRejasi.musiqa)
    await message.answer("🎵 O'yinda musiqa bo'ladimi?\n""Ha yoki yo'q deb yozing.")


async def musiqa(message: types.Message, state: FSMContext):
    await state.update_data(musiqa=message.text)
    await state.set_state(OyInRejasi.izoh)
    await message.answer("📝 Qo'shimcha izoh yozing.\n""Agar izoh bo'lmasa, '-' yozing.")


async def izoh(message: types.Message, state: FSMContext):
    await state.update_data(izoh=message.text)

    data = await state.get_data()

    natija = (
        "🎮 <b>O'YIN REJASI</b>\n\n"
        f"📅 Sana: {data['sana']}\n"
        f"🕒 Boshlanish vaqti: {data['vaqt']}\n"
        f"⚽ O'yin turi: {data['oyin_turi']}\n"
        f"📍 O'yin joyi: {data['joy']}\n"
        f"👥 Ishtirokchilar: {data['ishtirokchilar']}\n"
        f"🎽 Jamoa nomi: {data['jamoa']}\n"
        f"🎟 Kirish bepulmi: {data['kirish']}\n"
        f"☕ O'yindan keyin: {data['keyin']}\n"
        f"🎵 Musiqa: {data['musiqa']}\n"
        f"📝 Qo'shimcha izoh: {data['izoh']}"
    )

    await message.answer(natija)

    await state.clear()