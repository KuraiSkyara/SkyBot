import math
import discord
from discord.ext import commands

#New command format
#@commands.[method]
#async def Method (self, ctx, [other parameters]):

class VanguardCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='Calculate required shield value')
    async def vgg(self, atk_pwr: str = -1, def_pwr: str = -1, unit_type: str = 'a'):
        """For Vanguard. Calculates required shield"""
        if atk_pwr == -1 or def_pwr == -1 or (unit_type.lower() != 'v' and unit_type.lower() != 'r'):
            await self.bot.say('Missing arguments for calculation (atk_pwr, def_pwr, unit_type)')
        else:
            try:
                guard_value = int(atk_pwr) - int(def_pwr)
                if guard_value % 5000 == 0:
                        guard_value = int(5000 * math.ceil(float(guard_value)/5000)) + 5000
                else:
                        guard_value = int(5000 * math.ceil(float(guard_value)/5000))
                            
            except ValueError:
                await self.bot.say('One or more arguments was incorrect')
                return
                
            if unit_type.lower() == 'r':
                if guard_value < 0:
                    await self.bot.say('This attack will not hit')
                else:                    
                    await self.bot.say('Required shield value: {}'.format(guard_value))
            else:
                guard_list = [guard_value]
                value = guard_list[0]
                for x in  range(5):
                    value= value + 5000
                    guard_list.append(value)
                for x in range(6):
                    if guard_list[x] < 0:
                        guard_list[x] = 0
                await self.bot.say("""Required shield value: {} for 1 drive
    {} for 2 drives
    {} for 3 drives
    {} for 4 drives
    {} for 5 drives
    {} for 6 drives""".format(*guard_list))
            
#Setup function
#Use file name to load the cog, and use class name as the parameter for add_cog
def setup(bot):
    bot.add_cog(VanguardCog(bot))
