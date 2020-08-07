
# All the following imports for this code.
import discord 
import time 
import asyncio 
from discord.ext import commands 


# The following information and variables for the functions and events. 
# id = 738868269343309829
messages = joined = 0 
client = commands.Bot(command_prefix = "!") 


# Start the bot function
def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

client = discord.Client() 



# Prints data about the messages sent and users joined every 5 minutes to the data.txt file
async def update_data(): 
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():  
        try:
            with open("data.txt", "a") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n")   

            messages = 0 
            joined = 0

            await asyncio.sleep(5)  
        except Exception as e:
            print(e)
            await asyncio.sleep(5)  

# To prevent anyone in the group from changing their nickname to official_mrbox.
@client.event
async def on_member_update(before, after): 
    n = after.nick
    if n:
        if n.lower().count("official_mrbox") > 0: 
            last = before.nick 
            if last:
                await after.edit(nick=last)
            else:
                await after.edit(nick="Nickname already in use") 




# Greets a new user that joined the group. 
@client.event
async def on_member_join(member): 
    global joined
    joined += 1
    for channel in member.guild.channels:
        if str(channel) == "welcomes":
            await channel.send(f"""Hey there, {member.mention}. Welcome to the Python Bot Test Server""")  



# An event which holds cutting out bad words, gives helpful commands, and commands.
@client.event
async def on_message(message):
    global messages 
    messages += 1

    id = client.get_guild(738868269343309829) 
    channels = ["commands"] 
    valid_users = ["official_mrbox#0177"]  
    bad_words = ["stupid", "shutup", "bad"]  
    public_channels = ['general', 'commands', 'welcomes']  

    for word in bad_words:
        if message.content.count (word) > 0:
            print(f"""User: {message.author} said a bad word in {message.channel} Swear Word: {message.content}""")  
            await message.channel.purge(limit=1)  

    if message.content == "!help":
        embed = discord.Embed(title="Help for Bot.py", description="Useful Commands for Bot.py")       
        embed.add_field(name="!hello", value="Greets the user with a friendly hello.") 
        embed.add_field(name="!users", value="Prints out the number of users in the server.")
        embed.add_field(name="!clear", value="Clears all messages in a channel.")
        embed.add_field(name="!help", value="Lists all the commands for this Bot") 
        embed.add_field(name="!about", value="Version and more Info")
        await message.channel.send(content=None, embed=embed)

    if str(message.channel) in channels and str(message.author) in valid_users:  
        if message.content.find("!hello") != -1:
            await message.channel.send("Hi") 
        elif message.content == "!members":
            await message.channel.send(f"""# of Members: {id.member_count}""") 
    else:
        print(f"""User: {message.author} tried to do command {message.content}, in channel {message.channel}""") 

    if str(message.channel) in public_channels and str(message.author) in valid_users:
        if message.content.find("!clear") != -1:
            await message.channel.purge(limit=5000)

    if message.content == "!about": 
        embed = discord.Embed(title="About Bot.py", description="Information about Bot.py") 
        embed.add_field(name="Version", value="BETA 1.0")
        embed.add_field(name="Copyright ©2020", value="Rights for all under the trademark discord.py rewrite") 
        await message.channel.send(content=None, embed=embed) 


client.loop.create_task(update_data()) 
client.run(token)  


