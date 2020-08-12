# All the following imports for this code.
import discord 
import time 
import asyncio


# The following information and variables for the functions and events. 
# id = 738868269343309829
messages = joined = 0 

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
            await channel.send.Embed(f"""Hey there, {member.mention}. Welcome to the Python Bot Test Server!""")    



# An event which holds cutting out bad words, gives helpful commands, and commands.
@client.event
async def on_message(message):
    global messages 
    messages += 1

    # All the variables for the if statements below.
    id = client.get_guild(738868269343309829) 
    channels = ["commands"] 
    valid_users = ["official_mrbox#0177"]  
    public_channels = ['general', 'commands', 'welcomes']  

    # Runs the !help command
    if message.content == "!help" and valid_users and channels: 
        embed = discord.Embed(title="Help for Friendly Bot", description="Useful Commands Below")        
        embed.add_field(name="!hello", value="Greets the user with a friendly hello.") 
        embed.add_field(name="!members", value="Prints out the number of users in the server.") 
        embed.add_field(name="!clear", value="Clears all messages in a channel.")
        embed.add_field(name="!help", value="Lists all the commands for this Bot") 
        embed.add_field(name="!about", value="Version and more Info")
        await message.channel.send(content=None, embed=embed) 

    # Runs the !hello and !members command
    if str(message.channel) in channels and str(message.author) and valid_users:  
        if message.content.find("!hello") != -1:
            await message.channel.send(f"""Hi there, {message.author}, thanks for saying hello and I wish you a wonderful day :smile: """)  
        elif message.content == "!members":
            await message.channel.send(f"""There are, {id.member_count} members in this server!""")   
    else:
        print(f"""User: {message.author} tried to do command {message.content}, in channel {message.channel}""") 

    # Runs the !clear command
    if str(message.channel) in public_channels and str(message.author) and valid_users:
        if message.content.find("!clear") != -1:
            await message.channel.purge(limit=5000)

    # Runs the !about command 
    if message.content == "!about" and channels:   
        embed = discord.Embed(title="About Friendly Bot", description="By: @official_mrbox#0177") 
        embed.add_field(name="Data", value="Data will be printed to the server every 5 minutes about members joined and messages sent.") 
        embed.add_field(name="Owner Use Only", value="This bot can only be used by the owner official_mrbox#0177, if you would like adminstrator role for this Bot please DM official_mrbox#0177")
        embed.add_field(name="BotOS", value= "6.1") 
        embed.add_field(name="Serial Number", value="FJWTHJEJ2304J3")
        embed.add_field(name="Model Number", value="BOT1") 
        embed.add_field(name="Copyright ©2020", value="Rights for all under the trademark discord.py rewrite") 
        embed.add_field(name="Server Info", value="Hosted on Heroku.com") 
        await message.channel.send(content=None, embed=embed) 

    # Runs the !update command
    if message.content == "!update" and channels:
        embed = discord.Embed(title="Software Updates", description="BotOS is currently up to date!")
        embed.add_field(name="Current Version", value="6.1") 
        await message.channel.send(content=None, embed=embed) 

# Runs the bot and data.txt file
client.loop.create_task(update_data()) 
client.run(token)   


