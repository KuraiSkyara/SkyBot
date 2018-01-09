import random
import discord
from discord.ext import commands

#New command format
#@commands.[method]
#async def Method(self, [ctx], [other parameters])

class GeneralCog:
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def roll(self, dice : str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await self.bot.say('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await self.bot.say(result)

    @commands.command(description='For when you wanna settle the score some other way')
    async def choose(self,*choices : str):
        """Chooses between multiple choices."""
        await self.bot.say(random.choice(choices))

    @commands.command()
    async def joined(self, member : discord.Member):
        """Says when a member joined."""
        await self.bot.say('{0.name} joined in {0.joined_at}'.format(member))

# The setup function below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(GeneralCog(bot))
