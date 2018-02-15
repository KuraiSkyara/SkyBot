import random
import discord
from discord.ext import commands

#New command format
#@commands.[method]
#async def Method (self, ctx, [other parameters]):

class MemeCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='8b', description='The infamous fortune-telling ball, now bot-ified!')
    async def eb(self, str):
        """Makes a prediction on a Yes or No question"""
        quoteList=['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely',
                    'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes',
                    'Signs point to yes', 'Reply hazy try again', 'Ask again later',  'Better not tell you now',
                    'Cannot predict now',  'Concentrate and ask again', 'Don\'t count on it', 'My reply is no',
                    'My sources say no', 'Outlook not so good', 'Very doubtful']
        await self.bot.say(random.choice(quoteList))

    @commands.command(description='Defend your faith in Skyara')
    async def insult(self, str='Really'):
        """Teach pesky non-believers to not mess with Skyara"""
        
        await self.bot.say("""{}, u call that an insult?

i think its hilarious u kids talking shit about Skyara in the first place.
u wouldnt say this shit to him irl, hes jacked. not only that but he wears the
freshest clothes, eats at the chillest restaurants and hangs out with the hottest
chicks. yall are pathetic lol""".format(str))

    @commands.command(description='What would you rate it?')
    async def giveit(self, int=0):
        """What would you rate it?"""
        if int==0:
            await self.bot.say('Nothing appeared to happen...')
        else:
            await self.bot.say('**T H I C' + ' C' * int + '**')
            

    @commands.command(pass_context=True)
    async def lewd(self, ctx, value: str = 'a'):
        """Checks lewdness"""
        if value == 'a':
            value = ctx.message.author
        random.seed()
        await self.bot.say("{} is {}% lewd".format(value, random.randint(0,100)))

    @commands.command()
    async def sh(self, value:str='0'):
        """Play a game of Shiratori"""
        if value == '-r':
            shira_fo = open('cogs/txtfiles/shiratori.txt', 'w')
            shira_fo.write('Shiratori')
            shira_fo.close()
            await self.bot.say('Value reset.')
        else:       
            shira_fo = open('cogs/txtfiles/shiratori.txt', 'r+')
            shira_text = shira_fo.readline()
            if not shira_text:
                shira_fo.write('Shiratori')
                shira_fo.seek(0,0)
                shira_text = shira_fo.readline()
            if value != '0':
                if shira_text[len(shira_text)-1].lower() == value[0].lower():
                    shira_fo = open('cogs/txtfiles/shiratori.txt', 'w')
                    value = value[:1].upper() + value[1:]
                    shira_fo.write(value)
                    shira_fo.close()
                    await self.bot.say('Current word: **{}**'.format(value))
                else:
                    await self.bot.say('That was not a valid word. The current word is **{}**'.format(shira_text))
            else:
                await self.bot.say('Current word: **{}**'.format(shira_text))
                shira_fo.close()

#Setup function
#Use file name to load the cog, and use class name as the parameter for add_cog
def setup(bot):
    bot.add_cog(MemeCog(bot))
