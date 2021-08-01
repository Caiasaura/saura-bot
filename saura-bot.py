import discord

TOKEN = open("token.txt","r").readline()

intents = discord.Intents.default()
intents.members = True


client = discord.Client(intents = intents)

@client.event
async def on_ready():
	print('We have logged on under the name {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith(‘.hello’):
		await message.channel.send(‘Hello!’)

@client.event

async def on_member_join(member):
	print('got a thing')
	channel = client.get_channel([862127249889296385])
	await channel.send('Welcome to the server!')

@client.event
async def on_member_remove(member):

	print('lost a thing')

client.run(TOKEN)