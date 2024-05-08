from modules.games.startplay import start_play_module


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
