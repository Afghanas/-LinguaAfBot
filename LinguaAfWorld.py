@bot.message_handler(content_types=['new_chat_members'])
def welcome(message):
    for member in message.new_chat_members:
        welcome_text = f"""🌍✨ **𝐋𝐢𝐧𝐠𝐮𝐚𝐀𝐟𝗪𝗼𝗿𝗹𝗱 – 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲 𝗣𝗿𝗮𝗰𝘁𝗶𝗰𝗲 𝗛𝘂𝗯** ✨🌍

👤 Dear {member.first_name},

🇬🇧 **Welcome to the Global Speaking Group!**
Please respect others and follow the group rules.

🇦🇫 **په نړیوال سپیکینګ ګروپ کې ښه راغلاست!**
مهرباني وکړئ د ګروپ اصول ولولئ او له ټولو سره درناوی وکړئ.

🇸🇦 **أهلاً بك في مجموعة المحادثة العالمية!**
من فضلك احترم الآخرين واتبِع القوانين.

🇮🇷 **به گروه جهانی تمرین زبان خوش آمدید!**
لطفاً قوانین گروه را رعایت کنید و با احترام برخورد نمایید.

🇦🇫 **به گروپ جهانی تمرین زبان خوش آمدید!**  
لطفاً اصول گروه را مراعات کنید و با همه احترامانه برخورد کنید.

✍️ **Daily Writing & Q/A Group:**  
📚 که غواړئ چی هره ورځ لیکل تمرین کړئ، سوالونه وکړئ او ځوابونه زده کړئ، نو دلته یو ځای شئ:  
👉 [@LinguaAfWorldWrite](https://t.me/LinguaAfWorldWrite)

🕊️ Let’s build a world of learning, peace, and respectful communication!
"""
        bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown')