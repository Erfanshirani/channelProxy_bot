from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
import requests
import random
from config import TOKEN, CHANNEL_ID, PROXY_API

def start(update: Update, context: CallbackContext):
    """مدیریت دستور /start"""
    buttons = [
        [InlineKeyboardButton("🔐 دریافت پروکسی", callback_data="get_proxy")],
        [InlineKeyboardButton("📢 کانال ما", url=CHANNEL_ID)]
    ]
    update.message.reply_text(
        "سلام! برای دریافت پروکسی روی دکمه زیر کلیک کنید:",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

def get_proxy(update: Update, context: CallbackContext):
    """ارسال پروکسی تصادفی"""
    query = update.callback_query
    query.answer()
    
    try:
        proxy = fetch_random_proxy()
        query.edit_message_text(
            f"🛡️ پروکسی فعال:\n\n`{proxy}`\n\n⏳ اعتبار: 24 ساعت",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔄 پروکسی جدید", callback_data="get_proxy")],
                [InlineKeyboardButton("📢 کانال پروکسی", url=CHANNEL_ID)]
            ])
        )
    except Exception as e:
        print(f"⚠️ خطا: {e}")
        query.edit_message_text("❌ خطا در دریافت پروکسی. لطفاً مجدد تلاش کنید.")

def fetch_random_proxy():
    """دریافت پروکسی تصادفی از API"""
    response = requests.get(PROXY_API)
    proxies = response.text.splitlines()
    return random.choice(proxies) if proxies else "پروکسی یافت نشد"

def main():
    """تنظیمات و راه‌اندازی ربات"""
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # ثبت دستورات
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(get_proxy, pattern="^get_proxy$"))

    print("🤖 ربات فعال و آماده به کار!")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
  pip install -r requirements.txt
python bot.py
