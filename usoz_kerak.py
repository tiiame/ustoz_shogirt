from aiogram import Bot, types, Dispatcher, executor
from config import TOKEN
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text



storage = MemoryStorage()
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

class Partner(StatesGroup):
    full_name = State()
    age = State()
    technology = State()
    phone = State()
    location = State()
    price = State()
    job = State()
    oclock = State()
    desire = State()


def start_buttons():
    buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("Sherik kerak")
    button2 = KeyboardButton("Hodim kerak")
    button3 = KeyboardButton("Ish joyi kerak")
    button4 = KeyboardButton("Ustoz kerak")
    button5 = KeyboardButton("Shogird kerak")
    buttons.add(button1, button2)
    buttons.add(button3, button4)
    buttons.add(button5)
    return buttons


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    user_name = types.User.get_current()['first_name']
    text = f"Assalom alaykum, {user_name} \nUstozShogird kanalining rasmiy botiga xush kelibsiz!"
    await message.answer(text, reply_markup=start_buttons()) 

@dp.message_handler(Text(equals="Ustoz kerak"), state="*")
async def btn1(message: types.Message):
    text = ("Ustoz topish uchun ariza berish \nHozir sizga birnecha savollar beriladi.\nsavollarga to'g'ri va aniq  javob bering.\n"
            "Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz qabul qilinadi.")

    await message.answer(text=text)
    await Partner.full_name.set()

@dp.message_handler(state=Partner.full_name)
async def full_name(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    text = ("Ism, familiyangizni kiriting?")
    await message.answer(text=text)

    await Partner.next()

@dp.message_handler(state=Partner.age)
async def age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    text = (" Yosh: \n Yoshingizni kiriting?\nMasalan, 19")
    await message.answer(text=text)

    await Partner.next()



@dp.message_handler(state=Partner.technology)
async def technology(message: types.Message, state: FSMContext):
    await state.update_data(technology=message.text)
    text = ("📚 Texnologiya: \nTalab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating. Masalan, \nJava, C++, C#")
    await message.answer(text=text)
    await Partner.next()

@dp.message_handler(state=Partner.phone)
async def phone(message: types.Message, state: FSMContext):
        await state.update_data(phone=message.text)
        text = "📞 Aloqa: \n Bog`lanish uchun raqamingizni kiriting?\nMasalan, +998 90 123 45 67"
        await message.answer(text=text)
        await Partner.next()
 


@dp.message_handler(state=Partner.location)
async def location(message: types.Message, state: FSMContext):
    await state.update_data(location=message.text)
    text = "🌐 Hudud: \n Qaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting."
    await message.answer(text=text)

    await Partner.next()


@dp.message_handler(state=Partner.price)
async def price(message: types.Message, state: FSMContext):
   
        text = "💰 Narxi: \nTolov qilasizmi yoki Tekinmi?\nKerak bo`lsa, Summani kiriting?"
        await message.answer(text=text)
        await state.update_data(price=message.text)
        await Partner.next()
 


@dp.message_handler(state=Partner.job)
async def job(message: types.Message, state: FSMContext):
    await state.update_data(job=message.text)
    text = "👨🏻‍💻 Kasbi: \nIshlaysizmi yoki o`qiysizmi?\nMasalan, Talaba"
    await message.answer(text=text)

    await Partner.next()

@dp.message_handler(state=Partner.oclock)
async def oclock(message: types.Message, state: FSMContext):
        await state.update_data(oclock=message.text)
        text = "🕰 Murojaat qilish vaqti: \nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 9:00 - 18:00"
        await message.answer(text=text)

        await Partner.next()
 

@dp.message_handler(state=Partner.desire)
async def desire(message: types.Message, state: FSMContext):
    buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton(text="Ha")
    button2 = KeyboardButton(text="Yoq")
    buttons.add(button1, button2)
    await state.update_data(desire=message.text)
    data = await state.get_data()
    text = (f"Ustoz kerak:\n\n"
            f"🏅 Ustoz: {data['full_name']}\n"
            f"   Yosh: {data['age']}\n"
            f"📚 Texnologiya: {data['technology']}\n "
            f"🇺🇿 Telegram: {types.User.get_current()['first_name']}\n"
            f"📞 Aloqa:{data['phone']}\n "
            f"🌐 Hudud: {data['location']}\n"
            f"💰 Narxi: {data['price']}\n"
            f"👨🏻‍💻 Kasbi: {data['job']}\n"
            f"🕰 Murojaat qilish vaqti:{data['oclock']} "
            f"🔎 Maqsad:{data['desire']} ")
    await message.answer(text=text, reply_markup=buttons)
    await state.reset_state(with_data=False)


@dp.message_handler(Text(equals="Ha"))
async def send_app(message: types.Message, state: FSMContext):
    data = await state.get_data()
    text = (f"Ustoz kerak:\n\n"
            f"🏅 Ustoz: {data['full_name']}\n"
            f"   Yosh: {data['age']}\n"
            f"📚 Texnologiya: {data['technology']}\n "
            f"🇺🇿 Telegram: {types.User.get_current()['first_name']}\n"
            f"📞 Aloqa:{data['phone']}\n "
            f"🌐 Hudud: {data['location']}\n"
            f"💰 Narxi: {data['price']}\n"
            f"👨🏻‍💻 Kasbi: {data['job']}\n"
            f"🕰 Murojaat qilish vaqti:{data['oclock']}\n "
            f"🔎 Maqsad:{data['decire']} ")
    await bot.send_message(chat_id=204396345, text=text)

    await state.finish()


async def on_startup(_):
    print("-__-")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)