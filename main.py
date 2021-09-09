import discord
from discord.ext import commands
from settings import guild_id as g

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("online")

@client.command()
async def support(ctx):
    await ctx.author.send(f"Please describe your problem.\nOur Staff team will be with you as soon as possible.\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")

@client.event
async def on_message(message):

    channel_exists = discord.utils.get(client.get_guild(g).text_channels,name="support-" + str(message.author).lower().replace("#", "").replace(" ", "-").replace("|", "-"))

    if message.author.id == client.user.id:
        return
    if message.author != message.author.bot:
        if not message.guild:
            if channel_exists:
                embed = discord.Embed(color=0x77dd77)
                embed.add_field(name="**⚠ New Message ⚠**", value=f"**User: **{message.author.mention}\n**Message: **{message.content}\n**User-ID: ** {message.author.id}")
                embed.set_footer(text="Use '.reply UserId' to send a message to the User")
                msg1 = await client.get_guild(g).get_channel(channel_exists.id).send(embed=embed)
            else:
               new_channel = await client.get_guild(g).create_text_channel(name=f"support-{message.author}", reason="New ModMail ticket created.")
               msg = await client.get_guild(g).get_channel(new_channel.id).send(f"⚠️ **New Support Ticket** ⚠️\n**User:** {message.author.mention}\n**User-ID:** {message.author.id}\n\n**Message:** {message.content}")


            
    await client.process_commands(message)

@client.command()
async def reply(ctx, member : discord.User, *, args):
    embed = discord.Embed(color=0x77dd77)
    embed.add_field(name="Server Team", value=args)
    await member.send(embed=embed)

@client.command()
async def close(ctx, member : discord.Member, *, reason=None):
    c = ctx.channel
    await c.delete(reason=reason)
    await member.send(f"Your ticket has been closed. Reason: {reason}")


@client.command()
async def test(ctx):
    await ctx.send(str(ctx.author).lower().replace("#", "").replace(" ", "-").replace("|", "-"))

client.run("token")