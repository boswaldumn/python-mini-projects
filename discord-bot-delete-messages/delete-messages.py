import discord

client = discord.Client()

@client.event
async def on_message(message):
    if str(message.channel) == "general" and message.content != "hello":
        await message.channel.purge(limit=1)



client.run('YOUR_TOKEN_HERE')
