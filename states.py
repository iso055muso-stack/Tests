from aiogram.fsm.state import State, StatesGroup


class OyInRejasi(StatesGroup):
    sana = State()
    vaqt = State()
    oyin_turi = State()
    joy = State()
    ishtirokchilar = State()
    jamoa = State()
    kirish = State()
    keyin = State()
    musiqa = State()
    izoh = State()