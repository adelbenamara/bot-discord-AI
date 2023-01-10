import discord
from priv import *
import datetime
from discord.ext import commands
from dotenv import load_dotenv


bot= commands.Bot(command_prefix='$',intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("the bot is ready on ligne")
    
@bot.command()
async def  hello(ctx):
    user = ctx.message.author.mention
    await ctx.send(f" hello {user} in  {ctx.guild.name} ")

@bot.command()
async def  thanks(ctx):
    user = ctx.message.author.mention
    await ctx.send(f" you're welcome {user} ")
    await ctx.send(discord.Embed(title="thanks", description=f"{user}", color=0x00ff00))


@bot.command()
async def welcomed(ctx,member: discord.Member = None):
    await ctx.send(f"{member.mention} welcome to {ctx.guild.name} nice to meet you")

@bot.command()
@commands.has_any_role( "administrator", "moderator" ,"Owner" )
async def ban(ctx,member: discord.Member ,* , reason:None):
    if reason== None :
         reason = f"no reason  this  {member.name} is  banned by {ctx.author.name}"
         await member.ban(reason=raison)
         await ctx.send(f"ban {member}")

@bot.command()
@commands.has_any_role( "administrator", "moderator" ,"Owner" )
async def kick(ctx, member: discord.Member ,* , reason:None):
    if reason== None :
         reason = f"no reason  this  {member.name} is  Kicked by {ctx.author.name}"
         await member.kick()(reason=raison)
         await ctx.send(f"kick {member}")
@bot.command()
async def mute(ctx,*,timelimit):
    if 's' in timelimit :
        timelimit = int(timelimit.replace('s',''))
    elif 'm' in timelimit:
        timelimit = int(timelimit.replace('m',''))*60
    elif 'h' in timelimit:
        timelimit = int(timelimit.replace('h',''))*3600
    elif 'd' in timelimit:
        timelimit = int(timelimit.replace('d',''))*86400
    else:
         timelimit = int(timelimit)

    if timelimit>2419000:
        await ctx.send("la durée est trop longue")
    else:   
        nexttime = datetime.datetime.now() + datetime.timedelta(seconds=timelimit) 
        member.edit(timeoutUntil=nexttime)
        await ctx.send(f"le joueur {ctx.author.mention} est mute pour {timelimit} secondes") 

@bot.command()
@commands.has_any_role( "administrator", "moderator" ,"Owner" )
async def unmute(ctx,member:discord.Member):
    await member.edit(mute=False)
    await ctx.send(f"le joueur {ctx.author.mention} est unmute")

@bot.command()
async def clear(ctx,amount:int):
    await ctx.channel.purge(limit=amount)

@bot.command()
async def help_full(ctx):
    embed = discord.Embed(title="help", description="help for commandes", colour=0x00ff00)  
    embed.add_field(name="$hello", value="hello", inline=False)
    embed.add_field(name="$ban", value="ban (member) (raison)", inline=False)
    embed.add_field(name="$kick", value="kick", inline=False)
    embed.add_field(name="$mute", value="mute", inline=False)
    embed.add_field(name="$unmute", value="unmute", inline=False)
    embed.add_field(name="$clear", value="clear", inline=False)
    await ctx.send(embed=embed)

# @bot.event()
# async def on_message(ctx):
#     if ctx.author.bot:
#         return
#     if ctx.content.startswith('$aibot'):
#         pass


 


bot.run(TOKEN)