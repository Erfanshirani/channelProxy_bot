# 🤖 ربات پروکسی تلگرام  

این ربات به صورت خودکار پروکسی‌های رایگان را برای کاربران ارسال می‌کند.

## 🚀 راه‌اندازی
1. توکن ربات را در `7708335061:AAHwNtnmLUBT0meIHoSYzARgqw2gl-hrONA` جایگزین کنید.
2. نیازمندی‌ها را نصب کنید:
   ```bash
   pip install -r requirements.txt
python bot.py
import requests
from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
    CallbackQueryHandler,
    MessageHandler,
    Filters
)

# تنظیمات اصلی
TOKEN = "7708335061:AAHwNtnmLUBT0meIHoSYzARgqw2gl-hrONA" # توکن_ربات_شما"  
CHANNEL_ID = "@fast_Proxy_pm کانال_شما"  # مثال: @fast_Proxy_pm
PROXY_API = "https://proxylist.geonode.com/api/proxy-list?limit=1&sort_by=lastChecked&sort_type=desc"

# --- توابع مربوط به کاربران ---
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("🔒 دریافت پروکسی", callback_data="get_proxy")],
        [InlineKeyboardButton("📢 کانال ما", url=f"https://t.me/{CHANNEL_ID.replace('@', '')}")]
    ]
    update.message.reply_text(
        "به ربات پروکسی خوش آمدید!\n\n✅ برای دریافت پروکسی روی دکمه زیر کلیک کنید:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def get_proxy(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    
    try:
        proxy = fetch_proxy()
        query.edit_message_text(
            f"🌐 پروکسی جدید:\n\n`{proxy['ip']}:{proxy['port']}`\n\nکشور: {proxy['country']}\nسرعت: {proxy['speed']}ms",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔄 پروکسی جدید", callback_data="get_proxy")],
                [InlineKeyboardButton("📢 عضویت در کانال", url=f"https://t.me/{CHANNEL_ID.replace('@fast_Proxy_pm', '')}")]
            ])
        )
    except Exception as e:
        print(f"Error: {e}")
        query.edit_message_text("❌ خطا در دریافت پروکسی. لطفاً بعداً تلاش کنید.")

# --- توابع مربوط به کانال ---
def handle_channel_post(update: Update, context: CallbackContext):
    """مدیریت پست‌های ارسالی در کانال."https://t.me/fast_Proxy_pm""
    post = update.channel_post
    if post:
        print(f"پست جدید در کانال:\n{post.text}")

def auto_send_proxy(context: CallbackContext):
    """ارسال خودکار پروکسی به کانال."""
    try:
        proxy = fetch_proxy()
        context.bot.send_message(
            chat_id=CHANNEL_ID,
            text=f"🆕 پروکسی رایگان:\n\n`{proxy['ip']}:{proxy['port']}`\nکشور: {proxy['country']}\nسرعت: {proxy['speed']}ms\n\n@ProxyBot",
            parse_mode="Markdown"
        )
    except Exception as e:
        print(f"Error in auto_send_proxy: {e}")

# --- توابع کمکی ---
def fetch_proxy():
    """دریافت پروکسی از API."""
    response = requests.get(PROXY_API).json()
    return response["data"][0]

def main():
    # تنظیمات ربات
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    job_queue = updater.job_queue

    # دستورات کاربران
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(get_proxy, pattern="^get_proxy$"))

    # مدیریت کانال
    dp.add_handler(MessageHandler(Filters.update.channel_post, handle_channel_post))

    # زمان‌بندی ارسال پروکسی به کانال (هر 1 ساعت)
    job_queue.run_repeating(auto_send_proxy, interval=3600, first=0)

    # شروع ربات
    print("✅ ربات فعال شد!")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
pip install python-telegram-bot requests
python bot.py
import requests

def send_proxy_to_channel(context: CallbackContext):
    proxy = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http").text.split("\n")[0]
    context.bot.send_message(
        chat_id=CHANNEL_ID,
        text=f"🔐 پروکسی جدید:\n\n`{proxy}`\n\n@ProxyBot",
        parse_mode="Markdown"
    )

# زمان‌بندی ارسال هر 1 ساعت
job_queue = updater.job_queue
job_queue.run_repeating(send_proxy_to_channel, interval=3600, first=0)
pip install python-telegram-bot requests
python bot.py
def filter_us_proxies(proxies):
    # این تابع نیاز به API تشخیص کشور IP دارد (مثلاً ipinfo.io)
    us_proxies = []
    for proxy in proxies:
        ip = proxy.split(":")[0]
        # در اینجا از یک سرویس مثل ipinfo.io استفاده کنید
        # country = get_country_from_ip(ip)
        # if country == "US":
        #     us_proxies.append(proxy)
    return us_proxies or proxies  # اگر فیلتر شکست خورد، همه را برگردان
    import random

def send_random_proxy(update: Update, context: CallbackContext):
    proxy = random.choice(proxies_list)
    update.message.reply_text(
        f"🔐 پروکسی تصادفی:\n\n`{proxy}`\n\nبرای استفاده، آن را در تنظیمات VPN وارد کنید.",
        parse_mode="Markdown"
    )

# در تابع main() اضافه کنید:
dp.add_handler(CommandHandler("proxy", send_random_proxy))
def load_proxies(filename="proxyscrape_premium_http_proxies.txt"):
    with open(filename, "r") as file:
        proxies = [line.strip() for line in file if line.strip()]
    return proxies

proxies_list = load_proxies()
print(f"تعداد پروکسی‌های بارگذاری شده: {len(proxies_list)}")
import requests

def check_proxy(proxy):
    try:
        response = requests.get(
            "http://ipinfo.io/json",
            proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"},
            timeout=5
        )
        return response.json()  # اطلاعات IP و کشور
    except:
        return None

# مثال استفاده:
working_proxies = [p for p in proxies_list if check_proxy(p)]
print(f"پروکسی‌های فعال: {len(working_proxies)}/{len(proxies_list)}")
pip install python-telegram-bot requests
python bot.py
