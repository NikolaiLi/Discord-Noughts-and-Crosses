import discord
import random

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
    
    if contents.startswith("!joke"):
        joke_id = random.randint(1,len(Jokes))
        reply = Jokes[joke_id]
        await message.channel.send(reply)

Jokes = {
    1: "What do you call it when a 4'9 woman dates a 6'5 man? A long-distance relationship.",
    2: "Why did the teddy bear say no to dessert? Because she was stuffed.",
    3: "What did the left eye say to the right eye? Between us, something smells.",
    4: "Why did the student eat his homework? Because the teacher told him it was a piece of cake.",
    5: "What do you call a boomerang that won’t come back? A stick.",
    6: "Why can’t Elsa from Frozen have a balloon? Because she will: let it go, let it go.",
    7: "How do you get a squirrel to like you? Act like a nut.",
    8: "What’s worse than finding a worm in your apple? Finding half a worm.",
    9: "What is a computer's favorite snack? Computer chips.",
    10: "What animal is always at a baseball game? A bat."
    
}

token = get_token()
client.run(token)