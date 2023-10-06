import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

TOK_FILE = "token.txt"

game_state = {"ingame":False}

def get_token():
  tokfile = open(TOK_FILE, 'r')
  token = tokfile.read()
  tokfile.close()
  return token

@client.event
async def on_ready():
    print("Connected!")


async def kitchen(channel):
    reply = ["You are in a very dark room", "It looks like you are in a kitchen", "Beside you, there's another room,"]
    for i in reply:
        await channel.send(i)


async def livingroom(channel):
    reply = "happy"
    await channel.channel.send(reply)


async def show_room(room_num, channel):
    print(channel)
    if room_num == 1:
        await kitchen(channel)
    if room_num == 2:
        await livingroom(channel)

@client.event
async def on_message(message):
    contents = message.content
    channel = message.channel
    user_id = message.author.id
   
    
    if contents.startswith("!adv.play"):
        reply = ["Welcome to this adventure!", "Type help for more information"]
        for i in reply:
            await message.channel.send(i)
        game_state["ingame"] = True
    current_room = 1

    if game_state["ingame"] == True:
        if contents.startswith("help"):
            reply = ["Your mission is to find the key and open the door - Type 'look' to see", "CONTROLS:", "'forward'", "'right'", "'left'", "'backwards'"]
            for i in reply:
                await message.channel.send(i)
            
        elif contents.startswith("look"):
            await show_room(current_room, channel)
        
        elif contents.startswith("forward"):
            await show_room(current_room, channel)


token = get_token()
client.run(token)