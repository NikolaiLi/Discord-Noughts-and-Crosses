import discord

board = [[":one:", ":two:", ":three:"],
        [":four:", ":five:", ":six:"],
        [":seven:", ":eight:", ":nine:"]]

coordinates = {"1":(0,0), "2":(0,1), "3":(0,2),
               "4":(1,0), "5":(1,1), "6":(1,2),
               "7":(2,0), "8":(2,1), "9":(2,2)}

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

async def check_win(channel):
    global play
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] in players:
                await channel.send("Player: " + board[i][0] + " wins")
                play = False
                return
        
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] in players:
                await channel.send("Player: " + board[0][i] + " wins")
                play = False
                return
        
        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] in players:
                await channel.send("Player: " + board[0][0] + " wins")
                play = False
                return
        
        if board[2][0] == board[1][1] == board[0][2]:
            if board[2][0] in players:
                await channel.send("Player: " + board[2][0] + " wins")
                play = False
                return
            
        if board[0][0] != ":one:" and board[0][1] != ":two:" and board[0][2] != ":three:" and board[1][0] != ":four:" and board[1][1] != ":five:" and board[1][2] != ":six:" and board[2][0] != ":seven:" and board[2][1] != ":eight:"and board[2][2] != ":nine:":
            await channel.send("It's a draw!")
            play = False
            return

@client.event
async def on_ready():
    print("Connected!")
    global play
    global player
    play = False
    player = False

@client.event
async def on_message(message):
    contents = message.content
    input = contents[0]
    channel = message.channel    

    if contents.startswith("!nac.play"):
        reply1 = "Here's your board:"
        await message.channel.send(reply1)
        await print_board(channel)
        await message.channel.send("Player1, enter the number you want to place your cross:")
        global play
        global player
        play = True
        player = True
        
    if play == True:
    
        await check_win(channel)

        if player == True:
            if board[coordinates[input][0]][coordinates[input][1]] == players[0] or board[coordinates[input][0]][coordinates[input][1]] == players[1]:
                await message.channel.send("You can't place your cross there!") 
            else:
                board[coordinates[input][0]][coordinates[input][1]] = players[0]
                await print_board(channel)
                await message.channel.send("Player2, enter the number where you want to place your nought")
                player = False
                   
        elif player == False:
            if board[coordinates[input][0]][coordinates[input][1]] == players[0] or board[coordinates[input][0]][coordinates[input][1]] == players[1]:
                await message.channel.send("You can't place your nought there!")
            else:
                board[coordinates[input][0]][coordinates[input][1]] = players[1]
                await print_board(channel)
                await message.channel.send("Player1, enter the number where you want to place your cross")
                player = True

         
                 
token = get_token()
client.run(token)