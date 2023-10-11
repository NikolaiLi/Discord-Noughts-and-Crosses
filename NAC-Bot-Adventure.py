import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

TOK_FILE = "token.txt"

game_state = {"ingame":False, "current_room":0, "dooropen":False}

def get_token():
  tokfile = open(TOK_FILE, 'r')
  token = tokfile.read()
  tokfile.close()
  return token

@client.event
async def on_ready():
    print("Connected!")

inventory = ["Musty Paper", "Empty Wallet"]

def addToInventory(item):
    inventory.append(item)

async def kitchen(channel):
    reply = ["You are in a very dark room", "It looks like you are in a kitchen", "Beside you, there's another room"]
    for i in reply:
        await channel.send(i)


async def livingroom(channel):
    reply = ["You see a bed and a desk - It looks like a bedroom", "There's a key on the ground right infront of you - It's maybe for the door - Type 'pickup' to pick the key up"]
    for i in reply:
        await channel.send(i)


async def show_room(room_num, channel):
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
        reply = ["Welcome to this adventure!", "You are in a very dark room. It looks like you are in a kitchen. Beside you, there's another room", "Quest: Your mission is to find the key and open the door", "Type 'help' for more information"]
        for i in reply:
            await message.channel.send(i)
        game_state["ingame"] = True
        game_state["current_room"] = 1
        game_state["dooropen"] = False

    if game_state["ingame"] == True:
        if contents.startswith("help"):
            reply = ["Your mission is to find the key and open the door - Type 'look' to see and 'inventory' to see your inventory", "CONTROLS:", "'forward'", "'right'", "'left'", "'backwards'"]
            for i in reply:
                await message.channel.send(i)
            
        elif contents.startswith("look"):
            await show_room(game_state["current_room"], channel)
        
        elif contents.startswith("forward"):
            if game_state["current_room"] == 1 or game_state["current_room"] == 2:
                await message.channel.send("Ultimate headache - You've hit a wall")
        
        elif contents.startswith("right"):
            if game_state["current_room"] == 1:
                await message.channel.send("There's a door - type 'open' to open the door'")
            elif game_state["current_room"] == 2:
                await message.channel.send("You walked back to the kitchen")
                game_state["current_room"] = 1

        
        elif contents.startswith("left"):
            if game_state["current_room"] == 1:
                await message.channel.send("You walked into another room")
                game_state["current_room"] = 2
            elif game_state["current_room"] == 2:
                await message.channel.send("Ultimate headache - You've hit a wall")
        
        elif contents.startswith("backwards"):
            if game_state["current_room"] == 1 or game_state["current_room"] == 2:
                await message.channel.send("Ultimate headache - You've hit a wall")
        
        elif contents.startswith("pickup"):
            if game_state["current_room"] == 2:
                addToInventory("Key")
                await message.channel.send("You succesfully picked up a key")
            elif game_state["current_room"] == 1:
                await message.channel.send("There's nothing to pick up")
        
        elif contents.startswith("open"):
            if game_state["current_room"] == 1:
                if game_state["dooropen"] == True:
                    await message.channel.send("You opened the door to the toilet. You see your mother sit on the toilet. You realise it's 3AM and you sleepwalked to the kichten. Your mother got mad and you went to bed again")
                elif game_state["dooropen"] == False:
                    await message.channel.send("The door is locked - type 'unlock' to unlock the door")
            
        elif contents.startswith("unlock"):
            if game_state["current_room"] == 1:
                if "Key" not in inventory:
                    await message.channel.send("You don't have a key to unlock the door")
                if "Key" in inventory:
                    game_state["dooropen"] = True
                    await message.channel.send("You unlocked the door - You are now available to open the door")
                    
                
        
        elif contents.startswith("inventory"):
            for i in inventory:
                await message.channel.send(i)

token = get_token()
client.run(token)