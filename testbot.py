import os
import discord
from discord.ext import commands
import pilights
from pilights import templates as pil_tmp


TOKEN = 'OTEzNTc5NzcyOTMwNTcyMzM4.YaAjdw.rwtMNy1zGdQCrdRHelhpwtnbeo0'

description = '''HeartRushBot -- A tool for playing and understanding Heart Rush more-better :)'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def map(ctx, map="alaria"):
    """Get a map."""
    if map == "alaria":
        map_url = "https://drive.google.com/file/d/11T1kRQVKmr52kzs7w0Nt6A1lXc9OyfPF/view?usp=sharing"
    await ctx.send(map_url)

@bot.command()
async def charsheet(ctx):
    """Get the Heart Rush character sheet."""
    await ctx.send("https://docs.google.com/spreadsheets/d/1QXFgu9T4Hmu5wLdI7JTxrj6JBfJ_GW1qdNOkzLZbYIA/edit?usp=sharing")

@bot.command()
async def get_rules(ctx, subject):
    """Get rules on a subject - choose subject from list below
    - all: link to pdf
    - currency
    """
    if subject == "all":
        await ctx.send("https://drive.google.com/file/d/1dxcwnfamLW_zkCMTr0z1o3g2evCAQcen/view?usp=sharing")
    elif subject == "currency":
        await ctx.send(file=discord.File(r'rules/currency.txt'))
        # await ctx.send(str(_get_rules("currency")))

def _get_rules(file):
    return _get_text("rules", file)

def _get_text(dir, file):
    with open(f'{dir}/{file}.txt') as f:
        lines = f.readlines()
    lines = str(lines).replace(r'\n', "\n".replace(r'\t', "    "))
    return "```" + lines.strip("[]") + "```"

blinker = pilights.Blinker(.1, pil_tmp.DEFAULT)
blinker.show()
bot.run(TOKEN)