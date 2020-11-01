# main.py
import os

import discord
from dotenv import load_dotenv
from datetime import datetime
from discord.ext import commands
from discord.ext.commands import bot
import sys
import asyncio
import traceback

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix="!!")

@bot.event
async def on_ready():
    now = datetime.now()

    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

    init_message_embed = discord.Embed(title="bot has successfully booted up.", color=0x00aeff)
    init_message_embed.set_footer(text=str(now.strftime("%d/%m/%Y - %H:%M:%S")))
    await bot.get_channel(772219545082396692).send(embed=init_message_embed)

@bot.event
async def on_message(message):
    now = datetime.now()
    guild = bot.get_guild(186610204023062528)
    mod_role = guild.get_role(219977258453041152)
    message_author = message.author
    is_mod = False
    if message.content.startswith("!!quit"):
        for role in message_author.roles:
            if role == mod_role:
                is_mod = True
        if is_mod:
            await message.channel.send("bot has been shutdown.")
            quit_message_embed = discord.Embed(title="bot has successfully shutdown.", color=0x00aeff)
            quit_message_embed.set_footer(text=str(now.strftime("%d/%m/%Y - %H:%M:%S")))
            await bot.get_channel(772219545082396692).send(embed=quit_message_embed)
            await exit()
        else:
            await mod_only_command(message)

@bot.event
async def on_reaction_add(reaction, user):
    try:
        now = datetime.now()
        if reaction.count == 1:
            channel_report = bot.get_channel(413488194819194891)
            guild = bot.get_guild(186610204023062528)
            mod_role = guild.get_role(219977258453041152)
            reacted_message = reaction.message
            reacted_message_content = reacted_message.content
            reacted_message_author = reaction.message.author
            reacted_message_author_roles = None
            long_message = False
            mod_report = False
            description = ""

            for role in reacted_message_author.roles:
                if role.name != '@everyone':
                    if reacted_message_author_roles is None:
                        reacted_message_author_roles = str(role)
                    else:
                        reacted_message_author_roles = str(reacted_message_author_roles) + ", " + str(role)

            
            if reaction.emoji == '🚫':
                #if a user auto reacts 🚫 to their message, it just deletes it without reporting it
                if user == reacted_message_author:
                    await reacted_message.delete()
                else:
                    for role in user.roles:
                        if role == mod_role:
                            #report_confirmation_embed = discord.Embed(title="The message has been reported.", color=0xff0000)
                            await reacted_message.delete()
                            mod_report = True
                            description = "*The message has been deleted as it has been reported by an admin.*"
                            #report_confirmation_message = await reacted_message.channel.send(embed=report_confirmation_embed)
                            #await asyncio.sleep(2)
                            #await report_confirmation_message.delete()

                    reported_message_embed = discord.Embed(title="Reported Message - ID: " + str(reacted_message.id), description=description, color=0xff0000)
                    reported_message_embed.set_thumbnail(url=reacted_message_author.avatar_url)
                    reported_message_embed.add_field(name="Username", value=reacted_message_author.name, inline=True)
                    reported_message_embed.add_field(name="Nickname", value=reacted_message_author.nick, inline=True)
                    reported_message_embed.add_field(name="User ID", value="<@" + str(reacted_message_author.id) + ">", inline=True)
                    reported_message_embed.add_field(name="Channel", value="<#" + str(reacted_message.channel.id) + ">", inline=True)
                    reported_message_embed.add_field(name="User Roles", value=str(reacted_message_author_roles), inline=True)
                    #if the message is too long
                    if len(reacted_message_content) >= 1000:
                        long_message = True
                        message_length = len(reacted_message_content)
                        reacted_message_content_part2 = reacted_message_content[999:message_length]
                        reacted_message_content = reacted_message_content[0:999]
                        reported_message_embed.add_field(name="Message", value=reacted_message_content, inline=False)
                        reported_message_part2_embed = discord.Embed(description="*The message is over 1000 characters, so it has been split into 2 Discord embeds.*", color=0xff0000)
                        reported_message_part2_embed.add_field(name="Message (part 2)", value=reacted_message_content_part2, inline=False)
                        reported_message_part2_embed.set_footer(text="Reported by " + str(user.name) + "#" + str(user.discriminator) + "  •  " + str(now.strftime("%d/%m/%Y - %H:%M:%S")), icon_url=user.avatar_url)
                    else:
                        #if the message only contains an attachment
                        if len(reacted_message_content) != 0:
                            reported_message_embed.add_field(name="Message", value=reacted_message_content, inline=False)
                        else:
                            reported_message_embed.add_field(name="Attachment", value="*The reported message only contained an attachment; make sure to have it saved before reporting it as the bot cannot currently save (deleted) pictures. You can also give out a description of the attachment below*", inline=False)
                        reported_message_embed.set_footer(text="Reported by " + str(user.name) + "#" + str(user.discriminator) + "  •  " + str(now.strftime("%d/%m/%Y - %H:%M:%S")), icon_url=user.avatar_url)

                    await channel_report.send(embed=reported_message_embed)
                    if long_message == True:
                        await channel_report.sen(embed=reported_message_part2_embed)
                    
    except:
        crash_traceback = traceback.format_exc()
        crash_message_embed = discord.Embed(title="it crashed :(", description=crash_traceback, color=0xff0000)
        reported_message_part2_embed.set_footer(text=str(now.strftime("%d/%m/%Y - %H:%M:%S")))
        await bot.get_channel(772219545082396692).send(embed=crash_message_embed)
        raise

@bot.event
async def mod_only_command(message):
    await message.channel.send("you cannot do this action as you are not a mod!")

if __name__ == "__main__":
    bot.run(TOKEN)