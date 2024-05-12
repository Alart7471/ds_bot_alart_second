from modules.games.startplay import start_play_module
from data.server.vk import createVkPost

def setup_commands(bot):
    @bot.command()
    async def check_module(ctx):
        await ctx.send("This is the check_module command.")

    @bot.command()
    async def ping(ctx):
        await ctx.send("Pong!")

    @bot.command()
    async def help(ctx):
        await ctx.send("Help!")

    @bot.command()
    async def info(ctx):
        await ctx.send(f"{ctx.author} used command {ctx.command} in {ctx.channel}")

    @bot.command()
    async def play(ctx):
        await start_play_module(ctx, bot)

    @bot.command()
    async def gpt(ctx):
        args = ctx.message.content[len('!gpt '):]
        print(args)
        await ctx.send(f"Вы задали боту вопрос: {args}, давайте подумаем...")

    @bot.command()
    async def vk(ctx):
        args = ctx.message.content[len('!vk '):]
        createVkPost(args)
        