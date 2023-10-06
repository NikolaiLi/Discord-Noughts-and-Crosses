import discord

board = [[":one:", ":two:", ":three:"],
[":four:", ":five:", ":six:"],
[":seven:", ":eight:", ":nine:"]]

players = [":x:",":o:"]

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

async def print_board(channel):
   for i in board:
      await channel.send(" ".join(i))

@client.event
async def on_ready():
    print("Connected!")
    global play
    play = False

@client.event
async def on_message(message):
    contents = message.content
    channel = message.channel
    user_id = message.author.id
    current_player = 0
    if contents.startswith("!nac.play"):
        reply1 = "Here's your board:"
        await message.channel.send(reply1)
        await print_board(channel)
        await message.channel.send("Player1, enter the number you want to place your cross:")
        global play
        play = True
    
    if play == True:
       if contents.startswith("1"):
          print("test")
          board[0][0] = players[current_player % 2]
          current_player = current_player + 1
          await print_board(channel)
          await message.channel.send("Player2, enter the number you want to place your nought")
    
          
  
      
token = get_token()
client.run(token)