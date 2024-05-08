def on_member_join(bot):
    @bot.event
    async def on_member_join(member):
        await member.create_dm() #Написать в личку присоединившемуся
        await member.dm_channel.send(
           f"Hi {member.name}, welcome to my Discord server!"
        )