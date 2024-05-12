from modules.bot_logger import log_message

def on_message(bot, os):
    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        await bot.process_commands(message)
        


        # print('{0.author}: {0.content}'.format(message))#интересная запись форматирования
        log_message(message, os)