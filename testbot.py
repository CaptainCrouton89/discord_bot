import os
import sys
import discord
import  difflib
import markdown
from discord.ext import commands
try:
    from pilights import blinker, templates
    rpi = True
except:
    print("pilights import failure: will not run custom R-Pi functionalities")
    rpi = False

with open("discord.key") as f:
    TOKEN = f.readline()

ALARIA_WIKI = "/Users/silasrhyneer/Documents/AlariaWiki/wiki"

description = '''HeartRushBot -- A tool for playing and understanding Heart Rush more-better :)'''
bot = commands.Bot(command_prefix='!', description=description)

def find_page(query):
    wiki_files = set()
    for filename in os.listdir(ALARIA_WIKI):
        path = os.path.join(ALARIA_WIKI, filename)
        if (".DS_Store" in path) or ("img" in path) or (".git" in path): continue
        wiki_files.add(filename.replace(".md", ""))

    return difflib.get_close_matches(query, wiki_files)[0] + ".md"

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
    subject = subject.lower()
    if subject == "all":
        await ctx.send("https://drive.google.com/file/d/1dxcwnfamLW_zkCMTr0z1o3g2evCAQcen/view?usp=sharing")
    else:
        try:
            await ctx.send(file=discord.File(rf'rules/{subject}.md'))
        except:
            all_subjects = sorted([section.replace(".md", "") for section in os.listdir("rules")])
            all_subjects_text = ', '.join(all_subjects)
            await ctx.send(f"Rules on `{subject}` could not be found. Try a subject in the following list: ```{all_subjects_text}```")

@bot.command()
async def wiki(ctx, subject):
    """Query the wiki for information on a subject
    """
    try:
        page = find_page(subject)
        print(page)
        html = markdown.markdown(open(f'{ALARIA_WIKI}/{page}').read())
        with open("tmp.html") as f:
            f.write(html)
        # print(html)
        await ctx.send(html)
        # await ctx.send(file=discord.File(rf'tmp.html'))
    except:
        all_subjects = sorted([section.replace(".md", "") for section in os.listdir("rules")])
        await ctx.send(all_subjects)


if rpi:
    bl = blinker.Blinker(.1, templates.DEFAULT)
    blink = int(sys.argv[1])
    if blink:
        bl.show()
bot.run(TOKEN)