# from modules.bot_logger import log_startup
from modules.bot_logger import log_startup
import datetime

def start_sys(bot, os):
    @bot.event
    async def on_ready():    
        print(f"Logged in as {bot.user} (ID: {bot.user.id})")
        # log_message(f"Logged in as {bot.user} (ID: {bot.user.id}), time: {bot.user.created_at.strftime('%d.%m.%Y %H:%M:%S')}", "sys", bot.user.created_at, os)

        date = datetime.datetime.now().strftime('%d%m%Y')
        message = f"{date}: logged in as {bot.user} (ID: {bot.user.id})"
        log_startup(message, date, os)


        # log_startup(f"Logged in as {bot.user} (ID: {bot.user.id}), time: {bot.user.created_at.strftime('%d.%m.%Y %H:%M:%S')}", "sys", bot.user.created_at, os)
        #Доделать потом #log_startup(f"Logged in as {bot.user} (ID: {bot.user.id}), time: {bot.user.created_at.strftime('%d.%m.%Y %H:%M:%S')}", "sys", os)

        # log_message(f"Logged in as {bot.user} (ID: {bot.user.id}), time: {bot.user.created_at.strftime('%d.%m.%Y %H:%M:%S')}", "sys", "", os)

        