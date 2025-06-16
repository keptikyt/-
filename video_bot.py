import telebot
import logging

TOKEN = "token"
# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_video(message):
    user = message.from_user
    username = user.username or "Без юзернейма"
    
    # Логируем в консоль Pydroid
    logger.info(f"🚀 Кто-то прописал /start! Юзернейм: {username} (ID: {user.id})")
    
    try:
        # Отправляем видео без описания
        with open("recroll.mp4", 'rb') as video_file:
            bot.send_video(
                chat_id=message.chat.id,
                video=video_file,
                caption=None  # Без текста
            )
        logger.info("✅ Видео успешно отправлено")
    except Exception as e:
        logger.error(f"❌ Ошибка при отправке видео: {e}")
        bot.send_message(message.chat.id, "Произошла ошибка при отправке видео")

if __name__ == '__main__':
    logger.info("🔥 Бот запущен! Ожидаю команду /start...")
    bot.polling(none_stop=True)
