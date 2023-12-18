from aiogram import types, executor, Bot, Dispatcher



bot = Bot(token="")

dp = Dispatcher(bot)


async def on_startup(_):
    print("Bot ishladi !!!")


if __name__== "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)