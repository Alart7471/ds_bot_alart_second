import disnake
import os
from disnake.ext import commands
from modules.bot_sys import start_sys
from modules.setup_commands import setup_commands #импорт одной функции
from modules.on_message import on_message
from modules.on_member_join import on_member_join
from modules_data.token import bot_token

bot = commands.Bot(command_prefix="!", help_command=None, intents=disnake.Intents.all())





start_sys(bot, os)
on_member_join(bot)  
setup_commands(bot)
on_message(bot, os)





bot.run(bot_token)
