from googletrans import Translator
from discord.ext import commands
import os
TOKEN = os.getenv('TOKEN')
bot = commands.Bot(command_prefix="!")
@bot.event
async def on_ready():
  print("Logged in!")
@bot.command()
async def translate(ctx, lang, *, args):
  try:
    translator = Translator()
    subtoexyrus = translator.translate(args, dest=lang)
    await ctx.send(subtoexyrus.text) 
  except ValueError:
    await ctx.send("Sorry, there was an error. If the error persists, DM Exyrus#2915 with the error code VALUE. **PLEASE NOTE** Chinese is not supported as of right now. Try again later.")
  except:
    await ctx.send("Sorry, an unknown error occured.")
bot.run(TOKEN)
