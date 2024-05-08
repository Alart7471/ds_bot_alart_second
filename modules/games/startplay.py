# from disnake import Button, View, MessageInteraction

def start_play_module(bot):
    @bot.command()
    async def play(ctx):
        await start_play(ctx, bot)

async def start_play(ctx, bot):
    print('PLAYYYYY')
    await ctx.send(f"{ctx.author}, в какую игру сыграем?")

    # Создаем 2 кнопки с названиями игр
    button1 = Button(label="Кости", style=Button.styles.green)
    button2 = Button(label="Монетка", style=Button.styles.red)

    # Инициализируем нажатие на кнопку, принимает аргумент какую игру запустить
    async def button_clicked(button: Button, interaction: MessageInteraction):
        if button.label == "Кости":
            await ctx.send("Вы выбрали игру Кости")
            from dice import start_game as play_dice
            await play_dice(interaction)
        elif button.label == "Монетка":
            await ctx.send("Вы выбрали игру Монетка")
            # from coin import start_game
            # await start_game(interaction)

    button1.callback = button_clicked