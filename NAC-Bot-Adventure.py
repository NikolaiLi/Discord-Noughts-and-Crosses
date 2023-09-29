import discord

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
    
    if contents.startswith("!adv.play"):
        reply = "Welcome to this adventure you stupid ass"
        
token = get_token()
client.run(token)