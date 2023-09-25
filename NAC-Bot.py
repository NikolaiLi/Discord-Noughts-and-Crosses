
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
    emoji = ("\N{EYES}")

    if contents.startswith("!echo"):
        
        rem = contents[5:]
        reply = rem
        await message.channel.send(reply)

    elif contents.startswith("!react"):
      contents = contents[6:]
      await message.add_reaction("\N{EYES}")
    
    elif contents.startswith("!favorite"):
      rem = contents[6:]
      rem = rem.strip()
      fav_emojis[user_id] = rem
    
    elif contents == "!react":
        msg = ""
        for (k,v) in reacts.items():
          msg += f"{k} : {v}\n"
        await message.channel.send(msg)
    if user_id in fav_emojis.keys():
      await message.add_reaction(fav_emojis[user_id])
    else:
      await message.add_reaction(emoji)
            
@client.event
async def on_reaction_add(reaction,user):
  
    if user == client.user:
      return
  
    emoji = reaction.emoji
    
    if user.id not in reacts:
      reacts [user.id] = {}

    if emoji in reacts[user.id]:
      reacts[user.id][emoji] += 1

    else:
      reacts[user.id][emoji] = 1

    highnumber = 0
    for (k,v) in reacts[user.id].items():
      if v > highnumber:
        highnumber = v
        fav_emojis[user.id] = k
  
    print(reacts[user.id])


token = get_token()
client.run(token)