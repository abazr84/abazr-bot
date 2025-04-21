import telebot
import schedule
import time
import threading

API_TOKEN = '7608757781:AAHrXLForD74nR6gFK4daTnx-VSLfHbPI2U'
bot = telebot.TeleBot(API_TOKEN)
AUTHORIZED_USER_ID = 853854576

@bot.message_handler(commands=['start', 'ابدأ'])
def send_welcome(message):
    if message.chat.id == AUTHORIZED_USER_ID:
        bot.send_message(message.chat.id, 
            "مرحبًا بك يا EN. Abazr!\n\n"
            "هذه أوامري المتاحة:\n"
            "/plan أو /الخطة – خطة التداول الأسبوعية\n"
            "/analysis أو /تحليل – تحليل الذهب/البيتكوين\n"
            "/news أو /الأخبار – أهم الأخبار الاقتصادية\n"
            "/summary أو /ملخص – ملخص الأداء الأسبوعي")
    else:
        bot.send_message(message.chat.id, "عذرًا، هذا البوت خاص.")

@bot.message_handler(commands=['plan', 'الخطة'])
def trading_plan(message):
    if message.chat.id == AUTHORIZED_USER_ID:
        bot.send_message(message.chat.id, 
            "خطة التداول الأسبوعية:\n"
            "✅ الاتجاه العام: صاعد\n"
            "✅ الدخول: 3310 – 3315\n"
            "✅ الهدف: 3325 – 3330\n"
            "✅ وقف الخسارة: 3305")

@bot.message_handler(commands=['analysis', 'تحليل'])
def live_analysis(message):
    if message.chat.id == AUTHORIZED_USER_ID:
        bot.send_message(message.chat.id, "جارٍ تحليل السوق اللحظي...")
        bot.send_message(message.chat.id, 
            "تحليل سريع:\n"
            "- الذهب مستقر حاليًا في نطاق ضيق\n"
            "- البيتكوين يتذبذب حول 84,500\n"
            "- لا توجد فرص دخول مؤكدة الآن")

@bot.message_handler(commands=['news', 'الأخبار'])
def send_news(message):
    if message.chat.id == AUTHORIZED_USER_ID:
        bot.send_message(message.chat.id, 
            "أخبار اليوم:\n"
            "- الفيدرالي يشير إلى تثبيت الفائدة\n"
            "- التوترات الجيوسياسية تدفع الذهب للصعود\n"
            "- البيتكوين يتأثر بالتصريحات التنظيمية")

@bot.message_handler(commands=['summary', 'ملخص'])
def weekly_summary(message):
    if message.chat.id == AUTHORIZED_USER_ID:
        bot.send_message(message.chat.id, 
            "ملخص الأسبوع:\n"
            "- عدد الصفقات: 5\n"
            "- نسبة النجاح: 80%\n"
            "- صافي الربح: +$18.50")

def schedule_tasks():
    schedule.every().monday.at("09:00").do(lambda: bot.send_message(AUTHORIZED_USER_ID, "⏰ خطة التداول الأسبوعية جاهزة! استخدم /plan"))
    schedule.every().friday.at("23:45").do(lambda: bot.send_message(AUTHORIZED_USER_ID, "تنبيه: السوق سيغلق خلال 15 دقيقة. راجع صفقاتك!"))
    schedule.every().friday.at("23:59").do(lambda: bot.send_message(AUTHORIZED_USER_ID, "📊 ملخص الأداء الأسبوعي جاهز! استخدم /summary"))

    while True:
        schedule.run_pending()
        time.sleep(10)

threading.Thread(target=schedule_tasks).start()
bot.polling()
