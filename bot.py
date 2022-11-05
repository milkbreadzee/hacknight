import discord
import responses

#token = api key,  connects the program to the bot
#TOKEN = 'MTAzODQyMzczNjA2OTY2MDcxNA.GZ_8N2._wZuvlJumPVPyNP1TWQ3yxOmNytfoDcl7HEhFg'

#async def https://realpython.com/async-io-python/#the-10000-foot-view-of-async-io
#msg - bot msg
#user_msg - text inputted by user
#is_private - checking if the channel is private or not.

#async await is a coupled thingy.
async def send_message(message, user_message, is_private):
    try:
         # needs to be implemented in responses.py
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
    

def run_discord_bot():
    #this token cannot be used in the actual discord bot.
    TOKEN = 'MTAzODQyMzczNjA2OTY2MDcxNA.GZ_8N2._wZuvlJumPVPyNP1TWQ3yxOmNytfoDcl7HEhFg'
    
    intents = discord.Intents.default() #to get the default intents, new thingy look it up !!!
    intents.message_content = True # to be able to read the messaage ???

    #creating clients

    client = discord.Client(intents=intents)


    @client.event
    async def on_ready(): #triggers each time we run the code.
        print(f'{client.user} is now running') #this tells us that the server is running

    
    @client.event
    async def on_message(message):#handles all the messages that comes into the discord server and how the bot respondes to them
        if message.author == client.user:
            # to prevent an infinity loop.
            #the client.user is the bot and if the program reads the text send by the bot as a user inputted msg (message.author),
            #then it will keep responding to its own text.
            return #ignoring it lol
        
        username = str(message.author) 
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" in ({channel})')

        if user_message[0] == '?': #for the user to write in a private channel, they have to start the string w a ? or any symbol i want
           # print("hihi help msg")
            user_message = user_message[1:] #slicing the string to remove the ?
            #print(user_message)
            await send_message(message, user_message, is_private = True)
        else:
            await send_message(message, user_message, is_private = False)

    
    #this code needs to be on the same indent as TOKEN, and not insdie @client.event !!!
    client.run(TOKEN)

