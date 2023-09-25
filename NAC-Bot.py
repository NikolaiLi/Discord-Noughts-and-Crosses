import discord

board = """
:green_square: :green_square: :green_square:
:green_square: :green_square: :green_square:
:green_square: :green_square: :green_square: """

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

TOK_FILE = "token.txt"

fav_emojis = {}
reacts = {}

def get_token():
  tokfile = open(TOK_FILE, 'r')
  token = tokfile.read()
  tokfile.close()
  return token

@client.event
async def on_ready():
    print("Connected!")

@client.event
async def on_message(message):
    contents = message.content
    user_id = message.author.id

    if contents.startswith("!nac.play"):
        reply1 = "Here's your board"
        reply = board
        await message.channel.send(reply1)
        await message.channel.send(reply)
        
token = get_token()
client.run(token)