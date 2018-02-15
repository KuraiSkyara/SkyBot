import queue
import discord
from discord.ext import commands

#New command format
#@commands.[method]
#async def Method(self, [ctx], [other parameters])

class MusicCog:
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context=True)
    async def join(self, ctx):
        """Join the voice channel"""
        author = ctx.message.author
        
        if not author.voice_channel:
            await self.bot.say("You must be in a voice channel to use this command")
            return
        else:
            voice_channel = author.voice_channel
            vc = await self.bot.join_voice_channel(voice_channel)
            
    @commands.command(pass_context=True)
    async def play(self, ctx, url):
        """Play a song"""
        author = ctx.message.author
        
        if self.bot.is_voice_connected(author.server):
                player = await vc.create_ytdl_player(url, after=self.play_clean)
                await self.bot.say("Now playing")
                p_em = discord.Embed(title=player.title,
                                     description=player.description,
                                     url=player.url,
                                     color=0x00ff00)
                p_em.set_thumbnail(url=player.url)
                await self.bot.send(author.channel, embed=p_em)
                player.start()

    def play_clean():
        coro = self.bot.send_message(some_channel, 'Song ended')
        fut = asyncio.run_coroutine_threadsafe(coro, self.bot.loop)
        try:
            fut.result()
        except:
            # an error happened sending the message
            pass

    @commands.command(pass_context=True)
    async def stop(self, ctx): 
        author = ctx.message.author

        if self.bot.is_voice_connected(author.server):
            vc.disconnect()
            
#Setup function
#Use file name to load the cog, and use class name as the parameter for add_cog
def setup(bot):
    bot.add_cog(MusicCog(bot))
