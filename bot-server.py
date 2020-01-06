import discord
from discord.ext import commands
import os
client = discord.Client()
from aiohttp import web, WSCloseCode
routes = web.RouteTableDef()

#Your Discord Token when you created the bot [Its not a webhook]
DISCORD_TOKEN = ''

#Server ID
GUILD_ID = 0

#The 'Verify' Section ID - Usually a text chat
VERIFY_ID = 0

#Name of the 'Admin' Role 
adminRoleName = ''

#Name of the Verification Role to give
verifiedRoleName = ''

#---Everything else requres no change:
BotGamePlay = "I Verify People On the Server"
lock = False

class DiscordBot(discord.Client):
    def __init__(self, VERIFY_ID, GUILD_ID, **kwargs):
        super().__init__(**kwargs)
        self.guildID = 0
        self.GUILD_ID = GUILD_ID
        self.VERIFY_ID = VERIFY_ID
        
    async def on_ready(self):
        global lock
        if lock == False:
            print('We have logged in as {0.user}'.format(self))

            await self.change_presence(activity=discord.Game(name=BotGamePlay))
            self.guildID = self.get_guild(self.GUILD_ID)

            if self.guildID == None:
                print('ERROR: You did not add the bot to the guild or you did not specify the correct guild ID')
                print('EXITING....')
                os._exit(0)

            
            global web
            app = web.Application()
            app.add_routes(routes)
            runner = web.AppRunner(app)
            await runner.setup()
            site = web.TCPSite(runner, '', 80)
            await site.start()

            lock = True

    
    async def on_message(self, message):
        global adminRoleName
        if message.author == self.user:
            return

        if message.content.startswith('!killbot') and message.guild == None:
            for role in self.guildID.get_member(message.author.id).roles:
                if role.name == adminRoleName:
                    await message.channel.send('Closing....')
                    os._exit(0)
                elif message.author == self.guildID.owner:
                    await message.channel.send('Closing....')
                    os._exit(0)
            await message.channel.send("Only users with the '{}' role or the Server owner can kill the bot.".format(adminRoleName))

        elif message.guild == None:

            embed = discord.Embed(
                title='About Me',
                colour = discord.Colour.blue()
            )
            embed.add_field(name='What I Do', value="Hey, I give the 'Verified' role on the server. If you wish to obtain the role, click the link to see how!", inline=True)
            embed.add_field(name='Verify Form Link', value='https://discordapp.com/channels/{}/{}'.format(GUILD_ID, VERIFY_ID))
            embed.add_field(name='Have a Question?', value='I do not save or forward any responses sent to me. Ask the server owner, admins, or mods for any questions!')
            await message.channel.send(embed=embed)


    async def give_role(self, usr_fnd):
        global verifiedRoleName
        if self.guildID.get_member_named(usr_fnd) != None:
            userObject = self.guildID.get_member_named(usr_fnd)
            role = discord.utils.get(self.guildID.roles, name=verifiedRoleName)
            if role in userObject.roles:
                await userObject.send(" You were already given the 'Verified' role! ")
            else:
                await userObject.add_roles(role)
                await userObject.send(" Your request has successfully been recieved and you have been given the 'Verified' role! ")
        else:
            #For now, just print out this message
            print("User '{}' does not exist".format(usr_fnd))

#The server only accepts POST requests
@routes.post('/discordverifier')
async def get_handler(request):
    data = await request.json()

    await DiscoBot.give_role(data['fields'][0]['value'])

    return web.Response(text='Success?')


DiscoBot = DiscordBot(VERIFY_ID=VERIFY_ID, GUILD_ID=GUILD_ID, DISCORD_TOKEN=DISCORD_TOKEN)
DiscoBot.run(DISCORD_TOKEN)
