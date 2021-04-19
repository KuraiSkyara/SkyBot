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
