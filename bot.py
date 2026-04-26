import asyncio, aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User, Base
from database import engine

Base.metadata.create_all(engine)  # создаёт таблицу автоматически

BOT_TOKEN = "8486740053:AAHrUYOgVcJNqdz3ysBsV-pGiV-mXrE4W4w"
bot = Bot(token=BOT_TOKEN)
dp  = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    user = message.from_user
    
    # Получаем аватарку
    photo_url = None
    photos = await bot.get_user_profile_photos(user.id, limit=1)
    if photos.total_count > 0:
        file = await bot.get_file(photos.photos[0][0].file_id)
        photo_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file.file_path}"

    # Сохраняем в MySQL
    db: Session = SessionLocal()
    existing = db.get(User, user.id)
    if not existing:
        db.add(User(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            username=user.username,
            photo_url=photo_url,
        ))
        db.commit()
    db.close()

    await message.answer(
        f"Привет, {user.first_name}! 👋\n"
        f"Твои данные сохранены. Открой сайт чтобы увидеть свой профиль."
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())