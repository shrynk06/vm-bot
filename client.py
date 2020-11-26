import discord
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'hello':
        await message.channel.send('hello')

client.run('NzgxMzg5NjUyNjE1MjMzNTQw.X7870g.9OBuziesET1Or_6dOqaCbwlF0sA')
