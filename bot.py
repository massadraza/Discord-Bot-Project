import discord 

# id = 738868269343309829

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

client = discord.Client()

@client.event
async def on_message(message):
    id = client.get_guild(738868269343309829) 

    if message.content.find("!hello") != -1:
        await message.channel.send("Hi") 
    elif message.content == "!members":
        await message.channel.send(f"""# of Members: {id.member_count}""") 



client.run(token)  

