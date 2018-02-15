import discord
from discord.ext import commands

import sys, traceback

def get_prefix(bot, message):
    prefix = '?'

    return commands.when_mentioned_or(prefix)(bot, message)

# Below cogs represents our folder our cogs are in. Following is the file name. So 'meme.py' in cogs, would be cogs.meme
# Think of it like a dot path import
initial_extensions = ['cogs.general',
                      'cogs.meme',
                      'cogs.music',
                      'cogs.vanguard']

#Dev note: Add some more cogs later

bot = commands.Bot(command_prefix=get_prefix, description='A bot written by Skyara for world domina- peace.')

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()


@bot.event
async def on_ready():

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    await bot.change_presence(game=discord.Game(name='with human lives'))
    print(f'Fired up and ready to serve...!')

bot_fio = open('token.txt')
bot_token = bot_fio.readline()
bot_fio.close()

bot.run(bot_token, bot=True, reconnect=True)
