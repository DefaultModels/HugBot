from discord.ext import commands
import discord

with open('sadwords.txt', 'r') as f:
  global sadwords
  words = f.read()
  sadwords = words.split("\n")

class auto_reply(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
      global user
      global msg

      msg = lower(message.content)
      user = message.author

      if "no" in msg:
        return

      if "nt" in msg:
        return

      if "n't" in msg:
        return
      
      for word in sadwords:          
        if word in msg:           
          if "I" or "i" in msg:
            print(msg)
            await message.author.send(f'You said: "{msg}". That didn\'t seem to joyful, here\'s a hug to cheer you up!')
            await message.author.send('https://tenor.com/view/hug-love-hi-bye-cat-gif-15999080')
            
def setup(bot):
  bot.add_cog(auto_reply(bot))