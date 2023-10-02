import discord

board = [[":green_square:", ":green_square:", ":green_square:"],
[":green_square:", ":green_square:", ":green_square:"],
[":green_square:", ":green_square:", ":green_square:"]]


intents = discord.Intents.default()
intents.message_content = True

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

TOK_FILE = "token.txt"

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
        await message.channel.send(reply1)
        for i in board:
          await message.channel.send(" ".join(i))
    
    play = True

    while play == True:
       await message.channel.send("Player1, enter row and coloumn numbers:")
       play == False
        
token = get_token()
client.run(token)